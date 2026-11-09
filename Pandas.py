import pandas as pd
# marks = pd.Series([80,55,44])
# print(marks)
data = {
    "Name" : ["Balwant","Rohit","Rahul"],
    "RollNo" :["0613CS241044","044","088"],
    "Branch": ["CSE","CSAI","ME"],
    "Subject":["PythonLab","PythonLab","PythonLab"]
}

df = pd.DataFrame(data)
# print(df.size)
# print(df.shape)
# print(df.ndim)
# print(df.columns)
# print(df.index)
# print(df.dtypes)
# print(df.T)
#print(df.info())
#print(df.describe())
#print(df.head())
# print(df.tail())
# print(df.isna())