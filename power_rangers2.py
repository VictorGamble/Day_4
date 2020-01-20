power_rangers = ["Jason", "zach", "billy", "tommy", "kim"]
whoToRemove = input("who would you remove from this list? ")


if whoToRemove in power_rangers:
    power_rangers.remove(whoToRemove)
    print(power_rangers)
else:
    print(whoToRemove + " " + "isn't part of the list ")