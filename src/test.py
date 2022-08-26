i = 0


def plus(i):
    def plus_one(i):
        i += 1
        return i
    i = plus_one(i)
    return i


while True:
    i = plus(i)
    print(i)
