-- 코드를 입력하세요
SELECT c.CAR_ID,c.CAR_TYPE,round((c.DAILY_FEE-(c.DAILY_FEE*p.discount_rate/100))*30) as FEE
from CAR_RENTAL_COMPANY_CAR c join (select car_type,discount_rate
                                   from CAR_RENTAL_COMPANY_DISCOUNT_PLAN
                                   where DURATION_TYPE='30일 이상') p
on c.car_type = p.car_type
where c.car_id not in (select car_id
               from CAR_RENTAL_COMPANY_RENTAL_HISTORY
               where end_date>'2022-11-00')
and c.car_type in ('세단','SUV')
having 500000<=FEE
and FEE<2000000
order by FEE desc, car_type asc, CAR_ID desc