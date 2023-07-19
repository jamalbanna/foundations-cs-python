def menu():
    choice = 0
    while (choice > 3) or (choice < 1) and (choice != 4): 
        print("--------------")
        print("1. Sum Tuples\n2. Export JSON\n3. Import JSON\n4. Exit")
        print("---------------")
        choice = int(input(" enter a choice "))
        if choice == 1:
            firstChoice()
        elif  choice == 2:
            secondChoice()
        elif choice == 3:
            thirdChoice()

def firstChoice():
    input1 = input("enter the first tuple ")
    tuple1 = tuple(input1[1:-1].split(",")) # trasnform user input from string to tuple
    input2 = input("enter the second tuple ")
    tuple2 = tuple(input2[1:-1].split(",")) # trasnform user input from string to tuple
    newTuple = sumTuples(tuple1, tuple2)
    print(newTuple)


#precondition: tuples are of equal size and it should contains numbers only(doesn't matter if in number or string format)
#postcondition: a new tuple that containts the addition of elements of same indexes from the input tuples
def sumTuples(tup1, tup2):
    tup3 = ()
    for i in range(len(tup1)):
        tup3 += (int(tup1[i]) + int(tup2[i]),) #tuples are immutable but we can add a tuple to another tuple
    return tup3

def secondChoice():
    fileName = input("input file name (example.txt): ")
    dictionary = input("input a dictionary: ")
    exportToJSONFile(dictionary,fileName)

#precondition: dictionary is in correct form and fileName is string with correct file extension
#postcondition: if file already exists overwrites existing data with new dictionary in json format else creates new file and writes dictionary 
def exportToJSONFile(dictionary, fileName):
    file = open(fileName, "w") #opens the file in write mode, if file doesn't exist creates new one
    file.write(dictionary) #overwrites existing data if there is any
    file.close()

def thirdChoice():
    fileName = input("input file name (example.txt): ")
    importFromJSONFile(fileName)

#precondition: file exists and is in json format
#postcondition: list of dictionaries that contain objects read from the file
def importFromJSONFile(fileName):
    dictionaryList = []
    file = open(fileName, "r")
    content = file.read() #read file as string
    file.close()
    contentToList = content[1:-1].split('},') #seperate objects 
    cleaned_list = []
    for string in contentToList:
        newString = string.replace(" ","").replace("\n","").replace('"',"") #remove spaces, new lines and extra quotations from objects that were read as strings 
        cleaned_list.append(newString[1:-1])# to remove the "}" from last element because when we split using "}," we will have an extra "}" at the end
    for obj in cleaned_list: #iterate over objects read as string
        obj_dict = {}
        for item in obj.split(","): #change each object into list of strings that containt key value pairs
            key,value = item.split(":") #read key value pairs
            obj_dict[key] = value #append the key value pair to a dictionary
        dictionaryList.append(obj_dict)
    return dictionaryList

  
menu()

# Exercise:
# a. N^3
# b. N^3
# c. N!
# d. NlogN
# e. N
# f. N^2
# g. N^2 https://stackoverflow.com/questions/13710629/on2-vs-o-nlogn2
# h. N! 