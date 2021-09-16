# 1 から n まで番号が付けられた人々がいます。 i 番目の人の財産は a_i 円です。金額 k が与えられるので（k は a_1, ..., a_n のいずれか）、財産が k 円である人の番号を出力してください。ただし、そのような人が複数いる場合には、そうした人々の中で最も小さい番号を出力してください。


n = int(input())

money = []
for _ in range(n):
    money.append(int(input()))

k = int(input())

print(money.index(k)+1)


# 解答2
n = int(input())

a = [0] * n

for i in range(n):
    a[i] = input()

k = input()

for i in range(n):
    if a[i] == k:
        print(i + 1)
        break