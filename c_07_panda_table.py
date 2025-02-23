import pandas

names = ["John","Bob","Jeff","Hillary","Colin"]
ticket_costs = [6.50,7.50,10.50,10.50,6.50]
surcharges = [0, 0.38, 0, 0.53, 0.33]
dictionary = {
    "Name": names,
    "Ticket Price": ticket_costs,
    "Surcharge": surcharges
}

frame = pandas.DataFrame(dictionary)
frame["Total"] = frame["Ticket Price"] + frame["Surcharge"]
frame["Profit"] = frame["Ticket Price"] - 5.00
total_cost = frame["Total"].sum()
total_profit = frame["Profit"].sum()
print(frame)
print()
print(f"Total Cost: {total_cost:.2f}")
print(f"Total Profit: {total_profit:.2f}")