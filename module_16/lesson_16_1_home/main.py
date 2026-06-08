from database import Session
from models import Academy


session = Session()


def main():
    academy = Academy()

    print("групи:")
    academy.show_groups(session)
    print("\n", "викладачі:")
    academy.show_teachers(session)
    print("\n")
    academy.show_departments(session)
    print("\n")
    academy.show_teachers_info(session, "G-58")
    print("\n")
    academy.show_departments_groups(session)
    print("\n")
    academy.show_max_groups(session)
    print("\n")
    academy.show_min_groups(session)
    print("\n")
    academy.show_teacher_subjects(session, "Name37 Surname37")
    print("\n")
    academy.show_subject_departments(session, "Subject 7")
    print("\n")
    academy.show_department_groups(session, "Факультет права")


if __name__ == "__main__":
    main()
