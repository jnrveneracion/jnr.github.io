#printing text
print("hello, janrie!!")

#variables
print("a = 28 - integer")
print("b = 26.5 - float")
print('c = "Janrie" - str')
print("d = True - bool")
print("e = None - NoneType")

#input from user
name = input("Name: ")
age = int(input("Age: "))
#sample formatted string print
print(f"\nHello, {name}. You're {age}")

#conditions
if age < 100:
    print("Surely you're alive")
else:
    print("Are you ghost?")
    Ag = input("[Y] Yes or [N] No: ")
    if Ag == 'Y':
        print("okay!")
    else:
        print("gege")    


#sequences/index/array
print("The first letter on your name is: ",name[0])


