SELECT PRODUCT_CODE,sum(P.PRICE*O.SALES_AMOUNT) as SALES
from PRODUCT P,OFFLINE_SALE O
where P.PRODUCT_ID=O.PRODUCT_ID
group by P.PRODUCT_CODE
order by SALES desc,PRODUCT_CODE asc