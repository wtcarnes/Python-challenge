import os
import csv
budget_csv = os.path.join("..", "PyBank", "budget_data.csv")
month = []
profit_loss = []
with open(budget_csv, newline="") as csvfile:
    csvReader = csv.reader(csvfile, delimiter=",")
    next(csvfile, None)
    For row in csvReader
        month.append(row[0])
        Profit_loss.append(row[1])
    total_months = len(month)
    positive_delta = profit_loss[0] 
    negative_delta = profit_loss[0]
    sum_profit_loss = 0 
    For m in range(len(profit_loss)):
        if profit_loss[m] >= positive_delta:
            positive_delta = profit_loss[m]
            p_date = month[m]
        elif profit/loss[m] <= negative_delta:
            negative_delta = profit_loss[m]
            n_date = month[m]
        sum_profit_loss += profit_loss[m]
    avg_profit_loss = (sum_profit_loss/total_months)

    