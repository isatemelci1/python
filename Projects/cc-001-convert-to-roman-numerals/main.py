def intToRoman(num):
    romanNum = ''
    mapping = {1000:'M', 900:'CM', 500:'D', 400:'CD', 100:'C', 90:'XC', 50:'L', 40:'XL', 10:'X', 9:'IX', 5:'V', 4:'IV', 1:'I'}
 
    while num != 0:
        for k, v in mapping.items():
            if num >= k:
                dividend = int(num/k)
                num %= k
                romanNum += dividend*v
    return romanNum

messageToUser = """###  This program converts decimal numbers to Roman Numerals ###
(To exit the program, please type "exit")
Please enter a number between 1 and 3999, inclusively : """

userInp = input(messageToUser)

numberToConvert = int(userInp)

if numberToConvert>0:
    print(intToRoman(numberToConvert))