# N 人組のロボットアイドルグループのマネージャーとなった paiza 君は、グループに所属しているアイドル全員の名前を把握しておく必要があります。アイドルグループにはメンバーの加入と脱退がつきものなので、その度メンバーを覚えたり忘れたりする必要があります。
# paiza 君は仕事として握手会の度にアイドル全員の名前を書き出します。
# ロボットの名前はほとんどが乱数的に付けられたものなので覚えるのが大変です。
# そこで、イベント（メンバーの加入・脱退と握手会）が与えられるので、それらに伴う paiza 君の仕事を行うプログラムを作成しましょう。

n, k = list(map(int,input().split()))
names = set()

for _ in range(n):
    names.add(input())

for _ in range(k):
    event = input()
    if event == "handshake":
        list_names = list(names)
        if len(list_names) > 0:
            list_names.sort()
            for n in list_names:
                print(n)
    else:
        action, name = event.split()
        if action == "join":
            join, name = event.split()
            names.add(name)
        elif action == "leave":
            leave, name = event.split()
            names.remove(name)

