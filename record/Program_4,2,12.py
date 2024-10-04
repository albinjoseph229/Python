import pandas as pd

# Creating a sample DataFrame
data = {'name': ['albin', 'alfia', 'anjaleena'],
        'rollno': [5, 6, 7],
        'age': [21, 22, 22]}

df = pd.DataFrame(data)

# Writing the DataFrame to a CSV file using a tab separator
df.to_csv('output_file.csv', sep='\t', index=False)

print("DataFrame has been written to 'output_file.csv' using a tab separator.")
