import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned files globally
patients = pd.read_csv(r"D:\python project files\Health Care Revenue Cycle & Patient Risk Analytics\data\cleaned\clean_patients.csv")
visits   = pd.read_csv(r"D:\python project files\Health Care Revenue Cycle & Patient Risk Analytics\data\cleaned\clean_visits.csv")
claims   = pd.read_csv(r"D:\python project files\Health Care Revenue Cycle & Patient Risk Analytics\data\cleaned\clean_claims.csv")
followups= pd.read_csv(r"D:\python project files\Health Care Revenue Cycle & Patient Risk Analytics\data\cleaned\clean_followups.csv")

print("Files loaded successfully")

# -------------------------
# Patient Age Distribution
# -------------------------
def patient_age_distribution_analysis():
    print("Patient Age Summary:")
    print(patients['age'].describe())  # stats like mean, min, max
    return patients['age']

def patient_age_distribution_plot():
    patients['age'].plot(kind="hist", bins=20, edgecolor="black")
    plt.title("Patient Age Distribution")
    plt.xlabel("Age")
    plt.ylabel("Count")
    plt.show()

# -------------------------
# Department Revenue
# -------------------------
def department_revenue_analysis():
    dept_revenue = visits.groupby("department")["treatment_cost"].sum().sort_values(ascending=False)
    print("Department Revenue Totals:")
    print(dept_revenue)
    return dept_revenue

def department_revenue_plot():
    dept_revenue = department_revenue_analysis()
    dept_revenue.plot(kind="bar")
    plt.title("Department Revenue")
    plt.xlabel("Department")
    plt.ylabel("Revenue")
    plt.show()

# -------------------------
# Claim Status
# -------------------------
def claim_status_analysis():
    claim_status = claims["claim_status"].value_counts()
    print("Claim Status Counts:")
    print(claim_status)
    return claim_status

def claim_status_plot():
    claim_status = claim_status_analysis()
    claim_status.plot(kind="bar")
    plt.title("Claim Status Distribution")
    plt.xlabel("Status")
    plt.ylabel("Count")
    plt.show()

# -------------------------
# Readmission
# -------------------------
def readmission_analysis():
    readmission = followups["readmission_flag"].value_counts()
    print("Readmission Counts:")
    print(readmission)
    return readmission

def readmission_plot():
    readmission = readmission_analysis()
    readmission.plot(kind="bar")
    plt.title("Readmission Analysis")
    plt.xlabel("Readmission")
    plt.ylabel("Count")
    plt.show()

# -------------------------
# Wrapper
# -------------------------
def run_eda():
    print("Running EDA...")

    patient_age_distribution_analysis()
    patient_age_distribution_plot()

    department_revenue_analysis()
    department_revenue_plot()

    claim_status_analysis()
    claim_status_plot()

    readmission_analysis()
    readmission_plot()

    print("EDA completed successfully.")

# Runner pipeline
if __name__ == "__main__":
    run_eda()

    