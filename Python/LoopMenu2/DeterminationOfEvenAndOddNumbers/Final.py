# N 個の整数 a_1, a_2, ..., a_N が与えられます。
# この N 個の整数について、a_1 から順に 奇数か偶数か判定し、奇数なら odd 、偶数なら even を改行区切りで出力してください。

n = int(input())
nums = list(map(int,input().split()))

for n in nums:
    if n % 2 == 0:
        print("even")
    else:
        print("odd")