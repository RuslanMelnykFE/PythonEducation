-- Відображення усіх овочів з калорійністю, менше вказаної.
-- SELECT * FROM FRUITS_VEGETABLES
-- WHERE TYPE = 'овоч' AND CALORIES < 100

-- ■ Відображення усіх фруктів з калорійністю у вказаному діапазоні.
-- WHERE TYPE = 'фрукт' AND CALORIES BETWEEN 70 AND 80

-- ■ Відображення усіх овочів, у назві яких є вказане слово. Наприклад, слово: капуста.
-- WHERE TYPE = 'овоч' AND NAME ILIKE'%капуста%'

-- ■ Відображення усіх овочів та фруктів, у короткому описі яких є вказане слово. Наприклад, слово: гемоглобін.
-- WHERE DESCRIPTION ILIKE'%солодкий%'

-- ■ Показати усі овочі та фрукти жовтого або червоного кольору
-- WHERE COLOR IN ('жовтий', 'червоний')

-- Показати кількість овочів.
-- SELECT COUNT(*) AS VEGETABLES_COUNT FROM FRUITS_VEGETABLES
-- WHERE TYPE = 'овоч'

-- ■ Показати кількість фруктів.
-- SELECT COUNT(*) AS FRUITS FROM FRUITS_VEGETABLES
-- WHERE TYPE = 'фрукт'

-- ■ Показати кількість овочів та фруктів заданого кольору.
-- SELECT COLOR, TYPE, COUNT(*) AS PRODUCT_COUNT FROM FRUITS_VEGETABLES
-- WHERE COLOR IN ('жовтий', 'червоний')
-- GROUP BY COLOR, TYPE
-- ORDER BY COLOR, TYPE

-- ■ Показати кількість овочів та фруктів кожного кольору.
-- SELECT COLOR, COUNT(*) AS PRODUCT_COUNT,
-- COUNT(*) FILTER (WHERE TYPE = 'фрукт') AS FRUITS_COUNT,
-- COUNT(*) FILTER (WHERE TYPE = 'овоч') AS VEGETABLES_COUNT
-- FROM FRUITS_VEGETABLES
-- GROUP BY COLOR
-- ORDER BY PRODUCT_COUNT

-- ■ Показати колір мінімальної кількості овочів та фруктів.
-- WITH COLOR_COUNTS AS (
-- 	SELECT COLOR,
-- 	COUNT (*) AS TOTAL_COUNT,
-- 	COUNT (*) FILTER (WHERE TYPE = 'фрукт') AS FRUITS_COUNT,
-- 	COUNT(*) FILTER (WHERE TYPE = 'овоч') AS VEGETABLES_COUNT
-- 	FROM FRUITS_VEGETABLES
-- 	GROUP BY COLOR
-- )

-- SELECT * FROM COLOR_COUNTS
-- WHERE TOTAL_COUNT = (
-- 	SELECT MIN(TOTAL_COUNT) FROM COLOR_COUNTS
-- )

-- ■ Показати колір максимальної кількості овочів та фруктів.
-- SELECT * FROM COLOR_COUNTS
-- WHERE TOTAL_COUNT = (
-- 	SELECT MAX(TOTAL_COUNT) FROM COLOR_COUNTS
-- )

-- ■ Показати мінімальну калорійність овочів та фруктів.
-- SELECT TYPE, NAME, CALORIES FROM FRUITS_VEGETABLES FV
-- WHERE CALORIES = (
-- 	SELECT MIN(CALORIES) FROM FRUITS_VEGETABLES
-- 	WHERE TYPE = FV.TYPE
-- )


-- ■ Показати максимальну калорійність овочів та фруктів.
-- SELECT TYPE, NAME, CALORIES FROM FRUITS_VEGETABLES FV
-- WHERE CALORIES = (
-- 	SELECT MAX(CALORIES) FROM FRUITS_VEGETABLES
-- 	WHERE TYPE = FV.TYPE
-- )

-- ■ Показати середню калорійність овочів та фруктів.
-- SELECT TYPE, AVG(CALORIES) AS AVG_CALORIES FROM FRUITS_VEGETABLES
-- GROUP BY TYPE

-- ■ Показати фрукт з мінімальною калорійністю.
-- SELECT NAME, CALORIES FROM FRUITS_VEGETABLES
-- WHERE CALORIES = (
-- 	SELECT MIN(CALORIES) FROM FRUITS_VEGETABLES
-- 	WHERE TYPE = 'фрукт'
-- )

-- ■ Показати фрукт з максимальною калорійністю.
-- SELECT NAME, CALORIES FROM FRUITS_VEGETABLES
-- WHERE CALORIES = (
-- 	SELECT MAX(CALORIES) FROM FRUITS_VEGETABLES
-- 	WHERE TYPE = 'фрукт'
-- )
