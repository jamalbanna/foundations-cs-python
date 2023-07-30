from datetime import date

def getDate():
    today = str(date.today()) #https://www.geeksforgeeks.org/get-current-date-using-python/
    today = today.replace("-","")
    return today

#https://stackoverflow.com/questions/67786912/sorting-a-multidimensional-array-using-merge-sort
def merge(left, right):
    
    result = []
    i, j = 0, 0
    while (len(result) < len(left) + len(right)):
        if left[i][3] < right[j][3]:
            result.append(left[i])
            i+= 1
        elif left[i][3] > right[j][3]:
            result.append(right[j])
            j+= 1
        else:
            if left[i][1] < right[j][1]:
                result.append(left[i])
                i+= 1
            elif left[i][1] > right[j][1]:
                result.append(right[j])
                j+= 1
            else:
                if left[i][4] > right[j][4]:
                    result.append(left[i])
                    i+= 1
                else:
                    result.append(right[j])
                    j+= 1               
            
        if i == len(left) or j == len(right):
            result.extend(left[i:] or right[j:])
            break

    return result

def mergesort(list):
    if len(list) < 2:
        return list
    
    middle = len(list)//2
    left = mergesort(list[:middle])
    right = mergesort(list[middle:])

    return merge(left, right)

def readFromFileAndClean(fileName):
    file = open(fileName, "r")
    content = file.read() 
    file.close()
    ticketsList = content.split("\n")[:-1]
    ticketsListNested = []
    today = getDate()
    for i in range(len(ticketsList)):
        currTicketToList = ticketsList[i].split(", ")
        currTicketDate = currTicketToList[3]
        today = getDate()
        ticketsListNested.append(currTicketToList)
        if currTicketDate >= today:
            activeTickets.append(currTicketToList)
    return ticketsListNested

activeTickets = []
ticketsList = readFromFileAndClean("tickets.txt")
sortedTicketsList = mergesort(activeTickets)

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
 
def userMenu(username):
    choice = 0
    while(choice != 2):
        print("1. Book a Ticket\n2.Exit ")
        choice = input("Please select from the above choices")
        if(choice == "1"):
            event = input("Please enter event id")
            userBookATicket(username, event)
        # userIn bookATicket its always saving by appending so no need to save on exit
         
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
    for ticket in sortedTicketsList:
        print(ticket[0], ticket[1], ticket[2], ticket[3], ticket[4])
   
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
    lastIndex = 0
    today = getDate()
    global sortedTicketsList #https://stackoverflow.com/questions/9970400/resetting-values-in-global-array-within-a-function-python
    for ticket in sortedTicketsList:
        lastIndex += 1
        if(ticket[3] > today):
            break;
        print(ticket[0], ticket[1], ticket[2], ticket[3], ticket[4])
    sortedTicketsList = sortedTicketsList[lastIndex:]

def userBookATicket(username, eventId,eventDate):
    lastTicketID = int(ticketsList[-1][0].replace("tick",""))
    newTicket = ["tick" + str(lastTicketID + 1), eventId, username, eventDate , 0]
    ticketsList.append(newTicket)
    appendNewTicket(newTicket)

def appendNewTicket(newTicket):
    content = ""
    for element in newTicket:
        content += element + ", "
    content = content[:-2] + "\n"
    file = open("tickets.txt", "a")
    file.write(content)
    file.close()

logInMenu()

