-- 코드를 입력하세요
SELECT ANIMAL_ID, NAME, if(SEX_UPON_INTAKE like "%Neutered%" or SEX_UPON_INTAKE like "%Spayed%", "O", "X") 중성화
from ANIMAL_INS
order by animal_id