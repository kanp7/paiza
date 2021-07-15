# あなたはおやつにゆで卵を作ることにしました。

# しかし、ゆで卵ができるのが待ちきれないので、そのときの卵の状態が生なのか、半熟なのか、固ゆでなのかを知りたいと思いました。

# 卵をお湯に入れている時間（分）を入力として与えたとき、そのときの卵の状態を出力するプログラムを作成してください。


# 0 ≤ m ≤ 5 のとき raw
# 6 ≤ m ≤ 7 のとき soft boiled
# 8 ≤ m ≤ 15 のとき hard boiled

m = int(input())

if m >= 0 and m <= 5:
    print("raw")
elif m >= 6 and m <= 7:
    print("soft boiled")
elif m >= 8 and m <= 15:
    print("hard boiled")