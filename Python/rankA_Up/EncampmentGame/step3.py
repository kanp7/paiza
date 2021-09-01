
# 不正解
h, w = map(int,input().split())
s = [list(input()) for _ in range(h)]
flag_out = False

for y in range(h):
    for x in range(w):
        if s[y][x] == "*":
            if y > 0 and s[y-1][x] != "#":
                s[y-1][x] = "*"
            if y < h-1 and s[y+1][x] != "#":
                s[y+1][x] = "*"
            if x > 0 and s[y][x-1] != "#":
                s[y][x-1] = "*"
            if x < w - 1 and s[y][x+1] != "#":
                s[y][x+1] = "*"
for y in range(h):
    print("".join(s[y]))


# 解答
H, W = map(int, input().split())
s = [list(input()) for _ in range(H)]
my_p = []

for y in range(H):
    for x in range(W):
        if s[y][x] == "*":
            my_p.append([y, x])

while my_p:
    [y, x] = my_p.pop(0)

    if y > 0 and s[y - 1][x] == ".":
        s[y - 1][x] = "*"
        my_p.append([y - 1, x])
    if y < H - 1 and s[y + 1][x] == ".":
        s[y + 1][x] = "*"
        my_p.append([y + 1, x])
    if x > 0 and s[y][x - 1] == ".":
        s[y][x - 1] = "*"
        my_p.append([y, x - 1])
    if x < W - 1 and s[y][x + 1] == ".":
        s[y][x + 1] = "*"
        my_p.append([y, x + 1])

for y in range(int(H)):
    for x in range(int(W)):
        print(s[y][x], end="")
    print()