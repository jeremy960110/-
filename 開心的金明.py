from sys import stdin
n,m = map(int,input().split())
data = [[int(i) for i in stdin.readline().strip().split()] for _ in range(m)]

#二維DP
status = [[float("-inf")]*(n+1) for _ in range(m+1)]
for i in range(n+1):status[0][i] = 0 # 之後要以他們為基礎加數字，不能是負無限
for i in range(1,m+1):#迭代m項物品
    p,imp = data[i-1]
    for j in range(0,n+1):
        if p>j:
            status[i][j] = status[i-1][j]
        else:
            status[i][j] = max(status[i-1][j], status[i-1][j-p]+p*imp)
print(max(status[-1]))


#一維DP
status = [float("-inf")]*(n+1)# 把每個地方都先設為負無限，才可以用max一次解決
status[0] = 0
for i in range(m):
    p,imp = data[i] 
    for j in range(n,0,-1):
        if p>j:
            pass
        else:
            status[j] = max(status[j],status[j-p]+p*imp)
print(max(status))
