select p.MEMBER_NAME, r.REVIEW_TEXT, date_format(r.REVIEW_DATE,"%Y-%m-%d")
from MEMBER_PROFILE p, REST_REVIEW r
where p.member_id = (select member_id from REST_REVIEW
                     group by member_id
                     order by count(member_id) desc
                    limit 1)
and p.member_id = r.member_id
order by 3, 2