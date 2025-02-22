MAX_TICKETS = 5 #for testing purposes
EXIT_CODE = "xxx"
tickets_sold = 0

while tickets_sold < MAX_TICKETS:
    name = input("Name: ")
    if name == EXIT_CODE:
        break
    tickets_sold += 1

if tickets_sold == MAX_TICKETS:
    print(f"All {MAX_TICKETS} have been sold")
else:
    print(f"{tickets_sold} / {MAX_TICKETS} have been sold")
