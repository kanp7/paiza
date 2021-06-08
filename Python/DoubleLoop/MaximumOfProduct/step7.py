# 整数 N , K と N 行 K 列 の二次元配列 A が与えられます。 A の要素のうち、最大の要素の値を出力してください。

n , k = list(map(int,input().split()))

numbers = []
for _ in range(n):
    nums = list(map(int,input().split()))
    numbers.extend(nums)
print(max(numbers))