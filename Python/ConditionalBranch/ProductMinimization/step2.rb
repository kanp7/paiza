# 整数N, A, B ( - 99 ≦ N, A, B ≦ 100 ) があります。以下の 2 つの操作をそれぞれ 1 回ずつおこなったとき、Nを 0 にできる場合はYESを、できない場合はNOを出力してください。
# 1. NにAを足す、またはNからAを引く
# 2. NにBを足す、またはNからBを引く

n,a,b = map(int,input().split())

if (n + a + b) == 0 or (n - a - b ) == 0 or (n + a -b) == 0 or (n - a + b) == 0:
    print("YES")
else:
    print("NO")
