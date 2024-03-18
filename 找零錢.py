from sys import stdin
C,N = map(int,stdin.readline().strip().split())
coins = [int(stdin.readline()) for _ in range(N)]
coins.sort()#先做排序
status = [float("inf")]*(C+1)#方便之後使用min時不會出錯
status[0] = 0
for i in range(N):
    coin = coins[i]#coin為當前幣值
    for j in range(1,C+1):
        if coin>j:
            pass
        else:
            status[j] = min(status[j],status[j-coin]+1)
print(status[C])