# 1 行目に整数 N が与えられます。
# N 番目までのフィボナッチ数を出力してください。

# フィボナッチ数は

# F_0 = 0
# F_1 = 1
# F_(n+2) = F_n + F_(n+1) (n は 0 以上)

# とし、F_0 を 1 番目とします。

n = int(input())

numbers = []
for i in range(n):
    if i == 0:
        print(i)
        numbers.append(i)
    elif i == 1:
        print(i)
        numbers.append(i)
    else:
        print(numbers[i-2] + numbers[i-1])
        numbers.append(numbers[i-2] + numbers[i-1])
        