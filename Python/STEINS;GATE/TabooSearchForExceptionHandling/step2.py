# 長さ n の 2 つの数列 A = {a_1, a_2, ..., a_n}, B = {b_1, b_2, ..., b_n} が与えられます。
# 数列の差 C = {b_1-a_1, b_2-a_2, ..., b_n-a_n} を求めてください。


n = int(input())
nums = list(map(int,input().split()))
nums2 = list(map(int,input().split()))

ans = []
for i in range(n):
    ans.append(str(nums2[i] - nums[i]))
print(" ".join(ans))


# 解答2
n = int(input())
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]

for i in range(n):
    if i < n - 1:
        print(b[i] - a[i], end=" ")
    else:
        print(b[i] - a[i])