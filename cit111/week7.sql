
#1
SELECT * FROM v_art.artist;
insert into v_art.artist (artist_id, fname, mname, lname, dob, dod, country, local)
values (9, 'Johannes',NULL, 'Vermeer',1632,1674,'Netherlands','n');
#2
select * from v_art.artist
order by artist_id asc;

#3
update v_art.artist
set dod = 1675
where artist_id = 9;
#4
delete from v_art.artist
WHERE artist_id = 9;
#5
SELECT first_name,last_name,phone FROM bike.customer
WHERE city = 'Houston';
#6
SELECT product_name, list_price, (list_price - 500) AS 'Discount Price'
FROM bike.product
WHERE list_price >= 5000.00
ORDER BY list_price desc;
#7
SELECT first_name, last_name, email FROM bike.staff
WHERE store_id != 1;
#8
SELECT product_name, model_year, list_price FROM bike.product
WHERE product_name LIKE '%spider%';
#9
SELECT product_name, list_price FROM bike.product
WHERE list_price BETWEEN 500 AND 550
ORDER BY list_price ASC;
#10
SELECT first_name, last_name, phone, street, city, state, zip_code FROM bike.customer
WHERE phone IS NOT NULL
AND city LIKE '%ach%' OR city LIKE'%och%' OR last_name = 'William'
LIMIT 5; 