# N 個の整数 a_1, a_2, ..., a_N が与えられます。
# a_i に i を足したとき、N 個の整数の最小値を出力してください。

n = int(input())
nums = list(map(int,input().split()))

i = 1
sums = 101
for num in nums:
    if num + i < sums:
        sums = num +i
    i += 1


print(sums)
    