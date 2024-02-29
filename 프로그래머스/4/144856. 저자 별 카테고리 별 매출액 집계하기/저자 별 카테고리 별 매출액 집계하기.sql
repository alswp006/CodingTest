-- 코드를 입력하세요
SELECT b.AUTHOR_ID, a.AUTHOR_NAME, b.CATEGORY, sum(b.price*s.sales) TOTAL_SALES
from book b, author a, (select book_id, sales from book_sales 
                   where sales_date like "2022-01%") s
where b.author_id = a.author_id and b.book_id = s.book_id
group by category, author_name
order by 1, 3 desc