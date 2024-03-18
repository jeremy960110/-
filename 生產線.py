from sys import stdin
n,m = map(int,input().split())
data = []
for _ in range(m):
    s = [int(i) for i in stdin.readline().strip().split()]
    data.append(s)
machine = [int(i) for i in stdin.readline().strip().split()]#機器的生產時間
length = len(machine)
line = [0]*(length+2)
for L,R,W in data:
    line[L]+=W
    line[R+1]-=W
for i in range(1,len(line)):
    line[i]+=line[i-1]          
line.sort(reverse=True)#反向排序
machine.sort()#正向排序
idx = 0
ans = 0
while line[idx]!=0:#代表工作都做完了
    ans += machine[idx]*line[idx]
    idx+=1
print(ans)
