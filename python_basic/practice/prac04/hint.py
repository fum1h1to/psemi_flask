# 34 行目から処理を追うと分かりやすいです。

# 引数のリストをもとに、次のリストを生成して返す関数
def generate_next_list(prev_list):
    next_list = []
    for i in range(len(prev_list)):
        if i == 0:  # 先頭（左端）の要素の場合
            # prev_listの j + 1 の要素が 1 なら 1 を、0 なら 0 を next_list に追加する
            # 下の pass を消して、ここを書く
            pass
        elif i == len(prev_list) - 1:  # 末尾（右端）の要素の場合
            # prev_listの j - 1 の要素が 1 なら 1 を、0 なら 0 を next_list に追加する
            # 下の pass を消して、ここを書く
            pass
        else:
            # prev_listの j - 1 の要素と j + 1 の要素が同じなら 0 を、違うなら 1 を next_list に追加する
            # 下の pass を消して、ここを書く
            pass

    return next_list


# 引数のリスト li の各要素が 1 ならアスタリスク "*" を、0 なら半角スペース " " を出力する関数
def print_list(li):
    string = ""
    for i in range(len(li)):
        # li[i] の要素が 1 なら "*" を、0 なら " " を文字列 string に結合する
        # 下の pass を消して、ここを書く
        pass

    print(string)


# 初期値 list_0
list_0 = [0, 0, 0, 1, 0, 0, 0, 0]

# これから生成するリストを保持するリスト
lists = []

# lists に要素 list_0 を追加する
lists.append(list_0)

# lists の要素をもとに次のリストを作成し、lists に追加する
for i in range(1, len(list_0) * 2):
    prev_list = lists[len(lists) - 1]  # listsの最後に格納されているリストを取り出す
    # prev_list を引数として generate_next_list 関数を呼び出して、返り値の次のリストを lists に追加する
    # 下の pass を消して、ここを書く
    pass

# 生成したリストを、print_list 関数を用いて出力する
for li in lists:
    print_list(li)
