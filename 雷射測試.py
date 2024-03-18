import bisect
from sys import stdin
mirX = dict();mirY = dict()#x座標為i的鏡子依y座標排序;y座標同理
mirXy = dict();mirYx = dict()#把mirX的y座標獨立出來，以做bisect;mirY同理
n = int(stdin.readline())
data = [[int(i) for i in stdin.readline().strip().split()] for _ in range(n)]
X = sorted(data,key=lambda x:[x[0],x[1]])#照X排序
Y = sorted(data,key=lambda x:[x[1],x[0]])#照Y排序
for x,y,t in X:
    if mirX.get(x)==None:
        mirX[x] = [[x,y,t]]
        mirXy[x] = [y]
    else:
        mirX[x].append([x,y,t])
        mirXy[x].append(y)
for x,y,t in Y:
    if mirY.get(y)==None:
        mirY[y] = [[x,y,t]]
        mirYx[y] = [x]
    else:
        mirY[y].append([x,y,t])
        mirYx[y].append(x)
ref = [[3,2,1,0],[1,0,3,2]]#左(0)上(1)右(2)下(3)
def refract(mirX,mirY,mirXy,mirYx):
    start = mirY[0][0]
    way = ref[start[2]][2]
    count = 1
    while True:
        x,y,t = start
        if way==0:#向左
            idx = bisect.bisect_left(mirYx[y],x)-1
            if idx==-1:
                break
            else:
                count += 1
                start = mirY[y][idx]
                way = ref[start[2]][way]
        elif way==1:#向上
            idx = bisect.bisect_right(mirXy[x],y)
            if idx==len(mirXy[x]):
                break
            else:
                count += 1
                start = mirX[x][idx]




                way = ref[start[2]][way]
        elif way==2:#向右
            idx = bisect.bisect_right(mirYx[y],x)
            if idx==len(mirYx[y]):
                break
            else:
                count += 1
                start = mirY[y][idx]
                way = ref[start[2]][way]
        else:#向下
            idx = bisect.bisect_left(mirXy[x],y)-1
            if idx==-1:
                break
            else:
                count += 1
                start = mirX[x][idx]
                way = ref[start[2]][way]
    return count
if mirY.get(0)==None:#有可能根本沒反射(x軸正向根本沒有鏡子)
    print(0)
else:
    print(refract(mirX,mirY,mirXy,mirYx))
