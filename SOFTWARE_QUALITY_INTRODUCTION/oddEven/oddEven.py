numbers = [13, 44, 23, 1, 0, 45, 66, 63, 78, 79]

def oddEven(numbers):

    i = 0
    totalEven = 0
    totalOdd = 0

    while i < len(numbers):

        if(numbers[i] % 2 == 0):
            totalEven = totalEven + 1
        else:
            totalOdd = totalOdd + 1


        i = i + 1

        print("Total even:" + str(totalEven))
        print("Total odd:" + str(totalOdd))
        
oddEven(numbers)