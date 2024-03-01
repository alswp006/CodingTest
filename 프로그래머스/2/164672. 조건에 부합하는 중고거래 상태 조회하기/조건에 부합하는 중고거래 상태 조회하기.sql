SELECT BOARD_ID, WRITER_ID, TITLE, PRICE, 
CASE STATUS
when "DONE" then "거래완료"
when "RESERVED" then "예약중"
when "SALE" then "판매중"
END STATUS
from USED_GOODS_BOARD
where CREATED_DATE = "2022-10-05"
order by 1 desc