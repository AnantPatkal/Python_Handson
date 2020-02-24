
Films = {
    "Malang":[15,5], #Here 1 element is age ,second is seats available
    "Bhoot":[16,4],
    "Street Dancer":[12,6],
    "Love Aaj Kal":[14,5]
}

print("Please select movie from the  list of movies  :")
print(" 1-Malang \n 2-Bhoot \n 3-Street Dancer \n 4-Love Aaj Kal  ")

while True:
    choice=input("Which movie you want to watch :").title()
    if choice in Films:
        age=int(input("How old are you? ").strip())
        #check user 's age
        if age>= Films[choice][0]:
         #checks seats available
            seats_available=Films[choice][1]
            if seats_available>0:
                NoOfTickets=int(input("How many tickets you want to book? : "))
                if Films[choice][1]>NoOfTickets:
                  print(" You want to book {} tickets :".format(NoOfTickets))
                  Films[choice][1]=Films[choice][1]-NoOfTickets
                  print("Tickets available : ")
                  print("Enjoy your movie!! ")
                else :
                    print("OOps!!  The no. of seats to book is more than available seats  ")
                    print("Available seats: {} ".format(Films[choice][1]))
            else:
                print("No seats available!!OOps ")
        else :
            print("Oops you are too young")
    else :
        print("Please select movies from list")
        print(" 1-Malang \n 2-Bhoot \n 3-Street Dancer \n 4-Love Aaj Kal  ")
