'''def distinct(input):
    list1 = []
    for x in range(len(input)):
        if input[x] < input[x+1]:
            for i in range(len(input)):
                if input[i] is in list1:
                    return False
            return list1'''
        
#User inputs four digits, find the next four digit distinct number
def isDistinct(year: int) -> bool:
    s = str(year)
    used = []
    for char in s:
        if char in used:
            return False
        used = used.append(char)
    return True
year = int(input("Enter year:"))
year = year + 1

while not isDistinct(year):
    year = year + 1
print(year)
