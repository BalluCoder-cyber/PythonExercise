import pandas as pd
##df from list inside list...
# data =[
#     ["Aman",21,85],
#     ["Balwant",66,77],
#     ["Sobhit",88,92]
# ]
# df = pd.DataFrame(
#     data,
#     columns=["Name","Age","Marks"]
# )

# print(df)
# print(df.dtypes)

##df from dictonary with list...

# data2 =[
# {"Name":"Balwant","Marks":90.6},
# {"Name":"Ankesh","Marks":91.6},
# {"Name":"Shobhit","Marks":99.6},
# {"Name":"Sonu","Marks":81.6},
# {"Name":"Monu","Marks":75.6},
# {"Name":"Manshi","Marks":61.6},
# {"Name":"Rohit","Marks":11.6},
# {"Name":"Rahul","Marks":31.6},
# {"Name":"Riya","Marks":66.6},
# {"Name":"Jiya","Marks":31.6},
# {"Name":"Golu","Marks":21.6},
# {"Name":"Molu","Marks":61.6},
# {"Name":"Dolu","Marks":88.6},
# ] 
# df_LD = pd.DataFrame(
#     data2,
#     index=["S1","S2","S3","S4","S5","S6","S7","S8","S9","S10","S11","S12","S13"]
# )
# print(df_LD)
# print(df_LD.head())
# print(df_LD.tail())
# print(df_LD.iloc[0:4])
# print(df_LD.iloc[4:11])
# print(df_LD.loc["S1"])
# print(df_LD.loc["S4","Marks"])
# print(df_LD.loc["S2":"S8"])

##Exercise question
# display the first 5 rows of the data frame
# display the last 3 rows of the data frame
# find the total number of rows and colmn 
# find the number or dim. fo the df
# find the NaN values from given df
# display only the structural information of the data frame
