
import queryEngine

SCOPES = [
    'https://www.googleapis.com/auth/classroom.courses.readonly',
    'https://www.googleapis.com/auth/classroom.rosters.readonly',
    'https://www.googleapis.com/auth/classroom.coursework.students.readonly'
]

def main():
    coursesEngine = queryEngine.service(
        'https://www.googleapis.com/auth/classroom.courses.readonly'
    )

    coursesEngine.getCourses()



    return


if __name__ == "__main__":
    main()