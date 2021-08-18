# 1行目で血液型が1つ与えられます。
# m 行の血液型と占い結果の組が与えられるので、血液型をキー、占い結果を値として、連想配列（辞書）に保存してください。
# その後、1行目で与えられた血液型に対応する占い結果を表示してください。


t = input()
m = int(input())
dic = {}
for _ in range(m):
    key, value = input().split()
    dic[key] = value
print(dic[t])