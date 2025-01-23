select a.user_id,round(COALESCE((cnt2/cnt1),0),2) confirmation_rate
from
(select * from Signups) a
left join (select user_id,count(*) cnt1 from Confirmations group by user_id) b
on a.user_id = b.user_id
left join (select user_id,count(*) cnt2 from Confirmations where action = 'confirmed' group by user_id) c
on a.user_id = c.user_id
