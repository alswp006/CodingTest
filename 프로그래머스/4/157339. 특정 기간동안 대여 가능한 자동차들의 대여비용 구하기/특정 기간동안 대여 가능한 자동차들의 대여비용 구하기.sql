-- 코드를 입력하세요
SELECT c.CAR_ID,c.CAR_TYPE,round((c.DAILY_FEE-(c.DAILY_FEE*p.discount_rate/100))*30) as FEE
from CAR_RENTAL_COMPANY_CAR c, (select car_type,discount_rate
                                   from CAR_RENTAL_COMPANY_DISCOUNT_PLAN
                                   where DURATION_TYPE like '30%'
                                   and car_type in ('SUV','세단')) p
where c.CAR_TYPE=p.car_type
and c.car_id not in (select car_id from CAR_RENTAL_COMPANY_RENTAL_HISTORY
               where start_date<'2022-12-00' and end_date>'2022-11-00')
having FEE>=500000 and FEE<2000000
order by 3 desc,2,1 desc