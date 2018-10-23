-- Author: Kai Tanaka

/*
Eucledian distance:
In a plane with 
p1 at (x1, y1) and p2 at (x2, y2), it is sqrt((x1 - x2)^2 + (y1 - y2)^2).
*/

SELECT ROUND(SQRT(POWER(MAX(LAT_N)-MIN(LAT_N),2) + POWER(MAX(LONG_W)-MIN(LONG_W),2)),4)
FROM STATION;