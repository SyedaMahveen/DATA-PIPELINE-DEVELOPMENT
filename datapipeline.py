import pandas as pd
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler

print("🚀 Starting Data Pipeline...")

# ✅ Extract
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['target'] = iris.target
print("✅ Raw Data Loaded!")
print(df.head())

# ✅ Save raw data before cleaning
df.to_csv("raw_data.csv", index=False)
print("✅ Raw data saved as 'raw_data.csv'")

# ✅ Preprocessing
df.loc[0:5, 'sepal length (cm)'] = None  
print("\nMissing Values Before Cleaning:")
print(df.isnull().sum())
df.fillna(df.mean(), inplace=True)
print("\n✅ Missing Values Handled!")
print(df.isnull().sum())

# ✅ Transformation
scaler = StandardScaler()
scaled_data = scaler.fit_transform(df.iloc[:, :-1])
df_scaled = pd.DataFrame(scaled_data, columns=iris.feature_names)
df_scaled['target'] = df['target']
print("\n✅ Data Transformation Complete!")
print(df_scaled.head())

# ✅ Save cleaned & transformed data
df_scaled.to_csv("cleaned_data.csv", index=False)
print("\n✅ Data Pipeline Complete! Cleaned data saved as 'cleaned_data.csv'")
