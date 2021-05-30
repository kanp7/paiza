n = int(input())

user_data = []
for _ in range(n):
    user_data.append((input().split()))

class UserInfo:
    def __init__(self):
        self.nickname = ''
        self.old = 0
        self.birth = 0
        self.state = ''

for i in range(n):
    user = UserInfo
    user.nickname = user_data[i][0]
    user.old = user_data[i][1]
    user.birth = user_data[i][2]
    user.state = user_data[i][3]
    print("User{")
    print(f"nickname : {user.nickname}")
    print(f"old : {user.old}")
    print(f"birth : {user.birth}")
    print(f"state : {user.state}")
    print("}")
