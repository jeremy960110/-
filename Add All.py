from sys import stdin
import bisect

for i in stdin:
    N=int(i.strip())
    if N==0:#如果輸入為0，就結束
        break

    data=list(map(int,stdin.readline().split()))
    data.sort()#先排序，以便之後好找出最小值
    idx=0
    ans=0
    while (idx<len(data)-1):#這裡把data當成queue，這樣就不用一直pop。
        s=data[idx]+data[idx+1]
        ans+=s
        bisect.insort(data,s)
        idx+=2
    print(ans)
