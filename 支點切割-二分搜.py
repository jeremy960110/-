n,k = map(int,input().split())
data = [int(i) for i in input().split()]
def Tor(L,R,M,data):# 回傳以M當支點的合力矩值
    L_Tor = 0
    R_Tor = 0
    for i in range(L,M):
        L_Tor += data[i]*(M-i)
    for i in range(M+1,R+1):
        R_Tor += data[i]*(i-M)
    return L_Tor-R_Tor
def binary_search(data,L,R):
    left = L+1#排除左邊界
    right = R-1#排除右邊界
    while right>left+1:
        M = (left+right)//2
        result = Tor(L,R,M,data)
        if result == 0:
            return M
        elif result>0:
            right = M
        else:
            left = M
    if abs(Tor(L,R,left,data))>abs(Tor(L,R,right,data)):
        return right
    else:
        return left
def cut(L,R,data,k):
    if R-L<2 or k == 0: #長度小於3或達到切割次數上限
        return 0
    else:
        idx = binary_search(data,L,R)
        return cut(L,idx-1,data,k-1)+cut(idx+1,R,data,k-1)+data[idx]
ans = cut(0,n-1,data,k)
print(ans)
