def patient_age_distribution_analysis():
    #Load cleaned files 

    import pandas as pd 
    import matplotlib.pyplot as plt 

    patients = pd.read_csv(r"D:\python project files\Health Care Revenue Cycle & Patient Risk Analytics\data\cleaned\clean_patients.csv")
    visits   = pd.read_csv(r"D:\python project files\Health Care Revenue Cycle & Patient Risk Analytics\data\cleaned\clean_visits.csv")
    claims   = pd.read_csv(r"D:\python project files\Health Care Revenue Cycle & Patient Risk Analytics\data\cleaned\clean_claims.csv")
    followups= pd.read_csv(r"D:\python project files\Health Care Revenue Cycle & Patient Risk Analytics\data\cleaned\clean_followups.csv")
    print("Files loaded successfully")

def department_revenue_analysis():
    #department revenue

    dept_revenue = visits.groupby(  
        "department"
    )["treatment_cost"].sum().sort_values(
        ascending=False
    )
    print(dept_revenue)

def department_revenue_plot: 
    dept_revenue.plot(kind="bar")

    plt.title("Department Revenue")
    plt.xlabel("Department")
    plt.ylabel("Revenue")

    plt.show()

def claim_status_analysis():
    #claim status analysis

    claim_status = claims[
        "claim_status"
        ].value_counts()
    print(claim_status)
    
def claim_status_plot():
    claim_status.plot(kind="bar")
    plt.title("Claim Status Distribution")
    plt.xlabel("Status")
    plt.ylabel("Count")
    plt.show()

def readmission():
    readmission = followups[
        "readmission_flag"
        ].value_counts()
print(readmission)

def readmission_plot():
    readmission.plot(kind="bar")
    plt.title("Readmission Analysis")
    plt.xlabel("Readmission")
    plt.ylabel("Count")
    plt.show()