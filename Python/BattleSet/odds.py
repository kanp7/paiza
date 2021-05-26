# この問題は、弊社営業社員が競技プログラミングに挑戦したものです。
# https://youtu.be/Vf2RFjXCmZY

# あなたは奇数が大好きな山田さんと数字の仕分けをすることになりました。
# 仕分けをする数字が与えられますので、奇数であるものを小さい順に出力してください。

n = int(input())

nums = []
for _ in range(n):
    num = int(input())
    if num % 2 == 1:
        nums.append(num)
sort_num = sorted(nums)

for num in sort_num:
    print(num)
