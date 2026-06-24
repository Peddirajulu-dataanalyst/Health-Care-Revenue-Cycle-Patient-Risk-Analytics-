# Department Revenue
#which hospital departments generate the highest revenue?
CREATE VIEW department_revenue AS
SELECT 
    department,
    COUNT(visit_id) AS total_visits,
    SUM(treatment_cost) AS total_revenue,
    AVG(treatment_cost) AS avg_revenue_per_visit
FROM visits
GROUP BY department
ORDER BY total_revenue DESC;