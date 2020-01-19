def solution(xs):
    positive = [x for x in xs if 1000 > x > 0]
    negative = sorted([x for x in xs if x < 0])

    output = 1

    if len(xs) == 1:
        return str(xs[0])

    if len(xs) - (len(positive) + len(negative)) == 0:
        return '0'

    if len(negative) % 2 == 1:
        negative = negative[:-1]

    for i in negative:
        output *= i
    for i in positive:
        output *= i

    return str(output)
