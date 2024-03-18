import bisect
n,k = map(int,input().split())
data = [int(i) for i in input().split()]
data.sort()
#從最大半徑(1000000000)到最小半徑(1)
#找起點用bisect_right，因為如果最右邊界剛好在某個服務點，必需找下一個
#如果用left會造成某個服務點有兩個伺服器
def put(data,k,r):
    end = data[0]+r#放第一次
    for _ in range(k-1):#接下來放置(k-1)次，上一行有放一次了
        idx = bisect.bisect_right(data,end)
        #用bisect_right是因為如果end剛好在服務點,則需要跳到下一個服務點。
        if idx>=len(data):
            return True
        end = data[idx]+r
    if end>=data[-1]:#都有覆蓋到
        return True
    else:
        return False
def binary_search(data,k):
    L =1
    R =1000000000
    while R>=L+1:
        M = (L+R)//2
        if put(data,k,M):
            R = M
        else:
            L = M+1
    if put(data,k,L):
        return L
    else:
        return R
        
ans = binary_search(data,k)
print(ans)
