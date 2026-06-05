from database import Session
from models import (
    show_doctors_specialization,
    show_doctors_salary,
    show_wards,
    show_donations,
    show_departments,
)


session = Session()


if __name__ == "__main__":
    show_doctors_specialization(session)
    show_doctors_salary(session)
    show_wards(session, "Терапія")
    show_donations(session, 3, 2024)
    show_departments(session)
