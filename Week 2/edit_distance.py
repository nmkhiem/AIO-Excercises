def edit_distance(str1, str2):
    distances = [[0]*(len(str2)+1) for _ in range(len(str1)+1)]

    for t1 in range(len(str1) + 1):
        distances[t1][0] = t1

    for t2 in range(len(str2) + 1):
        distances[0][t2] = t2

    a = 0
    b = 0
    c = 0

    for t1 in range(1, len(str1) + 1):
        for t2 in range(1, len(str2) + 1):
            if (str1[t1-1] == str2[t2-1]):
                distances[t1][t2] = distances[t1 - 1][t2 - 1]
            else:
                a = distances[t1][t2 - 1]
                b = distances[t1 - 1][t2]
                c = distances[t1 - 1][t2 - 1]

                if (a <= b and a <= c):
                    distances[t1][t2] = a + 1
                elif (b <= a and b <= c):
                    distances[t1][t2] = b + 1
                else:
                    distances[t1][t2] = c + 1

    get_distance(distances, len(str1), len(str2))
    return distances[len(str1)][len(str2)]


def get_distance(distances, len1, len2):
    for t1 in range(len1 + 1):
        for t2 in range(len2 + 1):
            print(int(distances[t1][t2]), end=" ")
        print()
