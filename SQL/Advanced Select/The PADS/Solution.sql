-- Author: Kai Tanaka

-- First query
SELECT CONCAT(Name,"(", LEFT(Occupation,1),")") as Name
FROM OCCUPATIONS
ORDER BY Name;

-- Second query
SELECT CONCAT("There are a total of ", COUNT(Occupation), " " ,LOWER(Occupation),"s.")
FROM OCCUPATIONS
GROUP BY Occupation
ORDER BY COUNT(Occupation),Occupation;