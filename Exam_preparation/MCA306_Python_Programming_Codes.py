
# Basic Python Programming
# Example 1: Simple Calculator
def calculator():
    print("Select operation:")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    choice = input("Enter choice(1/2/3/4): ")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    if choice == '1':
        print(f"{num1} + {num2} = {num1 + num2}")
    elif choice == '2':
        print(f"{num1} - {num2} = {num1 - num2}")
    elif choice == '3':
        print(f"{num1} * {num2} = {num1 * num2}")
    elif choice == '4':
        if num2 != 0:
            print(f"{num1} / {num2} = {num1 / num2}")
        else:
            print("Cannot divide by zero!")
    else:
        print("Invalid input")

# Example 2: Reverse the digits of a number and check palindrome
def reverse_and_add(n):
    rev = int(str(n)[::-1])
    return n + rev

def is_palindrome(n):
    return str(n) == str(n)[::-1]

def reverse_and_check_palindrome(n):
    while not is_palindrome(n):
        n = reverse_and_add(n)
        print(f"New number: {n}")
    return n

# Handling Missing Values in a DataFrame
import pandas as pd
data = {'Name': ['John', 'Anna', 'Peter', None],
        'Age': [28, None, 34, 29],
        'Salary': [None, 50000, 40000, 60000]}
df = pd.DataFrame(data)

# Fill missing values with mean or mode
df['Age'].fillna(df['Age'].mean(), inplace=True)
df['Name'].fillna(df['Name'].mode()[0], inplace=True)
df['Salary'].fillna(df['Salary'].mean(), inplace=True)

# Encoding Categorical Values
df['Name'] = df['Name'].astype('category').cat.codes

# Database Operations: MySQL Connection
import mysql.connector
def connect_to_db():
    db = mysql.connector.connect(
        host="localhost",
        user="user",
        password="password",
        database="school"
    )
    cursor = db.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS students (id INT, name VARCHAR(255), age INT)")
    db.commit()

# NumPy Program for Matrix Operations
import numpy as np
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# Matrix multiplication
C = np.dot(A, B)
print(C)

# RandomForestRegressor Example
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_boston

boston = load_boston()
X_train, X_test, y_train, y_test = train_test_split(boston.data, boston.target, test_size=0.2)

model = RandomForestRegressor(n_estimators=100)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# Decision Tree on Iris Dataset
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_iris

iris = load_iris()
clf = DecisionTreeClassifier(max_depth=4)
clf.fit(iris.data, iris.target)

import matplotlib.pyplot as plt
from sklearn import tree

plt.figure(figsize=(12,8))
tree.plot_tree(clf, filled=True)
plt.show()

