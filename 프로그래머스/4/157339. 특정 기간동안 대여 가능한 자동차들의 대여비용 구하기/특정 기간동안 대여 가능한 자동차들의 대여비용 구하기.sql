select c.car_id, c.car_type,round((c.daily_fee-(c.daily_fee*d.discount_rate/100))*30) FEE
from car_rental_company_car c, (select car_type, discount_rate
                               from car_rental_company_discount_plan
                               where duration_type like "30일%"
                               and car_type in ("SUV", "세단")) d
WHERE c.car_type = d.car_type and c.car_id NOT IN (
    SELECT car_id 
    FROM car_rental_company_rental_history
    where start_date<'2022-12-00' and end_date>'2022-11-00'
)
having FEE>=500000 and FEE<2000000
order by 3 desc, 2, 1 desc