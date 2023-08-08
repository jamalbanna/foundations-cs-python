users = {}

def menu():
    choice = 0
    while choice != 7 :
        print("1. Add a user to the platform.\n2. Remove a user from the platform.\n3. Send a friend request to another user.\n4. Remove a friend from your list.\n5. View your list of friends.\n6. View the list of users on the platform.\n7. Exit\n- - - - - - - - - - - - - - -")
        choice = input("Enter a choice: ")
        if choice.isnumeric:
            choice = int(choice)
            if choice == 1:
                createUser()
            elif choice == 2:
                deleteUser()
            elif choice == 3:
                sendFriendRequest()
            elif choice == 4:
                removeFriend()
            elif choice == 5:
                viewFriendList()
            elif choice == 6:
                viewUsersList()

def userExists(username):
    return users.get(username) != None

def createUser():
    validNewUser = False
    while(not validNewUser):
        username = input("Enter new user's username: ")
        validNewUser = not userExists(username)
        if not validNewUser:
            print("username is taken") 
    users[username] = []

def deleteUser():
    username = getValidUser()
    usersConnectionList = userConnectionList(username)
    for friend in usersConnectionList:
        removeConnection(username, friend)
    del users[username]

def getValidUser():
    validUser = False
    while(not validUser):
        username = input("Enter username: ")
        validUser = userExists(username)
        if not validUser:
            print("username doesn't exist")
    return username

def sendFriendRequest():
    user1 = getValidUser()
    user2 = getValidUser()
    addConnection(user1,user2)

def addConnection(user1,user2):
    users[user1].append(user2)
    users[user2].append(user1)

def userConnectionList(username):
    return users.get(username)

def removeFriend():
    user1 = getValidUser()
    user2 = getValidUser()
    removeConnection(user1,user2)

def removeConnection(user1,user2):
    users[user1].remove(user2)
    users[user2].remove(user1)

def viewFriendList():
    user = getValidUser()
    print(userConnectionList(user))
    return userConnectionList(user)

def viewUsersList():
    print(users.keys())

menu()