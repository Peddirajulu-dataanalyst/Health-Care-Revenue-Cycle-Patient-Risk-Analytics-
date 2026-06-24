#insurance claim denial
#which insurance providers create most claim denials
SELECT 
    p.insurance_provider,
    COUNT(c.claim_id) AS total_claims,
    SUM(
        CASE 
            WHEN c.claim_status = 'Denied' THEN 1
            ELSE 0
        END
    ) AS denied_claims
FROM patients p
JOIN claims c
ON p.patient_id = c.patient_id
GROUP BY p.insurance_provider;