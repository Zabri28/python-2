#Voronoi Villages problem
'''def villages(n):
    villagenumb = []
    for i in range(n):
        villagenumb.append(int(input("What is the position of the village: ")))
    villagenumb.sort()
    
    for i in range(n):'''

def calNeigh(index: int, positions) -> float:
    left = (positions[index] - positions[index-1])/2
    right = (positions[index +1] - positions[index])/2
    return left + right

def villages(n):
    n = int(input(""))
    positions = []
    for i in range(n):
        loc = int(input(""))
        positions.append(loc)
    positions.sort()
    sizes = []
    for i in range(1, n-1):
        size = calNeigh(i, positions)
        sizes.append(size)
    sizes.sort()