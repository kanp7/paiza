# 西暦 1,000,000,000 年に行われた歴史の授業のグループワークで、歴史上のいくつかの出来事についての記事を年代順に並べて歴史年表を作成することになりました。
# ところが、歴史年表は 1 枚の紙にまとめる必要があるため、古い出来事を担当する人から順番に歴史年表を書くことにしました。
# グループの人数 N とそのメンバー S_1 ... S_N が与えられます。
# 続けて、歴史年表に載せる出来事の数 K , 各出来事の起こった年 Y_i , その出来事の記事を担当する生徒の名前 C_i が与えられるので、歴史年表を書く担当者の順番を出力してください。
# なお、 1 人の生徒が複数の出来事の記事を担当することがある点に注意してください。



n, k = list(map(int,input().split()))
names = set()
for _ in range(n):
    name = input()
    names.add(name)
    
dic = {}
for _ in range(k):
    year, in_charge = input().split()
    year = int(year)
    dic[year] = in_charge
dic_sorted = sorted(dic.items(), key=lambda x:x[0])

for year, name in dic_sorted:
    print(name)