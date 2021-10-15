# A さんと B さんは次の操作を交互に繰り返すことで陣取りゲームをしようと考えました。 2 人の操作によって盤面が変化しなくなったらゲームを終了します。

# ・ 現在の陣地から上下左右に 1 マス移動することで到達できる、まだ誰の陣地でもない全てのマスを新たに陣地にする。ただし、障害物( '#' )のマスは陣地にできない。
# ・ 新たに陣地にできるマスが無い場合、何もしない。

# 盤面の情報と、先攻のプレイヤーの名前が与えられます。
# 盤面では、はじめに A さんのいるマスが 'A' , B さんのいるマスが 'B' で表されています。
# ゲーム終了時に A さん、B さん、それぞれの陣地のマス数と勝った人の名前を出力してください。

# なお、引き分けにはならないことが保証されています。

H, W = map(int, input().split())
ab = input()
s = [list(input()) for _ in range(H)]
count = 0
aadd = 0
sums = [1, 1]
flag_pass = True
ab_point = [[], []]

if ab == "B":
    count += 1
    aadd += 1

for y in range(H):
    for x in range(W):
        if s[y][x] == "A":
            ab_point[0].append([y, x, aadd])
        if s[y][x] == "B":
            ab_point[1].append([y, x, 0])


while len(ab_point[0]) > 0 or len(ab_point[1]) > 0:
    if len(ab_point[count % 2]) == 0:
        count += 1
        flag_pass = False

    [y, x, n] = ab_point[count % 2][0]

    if count / 2 < n and flag_pass:
        count += 1
        [y, x, n] = ab_point[count % 2][0]

    ab_point[count % 2].pop(0)
    ab = "A" if count % 2 == 0 else "B"

    if y > 0 and s[y - 1][x] == ".":
        s[y - 1][x] = ab
        sums[count % 2] += 1
        ab_point[count % 2].append([y - 1, x, n + 1])
    if y < H - 1 and s[y + 1][x] == ".":
        s[y + 1][x] = ab
        sums[count % 2] += 1
        ab_point[count % 2].append([y + 1, x, n + 1])
    if x > 0 and s[y][x - 1] == ".":
        s[y][x - 1] = ab
        sums[count % 2] += 1
        ab_point[count % 2].append([y, x - 1, n + 1])
    if x < W - 1 and s[y][x + 1] == ".":
        s[y][x + 1] = ab
        sums[count % 2] += 1
        ab_point[count % 2].append([y, x + 1, n + 1])


print(sums[0], sums[1])
if sums[0] > sums[1]:
    result = "A"
elif sums[0] == sums[1]:
    result = "Draw"
else:
    result = "B"
print(result)