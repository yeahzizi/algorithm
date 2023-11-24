// avg 사용법 기억하기
// % 의외로 주의해서 써야 한다..

SELECT A.REST_ID, A.REST_NAME, A.FOOD_TYPE, A.FAVORITES, A.ADDRESS, 
round(AVG(B.REVIEW_SCORE), 2) AS SCORE
from REST_INFO A join  REST_REVIEW B on A.REST_ID = B.REST_ID
where A.ADDRESS LIKE "서울%"
group by A.REST_ID
order by SCORE desc, FAVORITES desc