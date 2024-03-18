n = int(input())
data = [int(i) for i in input().split()]
pre = 0
presum = [0]*n
for i in range(n):
    pre+=data[i]
    presum[i] = pre
data.insert(0,0)
presum.insert(0,0)
Vsort = [i for i in enumerate(data)]
Vsort.sort(key=lambda x:-x[1])
def findmin(Vsort,L,R):
    while True:
        x = Vsort.pop()
        if L<=x[0]<=R:
            return x[0]

def lucky_number(data,L,R):
    while R>L:#不能用R>L+1，這樣會少比較一次
        idx = findmin(Vsort,L,R)
        L_sum = presum[idx-1]-presum[L-1]
        R_sum = presum[R]-presum[idx]
        if L_sum>R_sum:
            R = idx-1
        else:
            L = idx+1
    return data[R]
ans = lucky_number(data,1,n)
print(ans)