# n 人の生徒がテストを受けました。このテストで k 点以上の点数を取った人が合格です。

# n 人の各生徒について、その人の名前とその人が取った点数が入力として与えられるので、このテストに合格した人の名前をすべて、入力された順に改行区切りで出力してください。

# なお、合格者が一人もいない場合は、何も出力しないでください。

n = int(input())
dic = {}
for _ in range(n):
    name, point = input().split()
    dic[name] = int(point)
border = int(input())

for name,point in dic.items():
    if point >= border:
        print(name)
