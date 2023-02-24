-- 코드를 입력하세요
SELECT I.ANIMAL_ID,I.ANIMAL_TYPE,I.NAME
from ANIMAL_INS I,ANIMAL_OUTS O
where I.animal_id=O.animal_id
and SEX_UPON_INTAKE like 'intact%'
and SEX_UPON_OUTCOME not like 'intact%'