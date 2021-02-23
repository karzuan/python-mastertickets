import math

def count(total_value, number_of_guests):
    if number_of_guests <= 1:
        raise ValueError("More than 1 person is required to split")
    result = total_value/number_of_guests
    return math.ceil(result)
try:
    guests = int(input( "How many guests?"))
    bill = int(input( "How much?"))
    the_share = count(bill, guests)
except ValueError as err:
    print("Oh no, there is a Value Error. Try again...")
    print("({})".format(err))
# except ZeroDivisionError:
#     print("You can't share the bill with 0 ppl. Try again with more ppl...")
else:
    print("You guys shall pay each: ${}".format(the_share))