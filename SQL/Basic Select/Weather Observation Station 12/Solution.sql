-- Author: Kai Tanaka

/*
Note: "^..." denotes begging of string while
      "[^...]" denotes any character not listed between the square brackets
*/

SELECT DISTINCT CITY
FROM STATION
WHERE CITY REGEXP  "^[^aeiou].*[^aeiou]$" ;