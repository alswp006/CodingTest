-- 코드를 입력하세요
SELECT distinct CAR_ID
from CAR_RENTAL_COMPANY_RENTAL_HISTORY
where car_id in (select car_id from CAR_RENTAL_COMPANY_CAR
                where car_type = "세단")
and start_date like "2022-10%"
order by 1 desc
