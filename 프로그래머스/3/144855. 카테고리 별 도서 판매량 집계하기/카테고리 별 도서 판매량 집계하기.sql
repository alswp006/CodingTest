SELECT b.CATEGORY, sum(s.sales) TOTAL_SALES
from book b, book_sales s
where b.book_id = s.book_id and s.sales_date like "2022-01%"
group by 1
order by 1