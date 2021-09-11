# n 人の人の名前 s_1, ..., s_n が与えられたのち、 m 回の「攻撃」に関する情報が与えられます。各行は “p_i a_i” というフォーマットで与えられ、 p_i はダメージを受けた人の名前 （s_1, ..., s_n のいずれか） 、 a_i は p_i が受けたダメージ数を表す数です。なお、一度もダメージを受けていない人の合計ダメージは 0 とします。

# それぞれの人が受けた合計ダメージを、人の名前のアルファベットの辞書順に出力してください。

n = int(input())
dic = {}
for i in range(n):
    key = input()
    dic[key] = 0
m = int(input())
for _ in range(m):
    name, damege = input().split()
    damege = int(damege)
    dic[name] += damege

sorted_dic = sorted(dic.items(), key=lambda x:x[0])

for key, value in sorted_dic:
    print(value)



# keys は辞書のメソッドで、辞書のキー（今回だと人名）を取り出します。dmg.keys() はこれだけだとリストになっていないので、list関数 でリストに変換すると、dmg のキーになっている人名のリスト names を作ることができます。
# あとは names をソートして、names の要素をキーとする dmg の値を順に出力すれば OK です。
# Python のfor文はリストなどの要素を直接ループ用の変数に代入することができます。したがって、for i in range(n): とした後に names[i] のようにして人名にアクセスせずとも、for name in names: で name が names のそれぞれの要素を指すようになります。
n = int(input())
dmg = {}

for i in range(n):
    s = input()
    dmg[s] = 0

m = int(input())

for i in range(m):
    [p, a] = input().split()
    a = int(a)
    dmg[p] += a

names = list(dmg.keys())
names.sort()

for name in names:
    print(dmg[name])