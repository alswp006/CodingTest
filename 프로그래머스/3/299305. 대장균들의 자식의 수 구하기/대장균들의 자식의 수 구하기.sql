select ID, (select count(*)
           from ecoli_data e2
           where e1.id = e2.parent_id) CHILD_COUNT
from ecoli_data e1
order by id