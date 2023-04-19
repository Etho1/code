USE magazine;
SELECT subscriberFirstName, subscriberLastName,
	subscriber.subscriberKey, subscriptionStartDate, subscriptionLength
FROM subscriber INNER JOIN subscription 
	ON subscriber.subscriberKey = subscription.subscriberKey
ORDER BY subscriberLastName, subscriptionKey;

SELECT subscriptionKey, subscriptionStartDate, subscriptionLength, m.magazineKey, magazineName
FROM subscription AS s RIGHT OUTER JOIN magazine AS m ON s.magazineKey = m.magazineKey
ORDER BY subscriptionKey;

-- USE v_art;

-- SELECT artist.artist_id, fname, lname, artwork_id, title, artwork.artist_id
-- FROM artist rightouter JOIN artwork ON artist.artist_id = artwork.artist_id
-- ORDER BY artist.artist_id

