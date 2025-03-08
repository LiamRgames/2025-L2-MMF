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

#file information
file_name = "mega_movie_fundraiser"
file_path = "{}.txt".format(file_name)
text_file = open(file_path, "w+")

#Functions
def instructions():
    print(statement_decorator("Instructions", "=", 1))
    print('''
For each ticket holder, please enter...
- Their Name
- Their Age
- The Payment Method

The program will record the sale and calculate the total cost and profit.
Once you have sold all of the tickets or entered the exit code('xxx'), the program will display your ticket information and write it into a text file.
It will also choose one lucky ticket holder who will get their ticket for free''')

def statement_decorator(message, decoration, lines):
    if lines == 1:
        return f"{decoration * 3} {message} {decoration * 3}"


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
        global response
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
heading = statement_decorator("Movie Fundraiser", "=", 1)
ticket_table_heading = statement_decorator("Ticket Details","-",1)
totals_heading = statement_decorator("Totals", "-",1)
adjusted_totals_heading = statement_decorator("Adjusted Totals","-",1)
winner_heading = statement_decorator("Raffle Winner","-",1)
check = string_checker("Would you like to read the instructions?\n", ["yes","no"], 1)
print(f"You chose {response}")
if response == "yes":
    instructions()
else:
    print("Ok. Please proceed with your purchases")

while tickets_sold < MAX_TICKETS:
    user_name = not_blank("Name: ")
    if user_name == EXIT_CODE:
        if tickets_sold > 0:
            break
        else:
            print("You can't enter the exit code at this time. Please buy a ticket or close the program.")
            continue
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
if names != '':
    winner = random.choice(names)
    winner_index = names.index(winner)
    ticket_won = ticket_costs[winner_index]
    winner_surcharge =  surcharges[winner_index]
    winner_total_amount = frame.at[winner_index, "Total"]
    profit_won = frame.at[winner_index, "Profit"]
else:
    winner = ''
    winner_index = ''
    ticket_won = ''
    winner_surcharge = ''
    winner_total_amount = ''
    profit_won = ''
currency_format = ["Ticket Price","Surcharge","Total","Profit"]
for var_item in currency_format:
    frame[var_item] = frame[var_item].apply(currency)
frame_print_string = frame.to_string(index=False)

total_cost_string = f"Total Cost: ${total_cost:.2f}"
total_profit_string = f"Total Profit: ${total_profit:.2f}"

if names != '':
    winner_string = f"Winner: {winner}, list pos {winner_index}, they won a ${winner_total_amount:.2f} ticket for free"
    updated_total_cost = f"Total Cost is now: ${(total_cost - ticket_won):.2f}"
    updated_total_profit = f"Total Profit is now: ${total_profit - profit_won:.2f}"
else:
    winner_string = ''
    updated_total_cost = ''
    updated_total_profit = ''

if tickets_sold == MAX_TICKETS:
    total_tickets_sold = f"All {MAX_TICKETS} have been sold"
else:
    total_tickets_sold = f"{tickets_sold} / {MAX_TICKETS} have been sold"
write_to_file = [heading, "\n",
                 ticket_table_heading,
                 frame_print_string,"\n",
                 totals_heading,
                 total_cost_string,
                 total_profit_string, "\n",
                 winner_heading,
                 winner_string, "\n",
                 adjusted_totals_heading,
                 updated_total_cost,
                 updated_total_profit,"\n",
                 total_tickets_sold]
print()
for i in write_to_file:
    if i != '':
        print(i)

for i in write_to_file:
    if i != '':
        text_file.write(i)
        text_file.write("\n")
