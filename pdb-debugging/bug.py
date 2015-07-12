import pdb; pdb.set_trace()

numbers = [1, 2, 3, 4, 10, -4, -7, 0]

def all_even(l):

    even_numbers = []

    for number in l:
        if number / 2 == 0:
            even_numbers.extend(number)

    return even_numbers

print all_even(numbers)
