# ある月の 1 日は日曜日、 2 日は月曜日...です。X日は何曜日でしょう。

x = int(input())
week = { 1:"Sun", 2:"Mon", 3:"Tue", 4:"Wed", 5:"Thu", 6:"Fri", 7:"Sat" }

if x <= 7:
    print(week[x])
else:
    if  x % 7 == 0:
        print(week[7])
    else:
        i = x % 7
        print(week[i])