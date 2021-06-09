# 整数 N , K と N 行 K 列 の二次元配列 A が与えられます。 A の要素のうち、1 要素だけ 1 になっている要素があるので、その要素の行と列を出力してください。

n, k = list(map(int,input().split()))

loop_count = 0
for _ in range(n):
    nums = list(map(int,input().split()))
    if 1 in nums:
        print(f"{loop_count + 1} {nums.index(1)+1}")
    loop_count += 1
