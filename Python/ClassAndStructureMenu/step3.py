# クラスの学級委員である paiza 君は、クラスのみんなに次のような形式でアカウントの情報を送ってもらうよう依頼しました。

# 名前 年齢 誕生日 出身地

# 送ってもらったデータを使いやすいように整理したいと思った paiza 君はクラス全員分のデータを次の形式でまとめることにしました。

# User{
#     nickname : 名前
#     old : 年齢
#     birth : 誕生日
#     state : 出身地
# }


# この情報を扱いやすくするために、年齢が昇順になるようにデータを並び替えることにしました。
# クラスメートの情報が与えられるので、並び替えた後のデータを出力してください。


class User:
    def __init__(self, name, age, birthday, birthplace):
        self.name = name
        self.age = age
        self.birthday = birthday
        self.birthplace = birthplace

users = []
n = int(input())
for _ in range(n):
    name, age, birthday, birthplace = input().split()
    users.append(User(name,age,birthday,birthplace))

# sorted()関数のkey引数＋lamdaを利用
sorted_users = sorted(users, key=lambda u: u.age)

for user in sorted_users:
    print(user.name, user.age, user.birthday, user.birthplace)