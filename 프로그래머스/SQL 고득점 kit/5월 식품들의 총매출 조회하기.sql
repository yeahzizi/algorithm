SELECT B.PRODUCT_ID, A.PRODUCT_NAME	, sum(B.AMOUNT * A.PRICE) TOTAL_SALES
from FOOD_PRODUCT A join FOOD_ORDER B on A.PRODUCT_ID = B.PRODUCT_ID
where PRODUCE_DATE LIKE "%2022-05%"
group by B.PRODUCT_ID
order by TOTAL_SALES desc, B.PRODUCT_ID