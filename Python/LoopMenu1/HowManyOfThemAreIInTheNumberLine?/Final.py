# 長さ N の数列 a (a_1, a_2, ..., a_N) が与えられます。
# この数列の中に 1 が何個あるか出力してください。


n = int(input())
nums = list(map(int,input().split()))
print(nums.count(1))