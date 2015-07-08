"""
sales_report.py - Generates sales report showing the total number
                  of melons each sales person sold.
"""

salespeople = []
melons_sold = []

# Opens sales report file
report_file = open("sales-report.txt") # fixed typo in file name & renamed variable to be more clear

# Iterate through every line in the file
for line in report_file:

    # Get rid of whitespace and convert each line to a list
    line = line.rstrip()
    entries = line.split("|")

    # Store salesperson name and total price for the order in variable
    salesperson = entries[0]
    order_amount = int(entries[2]) # renamed variable

    # Add salesperson and their cumulative orders sold to salespeople and melons_sold lists
    if salesperson in salespeople:
        # The .index function returns the index of salesperson, which theoretically correlates to the index of their number of melons sold
        position = salespeople.index(salesperson)
        melons_sold[position] += melons
    else:
        salespeople.append(salesperson)
        melons_sold.append(melons)

# Prints a summary of the report
for i in range(len(salespeople)):
    print "%s sold %d melons" % (salespeople[i], melons_sold[i])
