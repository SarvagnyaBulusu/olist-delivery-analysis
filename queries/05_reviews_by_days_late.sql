WITH order_review AS (
    SELECT order_id, AVG(review_score) AS review_score
    FROM order_reviews
    GROUP BY order_id
)
SELECT
    CASE
        WHEN o.order_delivered_customer_date <= o.order_estimated_delivery_date THEN '1. On time'
        WHEN julianday(o.order_delivered_customer_date) - julianday(o.order_estimated_delivery_date) <= 3 THEN '2. 1-3 days late'
        WHEN julianday(o.order_delivered_customer_date) - julianday(o.order_estimated_delivery_date) <= 7 THEN '3. 4-7 days late'
        ELSE '4. 8+ days late'
    END AS delay_bucket,
    COUNT(*) AS orders,
    ROUND(AVG(r.review_score), 2) AS avg_review_score
FROM orders o
JOIN order_review r ON o.order_id = r.order_id
WHERE o.order_status = 'delivered'
  AND o.order_delivered_customer_date IS NOT NULL
GROUP BY delay_bucket
ORDER BY delay_bucket;