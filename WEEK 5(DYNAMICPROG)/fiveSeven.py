def change(amount):
    array = []
    if amount > 24 and amount < 1001:
        for i in range(200):
            for j in range(142):
                if amount == 5 * i + 7 * j:
                    if i != 0:
                        for t in range(i):
                            array.append(5)
                    if j != 0:
                        for k in range(j):
                            array.append(7)
        return array
    else:
        return








