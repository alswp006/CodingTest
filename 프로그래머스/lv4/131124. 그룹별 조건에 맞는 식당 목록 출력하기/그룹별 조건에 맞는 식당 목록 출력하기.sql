select M.MEMBER_NAME,R.REVIEW_TEXT,date_format(REVIEW_DATE,'%Y-%m-%d') as REVIEW_DATE
from MEMBER_PROFILE M,REST_REVIEW R
where M.member_id = R.member_id
and R.member_id = (select member_id
                           from REST_REVIEW
                           group by member_id
                           order by count(member_id) desc
                           limit 1)
order by 3,2