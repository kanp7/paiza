# m 個の文字 c_1, ..., c_m と、 n 個の文字列 S_1, ..., S_n が与えられます。各 c_i （1 ≤ i ≤ m） について、各 S_j （1 ≤ j ≤ n） に c_i が出現するかをそれぞれ調べ、出現する場合は "YES" を、そうでない場合には "NO" を、そのつど出力してください。


m = int(input())
check_list = []
for _ in range(m):
    check_list.append(input())

word_list = []
n = int(input())
for _ in range(n):
    word_list.append(input())

for c in check_list:
    for word in word_list:
        if c in word:
            print("YES")
        else:
            print("NO")


# 解答2
m = int(input())
c = [""] * m

for i in range(m):
    c[i] = input()

n = int(input())
S = [""] * n

for i in range(n):
    S[i] = input()

for i in range(m):
    for j in range(n):
        if c[i] in S[j]:
            print("YES")
        else:
            print("NO")