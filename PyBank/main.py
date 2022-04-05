#import from source file and read csv file
import os
import csv

csvpath = os.path.join("Resources","budget_data.csv")
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    header = next(csvreader)
    
#create list
    month_count = []
    profit = []
    change_profit = []
                      
#add values to list 
    for row in csvreader:
        month_count.append(row[0])
        profit.append(int(row[1]))
    for i in range(len(profit)-1):
        change_profit.append(profit[i+1]-profit[i])
                      
#max and min profits and dates
increase = max(change_profit)
decrease = min(change_profit)

month_increase = change_profit.index(max(change_profit))+1
month_decrease = change_profit.index(min(change_profit))+1

#calculate average change, greatest increase and decrease dates
average_change = round(sum(change_profit)/len(change_profit),2)
greatest_increase_date = month_count[month_increase]
greatest_decrease_date = month_count[month_decrease]


print("Financial Analysis")
print("------------------------")
print(f"Total Months:{len(month_count)}")
print(f"Total: ${sum(profit)}")
print(f"Average Change:{(average_change)}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${(str(increase))})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${(str(decrease))})")     

# save the output file path as a txt file to Analysis folder
output = os.path.join("Analysis", 'output.txt')
with open(output,"w") as new:
    new.write("Financial Analysis")
    new.write("\n")
    new.write("----------------------------")
    new.write("\n")
    new.write(f"Total Months:{len(month_count)}")
    new.write("\n")
    new.write(f"Total: ${sum(profit)}")
    new.write("\n")
    new.write(f"Average Change: {(average_change)}")
    new.write("\n")
    new.write(f"Greatest Increase in Profits: {greatest_increase_date} (${(str(increase))})")
    new.write("\n")
    new.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${(str(decrease))})")