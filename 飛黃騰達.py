from sys import stdin
import bisect
def LCS(data,n):
    # To find NLDS
    # 2 3 3 5 (if data[i] is 2) -> 2 2 3 5(by bisect_right)
    mindata = [data[0]]
    LCSlen = [0]*n
    LCSlen[0] = 1
    for i in range(1,n):
        idx = bisect.bisect_right(mindata,data[i])
        if idx==len(mindata):
            mindata.append(data[i])
            LCSlen[i] = len(mindata)
        else:
            mindata[idx] = data[i]
            LCSlen[i] = idx+1
    return max(LCSlen)
n = int(input())
data = []
for _ in range(n):
    data.append([int(i) for i in stdin.readline().strip().split()])
data.sort()
data = [i[1] for i in data]
ans = LCS(data,n)
print(ans)