select ITEM_ID, ITEM_NAME
from ITEM_INFO
where item_id in (select item_id from item_tree where PARENT_ITEM_ID is null)
order by 1