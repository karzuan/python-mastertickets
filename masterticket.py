TICKET_PRICE = 10
SERVICE_CHARGE = 2
tickets_remaining = 100

def calculate_price(number_of_tickets):
    result = number_of_tickets * TICKET_PRICE + SERVICE_CHARGE
    return result

user = input("What's your name?  ")

while(tickets_remaining>0):

    print("Hey {}! There are {} tickets remaining ".format(user, tickets_remaining))
    try:
        number_of_tickets = int(input("How many tickets would you like to buy, {}?  ".format(user)))
        # if there are less tickets then they want
        if ( tickets_remaining - number_of_tickets < 0):
            raise ValueError("Sorry, we don't have that much tickets. There are only {} remaining. Try to buy less...".format(tickets_remaining))

    except ValueError as err:
        print("Please, try again...")
        print("({})".format(err))    

    else:    
        total_cost = calculate_price(number_of_tickets)
        print("The total cost of your ofder gonna be ${}! (Service Charge ${} is included)  ".format(total_cost, SERVICE_CHARGE))

        decision = input("Would you like to confirm the order?( y/n )  ")

        if decision == "y":
            print("SOLD! Thank you for the purchase {}!".format(user))
            tickets_remaining = tickets_remaining - number_of_tickets
            print("The remaining amount of tickets is {}.".format(tickets_remaining))
        else:
            print("The remaining amount of tickets is {}.".format(tickets_remaining))

else:
      print("We are sold out!")