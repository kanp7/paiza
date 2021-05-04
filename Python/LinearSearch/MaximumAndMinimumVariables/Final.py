# ・ 1行目に数列の長さを表す整数 n が与えられます。
# ・ 2行目に、数列の値 a_i が先頭から順に半角スペース区切りで与えられます。

n = int(input())
numbers = list(map(int,input().split()))
print(max(numbers),min(numbers))