# STATUS: Complete

def run_report(day_num, file):
    # For a given log file, rints a more concise report by getting rid of formatting and whitespace.
    print "Day %d" % day_num
    logs = open(file)
    for line in logs:
        line = line.rstrip()
        words = line.split('|')

        melon = words[0]
        count = words[1]
        amount = words[2]

        print "Delivered %s %ss for total of $%s" % (count, melon, amount)


run_report(1, "um-deliveries-20140519.txt")

run_report(2, "um-deliveries-20140520.txt")

run_report(3, "um-deliveries-20140521.txt")
