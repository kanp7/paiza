# p 人のグループ A , q 人のグループ B , r 人のグループ C があります。各グループのメンバーにはそれぞれ番号がつけられており、 A グループの i 番目の人は B グループの j 番目の人に仕事を任せ、 B グループの j 番目の人は与えられた仕事を C グループの k 番目の人に任せます。すると結局、 A グループの i 番目の人の仕事をするのは C グループの k 番目の人だということになります。

# パイザ君は A グループの各人の仕事を結局 C グループの誰が行うことになるのか知りたがっています。 A グループの人のそれぞれが最終的に C グループの誰に仕事を頼むことになるのかを、 A グループの人の番号が小さい順に p 行出力してください。

p,q,r = map(int,input().split())

group_a = {}
group_b = {}

for _ in range(p):
    a,b = map(int,input().split())
    group_a[a] = b
# group_a {2: 1, 1: 2}  aの2番はbの1番に仕事を渡す

for _ in range(q):
    b,c = map(int,input().split())
    group_b[b] = c
#  group_b {1: 1, 2: 2} bの1番はcの1番に仕事を渡す

for i in range(p):
    print(str(i+1) + " " + str(group_b[group_a[i+1]]))

# aの1番の仕事はcの2番に渡った
# 1 2
# 2 1

