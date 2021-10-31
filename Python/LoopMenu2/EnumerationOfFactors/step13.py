# N 個の整数 a_1, a_2, ..., a_N が与えられます。
# a_1, a_2, ..., a_N のうち、1 がある位置を先頭から順に改行区切りで出力してください。
# a_1 を 1 番目とし、a_1, a_2, ..., a_N には少なくとも 1 個は 1 が含まれます。


n = int(input())
nums = list(map(int,input().split()))

index = 0
for i in nums:
    index += 1
    if i == 1:
        print(index)