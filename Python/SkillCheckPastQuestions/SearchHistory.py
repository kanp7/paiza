n = int(input())
words = []
for _ in range(n):
    word = input()
    if word in words:
        words.remove(word)
        words.insert(0, word)
    else:
        words.insert(0, word)

for ans in words:
    print(ans)