# 整数 N が与えられるので、次の処理を N 回してください。

# ・ 配列のサイズ K とその要素 A1 ... AK が与えられるので、全ての要素の和を求めて出力してください。

n = int(input())
for _ in range(n):
    nums = list(map(int,input().split()))
    k = nums.pop(0)
    print(sum(nums))