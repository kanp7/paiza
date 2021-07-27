# 次のような占いプログラムを作成してください。

# 最初に「ユーザー」 U が1つ与えられます。
# 続いて n 人の「ユーザー」と「ユーザーに対応する血液型」が与えられます。
# 続いて m 種類の「血液型」と「血液型に対応する占い結果」が与えられます。

# 与えられたユーザー U に対応する占い結果を表示してください。

# 入力例の1つ目は、ユーザーの血液型についてのラッキーカラーの占いです。

# 入力例の2つ目は、ユーザーの星座についてのラッキーパーソンの占いになっています。
# 「血液型」として「星座」などのさまざまな文字列を利用できるようにすることで、他の占いにも対応する必要があることに注意してください。


u = input()
n = int(input())

dic = {}
for _ in range(n):
    key, value = input().split()
    dic[key] = value

dic2 = {}
m = int(input())
for _ in range(m):
    key2, value2 = input().split()
    dic2[key2] = value2
print(dic2[dic[u]])


# 解答2
target = input()

n = int(input())
users = {}
for i in range(n):
    tmp = input().split()

    users[tmp[0]] = tmp[1]

m = int(input())
fortunes = {}
for i in range(m):
    tmp = input().split()

    fortunes[tmp[0]] = tmp[1]

user_blood = None
for user, blood in users.items():
    if user == target:
        user_blood = blood
        break

for blood, fortune in fortunes.items():
    if blood == user_blood:
        print(fortune)
        break