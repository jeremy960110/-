from sys import stdin
def Maxdepth(data,n):
    #如果在一條路徑上按正常速度來跑，就只能拿到原始分數，
  #如果他加速跑，就能拿到兩倍分數，不過她就會需要在加速跑完後的下一條路徑上休   息而速度變慢得到0分
    #如果這次要兩倍，上次必須0或者1
    #如果這次是一倍，上次必須1或者0
    #如果這次是零倍，上次必須2或者1
    status = [[0,0,0] for _ in range(n)]
    status[0] = [0,data[0],data[0]*2]
    for i in range(1,n):
        status[i][0] = max(status[i-1][1],status[i-1][2])
        status[i][1] = max(status[i-1][0],status[i-1][1])+data[i]
        status[i][2] = max(status[i-1][0],status[i-1][1])+data[i]*2
    return max(status[-1])
while True:
    n = int(input())
    if n==0:break
    data = [int(i) for i in stdin.readline().strip().split()]
    ans = Maxdepth(data,n)
    print(ans)