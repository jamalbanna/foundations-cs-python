def displayMenu():
    choice = 0
    while(choice != 4):
        print("\n1. Count Digits\n2. Find Max\n3. Count Tags\n4. Exit")
        print("----------------------------")
        choice = int(input("Enter a choice: ")) 
        if(choice == 1):
            firstChoice()
        elif(choice == 2):
            secondChoice()
        elif(choice == 3):
            thirdChoice()

def firstChoice():
    num = int(input("please enter an integer "))
    print(getNumberOfDigits(num ,0))

def getNumberOfDigits(num , count):
    if(num > 0):
        return getNumberOfDigits(num//10 , count + 1)
    else:
        return count

def secondChoice():
    lst = changeFromStrinListToIntList(input("please enter the list in the following form '[num, num, num]' : "))
    print(findMax(lst, 0, 0))

def findMax(lst, count, max):
    if(count == len(lst)):
        return max
    else:
        curr = int(lst[count])
        if(curr > max):
            max = curr
        return findMax(lst, count + 1, max)

def changeFromStrinListToIntList(s):
    if(s == "[]"):
        return []
    else:
        s = s[1 : len(s) - 1]
        s = s.split(", ")
        s = [eval(i) for i in s]
        return s

def thirdChoice():
    tag = "<" + input("Please enter an html tag name(example: html, div, etc..): ") + ">"
    htmlCode = """<html>
                <head>
                <title>My Website</title>
                </head>
                <body>
                <h1>Welcome to my website!</h1>
                <p>Here you'll find information about me and my hobbies.</p>
                <h2>Hobbies</h2>
                <ul>
                <li>Playing guitar</li>
                <li>Reading books</li>
                <li>Traveling</li>
                <li>Writing cool h1 tags</li>
                </ul>
                </body>
                </html>"""
    print(getTagCount(htmlCode, tag, 0))

def getTagCount(htmlCode, tag, occurr):
    try:
        index = htmlCode.index(tag)
        return getTagCount(htmlCode[index + len(tag):], tag, occurr + 1)
    except:
        return occurr
   

displayMenu()

