
# Important Codes for MCA306 Data Analytics using Python

# 1. Calculator Program
def calculator():
    while True:
        operation = input("Enter operation (+, -, *, /) or 'exit' to stop: ")
        if operation == 'exit':
            break
        if operation in ('+', '-', '*', '/'):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                if operation == '+':
                    print(f"Result: {num1 + num2}")
                elif operation == '-':
                    print(f"Result: {num1 - num2}")
                elif operation == '*':
                    print(f"Result: {num1 * num2}")
                elif operation == '/':
                    print(f"Result: {num1 / num2}")
            except ValueError:
                print("Invalid input. Please enter numbers.")
        else:
            print("Invalid operation.")
            
# 2. Set Operations
def set_operations():
    set1 = {1, 2, 3, 4, 5}
    set2 = {4, 5, 6, 7, 8}
    print(f"Union: {set1 | set2}")
    print(f"Intersection: {set1 & set2}")
    print(f"Difference: {set1 - set2}")
    
# 3. Dictionary to store factorials
def factorial(n):
    factorials = {}
    fact = 1
    for i in range(1, n+1):
        fact *= i
        factorials[i] = fact
    return factorials

# 4. MySQL Connection using Python
import mysql.connector
def mysql_connection():
    conn = mysql.connector.connect(host="localhost", user="root", password="password", database="test_db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    for row in cursor.fetchall():
        print(row)
    conn.close()

# 5. Handle Missing Values in Data
import pandas as pd
def handle_missing_values():
    df = pd.read_csv('data.csv')
    df.fillna(df.mean(), inplace=True)
    print(df.head())

# 6. Convert Categorical to Numerical Values
def convert_categorical():
    df = pd.DataFrame({'gender': ['Male', 'Female', 'Female', 'Male'], 'age': [23, 21, 22, 24]})
    df['gender'] = df['gender'].map({'Male': 1, 'Female': 0})
    print(df)

# 7. Numpy Operations (Matrix Multiplication)
import numpy as np
def matrix_multiplication():
    mat1 = np.array([[1, 2], [3, 4]])
    mat2 = np.array([[5, 6], [7, 8]])
    result = np.dot(mat1, mat2)
    print(result)

# 8. Pandas Dataframe Operations (Handling Missing Data)
def pandas_operations():
    df = pd.read_csv('dirtydata.csv')
    df.dropna(inplace=True)  # Remove rows with missing values
    print(df)

# 9. Matplotlib Visualization (Line Plot)
import matplotlib.pyplot as plt
def plot_graph():
    x = [1, 2, 3, 4]
    y = [10, 20, 25, 30]
    plt.plot(x, y)
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Line Plot Example')
    plt.show()

# 10. Scikit-learn Linear Regression
from sklearn.linear_model import LinearRegression
def linear_regression():
    df = pd.read_csv('boston.csv')
    X = df[['RM']]  # Feature
    y = df['MEDV']  # Target
    model = LinearRegression()
    model.fit(X, y)
    predictions = model.predict(X)
    print(f"Predictions: {predictions[:5]}")
    
# 11. Random Forest Classifier
from sklearn.ensemble import RandomForestClassifier
def random_forest_classifier():
    df = pd.read_csv('iris.csv')
    X = df.drop('species', axis=1)
    y = df['species']
    model = RandomForestClassifier()
    model.fit(X, y)
    print("Random Forest Classifier trained.")

# 12. K-means Clustering
from sklearn.cluster import KMeans
def kmeans_clustering():
    df = pd.read_csv('Mall_Customers.csv')
    X = df[['Age', 'Annual Income (k$)', 'Spending Score (1-100)']]
    kmeans = KMeans(n_clusters=5)
    kmeans.fit(X)
    print(f"Cluster Centers: {kmeans.cluster_centers_}")

# 13. Decision Tree Visualization
from sklearn.tree import DecisionTreeClassifier, plot_tree
def decision_tree():
    df = pd.read_csv('iris.csv')
    X = df.drop('species', axis=1)
    y = df['species']
    tree = DecisionTreeClassifier(max_depth=4)
    tree.fit(X, y)
    plot_tree(tree, filled=True)
    plt.show()

