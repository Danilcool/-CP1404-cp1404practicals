money_received = float(input("Enter the amount received: "))
money_paid = float(input("Enter the amount paid: "))

money_returned = money_received - money_paid
print("Money returned:", money_returned)

money_list = [2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01]

for money in money_list:
    count = int(money_returned / money)
    if count > 0:
        print(count, "x", money)
        money_returned -= count * money