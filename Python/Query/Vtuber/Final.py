# あなたは流行に乗っかり、Vtuber としての活動をスタートしました。活動も軌道にのり、配信をするたびに視聴者が superchat を送ってくれたり、メンバーシップ制度に加入してくれるようになりました。
# （わからない方は 「youtube superchat」「youtube membership」 などで検索してみてください。）
# あなたはお礼として superchat を読むお礼配信をおこなうことにしました。
# その配信で、前回の配信の superchat の総額が高いアカウントから順に、superchat をした全てのアカウントの名前を読んだ後、メンバーシップに入ってくれた全てのアカウントの名前を辞書順昇順で読むことにしました。
# superchat の金額が同じ場合、同じ金額の中で辞書順降順でアカウント名を読むことにしました。
# 前回の配信の superchat とメンバーシップ加入の履歴が与えられるので、読む順番にアカウント名を出力するプログラムを作成してください。

n = int(input())

members = {}
members_ship = set()
for _ in range(n):
    event = input()
    name = event.split()[0]
    order = event.split()[1]
    if order == "give":
        amount = int(event.split()[2])
        if name not in members:
            members[name] = amount
        else:
            members[name] += amount
    else:
        members_ship.add(name)
        

high_amount = sorted(members.items(), key=lambda x:(x[1],x[0]), reverse=True)
sort_member_ship = sorted(members_ship)
for name, amount in high_amount:
    print(name)
for m in sort_member_ship:
    print(m)

