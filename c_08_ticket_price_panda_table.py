import pandas
response = ''
EXIT_CODE = "xxx"
CHILD_PRICE = 7.50
ADULT_PRICE = 10.50
SENIOR_PRICE = 6.50
CREDIT_SURCHARGE = 0.05
total = 0
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

while True:
    user_name = not_blank("Name: ")
    if user_name == EXIT_CODE:
        break
    names.append(user_name)
    user_age = int_checker("Age: ")
    ages.append(user_age)

    if user_age < 12:
        print(f"{user_name} is too young")
        continue
    elif user_age > 120:
        print(f"{user_age} is too old")
        continue
    else:
        pass
    if user_age < 16:
        total = CHILD_PRICE
    elif user_age < 65:
        total = ADULT_PRICE
    else:
        total = SENIOR_PRICE
    ticket_costs.append(total)
    payment = string_checker("What payment method do you want to use: ", ["cash", "credit"], 2)
    if payment == "credit":
        surcharge = CREDIT_SURCHARGE*total
        total += surcharge
    else:
        surcharge = 0
    surcharges.append(surcharge)

    print(f"{user_name} has brought a ticket using {payment} for a total of ${total:.2f}, incurring a surcharge of ${surcharge:.2f}")

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

