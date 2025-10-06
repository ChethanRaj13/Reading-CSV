import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
file_path = "data.csv"
data = pd.read_csv(file_path)

# Display basic info
print("🔹 Shape of the dataset:", data.shape)
print("🔹 Column names:", data.columns.tolist())
print("\nFirst 5 rows:\n", data.head())

# Basic statistics
print("\nSummary Statistics:\n", data.describe())

# Check for missing values
print("\nMissing Values:\n", data.isnull().sum())

# Histogram for numeric column
data['Calories'].hist(bins=10, color='lightgreen', edgecolor='black')
plt.title('Calories Distribution')
plt.xlabel('Calories')
plt.ylabel('Count')
plt.show()
