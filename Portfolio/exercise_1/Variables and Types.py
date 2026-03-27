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