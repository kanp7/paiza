# 数列 A = {a_1, a_2, ..., a_n} と、整数 x が与えられます。
# 整数 x が数列 A の何番目に現れているかを求めてください。つまり、x = a_i を満たす i を求めてください。
# なお、整数 x は必ず数列 A に 1 つだけ含まれていることが保証されます。


n = int(input())
nums = [int(x) for x in input().split()]
x = int(input())

print(nums.index(x)+1)


# 解答2
n = int(input())
a = [int(x) for x in input().split()]
x = int(input())

pos_of_x = -1
for i in range(n):
    if a[i] == x:
        pos_of_x = i + 1
        break

print(pos_of_x)