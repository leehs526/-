def solution(n):
    answer = 0
    for i in range(1,n+1): #range 대신 n을 쓰는건 안됨, n이 정수이기 때문
        if i % 2 == 0:
            answer += i
    return answer