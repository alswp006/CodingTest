select count(USER_ID) as USERS
from USER_INFO
where JOINED LIKE '2021%' AND AGE between 20 and 29