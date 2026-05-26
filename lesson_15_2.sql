-- SELECT * FROM STUDENTS_GRADES

-- ■ Показати ПІБ усіх студентів з мінімальною оцінкою у вказаному діапазоні.
-- SELECT FULL_NAME FROM STUDENTS_GRADES
-- WHERE AVERAGE_GRADE > 10 AND AVERAGE_GRADE < 75

-- ■ Показати інформацію про студентів, яким виповнилося 20 років.
-- SELECT * FROM STUDENTS_GRADES
-- WHERE EXTRACT(YEAR FROM AGE(BIRTH_DATE)) = 24

-- ■ Показати інформацію про студентів з віком, у вказаному діапазоні.
-- SELECT * FROM STUDENTS_GRADES
-- WHERE EXTRACT(YEAR FROM AGE(BIRTH_DATE)) > 23 AND EXTRACT(YEAR FROM AGE(BIRTH_DATE)) < 26

-- ■ Показати інформацію про студентів із конкретним
-- ім’ям. Наприклад, показати студентів з ім’ям Борис.
-- SELECT * FROM STUDENTS_GRADES
-- WHERE FULL_NAME ILIKE('%Ігор%')

-- ■ Показати інформацію про студентів, в номері яких є три сімки.
-- SELECT * FROM STUDENTS_GRADES
-- WHERE PHONE LIKE'%33%'

-- ■ Показати електронні адреси студентів, що починаються з конкретної літери.
-- SELECT * FROM STUDENTS_GRADES
-- WHERE EMAIL ILIKE'B%'

-- Показати мінімальну середню оцінку по всіх студентах.
-- SELECT MIN(AVERAGE_GRADE) AS MIN_AVERAGE_GRADE FROM STUDENTS_GRADES

-- ■ Показати максимальну середню оцінку по всіх студентах.
-- SELECT MAX(AVERAGE_GRADE) AS MAX_AVERAGE_GRADE FROM STUDENTS_GRADES

-- ■ Показати статистику міст. Має відображатися назва міста та кількість студентів з цього міста.
-- SELECT CITY, COUNT(*) AS STUDENTS_COUNT
-- FROM STUDENTS_GRADES
-- GROUP BY CITY

-- ■ Показати статистику студентів. Має відображатися назва країни та кількість студентів з цієї країни.
-- SELECT COUNTRY, COUNT(*) AS STUDENTS_COUNT
-- FROM STUDENTS_GRADES
-- GROUP BY COUNTRY

-- ■ Показати кількість студентів з мінімальною середньою оцінкою з математики.
-- SELECT COUNT(*) AS STUDENTS_COUNT_MATH
-- FROM STUDENTS_GRADES
-- WHERE MIN_AVG_SUBJECT = 'Математика'

-- ■ Показати кількість студентів з максимальною середньою оцінкою з математики.
-- SELECT COUNT(*) AS STUDENTS_COUNT_MATH
-- FROM STUDENTS_GRADES
-- WHERE MAX_AVG_SUBJECT = 'Математика'

-- ■ Показати кількість студентів у кожній групі.
-- SELECT GROUP_NAME, COUNT(*) AS STUDENTS_COUNT
-- FROM STUDENTS_GRADES
-- GROUP BY GROUP_NAME

-- ■ Показати середню оцінку групи.
-- SELECT GROUP_NAME, AVG(AVERAGE_GRADE) AS AVG_GRADE_GROUP
-- FROM STUDENTS_GRADES
-- GROUP BY GROUP_NAME
