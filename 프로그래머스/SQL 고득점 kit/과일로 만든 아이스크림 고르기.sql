# 이게 level1?
SELECT A.FLAVOR
from ICECREAM_INFO AS A join FIRST_HALF AS B on A.FLAVOR = B.FLAVOR
where B.TOTAL_ORDER >= 3000 and A.INGREDIENT_TYPE = "fruit_based"
group by A.FLAVOR
order by B.TOTAL_ORDER desc