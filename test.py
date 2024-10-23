n = int(input())  # 讀取需要倒入飲料的次數
w1, w2, h1, h2 = map(int, input().split())  # 讀取第一部分和第二部分容器的寬度和高度
v = [int(x) for x in input().split()]  # 讀取每次倒入的飲料體積

nowv1 = 0  # 第一部分容器當前的體積
nowv2 = 0  # 第二部分容器當前的體積
res = []   # 存儲每次倒入後水位上升的高度
ind = 0    # 記錄第一部分容器倒入結束的索引

# 先處理第一部分容器的倒入過程
for i in range(n):
    if nowv1 < w1**2 * h1:
        pour_volume = v[i]  # 本次倒入的體積
        available_volume1 = w1**2 * h1 - nowv1  # 計算第一部分容器剩餘容量
        delta_h = 0  # 本次倒入導致的水位上升量

        # 如果本次倒入體積小於等於第一部分容器剩餘容量
        if pour_volume <= available_volume1:
            nowv1 += pour_volume  # 更新第一部分容器當前的體積
            delta_h = pour_volume / (w1**2)  # 計算水位上升
            res.append(delta_h)  # 將水位上升量添加到結果列表
        else:
            # 如果倒入體積超過了第一部分容器的剩餘容量，計算溢出部分
            overflow = pour_volume - available_volume1  # 計算溢出量
            nowv1 = w1**2 * h1  # 將第一部分容器填滿
            delta_h += available_volume1 / (w1**2)  # 計算第一部分容器的水位上升

            # 將溢出部分倒入第二部分容器
            available_volume2 = w2**2 * h2 - nowv2  # 計算第二部分容器剩餘容量
            if overflow <= available_volume2:
                nowv2 += overflow  # 更新第二部分容器的體積
                delta_h += overflow / (w2**2)  # 計算第二部分容器的水位上升
            else:
                delta_h += available_volume2 / (w2**2)  # 第二部分容器剩餘容量的水位上升
                nowv2 = w2**2 * h2  # 第二部分容器已滿
            res.append(delta_h)  # 添加本次總的水位上升量
            ind = i + 1  # 記錄下次倒入的位置
            break  # 停止第一部分容器的倒入
    else:
        ind = i  # 第一部分容器已滿，記錄當前索引
        break

# 接著處理第二部分容器的倒入過程
for j in range(ind, n):
    if nowv2 >= w2**2 * h2:
        # 如果第二部分容器已滿，水位不上升
        res.append(0)
        continue

    pour_volume = v[j]  # 本次倒入的體積
    available_volume2 = w2**2 * h2 - nowv2  # 計算第二部分容器剩餘容量
    delta_h = 0  # 本次倒入導致的水位上升量

    if pour_volume <= available_volume2:
        nowv2 += pour_volume  # 更新第二部分容器的體積
        delta_h = pour_volume / (w2**2)  # 計算水位上升
    else:
        delta_h += available_volume2 / (w2**2)  # 倒入剩餘的空間
        nowv2 = w2**2 * h2  # 第二部分容器已滿
    res.append(delta_h)  # 添加水位上升量

# 找出水位上升的最大值，並取整輸出
print(int(max(res)))
