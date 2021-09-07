
pins = []
stand = 0
target_row = None

for i in range(4):
    row = list(map(int,input().split()))
    pins.append(row)
    stand += row.count(1)
    if row.count(1) > 0:
        target_row = i

if target_row == 0:
    ans = 7
    for p in reversed(pins[target_row]):
        if p == 1:
            print(ans)
            break
        else:
            ans += 1
elif target_row == 1:
    ans = 4
    for p in reversed(pins[target_row]):
        if p == 1:
            print(ans)
            break
        else:
            ans += 1
elif target_row == 2:
    ans = 2
    for p in reversed(pins[target_row]):
        if p == 1:
            print(ans)
            break
        else:
            ans += 1
elif target_row == 3:
    ans = 1
    print(ans)

print(stand)


# 解答2
p = []
ans_p = 0
ans_num = 0

for i in range(4):
    p += input().split()

for i in range(10):
    if p[i] == "1":
        ans_num += 1
        ans_p = 10 - i

print(ans_p)
print(ans_num)