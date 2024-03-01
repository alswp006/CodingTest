select d.DEPT_ID, d.DEPT_NAME_EN, round(sum(SAL)/count(*),0) AVG_SAL
from HR_DEPARTMENT d, HR_EMPLOYEES e
where d.dept_id = e.dept_id
group by 1
order by 3 desc