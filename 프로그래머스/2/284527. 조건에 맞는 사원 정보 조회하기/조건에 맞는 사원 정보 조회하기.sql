select g.SCORE, e.EMP_NO, EMP_NAME, POSITION, EMAIL
from HR_EMPLOYEES e, (select emp_no, sum(score) SCORE
                     from hr_grade
                     where year = "2022"
                     group by emp_no
                     order by 2 desc
                     limit 1) g
where e.emp_no = g.emp_no