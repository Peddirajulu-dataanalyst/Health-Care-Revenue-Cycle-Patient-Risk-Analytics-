#pareto analysis
#do top patients contribute most revenue?
SELECT *
FROM (
    SELECT 
        patient_id,
        total_spend,
        NTILE(5) OVER (
            ORDER BY total_spend DESC
        ) AS bucket
    FROM patient_features
) t
WHERE bucket = 1;
