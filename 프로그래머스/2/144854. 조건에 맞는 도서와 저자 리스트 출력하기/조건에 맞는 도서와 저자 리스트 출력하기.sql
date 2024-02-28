select b.BOOK_ID, a.AUTHOR_NAME, DATE_FORMAT(b.PUBLISHED_DATE, "%Y-%m-%d")
from book as b, author as a
where a.author_id = b.author_id and b.category = "경제"
order by published_date