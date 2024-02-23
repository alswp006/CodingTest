select h.flavor
from first_half h join july j
on h.flavor = j.flavor
group by flavor
order by h.total_order + sum(j.total_order) desc
limit 3