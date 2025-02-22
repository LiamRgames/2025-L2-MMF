response = ''
def instructions():
    instruction_heading = statement_decorator("Instructions", "⚠️", 1)
    print("For each ticket holder, please enter...\n- Their Name\n- Their Age\n- The Payment Method")
    print("The program will record the sale and calculate the total cost and profit.\n")
    print("Once you have sold all of the tickets or entered the exit code('exit'), the program will display your ticket information and write it into a text file.\n")
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


heading = statement_decorator("Movie Fundraiser", "🎬", 1)
while True:
    check = string_checker("Would you like to read the instructions?\n", ["yes","no"], 1)
    print(f"You chose {response}")
    if response == "yes":
        instructions()
    else:
        print("Ok. Please proceed with your purchases")
