from sys import stdin
def cross(data):
    a = data[0]
    b = data[1]
    y = data[-2]
    z = data[-1]
    solu1 = z+a+y+a
    solu2 = b+a+z+b
    data.pop(-1)
    data.pop(-1)
    return min(solu1,solu2)#回傳兩種可能中最小的
for i in stdin:
    n = int(i.strip())
    data = [int(i) for i in stdin.readline().strip().split()]
    data.sort()
    #如果有4人以上,每個round把最慢兩個送過去
    #1. az過,a回來接y過去,a再回來。共耗z+a+y+a
    #2. ab過,a回來,yz過,b回來。共耗b+a+z+b
    ans = 0
    while len(data)>=4:
        ans += cross(data)
    if len(data)==3:
        ans += sum(data)
    elif len(data)==2:
        ans += data[1]
    else:
        ans += data[0]
    print(ans)
