import pandas as pd

# Load dataset
df = pd.read_csv("dataset/netflix_titles.csv")

print("Original Shape:", df.shape)

# Missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Remove duplicates
df = df.drop_duplicates()

# Standardize column names
df.columns = df.columns.str.lower().str.replace(" ", "_")

# Fill missing values
df["director"] = df["director"].fillna("Unknown")
df["cast"] = df["cast"].fillna("Unknown")
df["country"] = df["country"].fillna("Unknown")
df["rating"] = df["rating"].fillna("Not Rated")

# Convert date format
df["date_added"] = pd.to_datetime(df["date_added"], errors="coerce")

# Remove extra spaces
for col in df.select_dtypes(include="object").columns:
    df[col] = df[col].str.strip()

# Save cleaned dataset
df.to_csv("dataset/cleaned_netflix_dataset.csv", index=False)

print("\nCleaned Shape:", df.shape)
print("\nData Types:")
print(df.dtypes)

print("\nCleaning Completed Successfully!")