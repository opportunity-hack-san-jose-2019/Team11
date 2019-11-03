
import queryEngine


SCOPES = 'https://www.googleapis.com/auth/classroom.courses.readonly https://www.googleapis.com/auth/classroom.rosters.readonly https://www.googleapis.com/auth/classroom.student-submissions.students.readonly'

def main():
    coursesEngine = queryEngine.service(
        SCOPES
    )

    coursesEngine.getCourses()



    return


if __name__ == "__main__":
    main()