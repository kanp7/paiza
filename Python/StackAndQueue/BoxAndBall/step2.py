# N 個の要素からなる数列 A があります。 A に含まれる連続した X 個の要素の和の最大値とその区間の左端の値を出力してください。ただし、要素の和の最大となる区間が複数ある場合はそのうちもっとも先頭の値を出力してください。
# たとえば、 N = 4 , A = [2, 3, 4, 1] , X = 2 とします。連続した 2 個の要素の和が最大となる区間は A の 2 番目から 3 番目まで( 3 + 4 = 7 が最大値 )なので、最大値 7 とその区間の左端の値 3 を出力します。

# また、実行時間に注意しましょう。たとえば以下の Python3 のプログラムのような、数列の要素数 N と和を求める連続する要素数 X を用いて、約 N * X 回足し算をおこなうプログラムはタイムオーバーになってしまうことがあります。キューまたはスタックを用いて効率のよいプログラムを意識しましょう。


# タイムオーバー
n, x = map(int,input().split())

left_end = 0
ans = 0
nums = list(map(int,input().split()))

for i in range(n):
    sum_of_intervals = sum(nums[i:i+x])
    if sum_of_intervals > ans:
        ans = sum_of_intervals
        left_end = nums[i]
print(ans, left_end)

