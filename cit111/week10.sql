USE bike;

#Query 1
SELECT ROUND(AVG(quantity)) as 'Stock Average'
FROM stock;

#Query 2
SELECT DISTINCT product_name
FROM product AS p
	JOIN stock AS s ON p.product_id = s.product_id
WHERE quantity = 0
ORDER BY product_name;

#Query 3 
SELECT category_name, COUNT(quantity) AS instock
FROM product AS p
	JOIN category AS c ON p.category_id = c.category_id
    JOIN stock AS s ON p.product_id = s.product_id
    JOIN store AS st ON s.store_id = st.store_id
WHERE st.store_id = 2 
GROUP BY category_name
ORDER BY  instock asc;

#QUERY 4
USE employees;

SELECT COUNT(emp_no) AS 'Number of Employees'
FROM employees;

#QUERY 5
SELECT dept_name, FORMAT(AVG(salary), 2) AS average_salary
FROM departments AS d
	JOIN dept_emp AS de ON d.dept_no = de.dept_no
    JOIN employees AS e ON de.emp_no = e.emp_no
    JOIN salaries AS s ON e.emp_no = s.emp_no
GROUP BY dept_name
HAVING AVG(salary) < 60000;

#QUERY 6
SELECT dept_name, COUNT(*) AS 'Number of Females'
FROM departments AS d
	JOIN dept_emp AS de ON d.dept_no = de.dept_no
    JOIN employees AS e ON de.emp_no = e.emp_no
WHERE gender = 'f'
GROUP BY dept_name

