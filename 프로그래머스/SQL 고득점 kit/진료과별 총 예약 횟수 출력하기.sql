SELECT MCDP_CD AS 진료과코드, count(MCDP_CD) AS 5월예약건수
from APPOINTMENT 
where APNT_YMD LIKE "%2022-05%"
group by MCDP_CD
order by 5월예약건수, MCDP_CD