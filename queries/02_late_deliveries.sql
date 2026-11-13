-- Q: How often are delivered orders late, and how long does delivery take?
-- Worry: customers seem unhappy. Guess: orders arrive later than promised.
-- Late = delivered after the estimated delivery date shown to the customer.
SELECT
    COUNT(*) AS delivered_orders,
    SUM(CASE WHEN order_delivered_customer_date > order_estimated_delivery_date THEN 1 ELSE 0 END) AS late_orders,
    ROUND(100.0 * SUM(CASE WHEN order_delivered_customer_date > order_estimated_delivery_date THEN 1 ELSE 0 END) / COUNT(*), 2) AS pct_late,
    ROUND(AVG(julianday(order_delivered_customer_date) - julianday(order_purchase_timestamp)), 1) AS avg_days_to_deliver
FROM orders
WHERE order_status = 'delivered'
  AND order_delivered_customer_date IS NOT NULL;