# 周期表の元素番号がキー、元素記号が値の辞書 periodic_table があります。
periodic_table = {1: "H", 2: "He", 3: "Li", 4: "Be", 5: "Bo", 6: "C", 7: "N", 8: "O", 9: "F"}

# この辞書の中に元素番号と元素記号が一致しないものが一つあるので、正しくなるように変更してみよう。
# (分からない人は "周期表"を検索)
periodic_table[5] = 'B'
print(periodic_table)

# 元素番号 10 の元素を辞書に追加してみよう。
periodic_table[10] = 'Ne'
print(periodic_table)
