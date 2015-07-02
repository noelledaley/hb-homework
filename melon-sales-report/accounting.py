"""
* Counts the amounts of each type of melon that were sold
* Calculates the revenue from those melon tallies
* Separates sales into online sales and phone sales
* Produces fancy report to summarize the info for our CEO

Ordering tasks into their own functions would be a great
start!
"""

SALESPERSON_INDEX = 0
INTERNET_INDEX = 1

def print_divider():
    print '*' 80

def count_melons(orders_file):
    """Takes a file and returns the amount of each type of melon that was sold.
    """

    fin = open(orders_file)
    melon_tallies = {"Musk":0, "Hybrid":0, "Watermelon":0, "Winter": 0}

    print "*" * 80

    for line in fin:  # switched variable name from l to line to be more clear
        data = line.split("|")
        melon_type = data[1]
        melon_count = int(data[2])
        melon_tallies[melon_type] += melon_count

print_divider()
count_melons("orders-by-type.txt")

def calculate_revenue(melon_tallies):
    """Takes a dictionary of melon tallies and returns the sales revenue.
    """

    melon_prices = { "Musk": 1.15, "Hybrid": 1.30, "Watermelon": 1.75, "Winter": 4.00 }
    total_revenue = 0
    
    for melon_type in melon_tallies:
        price = melon_prices[melon_type]
        revenue = price * melon_tallies[melon_type]
        total_revenue += revenue
        print "We sold %d %s melons at %0.2f each for a total of %0.2f" % (melon_tallies[melon_type], melon_type, price, revenue)

print "******************************************"

f = open("orders-with-sales.txt")
sales = [0, 0]
for line in f:
    d = line.split("|")
    if d[1] == "0":
        sales[0] += float(d[3])
    else:
        sales[1] += float(d[3])
print "Salespeople generated %0.2f in revenue." % sales[1]
print "Internet sales generated %0.2f in revenue." % sales[0]
if sales[1] > sales[0]:
    print "Guess there's some value to those salespeople after all."
else:
    print "Time to fire the sales team! Online sales rule all!"
print "******************************************"
