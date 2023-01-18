import os
import csv

budget_data_csv = os.path.join("Resources", "budget_data.csv")

#set variables
output_text = "output.txt"

total_months = 0
net_total_profit = 0

revenue_change = 0 
previous_profit = 0
average_change = 0

max_increase = 0
max_decrease = 0
max_month = 0
min_month = 0

total_profit_list = []
revenue_change_list = []
date_list = []



with open(budget_data_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    header = next(csvreader)

    for row in csvreader:
        total_months = total_months + 1 # loops through the csv and counts each month to get the total months
        date_list.append(row[0])


        net_total_profit = net_total_profit + (int(row[1])) 
        total_profit_list.append(int(row[1])) # adds the total profit to the list. 

    for i in range(len(total_profit_list)-1): # to loops through each item in the profit/losses list (row 1)
        revenue_change_list.append(total_profit_list[i+1] - total_profit_list[i]) # find the difference between the previous profit and the current profit
    
        average_change = round(sum(revenue_change_list)/len(revenue_change_list),2) 
        
        max_increase = max(revenue_change_list) # python maximum function 
 
        max_decrease = min(revenue_change_list) #use python min function 
   

        max_month = revenue_change_list.index(max(revenue_change_list)) + 1 #https://www.geeksforgeeks.org/python-list-index/
        min_month = revenue_change_list.index(min(revenue_change_list)) + 1

        max_increase_date = date_list[max_month]
        max_decrease_date = date_list[min_month] 
    

# prints results in output file
with open(output_text, "w") as csvfile: 
  budget_analysis_final = (
    f"Financial Analysis \n" 
    f"---------------- \n"
    f"Total Months: {total_months} \n"
    f"Total Profit: ${net_total_profit} \n"
    f"Average Change: ${average_change} \n"
    f"Greatest Increase in Profits: {max_increase_date} ${max_increase} \n"
    f"Greatest Decrease in Profits: {max_decrease_date} ${max_decrease} \n" )
  print(budget_analysis_final)

  csvfile.write(budget_analysis_final)