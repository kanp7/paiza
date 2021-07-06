# paiza には N 個の部署があり、名前はそれぞれ S_1 ... S_N です。
# 経理係となったあなたは、どの部署が何円のどのような買い物をしたかを記録するように言われました。
# どの部署が何円で何を買ったかの領収書が K 枚与えられるので、各部署の会計表を作成しましょう。


n, k = list(map(int,input().split()))

departments = {}
for _ in range(n):
    department = input()
    departments[department] = []

for _ in range(k):
    dep, order_num, amount = input().split()
    departments[dep].append([order_num, amount])

for dep, values in departments.items():
    print(dep)
    for num, amount in values:
        print(num, amount)
    print("-----")