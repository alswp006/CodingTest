-- 코드를 입력하세요
SELECT H.FLAVOR
from FIRST_HALF H 
    join july J
on H.FLAVOR=J.FLAVOR
group by H.FLAVOR
order by H.TOTAL_ORDER+sum(J.TOTAL_ORDER) desc
LIMIT 3