-- Author: Kai Tanaka

-- Ceil: round to NEXT integer

SELECT CEIL(AVG(Salary) - AVG(REPLACE(Salary,"0","")))
FROM EMPLOYEES;