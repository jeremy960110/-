n,k = map(int,input().split())
a = [int(i)for i in input().split()]
pre = 0
presum = [0]*n
for i in range(n):
    pre+=a[i]
    presum[i] = pre
sub = 0
subsum = [0]*n
for i in range(n-1,-1,-1):
    sub+=a[i]
    subsum[i] = sub
a = [0]+a+[0]
presum = [0]+presum+[0]#頭尾補零以方便計算
subsum = [0]+subsum+[0]#頭尾補零以方便計算
def bestpoint(a,L,R,presum,subsum):
    # presum已經做過一次前綴和了，力矩的部分要再做一次
    L_tor[L] = 0
    for idx in range(L+1,R):
        L_tor[idx] = L_tor[idx-1] + presum[idx-1]-presum[L-1]
    R_tor[R] = 0
    for idx in range(R-1,L,-1):
        R_tor[idx] = R_tor[idx+1] + subsum[idx+1]-subsum[R+1]
    I = float("inf")#確保比最小值大
    for i in range(L+1,R):
        margin[i] = abs(L_tor[i]-R_tor[i])
        if margin[i]<I:
            I = margin[i]
            idx = i
    return idx
def cut(a,k,L,R,presum,subsum):
    if R-L<2 or k==0:
        return 0
    else:
        point = bestpoint(a,L,R,presum,subsum)
        return a[point]+cut(a,k-1,L,point-1,presum,subsum)+cut(a,k-1,point+1,R,presum,subsum)  
L_tor = [0]*len(a)#之後都是用這三個list，可以用來節省空間
R_tor = [0]*len(a)#
margin = [0]*len(a)#
ans = cut(a,k,1,n,presum,subsum)
#原本應為(....0,n-1....)，但是頭有加一項([0])，所以要往後移
print(ans)
