"""Ticket Booking Simulation:

Write a program that simulates a bus ticket booking system. The bus has 8 seats.
 Each time a seat is booked, the available seats decrease. When there are no seats left,
   the loop stops and displays a message saying "All seats are booked." """


capacity=8
booked=0
choice=input("Do you want to book tickets Yes or No: ")
while booked < capacity:
    if choice == "Yes":
        print("Welcome we are glad that u have selected our transport")
        name=input("What's ur name? ")
        age=int(input("What's ur age? "))
        quantity=int(input("The capacity of the bus is 8 how much seats do you want to book? "))
        if quantity+booked > capacity:
            print(f"Ohh u cannot book this number of seat but there is {capacity-booked} no of seats are left")
            continue
        booked=booked+quantity
        print(f"No of seat  booked is {quantity} successfully Thank u!")
        choice2=input("Do you want to book another? Yes or No: ")
        if choice2 == "Yes":
            if booked >= capacity:
                print("Oops the seats are out of stock!!!!")
            else:
                pass
        elif choice2 == "No":
            print("Ok it's ur wish")
            break
        else:
            print('Please enter either yes or no')
            break

    elif choice=="No":
        print("ohh you it seems you are looking for something else!")
        break
    else:
        print("Enter your choice as Yes or No")
        break

if booked > capacity:
    print("Oops the seats are out of stock!!!!")