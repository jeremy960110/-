#用merge法，AC
from sys import stdin
n = int(input())
data = []
for _ in range(n):
    data.append([int(i) for i in stdin.readline().strip().split()])
data.sort()#按照頭做排序
def merge(list1,list2):
    #如果list1跟list2有交集，則list1加list2繼續執行下一次merge()
    #如果list1跟list2完全沒有交集，改由list2作為主線段與下一個線段merge()
    if list1[1]>=list2[0]: 
        if list2[1]>list1[1]:
            list1[1]=list2[1]#list1 = list1+list2
        return True
    else:
        return False
ans = 0
p = [0,0]
for line in data:
    if merge(p,line):
        pass#繼續合併
    else:
        ans += p[1]-p[0]#無法合併
        p = line
ans += p[1]-p[0]
print(ans)