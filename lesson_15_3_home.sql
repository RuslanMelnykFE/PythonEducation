-- ¾ Кафедри (Departments)

-- CREATE TABLE DEPARTMENTS (
-- 	ID INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
-- 	FINANCING MONEY NOT NULL DEFAULT 0 CHECK (FINANCING > 0:: MONEY),
-- 	NAME VARCHAR (100) NOT NULL CHECK (NAME <> '') UNIQUE
-- )

-- INSERT INTO DEPARTMENTS (NAME, FINANCING) VALUES
-- ('Кафедра математики',        150000::money),
-- ('Кафедра фізики',            175000::money),
-- ('Кафедра хімії',             160000::money),
-- ('Кафедра інформатики',       200000::money),
-- ('Кафедра біології',          140000::money),
-- ('Кафедра історії',           120000::money),
-- ('Кафедра філології',         130000::money),
-- ('Кафедра економіки',         210000::money),
-- ('Кафедра менеджменту',       190000::money),
-- ('Кафедра права',             220000::money),
-- ('Кафедра психології',        145000::money),
-- ('Кафедра соціології',        135000::money),
-- ('Кафедра міжнародних відносин',180000::money)

-- ¾ Факультети(Faculties)
-- CREATE TABLE FACULTIES (
-- 	ID INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
-- 	DEAN VARCHAR (255) NOT NULL CHECK (DEAN <> ''),
-- 	NAME VARCHAR (100) NOT NULL CHECK (NAME <> '') UNIQUE
-- )

-- INSERT INTO FACULTIES (NAME, DEAN) VALUES
-- ('Факультет математики',              'Іван Петренко'),
-- ('Факультет фізики',                  'Олег Іваненко'),
-- ('Факультет хімії',                   'Марія Коваленко'),
-- ('Факультет інформатики',             'Андрій Шевченко'),
-- ('Факультет біології',                'Наталія Бондар'),
-- ('Факультет історії',                 'Сергій Мельник'),
-- ('Факультет філології',               'Олена Ткаченко'),
-- ('Факультет економіки',               'Василь Кравченко'),
-- ('Факультет менеджменту',             'Юлія Олійник'),
-- ('Факультет права',                   'Дмитро Романенко'),
-- ('Факультет психології',              'Катерина Лисенко'),
-- ('Факультет соціології',              'Ігор Савченко'),
-- ('Факультет міжнародних відносин',    'Світлана Яременко');


-- ¾ Групи (Groups)
-- CREATE TABLE GROUPS(
-- 	ID INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
-- 	NAME VARCHAR (100) NOT NULL CHECK (NAME <> '') UNIQUE,
-- 	RATING INT NOT NULL CHECK (RATING BETWEEN 0 AND 5),
-- 	YEAR INT NOT NULL CHECK (YEAR BETWEEN 1 AND 5)
-- )

-- INSERT INTO GROUPS (NAME, RATING, YEAR) VALUES
-- ('Група-101', 3, 1),
-- ('Група-102', 4, 1),
-- ('Група-103', 5, 1),
-- ('Група-201', 2, 2),
-- ('Група-202', 3, 2),
-- ('Група-203', 4, 2),
-- ('Група-301', 5, 3),
-- ('Група-302', 3, 3),
-- ('Група-303', 2, 3),
-- ('Група-401', 4, 4),
-- ('Група-402', 5, 4),
-- ('Група-403', 3, 4),
-- ('Група-501', 2, 5),
-- ('Група-502', 4, 5),
-- ('Група-503', 5, 5),
-- ('Група-104', 1, 1),
-- ('Група-204', 2, 2),
-- ('Група-304', 3, 3),
-- ('Група-404', 4, 4),
-- ('Група-504', 5, 5),
-- ('Група-105', 2, 1),
-- ('Група-205', 3, 2),
-- ('Група-305', 4, 3),
-- ('Група-405', 5, 4),
-- ('Група-505', 1, 5);


-- ¾ Викладачі(Teachers)
-- CREATE TABLE TEACHERS (
-- 	ID INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
-- 	EMPLOYMENT_DATE DATE NOT NULL CHECK (EMPLOYMENT_DATE >= '1990-01-01'),
-- 	IS_ASSISTANT BOOLEAN NOT NULL DEFAULT FALSE,
-- 	IS_PROFESSOR BOOLEAN NOT NULL DEFAULT FALSE,
-- 	NAME VARCHAR (255) NOT NULL CHECK (NAME <> ''),
-- 	POSITION VARCHAR (255) NOT NULL CHECK (POSITION <> ''),
-- 	PREMIUM MONEY NOT NULL DEFAULT 0 CHECK (PREMIUM > 0::MONEY),
-- 	SALARY MONEY NOT NULL CHECK (SALARY > 0::MONEY),
-- 	SURNAME VARCHAR (255) NOT NULL CHECK (SURNAME <> '')
-- )

-- INSERT INTO teachers (
--     name, surname, employment_date,
--     is_assistant, is_professor,
--     position, premium, salary
-- ) VALUES
-- ('Іван','Петренко','2001-09-01',false,true,'Професор',5000::money,30000::money),
-- ('Олег','Іваненко','2005-03-15',true,false,'Асистент',2000::money,20000::money),
-- ('Марія','Коваленко','2010-06-20',false,false,'Викладач',1500::money,22000::money),
-- ('Анна','Шевченко','2012-09-01',true,false,'Асистент',1000::money,18000::money),
-- ('Сергій','Бондар','2000-01-10',false,true,'Професор',4000::money,32000::money),
-- ('Олена','Мельник','2008-11-05',false,false,'Доцент',2500::money,25000::money),
-- ('Василь','Ткаченко','2015-02-12',true,false,'Асистент',800::money,17000::money),
-- ('Наталія','Кравченко','2013-07-07',false,false,'Викладач',1200::money,21000::money),
-- ('Дмитро','Олійник','1999-04-18',false,true,'Професор',4500::money,33000::money),
-- ('Юлія','Семенюк','2011-08-23',false,false,'Доцент',2000::money,24000::money),
-- ('Андрій','Романенко','2007-05-30',false,false,'Викладач',1800::money,23000::money),
-- ('Тетяна','Лисенко','2014-10-11',true,false,'Асистент',900::money,19000::money),
-- ('Павло','Гриценко','1998-12-01',false,true,'Професор',5000::money,34000::money),
-- ('Ігор','Дяченко','2003-06-14',false,false,'Доцент',2200::money,26000::money),
-- ('Людмила','Захарченко','2016-03-09',true,false,'Асистент',700::money,17500::money),
-- ('Роман','Марченко','2009-09-09',false,false,'Викладач',1600::money,22500::money),
-- ('Катерина','Паламарчук','2012-02-21',false,false,'Доцент',2100::money,25000::money),
-- ('Віктор','Савченко','2004-07-13',false,true,'Професор',4800::money,33500::money),
-- ('Світлана','Яременко','2010-01-25',false,false,'Викладач',1400::money,21000::money),
-- ('Максим','Білик','2017-06-17',true,false,'Асистент',600::money,16500::money),
-- ('Дарина','Коваль','2013-04-04',false,false,'Доцент',2000::money,24000::money),
-- ('Юрій','Приходько','2006-08-08',false,true,'Професор',4700::money,32000::money),
-- ('Оксана','Тимошенко','2015-09-09',true,false,'Асистент',900::money,18500::money),
-- ('Богдан','Чорний','2002-03-03',false,false,'Доцент',2300::money,25500::money),
-- ('Ірина','Гончар','2011-05-05',false,false,'Викладач',1500::money,22000::money),
-- ('Степан','Руденко','1997-10-10',false,true,'Професор',5200::money,34500::money),
-- ('Валерій','Поляк','2008-02-14',false,false,'Доцент',2100::money,25000::money),
-- ('Алла','Мороз','2016-12-12',true,false,'Асистент',700::money,17000::money),
-- ('Микола','Левченко','2005-07-07',false,false,'Викладач',1600::money,23000::money),
-- ('Галина','Кушнір','2014-06-06',false,false,'Доцент',2000::money,24000::money),
-- ('Станіслав','Клименко','2010-11-11',false,true,'Професор',4900::money,33000::money),
-- ('Юліан','Сидоренко','2018-01-01',true,false,'Асистент',500::money,16000::money),
-- ('Володимир','Панасюк','2009-03-03',false,false,'Доцент',2200::money,26000::money),
-- ('Неля','Бойко','2012-08-08',false,false,'Викладач',1500::money,22000::money),
-- ('Ростислав','Онищенко','2001-04-04',false,true,'Професор',5000::money,34000::money),
-- ('Артем','Дорошенко','2017-09-09',true,false,'Асистент',600::money,17000::money),
-- ('Євген','Кириленко','2006-05-05',false,false,'Доцент',2100::money,25000::money)


-- 1. Вивести таблицю кафедр, але розташувати її поля у зворотному порядку.
-- SELECT NAME, FINANCING, ID FROM DEPARTMENTS

-- 2. Вивести назви груп та їх рейтинги з уточненнями до назв полів відповідно до назви таблиці.
-- SELECT
-- 	NAME AS "Group name",
-- 	RATING AS "Group rating"
-- FROM GROUPS

-- 3. Вивести для викладачів їх прізвища, відсоток ставки по
-- відношенню до надбавки та відсоток ставки по відношенню до зарплати (сума ставки та надбавки).
-- SELECT
-- 	SURNAME,
-- 	SALARY / PREMIUM * 100 AS "Percent to premium",
-- 	SALARY / (SALARY + PREMIUM) * 100 AS "Percent to total"
-- FROM TEACHERS

-- 4. Вивести таблицю факультетів одним полем у такому форматі: «The dean of faculty [faculty] is [dean].».
-- SELECT
-- 	'The dean of faculty' || NAME || 'is' || DEAN || '.' AS INFO
-- FROM FACULTIES

-- 5. Вивести прізвища професорів, ставка яких перевищує 1050.
-- SELECT NAME FROM TEACHERS
-- WHERE IS_PROFESSOR = 'TRUE' AND SALARY > 20500::MONEY

-- 6. Вивести назви кафедр, фонд фінансування яких менший, ніж 11000 або більший за 25000.
-- SELECT NAME FROM DEPARTMENTS
-- WHERE FINANCING < 130000::MONEY OR FINANCING > 250000::MONEY

-- 7. Вивести назви факультетів, окрім факультету «Computer Science».
-- SELECT NAME FROM FACULTIES
-- WHERE NAME <> 'Факультет інформатики'

-- 8. Вивести прізвища та посади викладачів, які не є професорами.
-- SELECT SURNAME, POSITION FROM TEACHERS
-- WHERE IS_PROFESSOR = 'FALSE'

-- 9. Вивести прізвища, посади, ставки та надбавки асистентів, надбавка яких у діапазоні від 160 до 550.
-- SELECT SURNAME, POSITION, SALARY, PREMIUM FROM TEACHERS
-- WHERE IS_ASSISTANT = 'TRUE' AND PREMIUM BETWEEN 1600::MONEY AND 5500::MONEY

-- 10. Вивести прізвища та ставки асистентів.
-- SELECT SURNAME, SALARY FROM TEACHERS
-- WHERE IS_ASSISTANT = 'TRUE'

-- 11. Вивести прізвища та посади викладачів, які були прийняті на роботу до 01.01.2000.
-- SELECT SURNAME, POSITION FROM TEACHERS
-- WHERE EMPLOYMENT_DATE < '2000-01-01'

-- 12. Вивести назви кафедр, які в алфавітному порядку розміщені до кафедри «Software Development». Виведене поле
-- назвіть «Name of Department».
-- SELECT NAME AS "Name of Department" FROM DEPARTMENTS
-- WHERE NAME < 'Кафедра історії'
-- ORDER BY NAME

-- 13. Вивести прізвища асистентів із зарплатою (сума ставки та надбавки) не більше 1200.
-- SELECT SURNAME FROM TEACHERS
-- WHERE IS_ASSISTANT = 'TRUE' AND (PREMIUM + SALARY) > 20000::MONEY

-- 14. Вивести назви груп 5-го курсу з рейтингом у діапазоні від 2 до 4.
-- SELECT NAME FROM GROUPS
-- WHERE YEAR = 5 AND RATING BETWEEN 2 AND 4

-- 15. Вивести прізвища асистентів зі ставкою менше, ніж 550 або надбавкою менше, ніж 200.
-- SELECT SURNAME FROM TEACHERS
-- WHERE IS_ASSISTANT = 'TRUE' AND (SALARY < 3000::MONEY OR PREMIUM < 1000::MONEY)
