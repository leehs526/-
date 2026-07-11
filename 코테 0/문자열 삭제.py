1)
def solution(my_string, letter):
    return my_string.replace(letter,"")
    
2)
def solution(my_string, letter):
    answer = ''
    for string in my_string:
        if string != letter:
            answer += string
    return answer
