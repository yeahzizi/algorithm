SELECT B.USER_ID, B.NICKNAME,  
concat(CITY, ' ', STREET_ADDRESS1, ' ', STREET_ADDRESS2) AS 전체주소, 
concat(substr(TLNO, 1, 3), '-', substr(TLNO, 4, 4), '-', substr(TLNO, 8, 4)) AS 전화번호
from USED_GOODS_BOARD A join USED_GOODS_USER B on A.WRITER_ID = B.USER_ID
where B.USER_ID in (select WRITER_ID from USED_GOODS_BOARD group by  WRITER_ID having count(*) >= 3)
group by B.USER_ID
order by B.USER_ID desc