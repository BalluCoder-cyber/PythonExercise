# #dictonary is a collection of key:value pair it is mutable and doen't contain duplicate value with its orders

# marks  = {
#     "harry" : 100,
#     "shubhma" : 200,
#     "fohan" : 44,
#     "gta" :6,
#     "game" : "GTA-6",
#     "subject" : "python"
# }

#emptyDic = {}

# print(marks["shubhma"])

# #Methods..
# print(len(marks)) # give the length of dic
# print(marks.items()) # give us all key:value pair in tuple form 
# print(marks.keys()) #print all keys of dict
# print(marks.values()) # print all values of dic
# print(marks.update({"harry":55, "renuka":66})) #update dic
# print(marks.get("renuka")) #return the value of key
# print(marks.pop("fohan")) #delete the key and return value
# print(marks.popitem({"shubhma"})) #delete the key:value pair and return the pair as tuple


# #Sets is a collection of non-repetitive elements non order elem 
# s = {3,4,5,"akjgdkj",False,66,55}
# # emptySet = set()
# #Methods
# s.add(1)#add elem in set
# print(len(s))# give the length of set
# s.remove(3) # remove the elem in set
# s.pop(55) #delete and return the value
# s1 = {44,2,5,6,1,}
# print(s.union(s1))#give the union of s and s1 
# print(s.intersection(s1)) #give the intersection of s and s1


#create dic 
words = {
    "gadha":"donkey",
    "ghoda":"horse",
    "nine" : 9,
    "chidiya": "bird"
}

#take multiple num as input and store in set
num = set()
num1 = int(input("enter num 1"))
num.add(num1)
num2 = int(input("enter num 2"))
num.add(num2)
num3 = int(input("enter num 3"))
num.add(num3)
num4 = int(input("enter num 4"))
num.add(num4)
num5 = int(input("enter num 5"))
num.add(num5)
num7 = int(input("enter num 7"))
num.add(num7)
num8 = int(input("enter num 8"))
num.add(num8)
num9 = int(input("enter num 9"))
num.add(num9)
print(num)