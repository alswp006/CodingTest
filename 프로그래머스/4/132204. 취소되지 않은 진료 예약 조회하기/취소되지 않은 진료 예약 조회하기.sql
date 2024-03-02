-- 코드를 입력하세요
SELECT a.APNT_NO, p.PT_NAME, a.PT_NO, a.MCDP_CD, d.DR_NAME, a.APNT_YMD
from (select * from APPOINTMENT where apnt_ymd like "2022-04-13%"
     and APNT_CNCL_YN = "N" and MCDP_CD = "CS") a, 
     DOCTOR d, PATIENT p
where a.mddr_id = d.dr_id and a.pt_no = p.pt_no
order by 6