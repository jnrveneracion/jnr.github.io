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

#list
names = ["Harry", "Ron"]

#add the name input to last in the list
names.append(name)
print(names[0])
print(names[1])
print(names[2])

#sort
print("\n sorting items in the list")
names.sort()
print(names)

alpha = ['A', 'B', 'A', 'B', 'F', 'C']
alpha.sort()
print("osritn of letters: ", alpha)

#empty set
j = set()
i = 0
while i < 5: 
    ja = input("input to set: ")
    i += 1 
    j.add(ja)  

print("print elements in set: ", j)
# no element appears more than once/ also diff ordering
# note same input element in to set will be merge to 1 and it is printed
a = set()
a.add(1)
a.add('B')
a.add(3)
a.add('A')

#removing element in the set   
print("Printing set: ", a)  
print(f"The set has {len(a)} elements.")
a.remove(3)
print("removing 3\nPrinting set: ", a) 

#count elements
print(f"The set has {len(a)} elements.")

#loop
for i in[0,1,2,3,4,5,6]:
    print (i)

for i in range(6):
    print(i)

for i in names:
    print("set", i)

for i in name:
    print("every character", i)    


#dictionary
birthdays = {"janrie":"june", "julia":"june"}
print("Janrie's Birthday in on: ", birthdays["janrie"])
#adding item in dictionary
birthdays["jhaz"] = "july"

#functions
def cuberoot(x): #other file
    return x * x * x
#use from functions import cuberoot    
for i in range(5): #other file
    print(f"The cube of {i} is {cuberoot(i)}")



