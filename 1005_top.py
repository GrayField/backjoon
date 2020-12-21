node_list = []
queue = []

def GetTime(idx):
    for i in range(len(node_list)):
        if len(node_list[i]['prev'])==0:
            queue.append(i)
    
    while True:
        if len(node_list[idx]['prev']) == 0:
            return node_list[idx]['t_time']
        p_idx = queue.pop(0)
        next = node_list[p_idx]['next']
        for i in next:
            if node_list[p_idx]['t_time'] + node_list[i]['time'] > node_list[i]['t_time']:
                node_list[i]['t_time'] = node_list[p_idx]['t_time'] + node_list[i]['time']
            node_list[i]['prev'].remove(p_idx)
            if len(node_list[i]['prev'])==0:
                queue.append(i)

case = int(input())

for i in range(case):
    node_list = []
    queue = []
    num_of_node, num_of_rule = map(int, input().split())

    for i in range(num_of_node):
        node_list.append({'time':0, 't_time':0, 'prev':[], 'next':[]})
    
    input_list = list(map(int, input().split()))

    for i in range(num_of_node):
        node_list[i]['time'] = input_list[i]
        node_list[i]['t_time'] = input_list[i]
    
    for i in range(num_of_rule):
        req, idx = list(map(int, input().split()))
        node_list[idx-1]['prev'].append(req-1)
        node_list[req-1]['next'].append(idx-1)

    goal = int(input())

    print(GetTime(goal-1))

