import pandas as pd 
import matplotlib.pyplot as plt 

# Load cleaned files globally
patients = pd.read_csv(r"D:\python project files\Health Care Revenue Cycle & Patient Risk Analytics\data\cleaned\clean_patients.csv")
visits   = pd.read_csv(r"D:\python project files\Health Care Revenue Cycle & Patient Risk Analytics\data\cleaned\clean_visits.csv")
claims   = pd.read_csv(r"D:\python project files\Health Care Revenue Cycle & Patient Risk Analytics\data\cleaned\clean_claims.csv")
followups= pd.read_csv(r"D:\python project files\Health Care Revenue Cycle & Patient Risk Analytics\data\cleaned\clean_followups.csv")

print("Files loaded successfully")

def create_patient_features():
    patient_features = visits.groupby("patient_id").agg(
        visit_frequency=("visit_id", "count"),
        total_spend=("treatment_cost", "sum")
    ).reset_index()
    patient_features["total_spend"] = patient_features["total_spend"].round(2)
    print(patient_features.head())
    return patient_features

def readmission_count():
    readmission_counts = followups[followups["readmission_flag"] == "Yes"].groupby(
        "patient_id"
    ).size().reset_index(name="readmission_count")
    print(readmission_counts.head())
    return readmission_counts

def merge_features(patient_features, readmission_counts):
    patient_features = patient_features.merge(
        readmission_counts,
        on="patient_id",
        how="left"
    )
    patient_features["readmission_count"] = patient_features["readmission_count"].fillna(0)
    print(patient_features.head())
    return patient_features

def create_risk_score(patient_features):
    patient_features["risk_score"] = (
        patient_features["visit_frequency"] * 2 +
        patient_features["readmission_count"] * 5
    )
    return patient_features

def risk_segmentation(patient_features):
    def segment_risk(score):
        if score >= 30:
            return "Critical"
        elif score >= 20:
            return "High Risk"
        elif score >= 10:
            return "Moderate"
        else:
            return "Low Risk"

    patient_features["patient_segment"] = patient_features["risk_score"].apply(segment_risk)
    print(patient_features["patient_segment"].value_counts())

    patient_features.to_csv(
        r"D:\python project files\Health Care Revenue Cycle & Patient Risk Analytics\data\processed\patient_features.csv",
        index=False
    )
    print("patient_features.csv created successfully")
    return patient_features

# Wrapper pipeline
def run_feature_engineering():
    pf = create_patient_features()
    rc = readmission_count()
    pf = merge_features(pf, rc)
    pf = create_risk_score(pf)
    pf = risk_segmentation(pf)
    return pf

# Runner pipeline
if __name__ == "__main__":
    run_feature_engineering()
