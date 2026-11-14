import pandas as pd
# data = {
#     "name" : ["Balwant","Rahul","Rohit"],
#     "Number" : [55,155,77]
# }
# df = pd.DataFrame(data)
# df['Bonus'] = 5
# df["FinalMarks"] = df["Number"] + 5
# print(df)

# print(df["Number"].sum())
#print(df["Number"].mean())
# print(df["Number"].median())
# print(df["Number"].mode())
# print(df["Number"].min())
# print(df["Number"].max())
# print(df["Number"].count())
# print(df["Number"].std())
# print(df["Number"].var())
# print(df["Number"].prod())
# print(df["Number"].cumsum())
# print(df["Number"].cumprod())



##Reading excel file and perform operation...
# df = pd.read_excel("Excelfile.xlsx")
# # print(df.head())
# # print(df.count())
# # print(df["Order ID"].sum())

# result = df[
#     (df["Order ID"]>5000) 
# ]
# # print(result)

# hrow = df.head()
# print(hrow["Order ID"].cumsum())
# print(hrow["Order ID"].cumprod)




#Question Excersie...

# Display third row using iloc
# add 5 marks to every student and store them in a new column name updatedmarks
# Display students whoes scoring btw 70 and 90 marks
# Display record whoes name start with A
# Replace missing age with 20
# create a result column containing pass for marks > or = to 40 other wise fail
# create a grade column A for marks is >= 90 , B for marks is > 80 but below 90, C for marks >= 70 below 80, D for marks below 70 
# Display only student with grade A or B
# Display the toppers name and percentage 
# find the average  for marks each student
# Save the final report to student performing.csv

data = {
    "name" : ["Balwant","Rahul","Rohit","Sobhit","Sonu","Golu","Dolu"],
    "Number" : [55,155,77]
}
df = pd.DataFrame(data)
df['Bonus'] = 5
df["FinalMarks"] = df["Number"] + 5
print(df)
