#payment delay analysis
#which claims take longest to settle?
SELECT 
    claim_status,
    AVG(days_to_settlement) AS avg_days
FROM claims
GROUP BY claim_status;	