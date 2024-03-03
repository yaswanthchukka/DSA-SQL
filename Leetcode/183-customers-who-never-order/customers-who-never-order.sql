/* Write your PL/SQL query statement below */

select name as customers
from customers
where id not in (SELECT o.customerid
FROM customers c 
JOIN orders o 
ON c.id = o.customerid);



