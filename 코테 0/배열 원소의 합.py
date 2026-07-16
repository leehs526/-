1)
def solution(strlist):
    answer = []
    for i in strlist:
        answer.append(len(i))
    return answer

2)
def solution(strlist):
    return [len(i) for i in strlist]
  
strlist가 이미 배열로 들어오기때문에 "", 별로 나눠줄 필요 없음
python
strlist = ["hello", "world", "hi"]
이미 "hello", "world", "hi" 로 나눠져서 들어오는 거예요. 우리가 나눌 필요가 없어요!
for i in strlist 하면:
i = "hello"
i = "world"
i = "hi"
이렇게 하나씩 꺼내져요. 그래서 각각 len() 하면 [5, 5, 2] 가 나오는 거예요!
[12] 가 나오려면 strlist = ["helloworldhi"] 이렇게 하나로 붙어서 들어와야 해요.
