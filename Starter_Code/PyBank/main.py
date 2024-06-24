import os
import csv

# Define the path to the CSV file
csvpath = os.path.join("Resources", "budget_data.csv")
outputfile = os.path.join("analysis", "budget_summary.txt")
# Check if the file exists at the specified path
if not os.path.isfile(csvpath):
    print(f"File not found at {csvpath}")
else:
    # Sum the profit/losses column and calculate other metrics
    with open(csvpath) as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=",")
        next(csv_reader)  # Skipping header row

        # Initializing counters and variables
        total_months = 0
        total_profit_losses = 0
        prev_profit_loss = None
        changes = []
        months = []

        for row in csv_reader:
            # Extract month and profit/loss values
            month = row[0]
            profit_loss = int(row[1])
            
            # Count total months
            total_months += 1
            
            # Sum total profit/losses
            total_profit_losses += profit_loss
            
            # Calculate monthly changes in profit/losses
            if prev_profit_loss is not None:
                change = profit_loss - prev_profit_loss
                changes.append(change)
                months.append(month)
            prev_profit_loss = profit_loss
        
        # Calculate average change in profit/losses
        avg_change = sum(changes) / len(changes) if changes else 0
        
        # Find the greatest increase and decrease in profits
        greatest_increase = max(changes) if changes else 0
        greatest_decrease = min(changes) if changes else 0
        greatest_increase_month = months[changes.index(greatest_increase)] if changes else "N/A"
        greatest_decrease_month = months[changes.index(greatest_decrease)] if changes else "N/A"
        
       
data_output = (
        f"Financial Analysis\n"
        f"----------------------------\n"
        f"Total Months: {total_months}\n"
        f"Total: ${total_profit_losses}\n"
        f"Average Change: ${avg_change:.2f}\n"
        f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})\n"
        f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})\n")
print (data_output)

with open(outputfile, "w") as txt_file:
        txt_file.write(data_output)
    
