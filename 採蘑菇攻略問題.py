data = [int(i) for i in input().split()][1:]
n = len(data)
M = [0]*n
for i in range(n):
    M[i] = max(M[i],M[i-1]+data[i])
print(max(M))