#payment delay analysis
#which claims take longest to settle?
CREATE VIEW claim_delay_analysis AS
SELECT 
    claim_status,
    AVG(days_to_settlement) AS avg_days
FROM claims
GROUP BY claim_status;	