from sqlalchemy import text


# Завдання 2
# Для бази даних «Лікарня», яку ви розробляли в рамках
# курсу «Теорія Баз Даних», створіть додаток для взаємодії
# з базою даних, який дозволяє створювати звіти:


# ▷ Вивести прізвища лікарів та їх спеціалізації;
def show_doctors_specialization(session):
    query = """
        SELECT D.SURNAME, S.NAME
            FROM DOCTORS D
            JOIN DOCTORS_SPECIALIZATIONS DS
            ON DS.DOCTOR_ID = D.ID
            JOIN SPECIALIZATIONS S ON S.ID = DS.SPECIALIZATION_ID
    """

    query = text(query)
    results = session.execute(query)

    for row in results:
        print(row)


# ▷ Вивести прізвища та зарплати (сума ставки та надбавки) лікарів, які не перебувають у відпустці;
def show_doctors_salary(session):
    query = """
        SELECT D.SURNAME , D.SALARY + D.PREMIUM AS SALARY
            FROM DOCTORS D JOIN VACATIONS V ON V.DOCTOR_ID = D.ID
            WHERE V.START_DATE <= CURRENT_DATE AND V.END_DATE > CURRENT_DATE
    """

    query = text(query)
    results = session.execute(query)

    for row in results:
        print(row)


# ▷ Вивести назви палат, які знаходяться у певному відділенні;
def show_wards(session, department):
    query = f"""
        SELECT W.NAME
            FROM DEPARTMENTS D JOIN WARDS W ON W.DEPARTMENT_ID = D.ID
            WHERE D.NAME = '{department}'
    """

    query = text(query)
    results = session.execute(query)

    for row in results:
        print(row)


# ▷ Вивести усі пожертвування за вказаний місяць у вигляді: відділення, спонсор, сума пожертвування, дата пожертвування;
def show_donations(session, month_num, year):
    query = f"""
        SELECT D.NAME, S.NAME, DON.AMOUNT, DON.DATE
            FROM DEPARTMENTS D
            JOIN DONATIONS DON ON DON.DEPARTMENT_ID = D.ID
            JOIN SPONSORS S ON S.ID = DON.SPONSOR_ID
            WHERE EXTRACT(MONTH FROM DON.DATE) = {month_num}
                AND EXTRACT(YEAR FROM DON.DATE) = {year}
    """

    query = text(query)
    results = session.execute(query)

    for row in results:
        print(row)


# ▷ Вивести назви відділень без повторень, які спонсоруються певною компанією.
def show_departments(session, department_name="LifeCare Foundation"):
    query = f"""
        SELECT DISTINCT D.NAME
            FROM DEPARTMENTS D
            JOIN DONATIONS DON
            ON DON.DEPARTMENT_ID = D.ID
            JOIN SPONSORS S ON S.ID = DON.SPONSOR_ID
            WHERE S.NAME = '{department_name}'
    """

    query = text(query)
    results = session.execute(query)

    for row in results:
        print(row)
