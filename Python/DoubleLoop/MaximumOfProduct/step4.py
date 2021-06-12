# 整数 N , K が与えられるので、 1 から N までの数字を半角スペース区切りしたもの
# "1 2 ... (N-1) N" を K 行出力してください。

n, k = list(map(int,input().split()))

for _ in range(k):
    nums = (list(map(str,range(1,n+1))))
    print(' '.join(nums))