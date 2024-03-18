from sys import stdin
import heapq
n = int(input())
data = []
for _ in range(n):
    data.append([int(i) for i in stdin.readline().strip().split()])
data.sort(key=lambda x:-x[0])#反向是因為我要pop，這樣比較有效率
profit = []
heapq.heapify(profit)
while len(data)>0:
    task = data.pop()
    if task[0]==len(profit):
        if task[1]>profit[0]:
            heapq.heappushpop(profit,task[1])
        else:
            continue
    else:
        heapq.heappush(profit,task[1])
print(sum(profit))
