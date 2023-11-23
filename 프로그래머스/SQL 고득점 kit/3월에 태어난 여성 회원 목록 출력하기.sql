// month로 할 때 그냥 = 3으로 해도 되더라

SELECT MEMBER_ID, MEMBER_NAME, GENDER, DATE_FORMAT(DATE_OF_BIRTH, '%Y-%m-%d') DATE_OF_BIRTH
from MEMBER_PROFILE 
where GENDER = "W" and MONTH(DATE_OF_BIRTH) = '03' and TLNO is not null
order by MEMBER_ID