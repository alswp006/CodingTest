select e.EMP_NO, e.EMP_NAME, g.GRADE GRADE, 
CASE
when GRADE = "S" then e.sal/100*20
when GRADE = "A" then e.sal/100*15
when GRADE = "B" then e.sal/100*10
when GRADE = "C" then 0
END BONUS
from HR_EMPLOYEES e, (select EMP_NO,
                      CASE
                      when sum(score)/2 >= 96 then "S"
                      when sum(score)/2 >= 90 then "A"
                      when sum(score)/2 >= 80 then "B"
                      else "C"
                      END GRADE
                     from hr_grade
                     where year = "2022"
                     group by 1) g
where e.EMP_NO = g.EMP_NO
order by 1