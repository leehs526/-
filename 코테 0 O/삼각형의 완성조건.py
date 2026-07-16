1)
def solution(sides):
    if max(sides) < sum(sides) - max(sides):
        return 1
    else:
        return 2

2)
def solution(sides):
    return 1 if max(sides) < sum(sides) - max(sides) else 2
