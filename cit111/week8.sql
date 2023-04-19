
#QUERY 1
SELECT magazineName, ROUND((magazinePrice - magazinePrice * .03),2) AS '3% off' FROM magazine.magazine;
#QUERY 2
SELECT subscriberKey, ROUND(DATEDIFF('2020-12-20', STR_TO_DATE(subscriptionStartDate, '%Y-%m-%d')) / 365) AS yearsSinceSubscriptionStart
FROM subscription;
#QUERY 3
SELECT subscriptionStartDate, subscriptionLength, 
DATE_FORMAT(DATE_ADD(subscriptionStartDate, INTERVAL subscriptionLength MONTH), '%M %e, %Y') AS subscriptionEndDate 
FROM subscription;
#QUERY 4 ???
select product_name
from bike.product;


#QUERY 5
SELECT product_name, 
       CONCAT('$', FORMAT(list_price / 3, 2)) AS one_payment
FROM bike.product
WHERE RIGHT(product_name, 4) = 2019


