import pandas as pd
data={'name':['albin','alfia','anjaleena'],
      'rollno':[37,36,30],
      'age':[22,23,21]}
df=pd.DataFrame(data)
selected_columns=df[['name','age']]
print(selected_columns)
