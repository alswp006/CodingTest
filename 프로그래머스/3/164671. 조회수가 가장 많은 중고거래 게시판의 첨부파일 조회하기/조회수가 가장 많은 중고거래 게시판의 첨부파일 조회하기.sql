SELECT concat("/home/grep/src/",BOARD_ID,"/",FILE_ID,FILE_NAME,FILE_EXT) FILE_PATH
from USED_GOODS_FILE
where board_id = (select board_id from USED_GOODS_BOARD
                 order by views desc limit 1)
order by file_id desc