// and로 묶어줄 수 있다

SELECT A.ANIMAL_ID, A.ANIMAL_TYPE, A.NAME
from ANIMAL_INS A left join ANIMAL_OUTS B ON A.ANIMAL_ID = B.ANIMAL_ID
where A.SEX_UPON_INTAKE LIKE '%Intact%' and (B.SEX_UPON_OUTCOME LIKE '%Spayed%' or B.SEX_UPON_OUTCOME LIKE '%Neutered%')
order by A.ANIMAL_ID