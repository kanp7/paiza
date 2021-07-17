class Player:
    def __init__(self, hp, f_1, a_1, f_2, a_2, f_3, a_3):
        self.hp = hp
        self.f = [f_1, f_2, f_3]
        self.a = [a_1, a_2, a_3]
        self.alive = True

    def enhance(self):
        for i in range(3):
            if self.f[i] == 0 and self.a[i] == 0:
                continue

            self.f[i] = max(self.f[i]-3, 1)
            self.a[i] += 5

    def calc_hp(self, damage):
        self.hp -= damage

        if self.hp <= 0:
            self.alive = False

    def get_status(self, i):
        return (self.f[i], self.a[i])

    def get_alive(self):
        return self.alive


n, k = [int(x) for x in input().split()]

players = [None] * n
for i in range(n):
    hp, f_1, a_1, f_2, a_2, f_3, a_3 = [int(x) for x in input().split()]
    players[i] = Player(hp, f_1, a_1, f_2, a_2, f_3, a_3)

for _ in range(k):
    values = [int(x) for x in input().split()]

    p_1 = values[0] - 1
    t_1 = values[1] - 1

    p_2 = values[2] - 1
    t_2 = values[3] - 1

    f_1, a_1 = players[p_1].get_status(t_1)
    f_2, a_2 = players[p_2].get_status(t_2)

    # if players[p_1].get_alive() == False or players[p_2].get_alive() == False:
    if not players[p_1].get_alive() or not players[p_2].get_alive():
        continue

    if f_1 == 0 and a_1 == 0 and f_2 == 0 and a_2 == 0:
        players[p_1].enhance()
        players[p_2].enhance()
    elif f_1 == 0 and a_1 == 0:
        players[p_1].enhance()
        players[p_1].calc_hp(a_2)
    elif f_2 == 0 and a_2 == 0:
        players[p_2].enhance()
        players[p_2].calc_hp(a_1)
    else:
        if f_1 > f_2:
            players[p_1].calc_hp(a_2)
        elif f_1 < f_2:
            players[p_2].calc_hp(a_1)
        else:
            pass

ans = 0
for player in players:
    if player.get_alive():
        ans += 1

print(ans)