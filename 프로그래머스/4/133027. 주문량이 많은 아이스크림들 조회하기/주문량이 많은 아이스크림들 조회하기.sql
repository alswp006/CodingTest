select j.flavor
from july j, first_half h
where h.flavor = j.flavor
group by flavor
order by h.total_order+sum(j.total_order) desc
limit 3