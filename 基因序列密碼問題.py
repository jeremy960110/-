a = list(input())
b = list(input())
def ANS(path,A,B,a,b):
    x,y = A,B
    ans = ""
    while x!=0 and y!=0:
        if path[x][y]==3:
            ans+=a[x-1]
            x-=1;y-=1
        elif path[x][y]==2:#向上
            x-=1
        else:#向左
            y-=1
    return ans[::-1] if len(ans)>0  else "E"#如果找到就輸出(要反向)，沒有則輸出"E"
def LCS(a,b):
    A = len(a)
    B = len(b)
    status = [[0]*(B+1) for _ in range(A+1)]
    path = [[0]*(B+1) for _ in range(A+1)]#由上->2;由左->1
    for i in range(1,A+1):
        for j in range(1,B+1):
            if a[i-1]==b[j-1]:
                status[i][j] = status[i-1][j-1]+1
                path[i][j] = 3
            else:
                if status[i][j-1]>status[i-1][j]:#左大於上
                    status[i][j] = status[i][j-1]
                    path[i][j] = 1
                else:#status[i][j-1]<=status[i-1][j]
                    status[i][j] = status[i-1][j]
                    path[i][j] = 2
    # for i in path:
    #     print(*i)
    return ANS(path,A,B,a,b)
ans = LCS(a,b)
print(ans)
