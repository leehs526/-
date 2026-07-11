1)
def solution(my_string, n):
    answer = ""
    for c in my_string:
        answer += c * n
    return answer

2)
def solution(my_string, n):
    return ''.join(i*n for i in my_string)

3)
def solution(my_string, n):
    return "".join(map(lambda x: x*n, my_string))
