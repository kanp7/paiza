# 深夜の時刻を表すとき、午前1時は25時、午前2時は26時と表記されることがあります。

# このような24時を超える時刻を修正して、1〜12時で表してください。

n = int(input())
if n > 24:
    print(n-24)