#x=True
#y=False
#==(equal)
#!=(not equal)
#<=( less than or equal to)
j=65564353.54352434545
p=66536355.23141563241
y=j<p
y1=j>p
y2=j!=p
y3=j==p
print(y)
print(y1)
print(y2)
print(y3)
#own examples. Which of these is has the greatest value??
#52254562355863.55452475
#55558366385365.54774565
#55555354145434.435453453
a = 52254562355863.55452475
b = 55558366385365.54774565
c = 55555354145434.435453453
va = a>b
vb = b>c
vc = c>a
print(va)
print(vb)
print(vc)
#using and,or, not-operator
y1=a>b and b>c 
print(y1)
y2=a<b and b>c 
print(y2)
y3=a<b and b>c and c>a
print(y3)
#using or 
x1=a>b or b>c 
print(x1)
#using not 


age=25
is_in_age_range=age >20 and age<30
print(is_in_age_range)


age=34
x=age<2 or age<79
print(x)

age=34
x='The statement is true'
if age>18:
    print(x)

age=100
y="okayyyyy"
if age<120:
    print(y)


age=100
y="false statement"
if age>120:
    print(y)

age=100
y="false statement"
if age>120:
    print(y)
else:
    print("it is true")    
    
marks=103
y="false statement"
if marks<120:
    print(y)
else:
    print("it is true")    


age = 19
age_group = "child"
if age < 18:
    print(age_group) 
else:
    print("The age group is adult")   


wind_speed=35
y="it is a calm day"   
x="it is a windy day"
if wind_speed>10:
    print(x)
else:
    print(y)

wind_speed=10
y="it is a calm day"   
x="it is a windy day"
w="I understand now"
if wind_speed>10:
    print(x)
else:
    print(w)

wind_speed=10
y="it is a calm day"   
x="it is a windy day"
w="I understand now"
if wind_speed>10:
    print(x)
elif wind_speed==10:
    print(w)    
else:
    print(y)

student_grade=49.9999999992
y=""




