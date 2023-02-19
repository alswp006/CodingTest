-- 코드를 입력하세요
SELECT F.FLAVOR
FROM FIRST_HALF F,ICECREAM_INFO I
where F.FLAVOR=I.FLAVOR AND F.TOTAL_ORDER >=3000 AND I.INGREDIENT_TYPE = 'fruit_based'
group by FLAVOR
order by F.TOTAL_ORDER desc