select 
CASE
when (a.code & d.skill_code) and (c.code & d.skill_code) then "A"
when b.code & d.skill_code then "B"
when c.code & d.skill_code and !(a.code & d.skill_code) then "C"
end GRADE, d.ID, d.EMAIL
from developers d, 
(select code from skillcodes where name = "Python") a,
(select code from skillcodes where name = "C#") b,
(select sum(code) code from skillcodes where category = "Front end") c
having grade is not null
order by 1,2