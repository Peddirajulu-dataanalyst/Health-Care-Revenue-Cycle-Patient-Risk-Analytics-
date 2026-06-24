#patient risk segmentation
#which patients are most critical
SELECT 
    patient_segment,
    COUNT(*) AS total_patients,
    AVG(total_spend) AS avg_patient_value
FROM patient_features
GROUP BY patient_segment;