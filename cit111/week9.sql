USE v_art;
#QUERY 1
SELECT artfile FROM artwork
WHERE period = 'Impressionism';
#QUERY 2
SELECT artfile 
FROM artwork as a
	INNER JOIN artwork_keyword as ak on ak.artwork_id = a.artwork_id
	INNER JOIN keyword as k on k.keyword_id = ak.keyword_id
WHERE keyword LIKE '%flower%';
#QUERY 3
SELECT fname, lname, title
FROM artist as a
	LEFT JOIN artwork as aw on aw.artist_id = a.artist_id;
#QUERY 4
USE magazine;

SELECT magazineName, subscriberLastName, subscriberFirstName
FROM magazine as m
	JOIN subscription as s on s.magazineKey = m.magazineKey
    JOIN subscriber as sb on sb.subscriberKey = s.subscriberKey
ORDER BY magazineName;

#QUERY 5
SELECT magazineName
FROM magazine as m
	JOIN subscription as s on s.magazineKey = m.magazineKey
    JOIN subscriber as sb on sb.subscriberKey = s.subscriberKey
WHERE subscriberFirstName = 'Samantha' and subscriberLastName = 'Sanders'
ORDER BY magazineName;

#QUERY 6
USE employees;
SELECT first_name, last_name
FROM employees AS e
	JOIN dept_emp AS de ON e.emp_no = de.emp_no
    JOIN departments AS d on d.dept_no = de.dept_no
WHERE dept_name = 'Customer Service'
ORDER BY last_name
LIMIT 5;

#QUERY 7
SELECT first_name, last_name, dept_name, CONCAT('$', FORMAT(salary, 0)) AS salary, s.from_date
FROM employees AS e
	INNER JOIN salaries AS s ON e.emp_no = s.emp_no
    INNER JOIN dept_emp AS de ON e.emp_no = de.emp_no
    INNER JOIN departments AS d on d.dept_no = de.dept_no
WHERE first_name = 'Berni' and last_name = 'Genin'
ORDER BY from_date desc
LIMIT 1


