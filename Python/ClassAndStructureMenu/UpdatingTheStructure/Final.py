# クラスの学級委員である paiza 君は、クラスのみんなに次のような形式でアカウントの情報を送ってもらうよう依頼しました。

# 名前 年齢 誕生日 出身地

# 送ってもらったデータを使いやすいように整理したいと思った paiza 君はクラス全員分のデータを次の形式でまとめることにしました。

# User{
#     nickname : 名前
#     old : 年齢
#     birth : 誕生日
#     state : 出身地
# }


# 途中で名前が変わった際にいちいちデータを修正するのが面倒だと思ったあなたは、生徒の構造体と新しい名前を受け取り、その名前を修正する関数 changeName を作成し、それを用いて生徒の名前を更新することにしました。

# クラスの人数と全員の情報、更新についての情報が与えられるので、入力に従って名前を更新した後のクラスのメンバーの情報を出力してください。

class User:
    def __init__(self, name, age, birthday, birthplace):
        self.name = name
        self.age = age
        self.birthday = birthday
        self.birthplace = birthplace
    
    def ChangeName(self, new_name):
        self.name = new_name

users = []
n,k = list(map(int,input().split()))
for _ in range(n):
    name, age, birthday, birthplace = input().split()
    users.append(User(name,age,birthday,birthplace))
for _ in range(k):
    idx, new_name = input().split()
    idx = int(idx)
    for i, u in enumerate(users, start=1):
        if i == idx:
            u.ChangeName(new_name)
for u in users:
    print(u.name, u.age, u.birthday, u.birthplace)