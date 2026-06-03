import pandas as pd

# =====================================
# LOAD DATASET
# =====================================

df = pd.read_excel(
    "data/sample-superstore-subset-excel.xlsx"
)

# =====================================
# DATA OVERVIEW
# =====================================

print("=" * 50)
print("FIRST 5 ROWS")
print("=" * 50)
print(df.head())

print("\n" + "=" * 50)
print("DATASET SHAPE")
print("=" * 50)
print(df.shape)

print("\n" + "=" * 50)
print("COLUMN NAMES")
print("=" * 50)
print(df.columns)

print("\n" + "=" * 50)
print("DATA TYPES")
print("=" * 50)
print(df.dtypes)

# =====================================
# DATA QUALITY ASSESSMENT
# =====================================

print("\n" + "=" * 50)
print("MISSING VALUES")
print("=" * 50)
print(df.isnull().sum())

print("\n" + "=" * 50)
print("DUPLICATE ROWS")
print("=" * 50)
print(df.duplicated().sum())

# =====================================
# DATA CLEANING
# =====================================

# Fill missing values in Product Base Margin

df["Product Base Margin"] = (
    df["Product Base Margin"]
    .fillna(df["Product Base Margin"].median())
)

# Remove duplicates if any

df = df.drop_duplicates()

# =====================================
# DATE CONVERSION
# =====================================

df["Order Date"] = pd.to_datetime(
    df["Order Date"]
)

df["Ship Date"] = pd.to_datetime(
    df["Ship Date"]
)

# =====================================
# FEATURE ENGINEERING
# =====================================

# Create Shipping Days column

df["Shipping Days"] = (
    df["Ship Date"] -
    df["Order Date"]
).dt.days

# =====================================
# VALIDATION AFTER CLEANING
# =====================================

print("\n" + "=" * 50)
print("MISSING VALUES AFTER CLEANING")
print("=" * 50)
print(df.isnull().sum())

print("\n" + "=" * 50)
print("DUPLICATES AFTER CLEANING")
print("=" * 50)
print(df.duplicated().sum())

print("\n" + "=" * 50)
print("NEW COLUMN CREATED")
print("=" * 50)
print(df["Shipping Days"].head())

# =====================================
# BASIC STATISTICS
# =====================================

print("\n" + "=" * 50)
print("STATISTICAL SUMMARY")
print("=" * 50)
print(df.describe())

# =====================================
# SAVE CLEANED DATASET
# =====================================

df.to_csv(
    "output/cleaned_superstore.csv",
    index=False
)

print("\n" + "=" * 50)
print("TASK 1 COMPLETED SUCCESSFULLY")
print("Cleaned dataset saved in output folder")
print("=" * 50)