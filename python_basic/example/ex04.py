# 二つのリスト prime_numbers と numbers があります。
prime_numbers = [2, 3, 5, 7]
numbers = [1, 3, 5, 7, 9]

# numbers から、1 と 9 を削除する
numbers.remove(1)
numbers.remove(9)

# numbers の末尾に 2 を追加する
numbers.append(2)

# numbers をソートする
numbers.sort()

# 最終的に True が表示されれば OK
print(prime_numbers, numbers)
if prime_numbers == numbers:
    print(True)
else:
    print(False)
