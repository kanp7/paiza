# N 個の要素からなる数列A, Bが与えられます。 AまたはBに含まれる値をすべて列挙し、昇順に出力してください。ただし出力する数列は重複した要素を取り除いてください。

n = int(input())
list_a = list(map(int,input().split()))
list_b = list(map(int,input().split()))
list_ab = list_a + list_b
set_list = set(list_ab)  # 重複を削除
sort_list = sorted(set_list)  # 並べ替え
print(" ".join(list(map(str,(sort_list)))))o