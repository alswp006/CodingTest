SELECT YEAR(o.SALES_DATE) YEAR, MONTH(o.SALES_DATE) MONTH, i.GENDER, count(distinct(i.user_id)) USERS
from ONLINE_SALE o, (select user_id, gender
                    from user_info
                    where gender is not null) i
where o.user_id = i.user_id
group by 1, 2, 3
order by 1, 2, 3