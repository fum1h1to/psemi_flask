# 整数が代入された変数 math と eng があります。

math = 90
eng = 50

# 次のように出力するコードを書いてみよう。
# math と eng の両方の値が 80 以上: "S",
# 上に当てはまらず、片方が 80 以上で片方が 60 以上: "A",
# 上の 2 つに当てはまらず、片方が 80 以上で片方が 60 未満、または両方が 60 以上: "B",
# 上の 3 つに当てはまらない: "C"

# （コードが書けたら、math と eng の値を変更して確かめよう）
if math >= 80 and eng >= 80:
  print("S")
elif (math >= 80 or eng >= 80) and math >= 60 and eng >= 60:
  print("A")
elif math >= 80 or eng >= 80:
  print("B")
else:
  print("C")