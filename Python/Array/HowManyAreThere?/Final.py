# 1 行目に整数 N, M が与えられます。
# 2 行目に M 個の整数 a_1, a_2, ..., a_M が与えられます。
# M 個の整数に N が何個あるか数え、出力してください。
# また、N は M 個の整数の中に 1 個以上含まれるものとします。

n,m = map(int,input().split())
numbers = map(int,input().split())

count = 0
for num in numbers:
    if n == num:
        count += 1

print(count)

# またはcountで出現回数を数えることができるがstr型でないと使えない
n,m = map(int,input().split())
numbers = input().split()

print(numbers.count(str(n)))