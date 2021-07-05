# 2xxx年に paiza が設立した paiza 中央銀行に勤務する pai沢直樹は、故障した ATM の対応として、お金を引き出したい会社と電話をして、会社名が銀行の名簿に登録されており、かつ、会社側が会社の口座の暗証番号を正しく言えた場合にのみ現金を支払い、それを記帳するという業務を任されていました。

# 銀行に登録されている会社名とその口座の暗証番号と残高についての情報、また、直樹の電話の情報が与えられるので、全ての取引が終了した後の全ての会社の残高を出力してください。


n, k = list(map(int,input().split()))

customer_info = {}
for _ in range(n):
    company, password, balance = input().split()
    balance = int(balance)
    customer_info[company] = [password, balance]
# {'A': ['0000', 10000], 'B': ['1234', 23456], 'C': ['5678', 98765]}


for _ in range(k):
    company_c, pin_c, withdrawal = input().split()
    withdrawal = int(withdrawal)
    if company_c in customer_info:
        if customer_info[company_c][0] == pin_c:
            customer_info[company_c][1] -= withdrawal


for key, vals in customer_info.items():
    print(key, vals[1])




# 時間切れ
n, k = list(map(int,input().split()))

customer_info = []
for _ in range(n):
    company, password, balance = input().split()
    balance = int(balance)
    tmp = []
    tmp += [company, password, balance]
    customer_info.append(tmp)

for _ in range(k):
    company_c, pin_c, withdrawal = input().split()
    withdrawal = int(withdrawal)
    for c in customer_info:
        if company_c == c[0] and pin_c == c[1]:
            c[2] -= withdrawal

for c in customer_info:
    print(c[0], c[2])
