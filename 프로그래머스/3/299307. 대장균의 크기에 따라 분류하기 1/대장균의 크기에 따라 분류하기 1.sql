select ID, if(SIZE_OF_COLONY <= 100, "LOW", 
              if (SIZE_OF_COLONY <= 1000, "MEDIUM", "HIGH")) SIZE
from ecoli_data
order by id