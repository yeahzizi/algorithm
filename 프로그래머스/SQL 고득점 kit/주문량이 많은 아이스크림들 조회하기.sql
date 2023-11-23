// JULY 테이블의 FLAVOR는 
// FIRST_HALF 테이블의 FLAVOR의 외래 키입니다. 

SELECT A.FLAVOR
from FIRST_HALF A left join JULY B on A.FLAVOR = B.FLAVOR
group by A.FLAVOR
order by sum(A.TOTAL_ORDER + B.TOTAL_ORDER) desc
LIMIT 3