# パイザ君の家の前では毎週日曜日に工事が行われます。この先 N 週間、工事が日曜日の何時に始まり、どれくらいの時間続くのかは分かっています。パイザ君は工事の間は家を離れようと思っているので、それぞれの日に工事が何時に終わるのかを知りたいと思いました。

# 工事が N 週間続くとして、各週日曜日の工事が始まる時刻と、工事が何時間何分続くのかに関する情報が与えられるので、工事が終わる時刻を 00:00 から 23:59 までの 24 時間表記で出力してください（ここで「工事が終わる時刻」とは、工事が h 時間 m 分続くとした場合、工事が始まった時刻の h 時間 m 分後を指します）。


n = int(input())

for _ in range(n):
    time, h, m = input().split()
    h = int(h)
    m = int(m)
    
    a, b = time.split(":")
    a = int(a)
    b = int(b)
    
    if m + b > 59:
        b = str(m+b - 60)
        h += 1
    else:
        b = str(m+b)

    if a + h > 23:
        a = str(a+h - 24)
    else:
        a = str(a+h)
    a = a.zfill(2)
    b = b.zfill(2)
    print(f"{a}:{b}")


# 解答2
N = int(input())

for i in range(N):
    [t, h, m] = input().split()
    th = int(t[:2])
    tm = int(t[3:])
    h = int(h)
    m = int(m)

    ah = th + h
    am = tm + m

    if am >= 60:
        ah += 1
        am -= 60
    if ah >= 24:
        ah -= 24

    ah = str(ah)
    am = str(am)

    if len(ah) == 1:
        ah = "0" + ah
    if len(am) == 1:
        am = "0" + am

    print(ah + ":" + am)