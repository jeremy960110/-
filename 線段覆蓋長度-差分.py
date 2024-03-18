#差分法，70%會過，會超時
from sys import stdin
n = int(input())
data = []
Map = [0]*100002
for _ in range(n):
    a,b = [int(i) for i in stdin.readline().strip().split()]
    Map[a+1]+=1
    Map[b+1]-=1
count = 0
have = [0]*100002
for i in range(1,100002):
    have[i] +=  Map[i]+have[i-1]
    if have[i]>0:
        count += 1
print(count)

