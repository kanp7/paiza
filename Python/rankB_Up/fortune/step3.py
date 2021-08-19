# 1行目でユーザーが1つ与えられます。
# n 行のユーザーと血液型の組が与えられるので、ユーザーをキー、血液型を値として、連想配列（辞書）に保存してください。
# その連想配列（辞書）の中で1行目で与えられたユーザー名と、ユーザー名に対応する血液型を表示してください。


s = input()
n = int(input())

dic = {}
for _ in range(n):
    key, value = input().split()
    dic[key] = value
print(s, dic[s])


# 解答2
target = input()
n = int(input())
dictionary = {}

for i in range(n):
    tmp = input().split()
    dictionary[tmp[0]] = tmp[1]

for user, blood in dictionary.items():
    if user == target:
        print(user + " " + blood)
        break
