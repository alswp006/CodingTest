-- 코드를 입력하세요
SELECT 
year(s.SALES_DATE) YEAR, 
month(s.SALES_DATE) MONTH, 
count(distinct(i.user_id)) PUCHASED_USERS, 
round(count(distinct(i.user_id)) / (select count(*) from USER_INFO where joined like "2021%"), 1) PUCHASED_RATIO
from ONLINE_SALE s, (select user_id, joined from USER_INFO
                    where joined like "2021%") i
where s.user_id = i.user_id
group by month
order by 1, 2