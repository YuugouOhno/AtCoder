m = int(input())
m_list = []
for i in range(m):
    x,y = map(int,input().split())
    m_list.append((x,y))

n = int(input())
n_list = []
for i in range(n):
    x,y = map(int,input().split())
    n_list.append((x,y))

def get_d(origin, target):
    return (target[0] - origin[0], target[1] - origin[1])
    
def create_relation_map(star_list):
    relation_map = []
    for i in range(1,len(star_list)):
        relation = get_d(star_list[0],star_list[i])
        relation_map.append(relation)
    return relation_map

horoscope_pos = create_relation_map(m_list)

print(horoscope_pos)

def is_in_list(value, target_list):
    return value in target_list

for index, n_pos in enumerate(n_list):
    star_n = 0
    for distance in horoscope_pos:
        if is_in_list((n_pos[0] + distance[0], n_pos[1] + distance[1]), n_list):
            star_n += 1
            print(star_n)
        else:
            break
    if star_n == m-1:
        print(n_list[index][0] - m_list[index][0], n_list[index][1] - m_list[index][1])
        break










