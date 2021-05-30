# クラスの学級委員である paiza 君は、クラスのみんなに次のような形式でアカウントの情報を送ってもらうよう依頼しました。

# 名前 年齢 誕生日 出身地

# 送ってもらったデータを使いやすいように整理したいと思った paiza 君はクラス全員分のデータを次のような構造体でまとめることにしました。

# student{
#     name : 名前
#     old : 年齢
#     birth : 誕生日
#     state : 出身地
# }

# 年齢ごとの生徒の名簿を作る仕事を任された paiza 君はクラスメイトのうち、決まった年齢の生徒を取り出したいと考えました。
# 取り出したい生徒の年齢が与えられるので、その年齢の生徒の名前を出力してください。

n = int(input())

user_data = []
for _ in range(n):
    user_data.append((input().split()))
# user_data = [["mako","13","08/08", "nara"],["megumi","14","11/02","saitama"],["taisei","16","12/04","nagano"]]

class UserInfo:
    def __init__(self):
        self.nickname = ''
        self.old = 0
        self.birth = 0
        self.state = ''

old = input()
for i in range(n):
    user = UserInfo
    user.nickname = user_data[i][0]
    user.old = user_data[i][1]
    user.birth = user_data[i][2]
    user.state = user_data[i][3]
    if user.old == old:
        print(user.nickname)
