import pandas as pd
import numpy as np

missing_values_list = [
    "inapplicable", "proxy", "refusal", "don't know", "missing",
    "-8", "-1", "-9", "-7", "-2",
    -1, -2, -7, -8, -9
]

print("Reading combined CSV...")

df_renamed = pd.read_csv("/Users/faitholalere/Documents/Masters/Dissertation/Data/Combined Data/combined_core_analysis_v4.csv",
    na_values=missing_values_list,
    low_memory=False
)

# Renaming
print("Renaming columns") #add this to kmow the renaming has began
df_renamed = df_renamed.rename(columns={
    'pidp': 'id',
    'wave': 'wave',
    'year': 'year',
    'sex': 'gender',
    'age_dv': 'age',
    'mstat': 'marital_status',
    'nchild_dv': 'n_children',
    'rach16_dv': 'has_children_under16',
    'jbstat': 'employment_status',
    'jbhrs': 'hours_worked',
    'jbmngr': 'managerial_role',
    'jbsize': 'company_size',
    'jbsoc00_cc': 'current_job_condensed',
    'paygu_dv': 'gross_pay',
    'paynu_dv': 'net_pay',
    'hiqual_dv': 'highest_qualification'
})

# save cleaned file
save_path = "/Users/faitholalere/Documents/Masters/Dissertation/Data/Combined Data/BPHS_UKHLS_clean_renamed.csv"
print(f"Saving cleaned data to {save_path}...")

df_renamed.to_csv(save_path, index=False)

print(f"File saved successfully to: {save_path}")
