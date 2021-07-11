# 長さ N の数列 A と、K 個の区間 (l_1,r_1) ... (l_K,r_K) が与えられるので、各区間についての A の区間和 A_{l_i} + ... + A_{r_i} (1 ≦ i ≦ K) を求めてください。

n,k = list(map(int,input().split()))

sums = 0
accumulation_sum = []
for _ in range(n):
    num = int(input())
    sums += num
    accumulation_sum.append(sums)
# [16, 104, 114, 49]


for _ in range(k):
    start, end = list(map(int,input().split()))
    if start == 1:
        # startインデックスが1ならばendインデックスまでの累積和
        print(accumulation_sum[end-1])
    else:
        # endインデックスの値からstartインデックスの値の一つ前までの累積和を引く
        print(accumulation_sum[end-1] - accumulation_sum[start-2])
# A[l]+...+A[r] = (A[0]+...A[r]) - (A[0]+...A[l-1]) = S[r]-S[l-1]


# 時間切れ
n,k = list(map(int,input().split()))

nums = []
for _ in range(n):
    nums.append(int(input()))

for _ in range(k):
    start, end = list(map(int,input().split()))
    add_nums = sum(nums[start-1:end])
    print(add_nums)