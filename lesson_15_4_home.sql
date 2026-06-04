-- ¾ Куратори (Curators)
-- CREATE TABLE CURATORS (
-- 	ID SERIAL PRIMARY KEY,
-- 	NAME VARCHAR (255) NOT NULL CHECK (NAME <> '')
-- )

-- INSERT INTO CURATORS (NAME) VALUES
-- ('Іван Петренко'),
-- ('Олександр Шевченко'),
-- ('Марія Коваль'),
-- ('Анна Бондар'),
-- ('Дмитро Мельник'),
-- ('Ольга Ткаченко'),
-- ('Сергій Кравець'),
-- ('Наталія Савчук'),
-- ('Андрій Романюк'),
-- ('Ірина Мороз'),
-- ('Володимир Гриценко'),
-- ('Тетяна Лисенко');


-- ¾ Факультети (Faculties)
-- CREATE TABLE FACULTIES (
-- 	ID SERIAL  PRIMARY KEY,
-- 	FINANCING DECIMAL(10, 2) NOT NULL CHECK (FINANCING >= 0) DEFAULT 0,
-- 	NAME VARCHAR(100) NOT NULL CHECK(NAME <> '') UNIQUE
-- )

-- INSERT INTO FACULTIES (NAME, FINANCING) VALUES
-- ('Факультет інформаційних технологій', 150000.00),
-- ('Економічний факультет', 120000.00),
-- ('Факультет права', 100000.00),
-- ('Факультет інженерії', 180000.00);


-- ¾ Кафедри (Departments)
-- CREATE TABLE DEPARTMENTS (
-- 	ID SERIAL PRIMARY KEY,
-- 	FINANCING DECIMAL(10, 2) NOT NULL CHECK(FINANCING >= 0) DEFAULT 0,
-- 	NAME VARCHAR(100) NOT NULL CHECK(NAME <> '') UNIQUE,
-- 	FACULTY_ID INT NOT NULL,
-- 	FOREIGN KEY (FACULTY_ID) REFERENCES FACULTIES (ID)
-- )

-- INSERT INTO DEPARTMENTS (NAME, FINANCING, FACULTY_ID) VALUES
-- -- Факультет 1
-- ('Кафедра програмування', 50000.00, 1),
-- ('Кафедра кібербезпеки', 45000.00, 1),
-- ('Кафедра штучного інтелекту', 60000.00, 1),
-- ('Кафедра системного аналізу', 40000.00, 1),

-- -- Факультет 2
-- ('Кафедра економічної теорії', 30000.00, 2),
-- ('Кафедра фінансів', 35000.00, 2),
-- ('Кафедра маркетингу', 32000.00, 2),
-- ('Кафедра обліку і аудиту', 28000.00, 2),

-- -- Факультет 3
-- ('Кафедра цивільного права', 25000.00, 3),
-- ('Кафедра кримінального права', 27000.00, 3),
-- ('Кафедра міжнародного права', 26000.00, 3),

-- -- Факультет 4
-- ('Кафедра машинобудування', 55000.00, 4),
-- ('Кафедра електроніки', 53000.00, 4),
-- ('Кафедра будівництва', 52000.00, 4),
-- ('Кафедра енергетики', 54000.00, 4);


-- ¾ Групи (Groups)
-- CREATE TABLE GROUPS (
-- 	ID SERIAL PRIMARY KEY,
-- 	NAME VARCHAR(100) NOT NULL CHECK(NAME <> '') UNIQUE,
-- 	YEAR INT NOT NULL CHECK (YEAR BETWEEN 1 AND 5),
-- 	DEPARTMENT_ID INT NOT NULL,
-- 	FOREIGN KEY (DEPARTMENT_ID) REFERENCES DEPARTMENTS (ID)
-- )

-- INSERT INTO GROUPS (NAME, YEAR, DEPARTMENT_ID)
-- SELECT
--     'G-' || gs AS NAME,
--     (gs % 5) + 1 AS YEAR,
--     ((gs - 1) % 15) + 1 AS DEPARTMENT_ID
-- FROM generate_series(1, 75) AS gs


--  Групи та куратори (GroupsCurators)
-- CREATE TABLE GROUPS_CURATORS (
-- 	ID SERIAL PRIMARY KEY,
-- 	CURATOR_ID INT NOT NULL,
-- 	GROUP_ID INT NOT NULL,
-- 	FOREIGN KEY (CURATOR_ID) REFERENCES CURATORS (ID),
-- 	FOREIGN KEY (GROUP_ID) REFERENCES GROUPS (ID)
-- )

-- INSERT INTO GROUPS_CURATORS (CURATOR_ID, GROUP_ID)
-- SELECT
--     ((gs - 1) % 12) + 1 AS CURATOR_ID,  -- куратори 1–12 по колу
--     gs AS GROUP_ID                      -- групи 1–75
-- FROM generate_series(2, 76) AS gs


-- ¾ Викладачі(Teachers)
-- CREATE TABLE TEACHERS (
-- 	ID SERIAL PRIMARY KEY,
-- 	NAME VARCHAR (255) NOT NULL CHECK(NAME <> ''),
-- 	SURNAME VARCHAR (255) NOT NULL CHECK(NAME <> ''),
-- 	SALARY DECIMAL(10, 2) NOT NULL CHECK(SALARY > 0),
-- 	DEPARTMENT_ID INT NOT NULL,
-- 	FOREIGN KEY (DEPARTMENT_ID) REFERENCES DEPARTMENTS (ID)
-- )

-- INSERT INTO TEACHERS (NAME, SURNAME, SALARY, DEPARTMENT_ID)
-- SELECT
--     'Name' || gs AS NAME,
--     'Surname' || gs AS SURNAME,
--     (3000 + (gs % 10) * 500)::DECIMAL(10,2) AS SALARY,
--     ((gs - 1) % 15) + 1 AS DEPARTMENT_ID
-- FROM generate_series(1, 45) AS gs;

-- SELECT * FROM TEACHERS


-- ¾ Предмети (Subjects)
-- CREATE TABLE SUBJECTS (
-- 	ID SERIAL PRIMARY KEY,
-- 	NAME VARCHAR(100) NOT NULL CHECK(NAME <> '') UNIQUE,
-- 	DEPARTMENT_ID INT NOT NULL,
-- 	FOREIGN KEY (DEPARTMENT_ID) REFERENCES DEPARTMENTS (ID)
-- )

-- INSERT INTO SUBJECTS (NAME, DEPARTMENT_ID)
-- SELECT
--     'Subject ' || gs AS NAME,
--     ((gs - 1) % 15) + 1 AS DEPARTMENT_ID
-- FROM generate_series(1, 45) AS gs;


-- ¾ Лекції (Lectures)
-- CREATE TABLE LECTURES (
-- 	ID SERIAL PRIMARY KEY,
-- 	LECTURE_ROOM VARCHAR(255) NOT NULL CHECK(LECTURE_ROOM <> ''),
-- 	SUBJECT_ID INT NOT NULL,
-- 	TEACHER_ID INT NOT NULL,
-- 	FOREIGN KEY (SUBJECT_ID) REFERENCES SUBJECTS (ID),
-- 	FOREIGN KEY (TEACHER_ID) REFERENCES TEACHERS (ID)
-- )

-- INSERT INTO LECTURES (LECTURE_ROOM, SUBJECT_ID, TEACHER_ID)
-- SELECT
--     'Room ' || gs AS LECTURE_ROOM,
--     ((gs - 1) % 45) + 1 AS SUBJECT_ID,
--     ((gs - 1) % 45) + 1 AS TEACHER_ID
-- FROM generate_series(1, 75) AS gs;


-- ¾ Групи та лекції (GroupsLectures)
-- CREATE TABLE GROUPS_LECTURES (
-- 	ID SERIAL PRIMARY KEY,
-- 	GROUP_ID INT NOT NULL,
-- 	FOREIGN KEY (GROUP_ID) REFERENCES GROUPS (ID),
-- 	LECTURE_ID INT NOT NULL,
-- 	FOREIGN KEY (LECTURE_ID) REFERENCES LECTURES (ID)
-- )

-- INSERT INTO GROUPS_LECTURES (GROUP_ID, LECTURE_ID)
-- SELECT
--     g.ID,
--     l.ID
-- FROM GROUPS g
-- JOIN LECTURES l ON g.ID = l.ID;


-- 1. Виведіть усі можливі пари рядків викладачів і груп.
-- SELECT
-- 	T.NAME || ' ' || T.SURNAME AS FULL_NAME_TEACHER,
-- 	G.NAME
-- 	FROM TEACHERS T JOIN DEPARTMENTS D ON T.DEPARTMENT_ID = D.ID
-- 	JOIN GROUPS G ON G.DEPARTMENT_ID = D.ID

-- 2. Виведіть назви факультетів, фонд фінансування кафедр яких перевищує фонд фінансування факультету.
-- SELECT F.NAME
-- 	FROM FACULTIES F JOIN DEPARTMENTS D ON D.FACULTY_ID = F.ID
-- 	WHERE D.FINANCING > F.FINANCING

-- 3. Виведіть прізвища кураторів груп і назви груп, які вони курирують.
-- SELECT C.NAME, G.NAME
-- 	FROM CURATORS C JOIN GROUPS_CURATORS GC ON C.ID = GC.CURATOR_ID
-- 	JOIN GROUPS G ON GC.GROUP_ID = C.ID

-- 4. Виведіть імена та прізвища викладачів, які читають лекції у групі «P107».
-- SELECT
-- 	T.NAME || ' ' || T.SURNAME AS FULL_NAME_TEACHER
-- 	FROM TEACHERS T JOIN LECTURES L ON T.ID = L.TEACHER_ID
-- 	JOIN GROUPS_LECTURES GL ON GL.LECTURE_ID = L.ID
-- 	JOIN GROUPS G ON GL.GROUP_ID = G.ID
-- 	WHERE G.NAME = 'G-58'

-- 5. Виведіть прізвища викладачів і назви факультетів, на яких вони читають лекції.
-- SELECT T.SURNAME, F.NAME
-- 	FROM TEACHERS T JOIN DEPARTMENTS D ON T.DEPARTMENT_ID = D.ID
-- 	JOIN FACULTIES F ON F.ID = D.FACULTY_ID

-- 6. Виведіть назви кафедр і назви груп, які до них належать.
-- SELECT D.NAME, G.NAME
-- 	FROM DEPARTMENTS D JOIN GROUPS G ON D.ID = G.DEPARTMENT_ID

-- 7. Виведіть назви предметів, які викладає викладач «Samantha Adams».
-- SELECT S.NAME
-- 	FROM SUBJECTS S JOIN DEPARTMENTS D ON S.DEPARTMENT_ID = D.ID
-- 	JOIN TEACHERS T ON T.DEPARTMENT_ID = D.ID
-- 	WHERE T.NAME || ' ' || T.SURNAME = 'Name37 Surname37'

-- 8. Виведіть назви кафедр, на яких викладається дисципліна «Database Theory».
-- SELECT DISTINCT D.NAME
-- 	FROM SUBJECTS S JOIN DEPARTMENTS D ON S.DEPARTMENT_ID = D.ID
-- 	JOIN TEACHERS T ON T.DEPARTMENT_ID = D.ID
-- 	WHERE S.NAME = 'Subject 7'

-- 9. Виведіть назви груп, що належать до факультету «Computer Science».
-- SELECT G.NAME
-- 	FROM GROUPS G JOIN DEPARTMENTS D ON D.ID = G.DEPARTMENT_ID
-- 	JOIN FACULTIES F ON F.ID = D.FACULTY_ID
-- 	WHERE F.NAME = 'Факультет права'

-- 10. Виведіть назви груп 5-го курсу, а також назви факультетів, до яких вони належать.
-- SELECT G.NAME, F.NAME
-- 	FROM GROUPS G JOIN DEPARTMENTS D ON D.ID = G.DEPARTMENT_ID
-- 	JOIN FACULTIES F ON F.ID = D.FACULTY_ID
-- 	WHERE G.YEAR = 5

-- 11. Виведіть повні імена викладачів і лекції, які вони читають (назви предметів та груп). Зробіть відбір по тим лекціям,
-- які проходять в аудиторії «B103».
-- SELECT
-- 	T.NAME || ' ' || T.SURNAME AS FULL_NAME_TEACHER,
-- 	S.NAME, G.NAME
-- 	FROM TEACHERS T JOIN LECTURES L ON L.TEACHER_ID = T.ID
-- 	JOIN SUBJECTS S ON S.ID = L.SUBJECT_ID
-- 	JOIN GROUPS_LECTURES GL ON GL.LECTURE_ID = L.ID
-- 	JOIN GROUPS G ON G.ID = GL.GROUP_ID
-- 	WHERE L.LECTURE_ROOM = 'Room 46'
