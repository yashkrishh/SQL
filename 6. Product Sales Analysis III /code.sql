# Write your MySQL query statement below
select product_id,year first_year,quantity,price
from Sales 
where (product_id,year)
in
(select product_id,min(year) year from Sales group by product_id)
