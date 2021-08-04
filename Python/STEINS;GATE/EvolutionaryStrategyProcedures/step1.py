# あなたは RPG のダンジョンの設計をしています。

# そのダンジョンには N 個の部屋が用意されており、それぞれの部屋は 1, 2, ..., N で表されます。このダンジョンでは 1 部屋に 1 プレイヤーしか滞在できません。
# また、プレイヤーは M 人いて、現在 i (1 ≦ i ≦ M) 番目のプレイヤーは部屋 S_i (1 ≦ S_i ≦ N) に滞在しています。

# ダンジョンをクリアするには、プレイヤーはそれぞれ、部屋を移動する必要があります。

# しかし、部屋を移動しようと思ってもその部屋はまだ別のプレイヤーが滞在しているかもしれません。その場合はプレイヤーは部屋を移動することができません。

# そこで、それぞれのプレイヤーが部屋を移動できるか事前に判定することにしました。

# あなたの仕事は、各 i (1 ≦ i ≦ Q) について、現在の状況から E_i 番目のプレイヤーが部屋 T_i に移動できるか判定することです。

# ただし、滞在している部屋と移動先の部屋が同じ場合、つまり S_i = T_i (1 ≦ i ≦ M) の場合、そのプレイヤーは移動ができることとします。また各 i (1 ≦ i ≦ Q) について、部屋を移動できると判定された場合でも、実際に移動はしないものとします。



n, m, q = map(int,input().split())

dic = {}
for i in range(m):
    dic[i] = input()
values = [v for v in dic.values()]

for _ in range(q):
    key, value = input().split()
    key = int(key)
    if dic[key-1] == value:
        print("Yes")
    else:
        if value in values:
            print("No")
        else:
            print("Yes")


# 解答2
n, m, q = map(int, input().split())
s = [int(input()) for _ in range(m)]

s.insert(0, -1)
for _ in range(q):
    e, t = map(int, input().split())
    if s[e] == t:
        print("Yes")
        continue

    for i in range(1, m + 1):
        if i != e and s[i] == t:
            print("No")
            break

        if i == m:
            print("Yes")