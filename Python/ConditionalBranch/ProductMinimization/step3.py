# 整数N, 2 つの数列A, B が与えられます。 1 ≦ i ≦ N を満たす整数 i のうち、A_i と B_i が等しくなるような i の個数を求めてください。

n = int(input())

list1 = input().split()
list2 = input().split()

count = 0
for i in range(n):
    if list1[i] == list2[i]:
        count += 1

print(count)
