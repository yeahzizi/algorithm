IF절을 통해 대여 중인 경우 '대여중', 대여 중이 아닌 경우 '대여 가능' 이라고 출력될 것이다.
이때 문제에서 요구하는 '대여 가능'이 되려면,
해당 CAR_ID의 모든 값이 '대여 가능'이여야 '대여 가능' 이라고 판단할 수 있다.
만약 IF절에서 나온 값에 '대여중'과 '대여 가능'이 함께 있다면 이 자동차는 '대여중'이라고 출력되어야 한다.
(다시 말해, '대여 가능' 상태라면 모든 데이터가 '대여 가능'일 경우에만 가능하다.)

SELECT CAR_ID, 
MAX(IF(START_DATE <= '2022-10-16' and END_DATE >= '2022-10-16', "대여중", "대여 가능")) AS AVAILABILITY
from CAR_RENTAL_COMPANY_RENTAL_HISTORY
group by CAR_ID
order by CAR_ID desc