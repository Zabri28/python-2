def splitStream(x, y): 
    value = y.pop(x - 1)
    percentsplit = int(input("enter percentage of left stream:"))
    value1 = percentsplit/100 * value
    value2 = (100 - percentsplit)/100 * value
    y.insert(x - 1, value1)
    y.insert(x ,value2)

def joinStream(x, y):
    value1 = y.pop(x - 1)
    value2 = y.pop(x - 1)
    finalval = value1 + value2
    y.insert(x - 1, finalval)
    
m = int(input("enter amount of streams:")) 
stream = []
for i in range(m):
    waterflow = int(input("enter amount of water in stream:"))
    stream.append(waterflow)
print(stream)
while True:
    command = int(input("enter command number:"))
    if command == 77:
        break
    streamnumber = int(input("enter what number the stream is:"))
    if command == 99:
        result = splitStream(streamnumber,stream)
    if command == 88:
        result = joinStream(streamnumber, stream)
print(stream)
