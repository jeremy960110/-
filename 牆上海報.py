n,m = map(int,input().split())
w = [int(i) for i in input().split()]
p = [int(i) for i in input().split()]
p.reverse()
def past(w,h,p):
    p2 = p.copy() #p的副本
    idx = 0 #牆的index
    length = 0 #目前牆累計的最長寬度
    while len(p2)>0 and idx<len(w):
        if w[idx]>=h: #高度比海報高，有機會可以貼。
            length +=1
            if length==p2[-1]: #累計長度是否足夠這次海報的長度需求
                p2.pop()
                length = 0
        else: #途中遇到某個牆高度不合的情況
            length = 0
        idx +=1
    if len(p2)>0: #還有海報沒貼上
        return False
    else:
        return True
def binary_search(w,p):
    L = 1
    R = 1000000000
    while L+1<R:
        M = (L+R)//2
        if past(w,M,p):#can past
            L = M
        else:
            R = M
    if past(w,R,p):# can past on L+1
        return R
    else:
        return L
ans = binary_search(w,p)
print(ans)
