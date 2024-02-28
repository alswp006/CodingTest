select r.car_id, r.car_type, round(r.daily_fee * 30 *(100 - d.discount_rate)/100) FEE
from CAR_RENTAL_COMPANY_CAR R, (select car_type, discount_rate
                               from CAR_RENTAL_COMPANY_DISCOUNT_PLAN
                               where car_type in ("SUV","세단")
                               and duration_type like "30일%") D
where r.car_id not in (Select car_id from CAR_RENTAL_COMPANY_RENTAL_HISTORY where start_date<'2022-12-00' and end_date>'2022-11-00') and r.car_type = d.car_type
having FEE >= 500000 and FEE < 2000000
order by 3 desc, 2, 1 desc
