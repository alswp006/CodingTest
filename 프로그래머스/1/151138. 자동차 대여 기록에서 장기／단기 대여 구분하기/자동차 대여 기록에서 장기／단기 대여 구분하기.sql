SELECT HISTORY_ID, CAR_ID, date_format(START_DATE,"%Y-%m-%d") START_DATE, date_format(END_DATE,"%Y-%m-%d") END_DATE, if(datediff(END_DATE,START_DATE)>=29, "장기 대여", "단기 대여") RENT_TYPE
from CAR_RENTAL_COMPANY_RENTAL_HISTORY
where start_date like "2022-09%"
order by 1 desc