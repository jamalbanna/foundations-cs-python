from datetime import date

activeDatesDictionary = {}

def getDate():
    today = str(date.today()) #https://www.geeksforgeeks.org/get-current-date-using-python/
    today = today.replace("-","")
    return today

def readFromFileAndClean(fileName):
    file = open(fileName, "r")
    content = file.read() 
    file.close()
    ticketsList = content.split("\n")[:-1]
    ticketsListNested = []
    for i in range(len(ticketsList)):
        currTicketToList = ticketsList[i].split(", ")
        ticketsListNested.append(currTicketToList)
    #     currTicketDate = currTicketToList[3]
    #     if currTicketDate >= getDate():
    #         if activeDatesDictionary.get(currTicketDate) == None:
    #             activeDatesDictionary[currTicketDate] = {}
    #         currTicketEvent = currTicketToList[1]
    #         if(activeDatesDictionary[currTicketDate].get(currTicketEvent) == None):
    #             activeDatesDictionary[currTicketDate][currTicketEvent] = []
    #         activeDatesDictionary[currTicketDate][currTicketEvent].append(currTicketToList)
    # print(activeDatesDictionary)
    return ticketsListNested
    
ticketsList = readFromFileAndClean("tickets.txt")

def logInMenu():
    counter = 0
    password = "password"
    print("Hello!")
    while(counter < 5 and password != ""):
        username = input("Please enter your username: ")
        password = input("Please enter your password: ")
        if(username == "admin"):
            if(password == "admin123123"):
                adminMenu()
            else:
                counter += 1
                print("Inccorect Username or/and Password \nYou have " + str((5 - counter)) + " attempts left")
        else:
            if(password == ""):
                userMenu(username)

def adminMenu():
    choice = 0
    while(choice != 7):
        print("\n1. Display Statistics\n2. Book a Ticket\n3. Display all Tickets\n4. Change Ticket’s Priority\n5. Disable Ticket\n6. Run Events\n7. Exit")
        choice = input("Please select from the above choices")
        if(choice == "1"):
            displayStatistics()
        elif(choice == "2"):
            userName = input("enter username you want to book ticket for: ")
            event = input("enter event you want to book ticket for: ")
            priority = input("enter priority of the ticket")
            eventDate = input("enter event date")
            bookATicket(userName, event, priority, eventDate)
        elif(choice == "3"):
            displayAllTickets()
        elif(choice == "4"):
            ticket = input("enter the tickeID that you want to change priority of: ")
            priority = input("enter the new priority of the ticket")
            changeTicketsPriority(ticket, priority)
        elif(choice == "5"):
            ticket = input("enter the tickeID that you want to change priority of: ")
            disableTicket(ticket)
        elif(choice == "6"):
            runEvents()
        elif(choice == "7"):
            save = input("do you want to save? enter 'y' to save")
            if(save == "y"):
                writeNewTickets()
          
def displayStatistics():
    eventCount = {}
    max = 0
    maxEvent = ""
    for ticket in ticketsList:
        ticketCount = eventCount.get(ticket[1])
        if(ticketCount == None):
            eventCount[ticket[1]] = 1
        else:
            eventCount[ticket[1]] += 1
            if(ticketCount + 1 > max):
                max = ticketCount + 1
                maxEvent = ticket[1] 
    print("event with max tickets is: " + maxEvent)

def bookATicket(username, eventId, priority,eventDate):
    lastTicketID = int(ticketsList[-1][0].replace("tick",""))
    newTicket = ["tick" + str(lastTicketID + 1), eventId, username, eventDate , str(priority)]
    ticketsList.append(newTicket)
      
def appendNewTicket(newTicket):
    content = ""
    for element in newTicket:
        content += element + ", "
    content = content[:-2] + "\n"
    file = open("tickets.txt", "a")
    file.write(content)
    file.close()

def writeNewTickets():
    content = ""
    for ticket in ticketsList:
        for element in ticket:
            content += element + ", "
        content = content[:-2] + "\n"
    print(content)
    file = open("tickets.txt", "w")
    file.write(content)
    file.close()

def displayAllTickets():
    for ticket in ticketsList:
        if(ticket[4] >= getDate()):
            print("sorting algrithm")

def changeTicketsPriority(ticketToChange, newPriority):
    index = findTicketIndex(ticketToChange)
    if(index == -1):
        print("ticket not found")
    else:
        ticketsList[index][4] = newPriority

def findTicketIndex(ticketToFind):
    for i in range(len(ticketsList)):
        if(ticketsList[i][0] == ticketToFind):
            return i
    return -1

def disableTicket(ticketToChange):
    index = findTicketIndex(ticketToChange)
    if(index == -1):
        print("ticket not found")
    else:
        del ticketsList[index] #https://stackoverflow.com/questions/627435/how-to-remove-an-element-from-a-list-by-index       

def runEvents():
    ticketsOfToday = activeDatesDictionary[getDate()]
    sortedTicketsOfToday = sortEvents(ticketsOfToday)
    print(sortedTicketsOfToday)

def sortEvents(ticketsList):
    print()
    #merge sort algorithm

def userBookATicket(username, eventId,eventDate):
    lastTicketID = int(ticketsList[-1][0].replace("tick",""))
    newTicket = ["tick" + str(lastTicketID + 1), eventId, username, eventDate , 0]
    ticketsList.append(newTicket)
    appendNewTicket(newTicket)

def userMenu(username):
    choice = 0
    while(choice != 2):
        print("1. Book a Ticket\n2.Exit ")
        choice = input("Please select from the above choices")
        if(choice == "1"):
            event = input("Please enter event id")
            userBookATicket(username, event)
        # userIn bookATicket its always saving by appending so no need to save on exit

