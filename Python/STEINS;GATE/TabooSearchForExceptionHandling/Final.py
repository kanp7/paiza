# あなたは格闘ゲームのコンボのコマンド入力を練習しています。
# あるコンボのコマンドを入力しましたが、どのようにコマンドを入力したか記録するのを忘れてしまいました。
# ゲームのデータを分析しキャラクターの動作の状態を時系列順に保管されているデータだけ取得することができました。
# キャラクターの動作の状態は固定長のパラメータ列で表現されます。 また、コマンドごとに各パラメータの変化量が決まっており、どの 2 つのコマンド間でも少なくとも 1つのパラメータの変化量がお互いに異なります。

# あるコンボにおけるキャラクターの状態の時系列データが与えられます。 このとき、キャラクターに与えたコンボのコマンド入力を時系列順に復元するプログラムを作成してください。


n, m, l = map(int,input().split())

dic = {}
for i in range(n):
    amount_of_change = list(map(int,input().split()))
    dic[i] = amount_of_change

subtraction = []
for j in range(l):
    subtraction.append(list(map(int,input().split())))
    if j >= 1:
        diff = []
        for k in range(m):
            tmp = []
            sub = subtraction[j][k] - subtraction[j-1][k]
            diff.append(sub)
        ans = [k+1 for k,v in dic.items() if v == diff ]
        print(ans[0])


# 解答2
n, m, l = map(int, input().split())
d = [[int(x) for x in input().split()] for i in range(n)]
p = [[int(x) for x in input().split()] for i in range(l)]

for i in range(1, l):
    diff = [p[i][j] - p[i - 1][j] for j in range(m)]

    order = -1
    for j in range(n):
        same = True
        for k in range(m):
            if diff[k] != d[j][k]:
                same = False
        if same:
            order = j + 1
            break

    print(order)