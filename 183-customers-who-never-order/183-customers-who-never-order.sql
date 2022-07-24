# Write your MySQL query statement below
select name as 'Customers'
from Customers
where id not in
(select customerid from Orders);

#select name as 'Customers'
#from Customers
#left join Orders
#on Customers.id = Orders.customerid
#where Orders.customerid is null;