-- 코드를 입력하세요
SELECT NAME,DATETIME
from animal_ins
where animal_id not in(select animal_id from animal_outs)
order by datetime asc
limit 3