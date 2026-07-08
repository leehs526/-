피자를 7조각으로 나누어준다. 한사람당 한조각 이상을 먹으려면?
def solution(n):
    if n%7==0:
        return n//7
    else:
        return n//7+1
