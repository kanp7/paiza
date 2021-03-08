# 整数Nが与えられます。 Nが 3 で割り切れる場合はFizz、Nが 5 で割り切れる場合はBuzz、 Nが 3 と 5 の両方で割り切れる場合はFizzやBuzzの代わりにFizzBuzzを出力してください。ただし、Nが 3 の倍数でも 5 の倍数でもないときはNをそのまま出力してください。

n = int(input())

if n % 15 == 0:
  print("FizzBuzz")
elif n % 3 == 0:
  print("Fizz")
elif n % 5 == 0:
  print("Buzz")
else:
  print(n)
