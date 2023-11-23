// 매우 어려웠다.. 
group by 에 두개를 넣어주면 두개가 묶여서 다님

SELECT USER_ID, PRODUCT_ID
from ONLINE_SALE 
group by USER_ID, PRODUCT_ID
having count(*) > 1
order by USER_ID, PRODUCT_ID DESC