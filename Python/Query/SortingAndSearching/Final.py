# paiza 君のクラスには paiza 君を含めて N + 1 人の生徒がいます。paiza 君の身長は P cm で、他の N 人の生徒の身長はそれぞれ A_1 ... A_N です。
# このクラスには次のようなイベントが合計 K 回起こります。
# それぞれのイベントは以下のうちのいずれかです。

# ・転校生がクラスに加入する
# ・全員で背の順に並ぶ

# 全員で背の順で並ぶイベントが起こるたびに、そのとき paiza 君は前から何番目に並ぶことになるかを出力してください。

n, k, p_height = list(map(int,input().split()))
students = []
students += [p_height]
for _ in range(n):
    students.append(int(input()))
for _ in range(k):
    event = input()
    if "join" in event:
        join, height =  event.split()
        students.append(int(height))
    elif "sorting" in event:
        students.sort()
        print(students.index(p_height)+1)