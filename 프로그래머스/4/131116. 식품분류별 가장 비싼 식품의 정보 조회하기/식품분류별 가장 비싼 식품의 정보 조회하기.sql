-- 코드를 입력하세요
SELECT CATEGORY, price MAX_PRICE, PRODUCT_NAME
from FOOD_PRODUCT
where (price, category) in (select max(price), category
                              from food_product
                              where category in ('과자', '국', '김치', '식용유')
                              group by category)
order by 2 desc