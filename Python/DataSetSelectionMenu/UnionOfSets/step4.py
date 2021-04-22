# N 個の要素からなる数列Aが与えられます。 2 ≦ i ≦ Nの各iに対して、A_iと同じ値が、A_1 からA_( i - 1 )の間にあるか判定してください。ただし、A_iは非常に大きくなることがあります。

n = int(input())
l = list(map(int,input().split()))
# [1, 2, 3, 2, 5, 3, 3, 10, 2]

numbers = []
for i,n in enumerate(l):
    if i > 0:
        if n in numbers:
            print("Yes")
        else:
            print("No")
    numbers.append(n)
