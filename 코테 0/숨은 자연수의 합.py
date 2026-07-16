1)
def solution(my_string):
    answer = 0
    for i in my_string:
        if i.isdigit(): #isdigit 숫자인지 확인하는 함수, ()은 함수호출
            answer += int(i)
    return answer

2)
def solution(my_string):
    return sum(int(i) for i in my_string if i.isdigit())
