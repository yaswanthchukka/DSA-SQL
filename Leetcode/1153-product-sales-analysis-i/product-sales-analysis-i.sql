/* Write your PL/SQL query statement below */
select Product.product_name,Sales.year,Sales.price
from Sales
left join Product
on Product.product_id=sales.product_id;