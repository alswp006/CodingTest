-- 코드를 입력하세요
SELECT u.USER_ID, u.NICKNAME, sum(b.price) as TOTAL_SALES
from used_goods_board as b, used_goods_user as u
where (b.board_id, b.price) in (select board_id, sum(price) 
                                from used_goods_board 
                                where used_goods_board.status = "DONE" 
                                group by board_id) 
                                and b.writer_id = u.user_id 
group by u.user_id
having sum(price) >= 700000
order by total_sales