#Definitions/Imports
import pandas
import random
response = ''
EXIT_CODE = "xxx"

#Ticket Information
MAX_TICKETS = 5 #for testing purposes
tickets_sold = 0
CHILD_PRICE = 7.50
ADULT_PRICE = 10.50
SENIOR_PRICE = 6.50
CREDIT_SURCHARGE = 0.05
total = 0

#Arrays/Dictionaries
names = []
ages = []
ticket_costs = []
surcharges = []
dictionary = {
    "Name": names,
    "Age": ages,
    "Ticket Price": ticket_costs,
    "Surcharge": surcharges
}

#Functions
def instructions():
    instruction_heading = statement_decorator("Instructions", "⚠️", 1)
    print("For each ticket holder, please enter...\n- Their Name\n- Their Age\n- The Payment Method")
    print("The program will record the sale and calculate the total cost and profit.\n")
    print("Once you have sold all of the tickets or entered the exit code('xxx'), the program will display your ticket information and write it into a text file.\n")
    print("It will also choose one lucky ticket holder who will get their ticket for free")

def statement_decorator(message, decoration, lines):
    if lines == 1:
        print(f"{decoration * 3} {message} {decoration * 3}")
    elif lines == 2:
        print(f"{decoration * 3} {message} {decoration * 3}")
        for char in range(0, len(message) + 8):
            print(decoration, end="")
        print()
    else:
        for char in range(0, len(message) + 8):
            print(decoration, end="")
        print(f"\n{decoration * 3} {message} {decoration * 3}")
        for char in range(0, len(message) + 8):
            print(decoration, end="")
        print()

def string_checker(question, answers, len_letters):
    while True:
        global response
        response = input(question).lower()
        for i in answers:
            if response == i:
                response = i
                return response
            elif response == i[:len_letters]:
                response = i
                return response

        print(f"That response is invalid, please select an option from the following:\n{str(answers).replace(","," or ").strip("[").strip("]")}")

def not_blank(question):
    numbers_in_response = 0
    while True:
        response = input(question)
        if response != '':
            for char in response:
                if char.isdigit():
                    numbers_in_response += 1
            if numbers_in_response == 0:
                return response
            else:
                print("There was a number in your response. Please try again")
                numbers_in_response = 0
        else:
            print("That value is invalid")

def int_checker(question):
    error = "Please enter a valid age"
    while True:
        response = input(question).lower()

        try:
            response = int(response)
            if response == int(response):
                return response
            else:
                print(error)

        except ValueError:
            print(error)

def currency(x):
    return "${:.2f}".format(x)


#Main Routine
heading = statement_decorator("Movie Fundraiser", "🎬", 1)
check = string_checker("Would you like to read the instructions?\n", ["yes","no"], 1)
print(f"You chose {response}")
if response == "yes":
    instructions()
else:
    print("Ok. Please proceed with your purchases")

while tickets_sold < MAX_TICKETS:
    user_name = not_blank("Name: ")
    if user_name == EXIT_CODE:
        break
    user_age = int_checker("Age: ")

    if user_age < 12:
        print(f"{user_name} is too young for this movie")
        continue
    elif user_age > 120:
        print(f"{user_age} is too old for this film, perhaps you did a typo?")
        continue
    else:
        pass
    ages.append(user_age)
    names.append(user_name)
    if user_age < 16:
        total = CHILD_PRICE
    elif user_age < 65:
        total = ADULT_PRICE
    else:
        total = SENIOR_PRICE
    ticket_costs.append(total)
    payment = string_checker("What payment method do you want to use: ", ["cash", "credit"], 2)
    if payment == "credit":
        surcharge = CREDIT_SURCHARGE * total
        total += surcharge
    else:
        surcharge = 0
    surcharges.append(surcharge)
    tickets_sold += 1

frame = pandas.DataFrame(dictionary)
frame["Total"] = frame["Ticket Price"] + frame["Surcharge"]
frame["Profit"] = frame["Ticket Price"] - 5.00
total_cost = frame["Total"].sum()
total_profit = frame["Profit"].sum()
currency_format = ["Ticket Price","Surcharge","Total","Profit"]
for var_item in currency_format:
    frame[var_item] = frame[var_item].apply(currency)
print(frame.to_string(index=False))
print()
print(f"Total Cost: ${total_cost:.2f}")
print(f"Total Profit: ${total_profit:.2f}")
print()
winner = random.choice(names)
winner_index = names.index(winner)
winner_ticket_cost = ticket_costs[winner_index]
winner_surcharge =  surcharges[winner_index]
winner_total_amount = frame.at[winner_index, "Total"]
print(f"Winner: {winner}, list pos {winner_index}, they won a {winner_total_amount} ticket for free")

if tickets_sold == MAX_TICKETS:
    print(f"All {MAX_TICKETS} have been sold")
else:
    print(f"{tickets_sold} / {MAX_TICKETS} have been sold")
