USE magazine;

SELECT subscriptionStartDate, subscriptionLength,
	date_format(Date_add(subscriptionstartdate, interval subscriptionlength month), '%M %e, %Y')
    AS 'Subscription end'
FROM subscription