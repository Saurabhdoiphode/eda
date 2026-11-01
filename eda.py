
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Social_Network_Ads.csv")

print(df.head())
print("Shape:", df.shape)
df.info()

print("Missing values:")
print(df.isnull().sum())

print(df.describe())

# Age Distribution
plt.hist(df["Age"], bins=10)
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()

# Estimated Salary Boxplot
sns.boxplot(x=df["EstimatedSalary"])
plt.title("Estimated Salary Boxplot")
plt.show()

# Correlation Matrix
sns.heatmap(
    df[["Age", "EstimatedSalary", "Purchased"]].corr(),
    annot=True,
    cmap="coolwarm"
)
plt.title("Correlation Matrix")
plt.show()

# Purchase Distribution
sns.countplot(x=df["Purchased"])
plt.title("Purchase Distribution")
plt.xlabel("Purchased (0 = No, 1 = Yes)")
plt.show()
