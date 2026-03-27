

#%%
#Exercise 1 task: Variables and Types
var_1= True
var_2 = 1
var_3 = 3.14159
var_4 = "Hello World"
print(type(var_1))
print(type(var_2))
print(type(var_3))
print(type(var_4))

#%%
#Exercise 1 task 2: Casting Variables

my_int =5
my_float=5.5
my_bool=True

print(my_int)
print(my_float)
print(my_bool)

my_int_float = float(my_int)
my_float_int = int(my_float)
mybool_int = int(my_bool)

print("after casting")
print(my_int_float)
print(my_float_int)
print(mybool_int)

#%%
#Practice with the arithmetic operators
result_addition = 10+5
print("Addition:", result_addition)
#Subtraction
result_subtraction = 20-8
print("Subtraction:", result_subtraction)
#Multiplication
result_multiplication = 6*4
print("Multiplication:", result_multiplication)
#Division
result_division= 15/3
print("Division:",result_division)
#Floor Division
result_floor_division= 17//4
print("Floor_division:",result_floor_division)
#Modulus
result_modulus= 17%4
print("Modulus:",result_modulus)
#Exponentiation
result_exponentiation = 2**3
print("Exponentiation:", result_exponentiation)
# calculate the averaGE OF THREE numbers
num1=10
num2=20
num3=20
average=(num1+num2+num3)/3
print("Average of 3 numbers:", average)
# calculate the averaGE OF five numbers
num4=12
num5=56
average=(num1+num2+num3)/3
print("Average of 5 numbers:",average)
#Round the average to 2 dceimal places
print("Average of 3 mbers:", round(average,2))
average =(num1+num2+num3+num4+num5)/5
print("Average of 5 numbers:",average)

#calculating area of rectangle
length = 5
width =3
area =length * width
print("Area of the rectangle:",area)
#MODIFYING STRINGS Exercise 3
my_string="This class covers ISD"
print(my_string)
my_uppercase_string = my_string.upper()
print(my_uppercase_string)
my_lowercase_string=my_string.lower()
print(my_lowercase_string)
my_new_string=my_string.replace("ISD","Interactive Software Design")
print(my_new_string)
my_string_length=len(my_string)
print(my_string_length)
#String formatting with F-strings
my_name="Peter"
number_of_classes=4
campus="Paisley"
my_text =f"My name is {my_name} and I am studying {number_of_classes} classes in {campus}."
print(my_text)
#The code convesrts a number stored as celsius_input to fahrenheit and kelvin temperature 
#**temperature_converter.py
#Temperature Converter
#This program converts temperature from Celsius to Fahrenheit and Kelvin
celcius_input=20
#convert the input to a float
celcius_input=float(celcius_input)
degree_fahrenheit =(celcius_input *9/5)+32
degree_kelvin =celcius_input+273.15
print(f"{celcius_input} degree Celsius is equal to {degree_fahrenheit:.2f}Fahrenheit.")
print(f"{celcius_input} degree Celsius is equal to {degree_kelvin:.2f}Kelvin.")
print("Thank you for using t6he Temperature Converter")
