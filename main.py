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


#Floor division x // y
"""This results in the lowest whole nu. then the value"""
temp_result = 7 // 3 #Result is 2
temp_result = -7 // 3 #Result in -3

#Exponents are 3**2 :- 3^2

"""
Scientific notation:
print(16e3) :- 16000.0
print(7.1e-2) :- 0.071

For redablity num = 16_000
"""

#print(True or False or False) is equal to print((True and notFalse) or False)


#print(0b0101) we can input the binary number by using a prifix 0b in begning

"""
bitwise & and |

0b0101 & 0b0111 results in 5
"""

#Converting the binary string into the number using int(<binary string>, <number sys base>)
"""
# this is a binary string
binary_string = "100"

# convert binary string to integer
num = int(binary_string, 2)
print(num)
# 4
"""
print("="*20)

def binary_string_to_int(inputer):
    print(inputer) 

data_a, data_b, data_c = binary_string_to_int("100", "101", "110")
print(data_a)
# 4
print(data_b)
# 5
print(data_c)
# 6

### Once you are done with the DSA come back to this topic
"""
def binary_string_to_int(*binary_strings):
  
  #Converts any number of binary strings to their integer equivalents.
  
  # Use a list comprehension to convert each binary string to an integer
  # int(string, 2) tells Python to interpret the string as a base-2 (binary) number
  return [int(b_string, 2) for b_string in binary_strings]

# --- Example with 3 inputs ---
data_a, data_b, data_c = binary_string_to_int("100", "101", "110")

print(f"data_a is: {data_a}")
# Expected output: data_a is: 4
print(f"data_b is: {data_b}")
# Expected output: data_b is: 5
print(f"data_c is: {data_c}")
# Expected output: data_c is: 6

print("-" * 20) # A separator for clarity

# --- Example with 5 inputs ---
results = binary_string_to_int("1", "10", "11", "1000", "10001")
print(f"Results for 5 inputs: {results}")
# Expected output: Results for 5 inputs: [1, 2, 3, 8, 17]
"""

#if you want true or false as the answer of the express then better not to use it,
"""
is_equal = 5 == 5
# is_equal is True

"""
# Structure for the elif
score, high_score, secord_hight_score, third_highest_score = 0, 0, 0, 0
if score > high_score:
    print("High score beat!")
elif score > secord_hight_score:
    print("You got second place!")
elif score > third_highest_score:
    print("")

#For structure

for i in range(0, 10):
    print(i)
"""
for <variable> in range(<start>, <end>, <steps>):
    <body>
"""


#Range in for 
for i in range(0, 10, 2):
    print(i)
# prints:
# 0
# 2
# 4
# 6
# 8

# While Structure
num = 0
while num < 3:
    num += 1
    print(num)

# prints:
# 1
# 2
# 3
# (the loop stops when num >= 3)

#Continue Statement in Python 
numbers = [16, -4, 25, -9, 36, 0, 49]

for number in numbers:
    if number < 0:
        continue  # Skip negatives to avoid complex numbers

    print(f"The square root of {number} is {number ** 0.5}.")

# Break statement stop the loop and get out of the block

for n in range(42):
    print(f"{n} * {n} = {n * n}")
    if n * n > 150:
        break



#List in Python 

inventory = ["Iron Breastplate", "Healing Potion", "Leather Scraps"]

player_ages = [
    23,
    18,
    31,
    42
]

#indexing in python

best_languages = ["JavaScript", "Go", "Rust", "Python", "C"]
print(best_languages[1])
# prints "Go", because index 1 was provided

#length of the List
fruits = ["apple", "banana", "pear"]
length = len(fruits)
# 3

#Updating the item in the list
inventory = ["Leather", "Iron Ore", "Healing Potion"]
inventory[0] = "Leather Armor"
# inventory: ['Leather Armor', 'Iron Ore', 'Healing Potion']

#Adding the item to the end of the list using the .append() fxn
cards = []
cards.append("nvidia")
cards.append("amd")
# the cards list is now ['nvidia', 'amd']

#removing and returning the last item of the list using .pop()
vegetables = ["broccoli", "cabbage", "kale", "tomato"]
last_vegetable = vegetables.pop()
# vegetables = ['broccoli', 'cabbage', 'kale']
# last_vegetable = 'tomato'

#Using for to print all the items of the list using iteration
sports = ["Football", "Hockey", "Bat", "Halmet"]
for i in range(0, len(sports)):
    print(sports[i])

#printing the items of the list without using the iteration
trees = ['oak', 'pine', 'maple']
for tree in trees:
    print(tree)

#infinity in Python 
negative_infinity = float("-inf")
positive_infinity = float("inf")

#Slicing Lists in python
# my_list[ start : stop : step ]

scores = [50, 70, 30, 20, 90, 10, 50]
# Display list
print(scores[1:5:2])
# Prints [70, 20]

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers[:3] # Gives [0, 1, 2]
numbers[3:] # Gives [3, 4, 5, 6, 7, 8, 9]

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers[::2] # Gives [0, 2, 4, 6, 8]

#Concatinating the two lists 
total = [1, 2, 3] + [4, 5, 6]
print(total)
# Prints: [1, 2, 3, 4, 5, 6]

#Checking if the list contains the item
fruits = ["apple", "orange", "banana"]
print("banana" in fruits)
# Prints: True

fruits = ["apple", "orange", "banana"]
print("banana" not in fruits)
# Prints: False

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# delete the fourth item
del nums[3]
print(nums)
# Output: [1, 2, 3, 5, 6, 7, 8, 9]

# delete the second item up to (but not including) the fourth item
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
del nums[1:3]
print(nums)
# Output: [1, 4, 5, 6, 7, 8, 9]

# delete all elements
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
del nums[:]
print(nums)
# Output: []


#Tuples- These are ordered and unchangeable

my_tuple = ("this is a tuple", 45, True)
print(my_tuple[0])
# this is a tuple
print(my_tuple[1])
# 45
print(my_tuple[2])
# True

#List in a tuple 

my_tuples = [
    ("this is the first tuple in the list", 45, True),
    ("this is the second tuple in the list", 21, False)
]
print(my_tuples[0][0]) # this is the first tuple in the list
print(my_tuples[0][1]) # 45
print(my_tuples[1][0]) # this is the second tuple in the list
print(my_tuples[1][2]) # False

#For tuples with just an single element we use comma 
#so that it is not confused with the nomal barckers

dog = ("Fido",)

#Spliting the sentence in the list of words
message = "hello there sam"
words = message.split()
print(words)
# Prints: ["hello", "there", "sam"]


#Accepting the variable inputs
def binary_to_string(*inputs):
    itemss = []
    for input in inputs:
        itemss.append(int(input, 2))
    print(itemss)
binary_to_string("1001", "10010", "1101")

"""
Argument Packing: The *inputs syntax gathers all three string arguments—
"1001", "10010", and "1101"—and puts them into a tuple named inputs.
Inside the function, inputs is equal to:
("1001", "10010", "1101")
"""

#Tuples unpacking 
dog = ("Fido", 4)
dog_name, dog_age = dog
print(dog_name)
# Fido
print(dog_age)
# 4


#Split the sentence into the words of lists .split()

message = "hello there sam"
words = message.split()
print(words)
# Prints: ["hello", "there", "sam"]

#Join the list of words into a string .join()
list_of_words = ["hello", "there", "sam"]
sentence = " ".join(list_of_words)
print(sentence)
# Prints: "hello there sam"

#Dictonary the famous Key value pair

# use curly braces
# add key-value pairs
car = {
  "brand": "Toyota",
  "model": "Camry",
  "year": 2019,
}

#We can't have duplicate keys in the dictionary

def get_character_record(name, server, level, rank):
    return {
        "name": name,
        "server": server,
        "level": level,
        "rank": rank,
        "id": f"{name}#{server}",#Cool away of using the fstring to create id.
    }

#Accessing dictonary 
car = {
    "make": "Toyota",
    "model": "Camry"
}
print(car["make"])
# Prints: Toyota

#Setting values to the Dictonary keys

planets = {}
planets["Earth"] = True #This checks if the planets has Earth if not then adds it
planets["Pluto"] = False
print(planets["Pluto"])
# Prints False

planets["Pluto"] = True #Here it found Pluto already existed then it modified the Pluto's value
print(planets["Pluto"])

#Deleting the values in the dictonary

names_dict = {
    "jack": "bronson",
    "jill": "mcarty",
    "joe": "denver"
}

del names_dict["joe"]

print(names_dict)
# Prints: {'jack': 'bronson', 'jill': 'mcarty'}

#Checking if the key exists in the dictonary
if "jill" in names_dict:
    del names_dict["jill"]
    
print(names_dict)
# Prints: {'jack': 'bronson'}

#Iterating over the dictonary
fruit_sizes = {
    "apple": "small",
    "banana": "large",
    "grape": "tiny"
}

for name in fruit_sizes:
    print(f"name:{name}, size:{fruit_sizes[name]}")
    
    
#Nested dictonary
{
    "entity": {
        "character": {
            "name": "Shallan",
            "quests": {
                "bridge_run": {
                    "status": "Completed",
                },
                "talk_to_syl": {
                    "status": "In Progress",
                },
            },
        }
    }
}

#accessing th enested dictonary using the key chaining
outer_dictionary = {}
outer_dictionary["outer_key"]["inner_key"]


#Sets - Unordered and are always uniquee

fruits = {"apple", "banana", "grape"}

#Adding and removing values to the sets

fruits.add("pear")

fruits.remove("apple")

#Creating the Empty sets

fruits = set()
fruits.add("pear")

#Sets Subtraction

set1 = {"apple", "banana", "grape"}
set2 = {"apple", "banana"}
set3 = set1 - set2

#Error Handling in Python 

try:
  10 / 0
except Exception:
  print("can't divide by zero")
  
#Raising the own error

def craft_sword(metal_bar):
    if metal_bar == "iron":
        return "iron sword"
    raise Exception("invalid metal bar")

#Never Catch your own exception 

# don't do this
def craft_sword(metal_bar):
    try:
        if metal_bar == "bronze":
            return "bronze sword"
        if metal_bar == "iron":
            return "iron sword"
        if metal_bar == "steel":
            return "steel sword"
        raise Exception("invalid metal bar")
    except Exception as e:
        print(f"An error occurred: {e}")
        
# do this
try:
    craft_sword("gold bar")
except Exception as e:
    print(e)
    
#Types of the errors

# do this
try:
    craft_sword("gold bar")
except Exception as e:
    print(e)
    
#Always handle the specific error first 

try:
    nums = [0, 1]
    print(nums[2])
except Exception:
    print("An error occurred")
except IndexError:
    print("Index error")
#Here the Exception error happens first and IndexError will never run    


###Object Oriented Programing in Python...
"""
OBJECT ORIENTED PROGRAMING
"""

###Classs

# Defines a new class called "Soldier"
# with three properties: health, armor, damage
class Soldier:
    health = 5
    armor = 3
    damage = 2

#classes are custom types that you define.

health = 50
# health is an instance of an integer type
aragorn = Soldier()
# aragorn is an instance of the Soldier class type

class Archer:
    health = 40
    arrows = 10

# Create several instances of the Archer class
legolas = Archer()
bard = Archer()

# Print class properties
print(legolas.health) # 40
print(bard.arrows) # 10




class Soldier:
    health = 5

    # This is a method that reduces the
    # health of the soldier
    def take_damage(self, damage):
        self.health -= damage
        return self.health
    """Methods are defined within the class declaration.
      Their first parameter "self" is always the instance of 
      the class that the method is being called on. 
    """

soldier_one = Soldier()
soldier_one.take_damage(2)
print(soldier_one.health)
# prints "3"

soldier_two = Soldier()
soldier_two.take_damage(1)
print(soldier_two.health)
# prints "4"



class Soldier:
    health = 100

    def take_damage(self, damage, multiplier):
        # "self" is dalinar in the first example
        #
        damage = damage * multiplier
        self.health -= damage

dalinar = Soldier()
# "damage" and "multiplier" are passed explicitly as arguments
# 20 and 2, respectively
# "dalinar" is passed implicitly as the first argument, "self"
dalinar.take_damage(20, 2)
print(dalinar.health)
# 60

adolin = Soldier()
# Again, "adolin" is passed implicitly as the first argument, "self"
# "damage" and "multiplier" are passed explicitly as arguments
adolin.take_damage(10, 3)
print(adolin.health)
# 70


##We USe constructor to pass the values to the class vaiables

class Soldier:
    def __init__(self, name, armor, num_weapons):
        self.name = name
        self.armor = armor
        self.num_weapons = num_weapons

soldier_one = Soldier("Legolas", 2, 10)
print(soldier_one.name)
# prints "Legolas"
print(soldier_one.armor)
# prints "2"
print(soldier_one.num_weapons)
# prints "10"

soldier_two = Soldier("Gimli", 5, 1)
print(soldier_two.name)
# prints "Gimli"
print(soldier_two.armor)
# prints "5"
print(soldier_two.num_weapons)
# prints "1"


