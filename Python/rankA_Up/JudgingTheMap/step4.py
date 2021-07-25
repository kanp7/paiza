h, w = map(int,input().split())

s = [list(input()) for _ in range(h)]

for y in range(h):
    for x in range(w):
        # 一番上のマスか一つ上のマスが＃かを判定
        if y == 0 or s[y-1][x] == "#":
            # 一番下のマスか一つ下のマスが＃かを判定
            if y == h-1 or s[y+1][x] == "#":
                print(y, x)
