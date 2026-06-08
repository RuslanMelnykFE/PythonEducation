from sqlalchemy import text
from tabulate import tabulate  # type: ignore


class Academy:
    # Для бази даних Академія, яку ви розробили в рамках
    # курсу «Теорія Баз Даних», створіть додаток для взаємодії
    # з базою даних, який дозволяє:
    # ■ вставляти рядки в таблиці бази даних;
    # ■ оновлювати рядків у таблицях бази даних;
    # ■ видаляти рядки з таблиць бази даних;
    # ■ створювати звіти:

    # ▷ вивести інформацію про всі навчальні групи,
    @staticmethod
    def show_groups(session):
        query = """
            SELECT G.NAME, D.NAME, F.NAME
                FROM GROUPS G JOIN DEPARTMENTS D ON G.DEPARTMENT_ID = D.ID
                JOIN FACULTIES F ON D.FACULTY_ID = F.ID
        """

        query = text(query)
        results = session.execute(query)

        table = [list(row) for row in results]

        print(
            tabulate(table, headers=["Група", "Кафедра", "Факультет"], tablefmt="grid")
        )

    # ▷ вивести інформацію про всіх викладачів,
    @staticmethod
    def show_teachers(session):
        query = """
            SELECT T.NAME || ' ' || T.SURNAME AS FULL_NAME_TEACHER, D.NAME, F.NAME
                FROM TEACHERS T JOIN DEPARTMENTS D ON T.DEPARTMENT_ID = D.ID
                JOIN FACULTIES F ON D.FACULTY_ID = F.ID
        """

        query = text(query)
        results = session.execute(query)

        table = [list(row) for row in results]

        print(
            tabulate(
                table, headers=["Викладач", "Кафедра", "Факультет"], tablefmt="grid"
            )
        )

    # ▷ вивести назви усіх кафедр,
    @staticmethod
    def show_departments(session):
        query = """
            SELECT DEPARTMENTS.NAME FROM DEPARTMENTS
        """

        query = text(query)
        results = session.execute(query)

        table = [list(row) for row in results]

        print(tabulate(table, headers=["Кафедра"], tablefmt="grid"))

    # ▷ вивести імена та прізвища викладачів, які читають лекції в конкретній групі,
    @staticmethod
    def show_teachers_info(session, group):
        query = f"""
            SELECT T.NAME || ' ' || T.SURNAME AS FULL_NAME_TEACHER
                FROM TEACHERS T JOIN LECTURES L ON T.ID = L.TEACHER_ID
                JOIN GROUPS_LECTURES GL ON GL.LECTURE_ID = L.ID
                JOIN GROUPS G ON GL.GROUP_ID = G.ID
                WHERE G.NAME = '{group}'
        """

        query = text(query)
        results = session.execute(query)

        table = [list(row) for row in results]

        print(tabulate(table, headers=[f"Викладачі групи {group}"], tablefmt="grid"))

    # ▷ вивести назви кафедр і груп, які до них відносяться,
    @staticmethod
    def show_departments_groups(session):
        query = """
            SELECT D.NAME, G.NAME
                FROM DEPARTMENTS D JOIN GROUPS G ON D.ID = G.DEPARTMENT_ID
        """

        query = text(query)
        results = session.execute(query)

        table = [list(row) for row in results]

        print(tabulate(table, headers=["Кафедри", "Групи"], tablefmt="grid"))

    # ▷ відобразити кафедру з максимальною кількістю груп,
    @staticmethod
    def show_max_groups(session):
        query = """
            SELECT D.NAME
                FROM DEPARTMENTS D JOIN GROUPS G ON D.ID = G.DEPARTMENT_ID
                GROUP BY D.NAME
                HAVING COUNT(G.ID) = (
                    SELECT MAX(cnt)
                    FROM (
                        SELECT COUNT(*) AS cnt
                        FROM GROUPS
                        GROUP BY DEPARTMENT_ID
                    ) sub
                )
        """

        query = text(query)
        results = session.execute(query)

        table = [list(row) for row in results]

        print(tabulate(table, headers=["Кафедра з max групами"], tablefmt="grid"))

    # ▷ відобразити кафедру з мінімальною кількістю груп,
    @staticmethod
    def show_min_groups(session):
        query = """
            SELECT D.NAME
                FROM DEPARTMENTS D JOIN GROUPS G ON D.ID = G.DEPARTMENT_ID
                GROUP BY D.NAME
                HAVING COUNT(G.ID) = (
                    SELECT MIN(cnt)
                    FROM (
                        SELECT COUNT(*) AS cnt
                        FROM GROUPS
                        GROUP BY DEPARTMENT_ID
                    ) sub
                )
        """

        query = text(query)
        results = session.execute(query)

        table = [list(row) for row in results]

        print(tabulate(table, headers=["Кафедра з min групами"], tablefmt="grid"))

    # ▷ вивести назви предметів, які викладає конкретний викладач,
    @staticmethod
    def show_teacher_subjects(session, teacher):
        query = f"""
            SELECT S.NAME
                FROM SUBJECTS S JOIN DEPARTMENTS D ON S.DEPARTMENT_ID = D.ID
                JOIN TEACHERS T ON T.DEPARTMENT_ID = D.ID
                WHERE T.NAME || ' ' || T.SURNAME = '{teacher}'
        """

        query = text(query)
        results = session.execute(query)

        table = [list(row) for row in results]

        print(tabulate(table, headers=[f"Предмети {teacher}"], tablefmt="grid"))

    # ▷ вивести назви кафедр, на яких викладається конкретна дисципліна,
    @staticmethod
    def show_subject_departments(session, subject):
        query = f"""
            SELECT DISTINCT D.NAME
                FROM SUBJECTS S JOIN DEPARTMENTS D ON S.DEPARTMENT_ID = D.ID
                JOIN TEACHERS T ON T.DEPARTMENT_ID = D.ID
                WHERE S.NAME = '{subject}'
        """

        query = text(query)
        results = session.execute(query)

        table = [list(row) for row in results]

        print(tabulate(table, headers=[f"Кафедри предмету {subject}"], tablefmt="grid"))

    # ▷ вивести назви груп, що належать до конкретного факультету,
    @staticmethod
    def show_department_groups(session, department):
        query = f"""
            SELECT G.NAME
                FROM GROUPS G JOIN DEPARTMENTS D ON D.ID = G.DEPARTMENT_ID
                JOIN FACULTIES F ON F.ID = D.FACULTY_ID
                WHERE F.NAME = '{department}'
        """

        query = text(query)
        results = session.execute(query)

        table = [list(row) for row in results]

        print(tabulate(table, headers=[f"Групи кафедри {department}"], tablefmt="grid"))
