from generate_data import *
from clean_data import *
from eda_analysis import *
from feature_engineering import *

print("Starting Healthcare Analytics Pipeline...")

# Generate datasets
generate_patients()
generate_visits()
generate_claims()
generate_followups()

print("Data generation completed.")

# Clean data
clean_all_data()

print("Data cleaning completed.")

# Run EDA
run_eda()

print("EDA completed.")

# Feature engineering
run_feature_engineering()

print("Feature engineering completed.")

print("Healthcare analytics pipeline completed successfully.")