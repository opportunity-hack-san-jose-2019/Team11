
import pickle
import os.path
import sqlite3
import googleapiclient.discovery
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# ARGS
# AuthToken: The file which authorizes access to the classroom
# IOState: string which specifies what access level the service has with the api
class service:
    def __init__(self, IOState):
        self.creds = None

        # When AuthToken is given stores the user's access and refreshes tokens
        # automatically created when the authorization complete the first time
        if os.path.exists("token.pickle"):
            with open("token.pickle", "rb") as token:
                self.creds = pickle.load(token)
        # if not valid credentials let user log in
        if not self.creds or not self.creds.valid:
            if self.creds and self.creds.expired and self.creds.refresh_token:
                self.creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    "credentials.json", IOState
                )
                flow.authorization_url(
                    access_type='offline',
                    include_granted_scopes='true'
                )
                self.creds = flow.run_local_server(port=0)
            # save credentials for next session
            with open("token.pickle", "wb") as token:
                pickle.dump(self.creds, token)

        self.Service = googleapiclient.discovery.build("classroom", "v1", credentials=self.creds)

    def getCourses(self) -> list:
        return self.Service.courses().list().execute()["courses"]

    def getAssignments(self, courseId:str) -> list:
        ass =  self.Service.courses().courseWork().list(courseId=courseId).execute()
        return ass

    def getStudents(self, courseId:str) -> dict:
        student = self.Service.courses().students().list(courseId=courseId).execute()
        for i in student['students']:
            print(i["profile"])
        return student

class Course:
    def __init__(self, courseDict: dict, engine: service):
        self.courseName = courseDict["name"]
        self.students = [i for i in courseDict]

        pass


def PopulateDB(dp_path: str, engine: service) -> None:
    con = sqlite3.connect(dp_path)

    with con:
        for i in engine.getCourses():
            for j in engine.getStudents(i)['students']:
                profile = j['profile']
                con.execute('INSERT INTO Gradebook VALUES (?, ?, ?, ?, ?)', ("ineedbetteremail@joke.com", j['givenName'], j['familyName'], 0, 0))

    con.close()
