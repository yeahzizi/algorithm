// case when ~ then, when ~ then, else ~, end as ~
// 저거 꼭 기억하기!! 

SELECT ORDER_ID, PRODUCT_ID, DATE_FORMAT(OUT_DATE, '%Y-%m-%d') OUT_DATE,
CASE WHEN DATE_FORMAT(OUT_DATE, '%m-%d') > '05-01' THEN '출고대기'
WHEN DATE_FORMAT(OUT_DATE, '%m-%d') <= '05-01' THEN '출고완료'
ELSE '출고미정'
END AS '출고여부'

from FOOD_ORDER 
order by ORDER_ID