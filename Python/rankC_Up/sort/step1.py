# n 個の数 a_1, … , a_n が与えられます。与えられた数を小さい順に改行区切りで出力してください。

n = int(input())

numbers = []
for _ in range(n):
    i = int(input())
    numbers.append(i)
sort_number =sorted(numbers)

for n in sort_number:
    print(n)
