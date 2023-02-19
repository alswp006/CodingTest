SELECT  floor(price / 10000) * 10000 as PRICE_GROUP, count(*) as PRODUCTS
from PRODUCT
group by floor(price / 10000) * 10000
order by PRICE_GROUP