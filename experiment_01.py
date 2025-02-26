import random
fruits = ['apple','strawberry','banana','blueberry']
colours = ['red','red','yellow','blue']

random_fruit = random.choice(fruits)

#Finds the position of the randomly selected item in the array
fruit_index = fruits.index(random_fruit)

first_colour = colours[fruit_index]

print(f"first fruit: {fruits[fruit_index]} | first colour: {colours[fruit_index]}")