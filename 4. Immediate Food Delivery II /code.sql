SELECT 
    ROUND(
        COALESCE(
            SUM(CASE WHEN customer_pref_delivery_date = order_date THEN 1 ELSE 0 END) * 100.0 / COUNT(customer_id),
            0
        ),
        2
    ) AS immediate_percentage
FROM (
    SELECT 
        customer_id, 
        order_date, 
        customer_pref_delivery_date
    FROM Delivery
    WHERE (customer_id, order_date) IN (
        SELECT customer_id, MIN(order_date)
        FROM Delivery
        GROUP BY customer_id
    )
) AS tbl;
