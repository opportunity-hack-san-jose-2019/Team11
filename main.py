
import queryEngine
from queryEngine import PopulateDB


SCOPES = 'https://www.googleapis.com/auth/classroom.courses.readonly https://www.googleapis.com/auth/classroom.rosters.readonly https://www.googleapis.com/auth/classroom.student-submissions.students.readonly'


def main():
    coursesEngine = queryEngine.service(
        SCOPES
    )

    coursesEngine.getCourses()
    coursesEngine.getAssignments('46905735568')
    coursesEngine.getStudents('46905735568')

    PopulateDB("gradebook", coursesEngine)



if __name__ == "__main__":
    main()