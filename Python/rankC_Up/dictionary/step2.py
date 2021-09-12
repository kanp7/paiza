# n 人の人の名前 s_1, ..., s_n が与えられたのち、 m 回の「攻撃」に関する情報が与えられます。各行は “p_i a_i” というフォーマットで与えられ、 p_i はダメージを受けた人の名前 （s_1, ..., s_n のいずれか） 、 a_i は p_i が受けたダメージ数を表す数です。

# 最後に人名 S が与えられるので （S は s_1, ..., s_n のいずれか） 、 S が受けたダメージの合計を出力してください。なお、一度もダメージを受けていない人の合計ダメージは 0 とします。


n = int(input())
dic = {}
for _ in range(n):
    name = input()
    dic[name] = 0

m = int(input())
for _ in range(m):
    name, damage = input().split()
    damage = int(damage)
    dic[name] += damage
s = input()
print(dic[s])