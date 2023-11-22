// WHERE 절은 테이블의 레코드 전체에서 필터링을 수행하고, 
// HAVING 절은 그룹화된 결과에서 필터링을 수행

SELECT NAME, COUNT(NAME) AS COUNT
from ANIMAL_INS 
where NAME is not null
group by NAME
having COUNT(NAME) >= 2
order by NAME