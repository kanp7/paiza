# このメニューではスタックとキューというデータ構造をそれぞれ実装します。まずは、これらの実装に共通する部分のコードを用意することから始めましょう。
# そのため、各問題で書いたコードは消さずに、そのまま残しておくことをお勧めします( paiza 上にも保存はされています )。

# さて、 N 個の要素からなる数列 A が与えられます。 1 行目に N を、 2 行目以降に A の各要素を改行区切りで出力してください。
# また次の問題のために、与えられた数値は配列に入れ、配列の中に入っている要素数を変数で管理しておくとよいです。


n = int(input())
print(n)

nums = []
for _  in range(n):
    i = int(input())
    nums.append(i)
    print(i)