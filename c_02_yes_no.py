response = ''
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


while True:
    check = string_checker("Would you like to read the instructions?\n", ["yes","no"], 1)
    print(f"You chose {check}")
    funds = string_checker("Would you like to pay with Cash or Credit?\n", ["cash","credit"], 2)
    print(f"You chose {response}")
    print("Program Continues...")