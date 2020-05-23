import os
import csv

bank_csv = os.path.join('Resources', 'budget_data.csv')

profits = []
months = []

with open(bank_csv) as csv_file:

    csv_reader = csv.reader(csv_file, delimiter=',')
    # Create header
    header = next(csv_reader)

    for row in csv_reader:
        # fill the lists created for profits and months
        profits.append(int(row[1]))
        months.append(row[0])

sumProfit = sum(profits)

result = [profits[i + 1] - profits[i] for i in range(len(profits)-1)]

avgChange = round((sum(result)/len(result)), 2)

greatestIncrease = max(result)
increaseIndex = result.index(max(result))
increaseMonth = (months[increaseIndex + 1])

greatestDecrease = min(result)
decreaseIndex = result.index(min(result))
decreaseMonth = (months[decreaseIndex + 1])

month_count = len(months)

# Print Results
print("Financial Analysis")
print("------------------------")
print(f"Total Months: {month_count}")
print(f"Total Profits: ${sumProfit}")
print(f"Average Change: ${avgChange}")
print(f"Greatest Increase in Profits: {increaseMonth} ${greatestIncrease}")
print(f"Greatest Decrease in Profits: {decreaseMonth} ${greatestDecrease}")

# Output to txt file
PyBank = open("PyBank.txt", "w")

PyBank.writelines("Financial Analysis")
PyBank.writelines("\n------------------------")
PyBank.writelines(f"\nTotal Months: {month_count}")
PyBank.writelines(f"\nTotal Profits: ${sumProfit}")
PyBank.writelines(f"\nAverage Change: ${avgChange}")
PyBank.writelines(f"\nGreatest Increase in Profits: {increaseMonth} ${greatestIncrease}")
PyBank.writelines(f"\nGreatest Decrease in Profits: {decreaseMonth} ${greatestDecrease}")
