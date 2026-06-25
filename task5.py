import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("employees.csv")

# Remove duplicates
df = df.drop_duplicates()

# Fill missing values
for col in df.select_dtypes(include='number').columns:
    df[col] = df[col].fillna(df[col].mean())

for col in df.select_dtypes(include='object').columns:
    df[col] = df[col].fillna("Unknown")

# Save cleaned data
df.to_csv("cleaned_data.csv", index=False)

# Generate report
with open("report.txt", "w") as f:
    f.write(str(df.describe()))

# Create chart
df.select_dtypes(include='number').hist(figsize=(8,6))
plt.tight_layout()
plt.savefig("summary_chart.png")

print("✅ Data Cleaning Completed")