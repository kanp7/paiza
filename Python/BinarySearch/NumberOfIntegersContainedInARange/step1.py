# ソートされた数列 A = (A_1, A_2, ..., A_n) と、q 個の整数 k_1, k_2, ..., k_q が与えられます。各 k_i について、数列 A に含まれているなら Yes と、含まれていないなら No と出力してください。

# なお、n, q の最大値はいずれも 200,000 です。


n = int(input())
nums = list(map(int,input().split()))
q = int(input())

for i in range(q):
    t = int(input())
    left = 0
    right = n-1
    while left <= right:
        mid = (left + right) / 2
        mid = int(mid)
        if nums[mid] == t:
            print("Yes")
            break
        if nums[mid] < t:
            left = mid + 1
        else:
            right = mid - 1
    else:
        print("No")


