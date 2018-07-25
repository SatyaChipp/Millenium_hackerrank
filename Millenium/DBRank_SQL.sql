Question: 
Find number of employees per dept in lexographical order of name
Employee table: ID, NAME, DEPT_ID, AGE
Department table: ID, LOCATION, NAME


"""
/*
Enter your query here.
*/
SELECT 
    DEPARTMENT.NAME, 
    COUNT(EMPLOYEE.ID)
FROM 
    DEPARTMENT
LEFT JOIN 
    EMPLOYEE ON DEPARTMENT.ID = EMPLOYEE.DEPT_ID
GROUP BY 
    DEPARTMENT.ID, 
    DEPARTMENT.NAME
ORDER BY 
    COUNT(EMPLOYEE.ID) DESC, 
    DEPARTMENT.NAME
"""
