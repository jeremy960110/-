import bisect
m,n = map(int,input().split())
data = [int(i) for i in input().split()]
window = []
win0 = []
def add(window,win0,NO):
    idx = bisect.bisect_left(win0,NO)
    #如果是新的，有可能在win0之間或最後面
    if idx==len(win0):
        window.append([NO,1])
        win0.append(NO)
    elif win0[idx]==NO:
        window[idx][1]+=1
    else:#沒出現過
        window.insert(idx,[NO,1])
        win0.insert(idx,NO)
def remove(window,win0,NO):
    idx = bisect.bisect_left(win0,NO)
    if window[idx][1]>1:
        window[idx][1]-=1
    else:#如果等於1，拿掉後一定會變0
        window.pop(idx)
        win0.pop(idx)

ans=0
window=[[data[0],1]]
win0=[data[0]]

for i in range(1,m):
    add(window,win0,data[i])
if len(window)==m:
    ans+=1

for i in range(m,n):
    add(window,win0,data[i])    
    remove(window,win0,data[i-m])
    if len(window)==m:
        ans+=1       
print(ans)
