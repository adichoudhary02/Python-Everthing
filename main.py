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


print("="*20)

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

print("="*20)

def area_of_circle(radius):
    pi = 3.14
    result = pi * radius * radius
    return result

radius = 5
area = area_of_circle(radius)
print(f"Area of the circle is: {area}")

"""
Okey how the execution take place is given here it moves in the chronological order
1. The fucation is defined for the later use and it has for in input variable radius body is skipped for now.
2. Radius variable is declared and intialized with values 5
3. Now the function variable is called with input value as the radius
4. then redius is assigned the radius variable value. 
5. body is executed returned the result variable value.
6. area is assigned the value of the result of the funcation
7. print the line and the value of the area
"""

#All of the fucation need to be defined before they are called:
#For this use the main funcation approch

print("=")

def main():
    health = 10
    armor = 5
    add_armor(health, armor)

def add_armor(h, a):
    new_health = h + a
    print_health(new_health)

def print_health(new_health):
    print(f"The player now has {new_health} health")

# call entrypoint last
main()

"""
The main fuction deff:
def main():

#Define all fxn here

#Define all fxn here

#Entery Point
main()
"""

#All of these 3 functions return the none as the output
def my_func():
    print("I do nothing")
    return None

def my_func2():
    print("I do nothing")
    return

def my_func3():
    print("I do nothing")


#We can return the multiple values in python

def cast_iceblast(wizard_level, start_mana):
    damage = wizard_level * 2
    new_mana = start_mana - 10
    return damage, new_mana # return two values

#We can store the multiple values returned throught the fxn

one, two = cast_iceblast(5, 100)
print(f"Damage: {one}, Remaining Mana: {two}")
# Damage: 10, Remaining Mana: 90

#Defining the default values to the fxn

def get_greeting(email, name="there"):
    print("Hello", name, "welcome! You've registered your email:", email)

print("="*20)
