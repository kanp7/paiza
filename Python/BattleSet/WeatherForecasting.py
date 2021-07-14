# 明日からn日分の天気を占うために「明日天気にな〜れ」をすることにしました。

# 足に履いている靴の片方を蹴り上げて、靴が表向きだったら「晴れ」、裏向きだったら「雨」、横向きだったら「曇り」であるとします。

# 靴を蹴り上げた後の向きがn個入力されるので、n日分の天気占いの結果を出力してください。

n = int(input())
for _ in range(n):
    d = input()
    if d == "forward":
        print("Sunny")
    elif d == "reverse":
        print("Rainy")
    elif d == "sideways":
        print("Cloudy")