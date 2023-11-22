// 문제 잘 읽기! limit가 있을 수 있다

SELECT A.NAME, A.DATETIME
from ANIMAL_INS A left join ANIMAL_OUTS B ON A.ANIMAL_ID = B.ANIMAL_ID
where B.ANIMAL_ID is null
order by A.DATETIME
LIMIT 3