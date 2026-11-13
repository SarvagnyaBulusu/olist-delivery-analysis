-- Q: What share of orders were actually delivered?
-- Why: before analysing delivery and reviews, check how many orders are usable.
SELECT
    order_status,
    COUNT(*) AS orders,
    ROUND(100.0 * COUNT(*) / (SELECT COUNT(*) FROM orders), 2) AS pct_of_orders
FROM orders
GROUP BY order_status
ORDER BY orders DESC;