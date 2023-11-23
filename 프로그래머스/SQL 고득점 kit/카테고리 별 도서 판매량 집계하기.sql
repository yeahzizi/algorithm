// sum과 count 잘 구분!! 정신차리고 풀어야 한다

SELECT A.CATEGORY, sum(B.SALES) TOTAL_SALES
from BOOK A join BOOK_SALES B on A.BOOK_ID = B.BOOK_ID
where B.SALES_DATE LIKE '%2022-01%'
group by A.CATEGORY
order by A.CATEGORY