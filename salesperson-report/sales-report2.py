"""
Alternate version of sales_report.py - Generates sales report showing the total number of melons each sales person sold.
"""

def print_sales_summary(report_file):

    # Opens sales report file
    open_report = open(report_file)

    sales_summary = {}

    # Iterate through every line in the file and add each line to sales_summary
    for line in open_report:

        # Get rid of whitespace and convert each line to a list
        line = line.rstrip()
        entries = line.split("|")

        # Store salesperson name and total price for the order in variable
        salesperson = entries[0]
        melons = int(entries[2])

        # Add salesperson and cumulative melons sold to sales_summary
        if salesperson in sales_summary:
            sales_summary[salesperson] += melons
        else:
            sales_summary[salesperson] = melons

    # Print summary of sales data
    for salesperson, melon_count in sales_summary.items():
        print "%s sold %d melons." % (salesperson, melon_count)

print_sales_summary('sales-report.txt')
