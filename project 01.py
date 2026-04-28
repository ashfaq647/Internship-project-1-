# =========================
# 📊 Student Performance Analysis Project
# =========================

# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# =========================
# 1. Load the dataset
# =========================

# Use raw string (r"") to avoid path issues in Windows
df = pd.read_csv(r"D:\signature 11 internship projects\project 1\StudentsPerformance.csv")

# =========================
# 2. Explore the dataset
# =========================

# Show first 5 rows of data
print("\n🔹 First 5 rows of dataset:\n")
print(df.head())

# Show dataset information (data types, null values, etc.)
print("\n🔹 Dataset Info:\n")
print(df.info())

# Check for missing values
print("\n🔹 Missing values in each column:\n")
print(df.isnull().sum())

# Show basic statistical summary
print("\n🔹 Statistical Summary:\n")
print(df.describe())

# =========================
# 3. Basic performance analysis
# =========================

# Calculate average scores for each subject
print("\n📌 Average Scores:")
print("Math Score:", df['math score'].mean())
print("Reading Score:", df['reading score'].mean())
print("Writing Score:", df['writing score'].mean())

# =========================
# 4. Gender-based analysis
# =========================

# Group data by gender and calculate average scores
gender_avg = df.groupby('gender')[['math score', 'reading score', 'writing score']].mean()

print("\n📌 Average Scores by Gender:\n")
print(gender_avg)

# =========================
# 5. Parental education analysis
# =========================

# Analyze math score based on parental education level
parent_avg = df.groupby('parental level of education')['math score'].mean()

print("\n📌 Math Score by Parental Education:\n")
print(parent_avg)

# =========================
# 6. Test preparation effect
# =========================

# Compare students who completed test preparation vs those who didn't
prep_avg = df.groupby('test preparation course')[['math score', 'reading score', 'writing score']].mean()

print("\n📌 Effect of Test Preparation:\n")
print(prep_avg)

# =========================
# 7. Data Visualization
# =========================

# Set style for better-looking plots
sns.set(style="whitegrid")

# -------------------------
# 7.1 Math score distribution
# -------------------------

plt.figure(figsize=(8,5))
df['math score'].hist()
plt.title("Distribution of Math Scores")
plt.xlabel("Math Score")
plt.ylabel("Frequency")
plt.show()

# -------------------------
# 7.2 Average score comparison
# -------------------------

plt.figure(figsize=(8,5))
df[['math score','reading score','writing score']].mean().plot(kind='bar')
plt.title("Average Scores in All Subjects")
plt.ylabel("Score")
plt.show()

# -------------------------
# 7.3 Test preparation effect on reading score
# -------------------------

plt.figure(figsize=(8,5))
sns.barplot(data=df, x="test preparation course", y="reading score")
plt.title("Effect of Test Preparation on Reading Score")
plt.show()