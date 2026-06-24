#Readmission analysis
#which patients are returning frequently?
SELECT 
    readmission_flag,
    COUNT(*) AS total_cases
FROM followups
GROUP BY readmission_flag;