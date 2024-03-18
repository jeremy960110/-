from sys import stdin
n,m = map(int,stdin.readline().strip().split())
data = []
for i in range(n):
    data.append([int(i) for i in stdin.readline().strip().split()])

def walk(data,n,m):
    M=[[0]*m for _ in range(n)]
    for j in range(1,m):#上邊界
        M[0][j] = M[0][j-1]+data[0][j]
    for i in range(1,n):#左邊界
        M[i][0] = M[i-1][0]+data[i][0]
    for i in range(1,n):#其他地方
        for j in range(1,m):
            M[i][j] = min(M[i-1][j],M[i][j-1])+data[i][j]
    return M[-1][-1]#回傳最小消耗
ans = walk(data,n,m)
print(ans)
