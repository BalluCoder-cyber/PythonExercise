import pandas as pd
##Exercise question
# display the first 5 rows of the data frame
# display the last 3 rows of the data frame
# find the total number of rows and colmn 
# find the number or dim. fo the df
# find the NaN values from given df
# display only the structural information of the data frame

data = [
    {"Name":"Balwant","RollNo":613241044},
    {"Name":"Rahul","RollNo":613241045},
    {"Name":"Rohit","RollNo":613241046},
    {"Name":"Sohit","RollNo":613241047},
    {"Name":"Mohit","RollNo":613241048},
    {"Name":"Riya","RollNo":613241049},
    {"Name":"Jiya","RollNo":613241050},
    {"Name":"Sonu","RollNo":613241051},
    {"Name":"Rani","RollNo":613241052},
    {"Name":"Kumar","RollNo":613241053},
    {"Name":"Golu"},
]

df = pd.DataFrame(
    data,
)
# print(df)
# print(df.iloc[0:6])
# print(df.iloc[8:11])
# print(df.shape)
# print(df.ndim)
# print(df.info())
# print(df.describe)
print(df.isna())