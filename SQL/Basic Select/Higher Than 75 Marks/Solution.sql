-- Author: Kai Tanaka


/*
    RIGHT ( character_expression , integer_expression )
    
    Returns the right part of a character string with the specified number of characters.
*/
SELECT NAME 
FROM STUDENTS
WHERE MARKS > 75
ORDER BY RIGHT(NAME,3) ,ID ASC;