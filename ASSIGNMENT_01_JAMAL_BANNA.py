#Quest 1:
def factRecur(num):
    if(num == 1):
        return 1
    else:    
        return num * factRecur(num - 1)


def fact(num):
    sum = 1
    while(num > 1):
        sum *= num
        num -= 1
    return sum

def testCasesFactorial():
    assert fact(4) == 24
    assert fact(6) == 720
    assert fact(1) == 1
    assert factRecur(4) == 24
    assert factRecur(6) == 720
    assert factRecur(1) == 1
    
testCasesFactorial()

#Quest 2:
def divisors(num):
    divisors = []
    for i in range(1,num + 1):
        if(num % i == 0):
            divisors.append(i)
    return divisors

def testCasesDivisors():
    assert divisors(10) == [1,2,5,10]
    assert divisors(16) == [1,2,4,8,16]
    assert divisors(1) == [1]
    assert divisors(0) == []

testCasesDivisors()

#Quest 3:
def reverseString(s):
    counter = len(s)
    reverseString = ""
    while(counter > 0):
        counter -= 1
        reverseString += s[counter]
    return reverseString

def testCasesReverseString():
    assert reverseString("Hello World") == "dlroW olleH"
    assert reverseString("oneword") == "droweno"

testCasesReverseString()

#Quest 4:
def evenNumbers(original):
    even = []
    for num in original:
        if(num % 2 == 0):
            even.append(num)
    return even

def testCasesEvenNumber():
    assert evenNumbers([1,2,3,4,5,6]) == [2,4,6]
    assert evenNumbers([5, 3, 18, 4, 2, 7, 10]) == [18, 4, 2, 10] 
    assert evenNumbers([5, 3, 11, 5, 1, 7, 27]) == []

testCasesEvenNumber()

#Quest 5:
def strongPassword(password):
    length = len(password) > 7
    upperCaseLetter = False
    lowerCaseLetter = False
    digit = False
    specialCharacter = False
    for char in password:
        if char == " ":
            return "password can't contain spaces"
        elif( not( char.isalpha() ) and not( char.isdigit() ) ):
            specialCharacter = True
        elif(char.isdigit()):
            digit = True
        elif(char.isupper()):
            upperCaseLetter = True
        else: 
            lowerCaseLetter = True
        
        if(length and upperCaseLetter and lowerCaseLetter and digit and specialCharacter):
            return "Strong password"
            
    return "Weak password"       

def testCasesStrongPassword():
    assert strongPassword("Hello5?world") == "Strong password"
    assert strongPassword("password") == "Weak password"
    assert strongPassword("Password123") == "Weak password"

testCasesStrongPassword()

#Quest 6:
def ipIsValid(ip):

    if (len(ip) > 15):
        return "too long for an ipv4 address" 
    
    countDot = 0
    octet = ""
    lastCharDot = False
    octetCount = 1
    for char in ip:

        if(char == "-"):
                return "negative octet"
        
        if(char == "."):

            if lastCharDot: 
                return "consecutive periods"
            
            octet = ""
            countDot += 1
            lastCharDot = True
            octetCount += 1

        elif ((octet == "0") and (char != "0")) or (octet == "00") and (char != "0"):
            return "leading zero is octet"
        
        elif char.isalpha():
            return "octect can contain alphabets"
        
        else:
            octet += char
            lastCharDot = False
            if(int(octet) > 255):
                return "octet value too large"
            
            
        if(countDot > 3):
            return "extra period"
        
    if countDot < 3 :
        return "missing periods"
    
    return "valid"
        

def testCasesIPAddressValidation():
    assert ipIsValid("192.168.1.1") ==  "valid"
    assert ipIsValid("172.16.0.0") ==  "valid"
    assert ipIsValid("10.0.0.1") == "valid"
    assert ipIsValid("255.255.255.0") == "valid"
    assert ipIsValid("156.168.1.1") ==   "valid"
    assert ipIsValid("192.168.1") == "missing periods"
    assert ipIsValid("10.0.0.01") == "leading zero is octet"
    assert ipIsValid("192.168.1.1.1") == "extra period"
    assert ipIsValid("192.168..1") == "consecutive periods"
    assert ipIsValid("192.168.1.-1") == "negative octet"
    
    

testCasesIPAddressValidation()
    




