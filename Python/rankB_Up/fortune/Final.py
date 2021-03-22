# 次のような占いプログラムを作成してください。

# 「ユーザー」と「ユーザーに対応する血液型」、「血液型」と「血液型に対応する占い結果」が与えられます。

# それぞれのユーザーに対応する占い結果を表示してください。

# 入力例の1つ目は、ユーザーの血液型についてのラッキーカラーの占いです。

# 入力例の2つ目は、ユーザーの星座についてのラッキーパーソンの占いになっています。
# 「血液型」として「星座」などのさまざまな文字列を利用できるようにすることで、他の占いにも対応する必要があることに注意してください。

n = int(input())
dic = {}
for _ in range(n):
    key,value = input().split(" ")
    dic[key] = value

n2 = int(input())
dic2 = {}
for _ in range(n2):
    key,value = input().split(" ")
    dic2[key] = value

for k,v in dic.items():
    print(k + " " + dic2[v]) 

# 回答例2
from collections import OrderedDict
def main():
    n = int(input())
    user_map = OrderedDict()
    for _ in range(n):
        user, blood_type = input().split()
        user_map[user] = blood_type
    m = int(input())
    blood_type_map = OrderedDict()
    for _ in range(m):
        blood, fortune = input().split()
        blood_type_map[blood] = fortune
    for key, value in user_map.items():
        blood_type = blood_type_map.get(str(value))
        print("{} {}".format(key, blood_type))
if __name__ == "__main__":
    main()