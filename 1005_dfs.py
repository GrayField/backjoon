node_list = []
# node = {'time':0, 'dep':[1,2,3]}
# node_list.append({'time':0, 'dep':[]})
# node_list.append({'time':0, 'dep':[]})

# print(node_list)

def GetTime(idx):
    # print("index :", idx)
    # print(node_list[idx])

    time = node_list[idx]['time']
    dep = node_list[idx]['dep']
    prev_time = 0
    if len(dep) != 0:
        for i in range(len(dep)):
            temp_time = GetTime(dep[i]-1)
            if temp_time > prev_time:
                prev_time = temp_time


    return time + prev_time

case = int(input())

for i in range(case):
    node_list = []
    num_of_node, num_of_rule = map(int, input().split())

    for i in range(num_of_node):
        node_list.append({'time':0, 'dep':[]})

    
    input_list = list(map(int, input().split()))

    for i in range(num_of_node):
        node_list[i]['time'] = input_list[i]

    
    for i in range(num_of_rule):
        req, idx = list(map(int, input().split()))
        node_list[idx-1]['dep'].append(req)

    goal = int(input())

    print(GetTime(goal-1))
