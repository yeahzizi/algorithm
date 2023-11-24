WITH RECURSIVE HOURS AS (
    SELECT 0 AS NUM 
    UNION ALL
    SELECT NUM+1 FROM HOURS
    WHERE NUM < 23
)

SELECT HOURS.NUM AS HOUR, COUNT(AO.ANIMAL_ID) AS COUNT
FROM ANIMAL_OUTS AS AO
RIGHT JOIN HOURS ON HOUR(AO.DATETIME) = HOURS.NUM
GROUP BY HOURS.NUM
ORDER BY HOUR