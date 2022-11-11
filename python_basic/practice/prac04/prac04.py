list_0 = [0, 0, 0, 1, 0, 0, 0, 0]
N = 2 * len(list_0) - 1

data = [[] for i in range(N)]
data[0] = list_0

for i in range(N-1):
    for j in range(len(data[i])):
        jm1 = 0
        jp1 = 0
        if j - 1 >= 0:
            jm1 = data[i][j - 1]
        if j + 1 < len(data[i]):
            jp1 = data[i][j + 1]
        
        if jm1 == 1 or jp1 == 1:
            data[i + 1].append(1)
        else:
            data[i + 1].append(0)

for d1 in data:
    result = ''
    for d2 in d1:
        if d2 == 0:
            result += ' '
        else:
            result += '*'
    print(result)

