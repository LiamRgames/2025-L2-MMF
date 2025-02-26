import pandas
import random

names = ["John","Bob","Jeff","Hillary","Colin"]
ages = [10, 16, 45, 64, 65]
ticket_costs = [6.50,7.50,10.50,10.50,6.50]
surcharges = [0, 0.38, 0, 0.53, 0.33]
dictionary = {
    "Name": names,
    "Age": ages,
    "Ticket Price": ticket_costs,
    "Surcharge": surcharges
}

frame = pandas.DataFrame(dictionary)
frame["Total"] = frame["Ticket Price"] + frame["Surcharge"]
frame["Profit"] = frame["Ticket Price"] - 5.00
total_cost = frame["Total"].sum()
total_profit = frame["Profit"].sum()
print(frame.to_string(index=False))
print()
winner = random.choice(names)
winner_index = names.index(winner)
winner_ticket_cost = ticket_costs[winner_index]
winner_surcharge =  surcharges[winner_index]
winner_total_amount = frame.at[winner_index, "Total"]
print(f"Winner: {winner}, list pos {winner_index}, they won a ${winner_total_amount:.2f} ticket for free")
print(f"Total Cost: {total_cost:.2f}")
print(f"Total Profit: {total_profit:.2f}")