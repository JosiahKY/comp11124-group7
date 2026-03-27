#At the end, you will build a simple To-Do application, which combines the things we hae studied previously
def greet_user():
    print("Hello!")
greet_user()    
def greet_user(name):
    print(f"Hello {name}!")

greet_user("Glory to Jesus")    
greet_user("Faustina Amofa")    
def greet_user(first_name,last_name):
    print(f"Hello, {first_name} {last_name}")    
greet_user('Josiah',"Kyei-Yeboah")    
greet_user(last_name="Elioenai", first_name="Osei Francis")
greet_user(first_name="Hilkiah", last_name='Osei-Francis')
greet_user(first_name="Josephine Akosua", last_name="Adoma")
greet_user(first_name="Josephine", last_name ="Osei")
greet_user(first_name='Francisca', last_name="Ama Agyemang")
greet_user(first_name='Osei Yaw',last_name='Francis')
#Task
def greet_friends(name):
    print(f"Hello {name}!")
greet_friends("John")
greet_friends('Peter')
greet_friends("Cassandra")  

friend_list=['John','Jane','Jack']
print(friend_list)
greet_friends(friend_list)  
greet_friends(friend_list[0])
greet_friends(friend_list[-1])

def add_and_multiply_numbers( num1 , num2):
    sum = num1 + num2
    product = num1 * num2
    return sum, product
sum, product = add_and_multiply_numbers( 5, 10)
print(sum)
print(product)
#Task2
def calculate_tax(income , tax_rate):
    result= income * tax_rate
    print(int(result))  
calculate_tax(50000, 0.2)


def calculated_tax(income , tax_rate):
    result= income * tax_rate
    print("Calculated Tax:", result)
calculated_tax(50000, 0.2)  

#Task 3
def compound_interest(principal, duration , interest_rate):
    if interest_rate <0 or interest_rate >1:
        print("Please enter a decimal number between 1 and 0")
        return None
    if duration < 0:
        print("Please enter a posituve number of years")
        return None
    for i in range(1, duration +1):
        Total_of_the_year = principal * (1 + interest_rate)** i
        print(f"The total amount of money earned by the investment is {int(Total_of_the_year)} £")
    return int(Total_of_the_year)

print(compound_interest(1000, 5, 0.03))
assert compound_interest(1000, 5, 0.03) == 1159   


#Task
def new_wave(x,y):
    return x**y
print(new_wave(2, 3))

assert new_wave(2, 3) ==8
assert new_wave(2, 3) ==9   #Expwcted assertion error
assert new_wave(2,3) ==3       #Expected assertion error









    
