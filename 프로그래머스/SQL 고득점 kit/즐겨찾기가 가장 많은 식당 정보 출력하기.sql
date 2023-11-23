// where 절에 저렇게 select문으로 조건을 줄 수 있음

SELECT FOOD_TYPE, REST_ID, REST_NAME, FAVORITES
from REST_INFO 
where FAVORITES in (select max(FAVORITES) from REST_INFO group by FOOD_TYPE)
group by FOOD_TYPE
order by FOOD_TYPE desc