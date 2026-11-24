## if else conditions...

# age=int(input("Enter your age bebe : "))
# if(age>=18):
#     print("I am adult")
# else:
#     print("I am not adult")    

##Elif conditions
# marks = 89
# if(marks >= 90):
#     print("passed with first devision")
# elif(marks > 70 and marks < 90):
#     print("passed with second devision")    
# else:
#     print("passed with third devision")    

# #find greated among four number
# num1 = 5
# num2 = 6
# num3 = 13
# num4 = 111
# if(num1 > num2 and num1 > num3 and num1 > num4):
#     print("num1 is greater:" , num1)
# elif(num2 > num3 and num2 > num4):
#     print("num2 is greater:", num2)
# elif(num3 > num4):
#     print("num3 is greater:", num3)
# else:
#     print("num4 is greater:",num4)        


# # A spam comment is defined as a text containing following keywords:
# “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program
# to detect these spams

# message = input("Enter your message: ")
# if(not message.find("Make a lot money") == -1):
#     print("Spam call")
# elif(not message.find("buy now") == -1):
#     print("Spam call")
# elif(not message.find("click this") == -1):
#     print("Spam call")        
# else:
#     print("Not a spam Call")  


## Write a program which finds out whether a given name is present in a list or not.
name_List = ["Rahul","riya","Ballu","golu","Ankesh","badal"]
find_name = "gAnkesh"
if(find_name in name_List):
    print("Name is IN in the List")
else:
    print("Name is NOT the List")    