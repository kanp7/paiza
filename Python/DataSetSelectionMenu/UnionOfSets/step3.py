# N 個の要素からなる数列Aが与えられます。 2 ≦ i ≦ Nの各iに対して、A_iと同じ値が、A_1 からA_( i - 1 )の間にあるか判定してください。

n = int(input())
numbers = list(map(int,input().split()))
# [1, 2, 3, 2, 5, 3, 3, 10, 2]
new_numbers = []
for i, number in enumerate(numbers):
    if i == 0:
        new_numbers.append(number)
        continue
    else:
        if number in new_numbers:
            print("Yes")
        else:
            print("No")
        new_numbers.append(number)
