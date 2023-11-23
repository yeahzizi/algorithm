// 중복 제거하고 개수 세는 방법은 아래와 같다 외우자!

SELECT count(distinct name)
from ANIMAL_INS 
where NAME is not null