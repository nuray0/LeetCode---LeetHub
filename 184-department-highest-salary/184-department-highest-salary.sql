# Write your MySQL query statement below

SELECT
    Department.name AS 'Department',
    Employee.name AS 'Employee',
    Employee.salary as 'Salary'
FROM
    Employee,
    Department
WHERE
    Employee.DepartmentId = Department.Id
    and (Employee.DepartmentId , Salary) IN
    (   SELECT
            DepartmentId, MAX(Salary)
        FROM
            Employee
        GROUP BY DepartmentId
    )
;