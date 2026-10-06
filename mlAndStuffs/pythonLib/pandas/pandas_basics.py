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

# Handeling Missing data/null values:
'''
# Detection:
    df.isna() # True or False
    df.isna().sum() # no. of NaN count per column
    df.isna().sum().sum() #no. of NaN overall

# Filtering:
    df[df["col"].isna()] # Rows where 'col' is NaN
    df[df["col"].notna()] # Rows where 'col' is NOT NaN

# Dropping:
    df.dropna() # Drops the rows with any NaN
    df.dropna(how="all") # Drops rows where all values are NaN
    df.dropna(axis=1) # Drop columns with any NaN

# Filling:
    df.fillna(0) # Fill all the NaN with 0
'''

# Shape and others things:
'''
# Dimensions & Size:
    df.shape                             # (rows, cols) tuple e.g. (1000, 15)
    df.shape[0]                          # Row count
    df.shape[1]                          # Column count
    df.size                              # Total cells (rows * cols)
    df.ndim                              # Dimensions (always 2 for DataFrame, 1 for Series)

# Quick View & Stats:
    df.head(5)                           # First 5 rows
    df.tail(5)                           # Last 5 rows
    df.sample(5)                         # Random 5 rows
    df.describe()                        # Summary stats (mean, std, min, quartiles, max)
    df.describe(include="all")           # Summary stats including categorical/text
    df.nunique()                         # Distinct value count per column
'''

# Indexing and Slicing:
'''
# Core Difference:
## .loc  -> Label-based (uses row index names and column names; INCLUSIVE of end)
## .iloc -> Integer/Position-based (uses 0-indexed positions; EXCLUSIVE of end like standard Python)

# .loc (Label-based):
    df.loc[i] # ith rows
    df.loc[0:5,"col_a"] # # Rows labeled 0 through 5 (INCLUSIVE) of 'col_a'
    df.loc[0:4, "age":"salary"]          # Slice columns from 'age' to 'salary' inclusive

# .iloc (Position-based):
    df.iloc[0]                           # Very first row (position 0)
    df.iloc[-1]                          # Very last row
    df.iloc[::2 ]                        # Even
    df.iloc[1::2]                        # Odd
    df.iloc[0:5, 0]                      # Rows 0-4 (EXCLUSIVE of 5), first column (col 0)
    df.iloc[0:10, 2:5]                   # Sub-grid: rows 0-9, columns 2-4
'''


