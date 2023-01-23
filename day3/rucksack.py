'''
a through z is 1 through 26
A through Z is 27 through 52

'''

def findCommonElement(list1, list2):
    return [element for element in list1 if element in list2][0]

def main():
    items = []
    itemsSum = 0 # sum in ascii
    with open('/home/abdu/git/advent2022/day3/input.txt') as inputFile:
        for line in inputFile:
            length = len(line)
            compartment1 = line[:int(length/2)]
            compartment2 = line[int(length/2):]
            item = findCommonElement(compartment1, compartment2)
            itemAsciiValue = ord(item)
            if (itemAsciiValue > 96): # lower case
                itemsSum += (itemAsciiValue - 96)
            else: # upper case
                itemsSum += (itemAsciiValue - 38)
            
            # note: these magic numbers represent the ascii value needed to subtract to "normalize" their value to 1 through 26 for lowercase and 27 to 52 for uppercase
             
            items.append(item)
        
    print(items)
    print(itemsSum)

if __name__=="__main__":
    main()