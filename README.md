 📌  Project Overview 

This project simulates a real-world hospital analytics environment focused on improving operational efficiency, patient care quality, insurance claim performance, and financial sustainability. 

The project was built end-to-end using Python, MySQL, Power BI, and Tableau following a real data analyst workflow. 

🎯 Business Problem 

. Healthcare organizations often face: 
. High patient readmission rates 
. Insurance claim denials 
. Delayed settlements 
. Missed follow-up appointments 
. Revenue leakage across departments 

The objective of this project is to use analytics to identify operational risks, improve collections, and enhance patient outcomes. 

🎯 Project Objectives 

. Identify high-risk patients 
. Analyze insurance claim approval and denial trends 
. Measure department-level profitability 
. Track patient follow-up adherence 
. Reduce readmission risks 
. Improve revenue cycle performance 

🛠 Tech Stack 

. Python 
. Pandas 
. NumPy 
. Jupyter Notebook 
. MySQL 
. Power BI 
. Tableau 

🗂 Dataset Design 

The project contains 5 connected datasets linked by: 

patient_id 

1. patients.csv 

Contains patient master information. 

Columns: 

. patient_id 
. patient_name 
. age 
. gender 
. city 
. insurance_provider 
. chronic_condition 
. registration_date 

Rows: 50,000 

2. visits.csv 

Contains hospital visits. 

Columns: 

. visit_id 
. patient_id 
. visit_date 
. department 
. doctor_id 
. diagnosis 
. treatment_cost 
. payment_status 

Rows: 200,000 

3. claims.csv 

Contains insurance claims. 

Columns: 

. claim_id 
. patient_id 
. claim_amount 
. approved_amount 
. claim_status 
. denial_reason 
. days_to_settlement 

Rows: 120,000 

4. followups.csv 

Contains follow-up adherence data. 

Columns: 

. patient_id 
. followup_date 
. missed_followup 
. readmission_flag 

Rows: 100,000 

5. patient_features.csv 

Contains engineered business features. 

Columns: 

. patient_id 
. visit_frequency 
. total_spend 
. readmission_count 
. risk_score 
. patient_segment 

🟦 Project Workflow 

Step 1 —🟦 Data Generation 

Generated synthetic healthcare data using Python. 

Created realistic hospital scenarios: 

. Older patients → higher readmission probability 
. Frequent visitors → higher healthcare cost 
. Missed follow-ups → higher risk 

Step 2 —🧹 Data Cleaning 

Performed automated cleaning: 

. Removed duplicates 
. Standardized text values 
. Converted date columns 
. Handled missing values 
. Removed invalid cost records 

Output: 

. clean_patients.csv 
. clean_visits.csv 
. clean_claims.csv 
. clean_followups.csv 

Step 3 —📊 Exploratory Data Analysis (EDA) 

Performed analysis on: 

Patient Demographics 

. Age distribution 
. Gender distribution 

Financial Analysis 

. Department revenue 
. Visit patterns 

Claims Analysis 

. Approved vs denied claims 

Patient Risk Analysis 

. Follow-up adherence 
. Readmission behavior 

Step 4 —⚙ Feature Engineering 

Created business features: 

Visit Frequency 

Number of patient visits. 

Total Spend 

Total patient treatment value. 

Readmission Count 

Number of readmissions. 

Risk Score 

Calculated using: 

Risk Score = Visit Frequency + Readmission Behavior 

Patient Segments 

Created: 

. Low Risk 
. Moderate 
. High Risk 
. Critical 

Step 5 — 🗄 SQL Business Analysis 

Created analytical views. 

Department Profitability 

Measured: 

. Total visits 
. Total revenue 
. Average revenue per visit 

Insurance Denial Analysis 

Measured: 

. Total claims 
. Denied claims 
. Provider-level risk 

Patient Risk Segmentation 

Measured: 

. Patient counts 
. Average spend 

Readmission Analysis 

Measured: 

. Follow-up effectiveness 

Claim Settlement Analysis 

Measured: 

. Average settlement days 

Pareto Analysis 

Identified: 

Top 20% patients contributing most revenue. 

Step 6 —📈 Dashboard Development 

Built dashboards in Power BI and Tableau. 

Dashboard Pages 

1. Executive Dashboard 

KPIs: 

. Total Patients 
. Total Visits 
. Total Revenue 
. Claim Approval Rate 
. Readmission Rate 

2. Department Performance 

. Revenue by department 
. Visit volume 

3. Insurance Analytics 

. Claims by status 
. Provider denial trends 

4. Patient Risk Analytics 

. Risk segmentation 
. Patient value 

5. Follow-up & Readmission 

. Missed follow-up 
. Readmission trends 

Step 7 — Advanced Dashboard Filters 

Implemented interactive slicers: 

. Age Group 
. Gender 
. Department 
. Insurance Provider 
. City 

🔍  Key Business Insights 

1. High-risk patients showed significantly higher readmission behavior. 
2. Certain insurance providers showed elevated denial and pending claim ratios. 
3. Cardiology and Emergency departments contributed highest revenue. 
4. Missed follow-up patients had higher readmission probability. 

💡 Business Recommendations 

Revenue Optimization 

. Improve staffing in high-performing departments. 

Claims Optimization 

. Review insurers with high denial rates. 

Patient Care Optimization 

. Create proactive interventions for critical patients. 

Operational Improvement 

. Automate follow-up reminders.

🚀 Business Impact 

This analytics solution can help healthcare organizations: 

. Improve patient outcomes 
. Reduce operational inefficiencies 
. Improve collections 
. Lower readmission costs 
. Increase profitability 

🏁 Project Outcome 

This project demonstrates end-to-end healthcare analytics capabilities across: 

Data Engineering → Business Analysis → Dashboarding → Strategic Decision Support 
