response = ''
CHILD_PRICE = 7.50
ADULT_PRICE = 10.50
SENIOR_PRICE = 6.50
CREDIT_SURCHARGE = 0.05
total = 0

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

while True:
    user_name = not_blank("Name: ")
    user_age = int_checker("Age: ")

    if user_age < 12:
        print(f"{user_name} is too young")
        continue
    elif user_age > 120:
        print(f"{user_age} is too old")
        continue
    else:
        pass
    if 12 <= user_age <= 15:
        total = CHILD_PRICE
    elif 16 <= user_age <= 64:
        total = ADULT_PRICE
    else:
        total = SENIOR_PRICE

    payment = string_checker("What payment method do you want to use: ", ["cash", "credit"], 2)
    if payment == "credit":
        surcharge = CREDIT_SURCHARGE*total
        total += surcharge
    else:
        surcharge = 0

    print(f"{user_name} has brought a ticket using {payment} for a total of ${total:.2f}, incuring a surcharge of ${surcharge:.2f}")