-- Author: Kai Tanaka

SELECT COUNT(city) - COUNT(DISTINCT city)
FROM station;