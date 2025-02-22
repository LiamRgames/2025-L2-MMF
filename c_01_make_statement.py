#Statement Decorator Multi Line and Flexible

def statement_decorator(message, decoration, lines):
    if lines == 1:
        print(f"{decoration*3} {message} {decoration*3}")
    elif lines == 2:
        print(f"{decoration * 3} {message} {decoration * 3}")
        for char in range(0, len(message) + 8):
            print(decoration, end="")
        print()
    else:
        for char in range(0, len(message) + 8):
            print(decoration, end="")
        print(f"\n{decoration*3} {message} {decoration*3}")
        for char in range(0, len(message) + 8):
            print(decoration, end="")
        print()


instruction_heading = statement_decorator("Instructions", "⚠️", 1)