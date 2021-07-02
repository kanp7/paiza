# 3xxx 年、ロボット学校の先生である paiza 君は、新しく担当するクラスの生徒一人一人の出席番号と識別 ID を覚えるように言われました。
# 具体的には、出席番号が与えられたら、その生徒の識別 ID を言えるようになる必要があります。
# 覚えるべき生徒の出席番号と識別 ID のペアが与えられたのち、いくつか出席番号が与えられるので、各番号に対応する生徒の識別 ID を出力してください。


n, k = list(map(int,input().split()))

dic = {}
for _ in range(n):
    num, i = input().split()
    dic[num] = i
# {'1': 'Sin', '2': 'Sakura', '3': 'Kayo', '4': 'Yui'}

for _ in range(k):
    key = input()
    print(dic[key])