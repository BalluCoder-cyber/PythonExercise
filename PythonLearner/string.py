# In python String are immutable
# name = "BalluCoder"
# slice_String = name[0:3] # slicing in string
# print(slice_String)

# char = name[4] #accessing character by index
# char1 = name[-1] #reverse accessing
# revSlice = name[-5:-1]
# print(char, char1,revSlice)
# #slicing with skip value
# skip_slic = "rohitbhadwa"
# print(skip_slic[0:5:2])

# #Method or function in String
# name = "  my name is billu"

# print(len(name))
# print(name.endswith("u"))
# print(name.startswith("n"))
# print(name.capitalize())
# print(name.upper())
# print(name.lower())
# print(name.find("l"))
# print(name.replace("l","y"))
# print(len(name.strip()))

#greet a person
greet = "Good afternoon"
name = input("Enter the name :")
print(greet+name)

#fill the letter
letter = '''Dear <|name|>,
            Youp are selected!
            <|Date|>'''

print(letter.replace("|name|","Ballu").replace("|Date|","16/04/2026"))

#format sentence using escape sequence
letter1 ="Dear harry, this python course is nice . Thanks!"
letter2 = "Dear harry,\nthis python course is nice.\nThanks!"
print(letter2)

#find double space in letter
space = "hello how you"
print(space.find("  "))
print(space.replace("  ","&&"))