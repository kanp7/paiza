# n 行のユーザーと血液型の組が与えられるので、ユーザーをキー、血液型を値として、連想配列（辞書）に保存してください。
# そのあとで連想配列（辞書）をそのまま表示してください。

n = int(input())

dic = {}
for _ in range(n):
    key,value = input().split()
    dic[key] = value

for key,value in dic.items():
    print(key, value)