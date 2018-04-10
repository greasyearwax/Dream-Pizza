choice = 0
cost = 0
name = ""
pizzalist =[]
dorp = ""       ## Declaring Variables
stat = ""
number = 0
address = ""
pizzatypes = { ## List of different Pizzas
    1: "Crunchie Muchie",
    2: "Pleasin Cheesen",
    3: "Fat Cat",
    4: "Sour flower",
    5: "Beaty Meat",
    6: "jerken Gherkin",
    7: "Bloody Mary",
    8: "Pugs 'n' Spud",
    9: "Drunk Skunk",
    10: "Trippa Snippa",
    11: "xTRA greasy",
    12: "Base free Pizza"
    }
def dp():  ## Function for Delivery or Pickup
    global stat, dorp, number, address, cost
    stat = input("Do you want to pickup?(y/n)")
    while(True):
        if stat.lower() == 'y':
            dorp = "Pickup"
            break
        elif stat.lower() == 'n':
            dorp = "Delivery"
            cost = cost+3
            address = input("What is your address: ")
            number = input("What is your number: ")
            break
        else:
            print("Invalid Response")
def finalorder(): ## Function to display The final order
    global cost, name, pizzalist, dorp, stat, number, address
    print("*"*36)
    print("Client Name: ", name)
    print("Delivery or Pickup: ", dorp)
    if stat.lower() == "n":
        print("Phone Number: ", number)
        print("Address: ", address)
    print("Cost: $" + str(cost))
    print("*"*36)
def order(): ## Function to display a basic version of the final order
    global cost, name, pizzalist
    print("Client Name: ", name)
    print("Cost: $", cost)
    print(pizzalist)
    print("*"*36)
def menu(): ## Function to display the menu
    print("*"*16 + "MENU" + "*"*16)
    for k, v in pizzatypes.items():
        print(" "*10 + str(k) + " " + str(v))
    print("*"*36)
def main(): ## Main Function
    global cost, name, pizzalist
    name = input('Client Name: ')
    menu()
    for i in range(5):
        while(1 == 1):
            pizza = int(input('Please select a pizza:'))
            if pizza > 0 and pizza <13:            ## Making sure the client does not select a value outside of the range
                pizzalist.append(pizzatypes[pizza])
                break
            else:
                print("Error please enter pizza within the specified range")
        if pizza <= 7:
            cost = cost+8.50
        elif pizza >= 8:  ## Calculating cost
            cost = cost+8.50+5.00
        print('''
            1: "Cancel",
            2: "Finish"
            3: "Continue order"
            ''')
        orderchoice = int(input())
        while(1 == 1):
            if orderchoice == 1:
                cost = 0
                name = ""
                pizzalist =[]
                dorp = "" ## Clearing Variables
                stat = ""
                number = 0
                address = ""
                main()
                choice = 0
                break
            elif orderchoice == 2:
                dp()
                break
            elif orderchoice == 3:
                break
            else:
                print("Error please use specified integers")
        if orderchoice == 2:
            break
        if i == 5:
            dp()
            break
        menu()
        order()
    finalorder()
main()
