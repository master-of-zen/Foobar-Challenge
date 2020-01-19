from functools import reduce

# 4/5 tests

def solution(xs):
    output = []
    positive = [x for x in xs if x > 0]
    negative = sorted([x for x in xs if x < 0])
    print(negative)
    print(positive)
    if (len(negative) + len(positive)) == 0:
        return '0'
    if len(negative) % 2 == 0 and len(negative) > 0:
        for i in negative:
            output.append(i)
    elif (len(negative) - 1) != 0 and len(negative) % 2 != 0:
        for i in sorted(negative[:-1]):
            output.append(i)

    for i in positive:
        output.append(i)
    output = reduce(lambda x, y: x*y, output)
    return str(output)
