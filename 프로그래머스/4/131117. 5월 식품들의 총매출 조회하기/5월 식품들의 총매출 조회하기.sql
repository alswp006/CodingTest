select p.product_id, p.PRODUCT_NAME, p.price*o.amount TOTAL_SALES
from FOOD_PRODUCT p, (select product_id, sum(amount) amount from FOOD_ORDER
                     where PRODUCE_DATE like "2022-05%" group by product_id) o
where p.product_id = o.product_id
order by 3 desc, 1