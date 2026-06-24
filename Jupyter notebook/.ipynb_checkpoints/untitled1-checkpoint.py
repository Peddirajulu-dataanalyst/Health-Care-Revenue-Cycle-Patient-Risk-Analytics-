def clean_data(df):
    import pandas as pd
    import numpy as np

    print("Loading datasets...")

    # Load datasets
    patients = pd.read_csv(r"D:\python project files\Health Care Revenue Cycle & Patient Risk Analytics\data\raw\patients.csv")
    visits = pd.read_csv(r"D:\python project files\Health Care Revenue Cycle & Patient Risk Analytics\data\raw\visits.csv")
    claims = pd.read_csv(r"D:\python project files\Health Care Revenue Cycle & Patient Risk Analytics\data\raw\claims.csv")
    followups = pd.read_csv(r"D:\python project files\Health Care Revenue Cycle & Patient Risk Analytics\data\raw\followups.csv")


    # Generic cleaning function
    def clean_data(df):

        # Remove duplicates
        df = df.drop_duplicates()

        # Clean column names
        df.columns = df.columns.str.strip()

        # Standardize text columns
        for col in df.select_dtypes(include='object').columns:
            df[col] = df[col].astype(str).str.strip()

        # Replace blanks with NaN
        df = df.replace(r'^\s*$', np.nan, regex=True)

        # Fill numeric missing values
        numeric_cols = df.select_dtypes(include=np.number).columns
        for col in numeric_cols:
            df[col] = df[col].fillna(df[col].median())

        # Fill text missing values
        text_cols = df.select_dtypes(include='object').columns
        for col in text_cols:
            df[col] = df[col].fillna("Unknown")

        return df


    print("Cleaning datasets...")

    # Apply cleaning
    patients = clean_data(patients)
    visits = clean_data(visits)
    claims = clean_data(claims)
    followups = clean_data(followups)


    # Convert dates
    patients["registration_date"] = pd.to_datetime(
    patients["registration_date"],
    errors="coerce"
    )

    visits["visit_date"] = pd.to_datetime(
    visits["visit_date"],
    errors="coerce"
    )

    followups["followup_date"] = pd.to_datetime(
    followups["followup_date"],
    errors="coerce"
    ) 


    # Remove invalid treatment costs
    visits = visits[
    visits["treatment_cost"] > 0
    ]

    # Remove invalid claims
    claims = claims[
    claims["claim_amount"] > 0
    ]


    print("Saving cleaned files...")

    # Save cleaned files
    patients.to_csv(
    r"D:\python project files\Health Care Revenue Cycle & Patient Risk Analytics\data\cleaned\clean_patients.csv",
    index=False
    )

    visits.to_csv(
    r"D:\python project files\Health Care Revenue Cycle & Patient Risk Analytics\data\cleaned\clean_visits.csv",
    index=False
    )

    claims.to_csv(
    r"D:\python project files\Health Care Revenue Cycle & Patient Risk Analytics\data\cleaned\clean_claims.csv",
    index=False
    )

    followups.to_csv(
    r"D:\python project files\Health Care Revenue Cycle & Patient Risk Analytics\data\cleaned\clean_followups.csv",
    index=False
    )

    print("Healthcare data cleaning completed successfully.")