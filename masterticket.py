SERVICE_CHARGE = 2
TICKET_PRICE = 10

tickets_remaining = 100

def calculate_price(number_of_tickets):
    return (number_of_tickets * TICKET_PRICE) + SERVICE_CHARGE

while tickets_remaining >= 1:
    print("There are {} tickets remaining".format(tickets_remaining))
    name = input("What is your name?   ")
    num_tickets = input("{}, How many tickets would you like?  ".format(name))
    try:
        num_tickets = int(num_tickets)
        if num_tickets > tickets_remaining:
            raise ValueError("There are only {} ticket's remaining.".format(tickets_remaining))
    except ValueError as err:
        print("Oh no, we ran into an issue. {}. Please try again.".format(err))
    else:
        amount_due = calculate_price(num_tickets)
        print("Total due is {}".format(amount_due))
        should_proceed = input("Do you want to proceed?  Y/N  ")
        if should_proceed.lower() == "y":
            print("Sold")
            tickets_remaining -= num_tickets
        else:
            print("Thank you anyways, {}.".format(name))
print("Sorry, we are sold out")