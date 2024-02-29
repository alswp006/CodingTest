-- 코드를 입력하세요
SELECT i.ANIMAL_ID, i.NAME
from ANIMAL_INS i, ANIMAL_OUTS o
where i.animal_id = o.animal_id
order by datediff(o.datetime, i.datetime) desc
limit 2