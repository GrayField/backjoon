case = int(input())
position_set = []

def calc(position):
    x1 = int(position[0])
    y1 = int(position[1])
    r1 = int(position[2])
    
    x2 = int(position[3])
    y2 = int(position[4])
    r2 = int(position[5])

    distance = ((x1-x2)**2 + (y1-y2)**2)**0.5

    if distance == 0:
        if r1==r2:
            return -1
        elif r1 != r2:
            return 0
    else:
        if distance == r1+r2 or distance==abs(r1-r2):
            return 1
        elif abs(r1-r2) < distance and distance < r1+r2:
            return 2
        else:
            return 0


for i in range(case):
    position_set.append(input().split())
    print(calc(position_set[i]))
    

# (x1, y1) == (x2, y2)
#  - 
#  - r1 == r2
#  - r1 != r2

# (x1, y1) != (x2, y2)
#  - distance > r1+r2
#  - distance = r1+r2
#  - distance < r1+r2