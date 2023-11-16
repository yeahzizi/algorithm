SELECT P.PRODUCT_CODE, sum(SALES_AMOUNT * PRICE) AS SALES
from PRODUCT P JOIN OFFLINE_SALE O ON P.PRODUCT_ID = O.PRODUCT_ID
group by O.PRODUCT_ID
order by SALES DESC, P.PRODUCT_CODE