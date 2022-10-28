--Секция 2. Практическое задание SQL/PostgreSQL.
--2.1. Даны таблицы.
--Необходимо: использовав агрегатные функции, выбрать все шк и цены (reports.barcode, reports.price)
--с одинаковыми названиями точек продаж (pos.title).

CREATE TABLE pos
(
    id int PRIMARY KEY,
    title character varying
)
CREATE TABLE reports
(
    id int PRIMARY KEY,
    barcode character varying,
    price float,
    pos_id int
)

SELECT *
FROM
	(SELECT COUNT(*) as number, reports.barcode, reports.price, reports.title
	FROM (SELECT *
			FROM reports r
			JOIN pos p ON r.pos_id = p.id) as reports
	GROUP BY reports.barcode, reports.price, reports.title) as p
WHERE p.number > 1
