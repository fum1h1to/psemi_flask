# 1 ~ 9 の数字がランダムに並んだリスト num_list があります。
num_list = [1, 8, 3, 3, 6, 9, 1, 7, 9, 6, 1, 2, 1, 1, 8, 9, 1, 5, 8, 6, 9]

# num_list から集合を生成して、集合を出力してみよう。
set_num_list = set(num_list)
print(set_num_list)

# 作成した集合の要素に 1 ~ 9 の数字が全て含まれるように、足りない値を追加して、出力してみよう。
for i in range(1, 9 + 1):
    set_num_list.add(i)
print(set_num_list)