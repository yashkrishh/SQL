# Write your MySQL query statement below
WITH cte AS (
    SELECT 
        country,
        state,
        amount,
        SUBSTRING(trans_date, 1, 7) AS month  
    FROM 
        Transactions
)
SELECT 
    a.month,
    a.country,
    COALESCE(a.trans_count, 0) AS trans_count,
    COALESCE(b.approved_count, 0) AS approved_count,
    COALESCE(a.trans_total_amount, 0) AS trans_total_amount,
    COALESCE(b.approved_total_amount, 0) AS approved_total_amount
FROM 
    (SELECT 
         month,
         country,
         COUNT(*) AS trans_count,
         SUM(amount) AS trans_total_amount
     FROM 
         cte
     GROUP BY 
         month, country
    ) a
LEFT JOIN
    (SELECT 
         month,
         country,
         COUNT(*) AS approved_count,
         SUM(amount) AS approved_total_amount
     FROM 
         cte
     WHERE 
         state = 'approved'
     GROUP BY 
         month, country
    ) b 
ON 
    a.month = b.month AND (a.country = b.country OR (a.country IS NULL AND b.country IS NULL));
