from sys import stdin
import bisect
def LCS(data,n):
    mindata = [data[0]]
    lcslen = [0]*n
    lcslen[0] = 1
    for i in range(1,n):
        idx = bisect.bisect_left(mindata,data[i])
        if idx==len(mindata):
            mindata.append(data[i])
            lcslen[i] = len(mindata)
        else:
            mindata[idx] = data[i]
            lcslen[i] = idx+1
    return lcslen
data = [int(i) for i in stdin]
LCSlen = LCS(data,len(data))
s = max(LCSlen)
print(s)
ans = []
for i in range(len(data)-1,-1,-1):
    if LCSlen[i]==s:# 找到第一個
        ans.append(data[i])
        s-=1
print("-")
for i in ans[::-1]:# 反轉再輸出
    print(i)