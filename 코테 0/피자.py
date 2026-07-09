피자를 7조각으로 나누어준다. 한사람당 한조각 이상을 먹으려면?
def solution(n):
    if n%7==0:
        return n//7
    else:
        return n//7+1

피자 조각수 임의 slice, 사람 수 임의 n
def solution(slice, n):
    if n % slice == 0:
        return n // slice
    else:
        return n // slice + 1

피자를 여섯 조각으로 잘라줌 n명이 모두 같은 수의 피자 조각을 먹어야 한다면 최소 몇 판을 시켜야 하는지
1)
def solution(n):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    lcm = 6 * n // gcd(6, n)
    return lcm // 6
2)
import math

def solution(n):
    return (n * 6) // math.gcd(n, 6) // 6
