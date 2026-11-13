-- Q: Do late deliveries get lower review scores?
-- Guess: customers whose orders arrive late give lower scores.
-- Check: compare the average review score of late vs on-time delivered orders.
WITH order_review AS (
    -- some orders have more than one review, so average them to one score per order
    SELECT order_id, AVG(review_score) AS review_score
    FROM order_reviews
    GROUP BY order_id
)
SELECT
    CASE WHEN o.order_delivered_customer_date > o.order_estimated_delivery_date THEN 'Late' ELSE 'On time' END AS delivery,
    COUNT(*) AS orders,
    ROUND(AVG(r.review_score), 2) AS avg_review_score
FROM orders o
JOIN order_review r ON o.order_id = r.order_id
WHERE o.order_status = 'delivered'
  AND o.order_delivered_customer_date IS NOT NULL
GROUP BY delivery
ORDER BY delivery;