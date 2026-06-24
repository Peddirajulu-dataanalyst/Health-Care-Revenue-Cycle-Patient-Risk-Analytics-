def generate_patients():
    import pandas as pd 
    import numpy as np
    from faker import Faker
    import random

    fake = Faker()

    # Number of patients
    num_patients = 50000

    insurance_list = [
        "Aetna",
        "Blue Cross",
        "Cigna",
        "United Healthcare",
        "Medicure"
    ]

    chronic_conditions = [
        "Diabetes",
        "Hypertension",
        "Heart Disease",
        "Asthma",
        "None"
    ]

    patients = []

    # Loop to generate patients
    for i in range(1, num_patients + 1):
        patient = {
            "patient_id": i,
            "patient_name": fake.name(),
            "age": random.randint(18, 90),
            "gender": random.choice(["Male", "Female"]),
            "city": fake.city(),
            "insurance_provider": random.choice(insurance_list),
            "chronic_condition": random.choice(chronic_conditions),
            "registration_date": fake.date_between(
                start_date='-3y',
                end_date='today'
            )
        }
        patients.append(patient)

    # Convert to dataframe
    patients_df = pd.DataFrame(patients)

    # Save csv
    patients_df.to_csv(
        r"D:\python project files\Health Care Revenue Cycle & Patient Risk Analytics\data\raw\patients.csv",
        index=False
    )

    print("patients.csv created successfully")
    print(patients_df.head())


def generate_visits():
    import pandas as pd
    import numpy as np
    from faker import Faker

    fake = Faker()

    # Load patients
    patients_df = pd.read_csv(
    r"D:\python project files\Health Care Revenue Cycle & Patient Risk Analytics\data\raw\patients.csv"
    )

    # Convert registration_date to datetime
    patients_df['registration_date'] = pd.to_datetime(patients_df['registration_date'])

    # Number of visits
    num_visits = 200000

    # Step 1: Generate base visits with random patient IDs
    visits_df = pd.DataFrame({
       "visit_id": range(1, num_visits + 1),
       "patient_id": np.random.choice(patients_df['patient_id'], num_visits),
       "doctor_id": np.random.randint(1001, 1101, num_visits),
       "treatment_cost": np.round(np.random.uniform(100, 15000, num_visits), 2),
       "payment_status": np.random.choice(["Paid", "Pending", "Denied"], num_visits)
    })

    # Step 2: Merge patient info (registration_date + chronic_condition)
    visits_df = visits_df.merge(
    patients_df[['patient_id', 'registration_date', 'chronic_condition']],
    on='patient_id',
    how='left'
    )

    # Step 3: Ensure visit_date >= registration_date
    visits_df['visit_date'] = visits_df.apply(
    lambda row: fake.date_between(
        start_date=row['registration_date'].date(),
        end_date='today'
    ),
    axis=1
    )

    # Step 4: Define mapping
    condition_map = {
    "Diabetes": {"department": "General Medicine", "diagnosis": "Diabetes"},
    "Hypertension": {"department": "General Medicine", "diagnosis": "Hypertension"},
    "Heart Disease": {"department": "Cardiology", "diagnosis": "Chest Pain"},
    "Asthma": {"department": "Pulmonology", "diagnosis": "Asthma"},
    "None": {"department": "General Medicine", "diagnosis": "Fever"}
    }

    # Step 5: Apply mapping
    visits_df['department'] = visits_df['chronic_condition'].map(
    lambda cond: condition_map.get(cond, {}).get('department', "General Medicine")
    )
    visits_df['diagnosis'] = visits_df['chronic_condition'].map(
    lambda cond: condition_map.get(cond, {}).get('diagnosis', "Fever")
    )

    # Step 6: Randomness override (5% chance)
    randomness_probability = 0.05  # 5% random, 95% correct
    mask = np.random.rand(len(visits_df)) < randomness_probability

    visits_df.loc[mask, 'department'] = np.random.choice(
    ["Cardiology", "Orthopedics", "Neurology", "Emergency", "Pediatrics", "Oncology", "General Medicine"],
    mask.sum()
    )
    visits_df.loc[mask, 'diagnosis'] = np.random.choice(
    ["Diabetes", "Hypertension", "Fracture", "Chest Pain", "Migraine", "Asthma", "Fever", "Cancer"],
    mask.sum()
    )

    # Step 7: Drop helper columns (registration_date + chronic_condition)
    visits_df = visits_df.drop(columns=['registration_date', 'chronic_condition'])

    # Step 8: Save CSV
    visits_df.to_csv(
    r"D:\python project files\Health Care Revenue Cycle & Patient Risk Analytics\data\raw\visits.csv",
    index=False
    )

    print("visits.csv created successfully")
    print(visits_df.head())

def generate_claims():
    import pandas as pd
    import numpy as np
    import random

    # Load visits
    visits_df = pd.read_csv(
        r"D:\python project files\Health Care Revenue Cycle & Patient Risk Analytics\data\raw\visits.csv"
    )

    num_claims = 120000

    claim_status_list = ["Approved", "Pending", "Denied"]
    denial_reasons = ["Incomplete Documents", "Policy Expired", "Coverage Issue",
                      "Duplicate Claim", "Preauthorization Missing", "None"]

    # Sample claims from visits
    sampled_visits = visits_df.sample(num_claims)[['visit_id','patient_id']].reset_index(drop=True)

    claims = []
    for i in range(num_claims):
        visit_id = sampled_visits.loc[i, 'visit_id']
        patient_id = sampled_visits.loc[i, 'patient_id']
        claim_amount = round(random.uniform(500, 20000), 2)
        claim_status = random.choice(claim_status_list)

        if claim_status == "Approved":
            approved_amount = round(claim_amount * random.uniform(0.7, 1.0), 2)
            denial_reason = "None"
        elif claim_status == "Pending":
            approved_amount = 0
            denial_reason = "None"
        else:
            approved_amount = 0
            denial_reason = random.choice(denial_reasons[:-1])  # exclude "None"

        claim = {
            "claim_id": i+1,
            "visit_id": visit_id,
            "patient_id": patient_id,
            "claim_amount": claim_amount,
            "approved_amount": approved_amount,
            "claim_status": claim_status,
            "denial_reason": denial_reason,
            "days_to_settlement": random.randint(1, 90)
        }
        claims.append(claim)

    claims_df = pd.DataFrame(claims)
    claims_df.to_csv(
        r"D:\python project files\Health Care Revenue Cycle & Patient Risk Analytics\data\raw\claims.csv",
        index=False
    )
    print("claims.csv created successfully")
    print(claims_df.head())


def generate_followups():
    import pandas as pd
    import random
    from faker import Faker

    fake = Faker()

    # Load visits
    visits_df = pd.read_csv(
        r"D:\python project files\Health Care Revenue Cycle & Patient Risk Analytics\data\raw\visits.csv"
    )

    # Convert visit_date to datetime
    visits_df['visit_date'] = pd.to_datetime(visits_df['visit_date'])

    num_followups = 100000

    # Sample followups from visits
    sampled_visits = visits_df.sample(num_followups)[['visit_id','patient_id','visit_date']].reset_index(drop=True)

    followups = []
    for i in range(num_followups):
        visit_id = sampled_visits.loc[i, 'visit_id']
        patient_id = sampled_visits.loc[i, 'patient_id']
        visit_date = sampled_visits.loc[i, 'visit_date']

        missed_followup = random.choice(["Yes", "No"])

        if missed_followup == "Yes":
            readmission_flag = random.choices(["Yes", "No"], weights=[70, 30])[0]
        else:
            readmission_flag = random.choices(["Yes", "No"], weights=[20, 80])[0]

        record = {
            "followup_id": i+1,
            "visit_id": visit_id,
            "patient_id": patient_id,
            "followup_date": fake.date_between(start_date=visit_date.date(), end_date='today'),
            "missed_followup": missed_followup,
            "readmission_flag": readmission_flag
        }
        followups.append(record)

    followups_df = pd.DataFrame(followups)
    followups_df.to_csv(
        r"D:\python project files\Health Care Revenue Cycle & Patient Risk Analytics\data\raw\followups.csv",
        index=False
    )
    print("followups.csv created successfully")
    print(followups_df.head())

if __name__ == "__main__":
    generate_patients()
    generate_visits()
    generate_claims()
    generate_followups()
    print("All raw datasets generated successfully.")