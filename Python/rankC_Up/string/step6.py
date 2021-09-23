h,m = input().split(":")

h = int(h)
m = int(m)
m += 30

if m > 59:
    m = m - 60
    h += 1

h = str(h).zfill(2)
m = str(m).zfill(2)

print(f"{h}:{m}")


# 解答2
S = input()
h = int(S[:2])
m = int(S[3:])

if m + 30 >= 60:
    h = str(h + 1)
    m = str(m + 30 - 60)
else:
    h = str(h)
    m = str(m + 30)

if len(h) == 1:
    h = "0" + h
if len(m) == 1:
    m = "0" + m

print(h + ":" + m)