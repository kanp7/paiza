# 整数 N が与えられるので、次の規則に従って N 行の出力をしてください。

# ・ N 行のうち、 i 行目では、1 から i までの数字を半角スペース区切りで出力してください。

# 例として、 N = 3 のとき、出力は次の通りになります。

n = int(input())
nums = []
for i in range(n):
    nums.append(str(i+1))
    str_num = ' '.join(nums)
    print(str_num)

