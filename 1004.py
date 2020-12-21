def CheckInACircle(circle, target):
    x1 = circle[0]
    y1 = circle[1]
    r1 = circle[2]

    x2 = target[0]
    y2 = target[1]

    length = ((x2-x1)**2 + (y2-y1)**2)**0.5

    if length > r1:
        # print("out")
        return 0
    elif length < r1:
        # print("in")
        return 1

def CheckCross(circle, target1, target2):
    cnt = 0 
    cnt += CheckInACircle(circle, target1)
    cnt += CheckInACircle(circle, target2)

    if cnt == 1: 
        return 1
    else:
        return 0

case = int(input())

for i in range(case):
    count_of_cross = 0

    input_list = list(map(int, input().split()))
    start = [input_list[0],input_list[1]]
    dest = [input_list[2],input_list[3]]

    num_of_planet = int(input())

    for i in range(num_of_planet):
        planet = list(map(int, input().split()))
        count_of_cross += CheckCross(planet, start, dest)

    print(count_of_cross)