print("===============================================================")
      
print("                  FLIGHT RESERVATION SYSTEM                     ")

print ("===============================================================")
while True:
    print("\n1.Passenger\n2.Cashier\n3.Exit")
    choice=int(input("Enter your choice:"))
    if choice==1:
        while True:
            print("----------Passenger----------")
            print("\n1.SignUp\n2.SignIn\n3.Exit")
            passchoice=int(input("Enter your choice:"))
            if passchoice==1:
                print("---SignUp---")
                Name=input("Enter your Name:")
                Email=input("Enter your Email:")
                password=input("Enter your Password:")
                print(" Account Successfully Created.....")
            elif passchoice==2:
                print("---SignIn---")
                Email=input("Enter your Email:")
                password=input("Enter your Password:")
                print("successfully logged in!")
                while True:
                    print("---Passenger Menu---")
                    print("\n1. Check Availability\n2. Book Ticket\n3. Cancel Ticket\n4. Status Checking\n5. Exit")
                    option=int(input("Enter your option:"))
                    if option==1:
                        print("Available Flights:\nChennai To Mumbai:101 Flight\nMumbai To Delhi:102 Flight\nDelhi To Hyderabad:103 Flight")
                    elif option==2:
                        print("---Booking Ticket:---")
                        Flight=int(input("Enter your Flight Number:"))
                        Passenger=input("Enter your Passenger Name:")
                        Ticket=("Flight:",Flight,'\n'"Passenger:",Passenger)
                        print("Ticket Booked Successfully!")
                    elif option==3:
                        print("---Cancel Ticket:---")
                        ticket=input("Enter your Ticket Number:")
                        print("Ticket Canceled Successfully!")
                    elif option==4:
                        print("---Status---")
                        Ticket=input("Enter your Ticket Number:")
                        print("Ticket:",Ticket)
                        print("Waiting for Approval..")
                    elif option==5:
                        print("-->Exiting Passenger Menu..")
                        break
                    else:
                        print("Invalid Try again..")
            elif passchoice==3:
                print("--> Exiting Passenger....")
                break
            else:
                print("Invalid choice....")
    elif choice==2:
        while True:
            print("----------Cashier-----------")
            print("\n1.Approve Ticket\n2.Cancel Ticket\n3.Exit")
            caschoice=int(input("Enter your caschoice:"))
            if caschoice==1:
                Ticket=input("Enter your Ticket Number:")
                print("Ticket:",Ticket,"Approved successfully")
            elif caschoice==2:
                Ticket=input("Enter your Ticket Number:")
                print("Ticket:",Ticket,"Canceled successfully")
            elif caschoice==3:
                print("--> Exiting Cashier..")
                break
            else:
                print("Invalid Choice....")
    elif choice==3:
        print("Thank you for using Flight Reservation System...")
        break
    else:
        print("Invalid Choice.Try again..")










