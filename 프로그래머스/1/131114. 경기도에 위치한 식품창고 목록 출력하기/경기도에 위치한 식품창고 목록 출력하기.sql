-- 코드를 입력하세요
SELECT WAREHOUSE_ID, WAREHOUSE_NAME, ADDRESS, ifnull(FREEZER_YN,"N") FREEZER_YN
from FOOD_WAREHOUSE
where address like "경기도%"
order by 1