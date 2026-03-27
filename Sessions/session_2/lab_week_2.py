#Comparisons and conditionals
#Comparison always returns Boolean values
is_true=5>6
print(is_true)
is_true=20<21
print(is_true)
  
x=5
y=3
print(x==y)
#Logical operators combines 2 or more comparism operators
# "and" returns True if both operands are True
# 'or' operator returns True if at least one operand is True
# 'not-operator' returns True if the operand is False and vice versa
# Using AND
age=25
is_in_age_range= age>20 and age<30
print(is_in_age_range)  

age=1929030949
is_in_age_range=age>20 and age<2653675546
print(is_in_age_range)

ge=1929030949
is_in_age_range=age>20 and age>2653675546
print(is_in_age_range)
#Applying conditions to comparisons
#Eg1. "if someone is 18, they are not an adult". How to translate into python
age =19
age_group="child"
if age>18:
    age_group="adult"
print(f"The age group is {age_group}")    

age =19
age_group="child"
if age<18:
    age_group="adult"
print(f"The age group is {age_group}")  

age =19
age_group="child"
if age>18:
    print(f"This is an adult")
else:   
    print(f"This is a {age_group}")   
#%%
#%%
age =11
age_group="child"
if age>18:
    age_group="adult"
print(f"The age group is {age_group}")    

age =11
age_group="child"
if age<18:
    age_group1="adult"
print(f"The age group is {age_group}")  

age =15
age_group="child"
if age>18:
    print(f"This is an adult")
else:   
    print(f"This is a {age_group}")   

##Choosing an option out of 2. if-else
#Eg. "if the wind speed is over 10mph , it is a windy day,\\
#  otherwise it is a calm day"
speed_in_mph=25
Type_day="Calm day"
if speed_in_mph<10:
   print(f"it is a {Type_day}")
elif speed_in_mph>10:
    print(f"It is a windy day")
else:
    print("That is interesting")    

wind_speed=30
if wind_speed<10:
    print("It is a calm day")
else:
    print("It is a windy day")    


# %% 
#Building a grading system , you would need the elif conditionals
#Given the following rules:
#0-50%->FAIL ,50-60%->PASSED, 60-70%-> GOOD PASS, 70-80%-> EXCELLENT PASS
#We can reflect this in Python by putting an elif block between if and else blocks.
grade=55
if grade<50:
    print('Fail')
elif grade>50 and grade<60:
    print(f"passed")
elif grade>60 and grade<70:
    print(f"Good pass")
else:
    print("Excellent pass")      


grade=91
if grade<50:
    print('Fail')
elif grade>50 and grade<60:
    print(f"passed")
elif grade>60 and grade<70:
    print(f"Good pass")
else:
    print("Excellent pass")    

grade=96
if grade<50:
    print('Fail')
elif grade>50 and grade<60:
    print(f"passed")
elif grade>60 and grade<70:
    print(f"Good pass")
else:
    print("Excellent pass")    


grade=33.99
if grade<50:
    print('Fail')
elif grade>50 and grade<60:
    print(f"passed")
elif grade>60 and grade<70:
    print(f"Good pass")
else:
    print("Excellent pass")   


grade=59.99999999997
if grade<50:
    print('Fail')
elif grade>50 and grade<60:
    print(f"passed")
elif grade>60 and grade<70:
    print(f"Good pass")
else:
    print("Excellent pass")  
#Task 1 COMPARING TEMPERATURES
temperature1=20
temperature2=16
if temperature1==temperature2:
    print(f"The temperatures are the same") 
elif temperature1!=temperature2:
    print('There are different tempertures')
    
else:
    print("syntax unknown")   


#Python lists
# Creating a list in python. A list is similar to assigning a variables but\\
#  they need to start and end with square brackets. eaach item in the list\\
# should be separated by a comma and a space.
#Example
integer_list=[1,2,3,4,5]
string_list=["apple", "banana", "orange", "grape"]
empty_list=[]
list_with_differnt_types=[1, "two", 3.0, True]
#Creating list based on variables
person_1_age=20
person_2_age=30
age_list=[person_1_age, person_2_age]
list_within_a_list =[["red", "green", "blue"],["yellow", "orange", "purple"]]
#Task2
City_list=["Glasgow", "London", "Edinburgh"]
#Accessing a list
#List items are indexed with numbers starting from 0. for instance\\
#accessing the first item in string_list , you call it using code:\\
#'string_list[0]' which would yield item "apple"
#second item in this same list use; 'string_list[1]'which will yield "banana"
print(string_list[1])
print(string_list[0])
print(string_list[2])

#You can also access a range of items and this is called slicing
#You call out indices of the items separated with colon and not comma \\
# followed by second index+1
print(string_list[0:2]) #yields ["apple","banana"]
print(string_list[0:1]) #Returns only apple
print(string_list[0:3]) #Returns all items in the list
#You can also use negative numbers to access in the list.
#Negative numbers count backwards
print(string_list[-1]) #Yields "grape"
print(string_list[-1:1])
##Task 3
print(City_list[-1])
print(City_list[1:3]) #Returns ["London", "Edinburgh"]
#Modifying a list
#You can modify a list by assign a new value to an item in the list
#Changing first item in string_list
string_list[0]="pear"
print(string_list) #yields [pear, banana, orange, grape]

#Adding items to a list
#You can add items to a list by using the append() function
#Add orange to string list and add another city to city list
string_list.append("orange")
print(string_list)
City_list.append("Kumasi")
print(City_list) #So far , append() only adds one item in the last position
City_list[1]="Birmingham"
City_list.append("Manchester")
print(City_list)

#Task 4
colours=["violent", "Ash", "Blue"]
print(colours)
print(colours[1])
colours[0]="red"
print(colours)
print(len(colours))
if colours =="red": #very questionable . will sort out later
    print("yes")
else:
    print("no")    
selected_colours=colours[1:3]  
print(selected_colours)  #returns ash and blue
#%%
#Python loops. Types:
#sequence loops and
# while loops(continues loop as long as condition is True)
#EX1. print numbers from 0 to 4
i=0
while i <5:
    print(i)
    i+=1      #returns [0,1,2,3,4] \\
#Why does it specifically return only 5 characters?
i=0
while i <5:
    print(i)
    i+=1   
for fruit in string_list:
    print(fruit)    
for i in range(10):
    print(string_list)    
    
for city in City_list:
    print(city)    

for i in range(5):
    print(i)
#Stopping a loop before it uses all iterations


    





   