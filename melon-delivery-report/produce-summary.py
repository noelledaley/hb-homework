# STATUS: Complete

print "Day 1"
the_file = open("um-deliveries-20140519.txt")
for line in the_file:
    line = line.rstrip()
    words = line.split('|')  # splits line into a list where the items are separated by '|'

    melon = words[0]
    count = words[1] # changed index to correlate with the second item in list
    amount = words[2]  # changed index to correlate with third item in list

    print "Delivered %s %ss for total of $%s" % (count, melon, amount)
the_file.close()


print "Day 2"
the_file = open("um-deliveries-20140520.txt")
for line in the_file:
    line = line.rstrip()
    words = line.split('|')

    melon = words[0]
    count = words[1]
    amount = words[2]

    print "Delivered %s %ss for total of $%s" % (count, melon, amount)
the_file.close()


print "Day 3"
the_file = open("um-deliveries-20140521.txt")
for line in the_file:
    line = line.rstrip()
    words = line.split('|')

    melon = words[0]
    count = words[1]
    amount = words[2]

    print "Delivered %s %ss for total of $%s" % (count, melon, amount)
the_file.close()
