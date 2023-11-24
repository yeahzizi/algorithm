SELECT CATEGORY, PRICE AS MAX_PRICE, PRODUCT_NAME
from FOOD_PRODUCT 
where CATEGORY IN ('과자', '국', '김치', '식용유') and price in (select max(price) from food_product group by category)
group by CATEGORY
order by PRICE desc