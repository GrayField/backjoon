zero=[1, 0, 1]
one =[0, 1, 1]

def fibonacci(n):
    size = len(zero)
    if n >= size:
        for i in range(size, n+1):
            zero.append(zero[i-1]+zero[i-2])
            one.append(one[i-1]+one[i-2])
    print("%d %d"%(zero[n],one[n]))

case = int(input())
for i in range(case):
    num = int(input())
    fibonacci(num)

# N F 0 1
# 0 0 1 0
# 1 1 0 1
# 2 1 1 1
# 3 2 1 2
# 4 3 2 3
# 5 5 3 5
# 6 8 5 8
# 7 13 8 13
# 8 21 13 21
# 9 34 21 34
# 1은 n번째 피보나치랑 같음
# 0은 n-1번째 피보나치랑 같음