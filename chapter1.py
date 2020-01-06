# how to check a type of any data type?
"""y = type(2)
x = type("42")
print(y)
print(x)"""

#Excercise 1
minutes = int(input("Enter your minutes"))
second = int(input("Enter your seconds"))
outcome = minutes * 60 + second
print(outcome)

#with Function
def count_minutes(x,y):
    return x*60+y

print(count_minutes(45,45))

#Exercise 3

def kilo(x=10):
    return x/1.61

print(kilo())

def count_minutes(x=42,y=42):
    return (x*60+y)
print(count_minutes())

print(count_minutes()/kilo())
print(60/count_minutes()/kilo())

