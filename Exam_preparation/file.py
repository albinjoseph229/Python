# Creating a file named "pyimp.py" to store all the important Python programs

file_content = """
# Reading a CSV File
import pandas as pd
df = pd.read_csv('data.csv')
print(df.head())  # Display the first 5 rows of the dataset

# Handling Missing Data
# Drop rows with missing values
df_cleaned = df.dropna()
# Fill missing values with mean
df['column_name'].fillna(df['column_name'].mean(), inplace=True)

# Descriptive Statistics
print(df.describe())  # Summary of statistical measures like mean, median, standard deviation

# Filtering Data
# Filter rows where a column value is greater than a threshold
filtered_data = df[df['column_name'] > 50]
print(filtered_data)

# Group By Functionality
grouped_data = df.groupby('column_name').mean()  # Group by a categorical column and calculate mean
print(grouped_data)

# Numpy Array Operations
import numpy as np
arr = np.array([1, 2, 3, 4])
print(arr + 10)  # Add 10 to each element

# Reshaping Arrays
arr_reshaped = arr.reshape(2, 2)
print(arr_reshaped)

# Numpy Statistics
print(np.mean(arr))
print(np.median(arr))
print(np.std(arr))  # Standard deviation

# DataFrame Creation and Manipulation
data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35], 'Salary': [50000, 60000, 70000]}
df = pd.DataFrame(data)
print(df)

# One-Hot Encoding
df_encoded = pd.get_dummies(df, columns=['Gender'])
print(df_encoded)

# Sorting Data
sorted_df = df.sort_values(by='Salary', ascending=False)  # Sort by salary in descending order
print(sorted_df)

# Normalization (Scaling) of Data
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
df_scaled = scaler.fit_transform(df[['Age', 'Salary']])
print(df_scaled)

# Handling Missing Values in a Dataset
df['column_name'].fillna(df['column_name'].mean(), inplace=True)  # Impute missing values with mean

# Matplotlib Line Plot
import matplotlib.pyplot as plt
plt.plot(df['Age'], df['Salary'])
plt.xlabel('Age')
plt.ylabel('Salary')
plt.title('Age vs Salary')
plt.show()

# Seaborn Pairplot
import seaborn as sns
sns.pairplot(df)
plt.show()

# Bar Plot using Matplotlib
plt.bar(df['Name'], df['Salary'])
plt.xlabel('Name')
plt.ylabel('Salary')
plt.title('Salary Comparison')
plt.show()

# Correlation Heatmap using Seaborn
corr = df.corr()
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.show()

# Train-Test Split and Linear Regression
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

X = df[['Age']]
y = df['Salary']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print('Mean Squared Error:', mean_squared_error(y_test, y_pred))

# Logistic Regression for Classification
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

X = df[['Age']]
y = df['Target']  # Target variable should contain binary classification (0/1)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

classifier = LogisticRegression()
classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)
print('Accuracy:', accuracy_score(y_test, y_pred))

# Principal Component Analysis (PCA)
from sklearn.decomposition import PCA
pca = PCA(n_components=2)
df_pca = pca.fit_transform(df[['Age', 'Salary']])
print(df_pca)

# K-Means Clustering
from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=3)
df['Cluster'] = kmeans.fit_predict(df[['Age', 'Salary']])
print(df)

# Reading and Writing a CSV File
# Reading a CSV file
df = pd.read_csv('file.csv')
print(df.head())

# Writing to a CSV file
df.to_csv('output.csv', index=False)

# Writing and Reading JSON Files
# Writing to a JSON file
df.to_json('output.json', orient='records')
# Reading from a JSON file
df_json = pd.read_json('output.json')
print(df_json.head())

# Random Forest Classifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

X = df[['Age', 'Salary']]
y = df['Target']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

classifier = RandomForestClassifier()
classifier.fit(X_train, y_train)
y_pred = classifier.predict(X_test)
print(classification_report(y_test, y_pred))

# K-Nearest Neighbors (KNN)
from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)

y_pred = knn.predict(X_test)
print('Accuracy:', accuracy_score(y_test, y_pred))
"""

# Writing the content to a Python file
file_path = 'pyimp.py'
with open(file_path, 'w') as f:
    f.write(file_content)
