-- Author: Kai Tanaka

SELECT CITY 
FROM STATION 
WHERE CITY REGEXP "^[aeiou].*[aeiou]$";