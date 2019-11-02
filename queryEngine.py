
import pickle
import os.path
import googleapiclient.discovery
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from typing import *

class Classroom:
    def __init__(self, ):
        pass

#AGRS
#AuthToken: The file which authorizes access to the classroom
#IOState: string which specifies what access level the service has with the api
class service:
    def __init__(self, IOState:str, AuthTokenFile=None):
        self.creds = None

        #When AuthToken is given stores the user's access and refreshes tokens
        #automatically created when the authorization complete the first time
        if AuthTokenFile:
            with open("token.pickle", "rb") as token:
                self.creds = pickle.load(token)
        if not (self.creds and self.creds.valid):
            if self.creds and self.creds.expired and self.creds.refresh_token:
                self.creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    "credentials.json", IOState
                )
                self.creds = flow.run_local_server(port=0)
            with open("token.pickle", "wb") as token:
                pickle.dump(self.creds, token)

        self.Service = googleapiclient.discovery.build("classroom", "v1", )

    def getClasses(self) -> List:
        return self.Service.service.courses().list().execute()
