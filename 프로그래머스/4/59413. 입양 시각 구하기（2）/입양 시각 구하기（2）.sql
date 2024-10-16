SELECT HOUR, COUNT(ANIMAL_ID) AS COUNT
FROM ( SELECT (ROW_NUMBER() over() - 1) AS HOUR
       FROM ANIMAL_OUTS
       LIMIT 24) as a
     LEFT JOIN ANIMAL_OUTS ON HOUR = HOUR(DATETIME)
GROUP BY HOUR
ORDER BY HOUR