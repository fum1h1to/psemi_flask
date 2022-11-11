N = 100
result = []

for i in range(N, 0, -1):
    if i % 3 == 0 or i % 5 == 0:
        if i % 15 != 0:
            if i % 2 != 0:
                result.append(i)

print(result)