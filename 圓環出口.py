import bisect
n,m = map(int,input().split())
room = [int(i) for i in input().split()]
tasks = [int(i) for i in input().split()]
presum = [0]*n
pre = 0
for i in range(n):#做前綴和
    pre += room[i]
    presum[i] = pre
def run(presum,task,idx,start):
    target = task+start#任務+原本累積的點數=目標值
    if target>presum[-1]:#如果超出(要再跑一圈)
        target -= presum[-1]#需要減掉presum[-1](整個房間的點數)
    #此時的presum[0]<=target<=target
    idx = bisect.bisect_left(presum,target)
    return (idx+1)%n,presum[idx]#到下一個房間且調整，讓idx不會超出範圍
idx = 0
start = 0 #剛開始點數為0
for task in tasks:
    idx,start = run(presum,task,idx,start)
print(idx)
