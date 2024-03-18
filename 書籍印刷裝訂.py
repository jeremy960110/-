from sys import stdin
n = int(stdin.readline().strip())
data = []
for _ in range(n):
    data.append([int(i) for i in stdin.readline().strip().split()])
data.sort(key=lambda x:-x[1])
time_a = 0 #印刷時間
ans = 0 #總共時間
for a,b in data:
    time_a+=a #沒有裝訂的時間
    ans = max(ans,time_a+b) #加上裝訂後的時間
print(ans)
