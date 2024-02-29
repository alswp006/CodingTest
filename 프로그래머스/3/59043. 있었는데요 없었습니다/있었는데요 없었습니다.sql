select o.animal_id, o.name
from ANIMAL_OUTS o, animal_ins i
where o.animal_id = i.animal_id
and o.datetime<i.datetime
order by i.datetime