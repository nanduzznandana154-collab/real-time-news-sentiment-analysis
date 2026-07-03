SELECT * FROM news_data;
Count total news articles
SELECT COUNT(*) AS total_news
FROM news_data;


SELECT sentiment, COUNT(*) AS total
FROM news_data
GROUP BY sentiment;

SELECT *
FROM news_data
WHERE sentiment = 'Positive';


SELECT *
FROM news_data
WHERE sentiment = 'Negative';


SELECT *
FROM news_data
WHERE sentiment = 'Neutral';