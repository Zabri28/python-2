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
answer = ""
for flow in stream:
    answer += str(round(flow)) + " "
print(answer)
"""
n = int(input())
streams = []
for i in range(n):
    streams.append(int(input()))
done = False
while not done:
    command = int(input())
    if command == 77:
        done = True
    elif command == 99:
        stream_num = int(input()) - 1
        percentage = int(input())
        left_flow = streams[stream_num] * percentage/100
        right_flow = streams[stream_num] - left_flow
        streams = streams[:stream_num] + [left_flow, right_flow] + streams[stream_num + 1:]
    elif command == 88:
        stream_num = int(input()) - 1
        left_flow = streams[stream_num]
        right_flow = stream[stream_num + 1]
        streams = streams[:stream_num] + [left_flow + right_flow] + streams[stream_num +2:]
    answer = ""
    for flow in streams:
        answer += + str(flow) + ""
    print(answer)
    """

