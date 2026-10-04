import pandas as pd
import numpy as np

# To read the csv files
df = pd.read_csv("../data/Week1_GA_dataset.csv")
#To read other formats
'''
    ".csv": pd.read_csv,
    ".tsv": lambda p, **kw: pd.read_csv(p, sep="\t", **kw),
    ".txt": pd.read_csv,
    ".xlsx": pd.read_excel,
    ".xls": pd.read_excel,
    ".xlsm": pd.read_excel,
    ".json": pd.read_json,
    ".parquet": pd.read_parquet,
    ".pq": pd.read_parquet,
    ".feather": pd.read_feather,
    ".pkl": pd.read_pickle,
    ".pickle": pd.read_pickle,
    ".h5": pd.read_hdf,
    ".hdf5": pd.read_hdf,
    ".dta": pd.read_stata,
    ".sav": pd.read_spss,
'''

# Filtering Or Masking:
'''
# Single condition
mask = df["age"] > 25
filtered_df = df[mask]

# Direct one-liner
filtered_df = df[df["age"] > 25]

# Filter and select specific columns
df.loc[df["age"] > 30, ["name", "salary"]]

# Safe assignment (modifying data conditionally)
df.loc[df["status"] == "pending", "status"] = "resolved"
'''

# 
