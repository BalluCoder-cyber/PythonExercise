# #while Loop...
# i = 1
# while (i<11):
#     print(i)
#     i += 1

#For loop
# num = [5,6,8,9,8]
# for i in num:
#     print(i)

# for i in range(0,16,5):
#     print(i)
#     if(i==15):
#         break

#Write a program to greet all the person names stored in a list ‘l’ and which starts with S.

# name = ["Harry","Soham","Sachin","Rahul"]
# for i in name:
#    if(i.startswith("S")):
#       print("Good Morning ", i)


#print pattern.
# n = 4
# for i in range(1,n):
#     for j in range(1,i+1):
#       print("*", end="")
#     print()  


# n = 4 
# for i in range(1,n):
#     print(" "*(n-i), end="")
#     print("*"*(2*i-1), end="")
#     print("")

n = 4
for i in range(1,n+1):
  if(i==1 or i == n):
    print("*" * n, end="")
  else:
    print("*", end="")
    print(" " * (n-2), end="")
    print("*",end="")
  print("")  
