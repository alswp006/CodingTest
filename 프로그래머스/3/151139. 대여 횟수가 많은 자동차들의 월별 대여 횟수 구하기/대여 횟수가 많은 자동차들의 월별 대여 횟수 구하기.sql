SELECT MONTH(start_date) MONTH, CAR_ID, count(car_id) RECORDS
from CAR_RENTAL_COMPANY_RENTAL_HISTORY
where car_id in (select car_id
                 from CAR_RENTAL_COMPANY_RENTAL_HISTORY
                 where start_date BETWEEN '2022-08-01' AND '2022-10-31'
                 group by car_id
                 having count(car_id) >= 5)
                 AND START_DATE BETWEEN '2022-08-01' AND '2022-10-31'

group by 1, 2
order by 1, 2 desc