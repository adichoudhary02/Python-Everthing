"""
This is the multi-line comment
It can hold several line
"""
# This is the single line comment

name_with_single_quotes = 'boot.dev' # not so good
name_with_double_quotes = "boot.dev" # so good

#Number Variables
x = 5 # positive integer
y = -5 # negative integer

#Float Variables
fx = 5.2
fy = -5.2

#Boolean Variables
is_tall = True
is_short = False

#f"String"
fString = f"This is fString "

print(fString + f"Number x = {x} \nFloat num is {fx} \nThe boolean var is {is_tall}")

#Python has None that is similar to the null
my_test = None

#To accept input from the user - inpur("Text to be displayed ")
name = None
# name = input("Enter your name: ")
if name is None:
    name = "Adi"
print(f"Username is {name}")

#Multi variable Declaration
sword_name, sword_damage, sword_length = "Excalibur", 10, 200

print(f"sword_name: {sword_name}\nsword_damage : {sword_damage}\nsword_length : {sword_length}")

is_car = True
print(f"The type of is_car is: {type(is_car)}")
"""
type(<variable>) funcation which return the type of the datatype
type(<variable>).__name__ funcation which returns the exect name of data type
"""

def area_of_circle(radius):
    pi = 3.14
    result = pi * radius * radius
    return result

radius = 5
area = area_of_circle(radius)
print(f"Area of the circle is: {area}")

