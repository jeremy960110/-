from sys import stdin
import bisect
n,L = map(int,input().split())
data = []
for _ in range(n):
    data.append([int(i) for i in stdin.readline().strip().split()])
data.sort(key=lambda x:x[1])#要照著切割順序去做排序
data = [i[0] for i in data]#切割順序
#print(data)
p = [0,L]#用於記錄木棍的狀態
def cut(p,x):
    idx = bisect.bisect_left(p,x)#找出正確的切割位置
    p.insert(idx,x)
    cost = p[idx+1]-p[idx-1]
    return cost
ans = 0
for x in data:
    ans += cut(p,x)
print(ans)
