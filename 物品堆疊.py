n = int(input())
w = [int(i) for i in input().split()]
f = [int(i) for i in input().split()]
data = list(zip(w,f))
#data = [[w[i],f[i]] for i in range(n)]
data.sort(key=lambda x:x[0]/x[1])
ans = 0
up_w = data[0][0] #最上方的物品
for i in range(1,n): #從第二個開始，因為第一個上面沒東西
    ans += up_w*data[i][1] #每一層所需能量(承受重量x搬動次數)
    up_w+=data[i][0] #下一層需承受的重量
print(ans)
