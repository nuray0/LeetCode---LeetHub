# Write your MySQL query statement below
select a.name as 'Employee'
from Employee as a, Employee as b
where a.managerid = b.id
and a.salary > b.salary;
