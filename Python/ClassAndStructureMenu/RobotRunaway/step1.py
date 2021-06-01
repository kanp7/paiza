# 洞窟を探検していたあなたは出口のない迷路に迷い込んでしまいました。
# 脱出するには、迷路の地点を与えられた指示通りに移動し、移動で訪れた（移動の開始・終了地点を含む）地点に置かれたアルファベットを
# つなげた文字列を呪文として唱える必要があります。
# 各頂点からは、他の頂点に向かって一方通行の 2 つの道が伸びています。
# 各ポイントの情報と移動の指示が与えられるので、呪文となる文字列を出力してください。


class Location:
    def __init__(self, index, alp, road1, road2):
        self.index = index
        self.alp = alp
        self.road1 = road1
        self.road2 = road2
        

num_of_spot , num_of_move, initial_location = list(map(int,input().split()))

locations = []
for i in range(num_of_spot):
    alp, road1, road2 = input().split()
    location = Location(i+1, alp, road1, road2)
    locations.append(location)

# for l in locations:
#     print(l.__dict__.values())
# dict_values([1, 'p', '2', '4'])
# dict_values([2, 'a', '3', '1'])
# dict_values([3, 'i', '4', '2'])
# dict_values([4, 'z', '1', '2'])

spell = []
for i in range(num_of_move):
    road = int(input())
    if i == 0:
        next_idx = int(locations[initial_location-1].index)
        spell.append(locations[initial_location-1].alp)
    if road == 1:
        next_idx = int(locations[next_idx-1].road1)
        spell.append(locations[next_idx-1].alp)
    elif road == 2:
        next_idx = int(locations[next_idx-1].road2)
        spell.append(locations[next_idx-1].alp)
print(''.join(spell))