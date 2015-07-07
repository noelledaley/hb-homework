"""
Prints out all the melons in our inventory
"""

from melons import melons

def print_melon(melons):
    for melon_type, melon_data in melons.items():
        # items returns a list of tuples, making it easy to unpack multiple variables at once
        print melon_type
        for description, value in melon_data.items():
            print "%s: %r" % (description, value)
        print "\n"

print_melon(melons)
