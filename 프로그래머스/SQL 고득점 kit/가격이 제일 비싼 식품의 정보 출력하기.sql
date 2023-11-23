// 아래 두가지 모두 가능
// 의외로 max(price)는 안된다

SELECT *
from FOOD_PRODUCT
order by price desc
LIMIT 1

SELECT *
FROM FOOD_PRODUCT
WHERE PRICE = (SELECT MAX(PRICE) FROM FOOD_PRODUCT);