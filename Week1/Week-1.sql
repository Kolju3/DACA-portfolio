/*
SELECT COUNT(customer_id) AS "Klientide_koguarv"
From "Customers";
*/

/*
SELECT * --AS "Klientide_andmed"
FROM "Customers"
LIMIT 10;
*/

/*
SELECT DISTINCT city AS Eri_linnad
FROM "Customers";
*/

/*
SELECT *
FROM "Customers"
WHERE city = 'Tallinn'
LIMIT 15;
*/

/*
SELECT 
last_name, 
first_name, 
city 
FROM "Customers"
WHERE city = 'Tallinn';
*/

/*
SELECT DISTINCT 
    city, 
    (SELECT COUNT(*) FROM "Customers" c2 WHERE c2.city = c1.city) AS "Arv_kliente"
FROM "Customers" c1;
*/

/*
SELECT 
    INITCAP(TRIM(city)) AS "Linnad", 
    COUNT(*) AS "Kliendid"
FROM "Customers"
GROUP BY INITCAP(TRIM(city))
ORDER BY "Linnad";
*/

/*
SELECT DISTINCT 
    city, 
    (SELECT COUNT(*) FROM "Customers" c2 WHERE c2.city = c1.city)
FROM "Customers" c1;
*/

/*
WITH fixed_cities AS (
    SELECT 
        INITCAP(TRIM(city)) AS clean_city
    FROM "Customers"
)
SELECT DISTINCT 
    clean_city,
    (SELECT COUNT(*) FROM fixed_cities c2 WHERE c2.clean_city = c1.clean_city) AS "Kliendid"
FROM fixed_cities c1
ORDER BY clean_city;
*/