-- Author: Kai Tanaka

SELECT salary * months AS max_salary, COUNT(*)
FROM Employee
GROUP BY max_salary
ORDER BY max_salary DESC
LIMIT 1;