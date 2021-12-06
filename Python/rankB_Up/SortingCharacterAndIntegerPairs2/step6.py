# 1行目で整数 n が与えられ、2行目で n 個の整数が与えられます。
# n 個の整数を昇順に出力してください。

n = int(input())
nums = list(map(int,input().split()))
nums.sort()
for i in nums:
    print(i)


# 解答2
input()  # 1つ目の入力は使わないので読み飛ばす
strings = input().split()
nums = []

for num in strings:
    nums.append(int(num))

nums.sort()

for i in nums:
    print(i)