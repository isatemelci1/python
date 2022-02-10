count=0
userInpList=[]
while count < 5:
  number= int(input('Please enter the number: '))
  userInpList.append(number)
  count = count +1

def findLargestNumber(inpList):
    maxNumber = inpList[0]
    for i in inpList:
        if i > maxNumber:
            maxNumber = i
    return maxNumber

print("The largest number is : " + str(findLargestNumber(userInpList)))