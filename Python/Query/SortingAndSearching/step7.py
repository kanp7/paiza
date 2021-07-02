# 3xxx年、ロボット学校の先生である paiza 君は、新しく担当するクラスの生徒一人一人の出席番号と識別 ID を覚えて、出席番号が与えられたら、その生徒の識別 ID を言えるようになる必要があります。
# paiza 君の務める学校は転校が多く、頻繁に生徒が増減します。

# 覚えるべき生徒の出席番号と識別 ID が与えられたのち、いくつかのイベントを表す文字列が与えられるので、与えられた順に各イベントに応じて次のような処理をおこなってください。

# ・join num id
# 生徒番号 num , 識別ID id の生徒を新たに覚える

# ・leave num
# 生徒番号 num の生徒を忘れる

# ・call num
# 生徒番号 num の生徒の識別 ID を出力する



n, k = list(map(int,input().split()))

dic = {}
for _ in range(n):
    num, i = input().split()
    dic[num] = i

for _ in range(k):
    inputs = input()
    if  "call" in inputs:
        key = inputs.split()[1]
        print(dic[key])
    elif "join" in inputs:
        temp, key , new_i = inputs.split()
        dic[key] = new_i
    elif "leave" in inputs:
        key = inputs.split()[1]
        del dic[key]