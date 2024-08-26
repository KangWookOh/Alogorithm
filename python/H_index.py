def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    for num,citations in enumerate(citations):
        if citations >= num+1:
            answer = num+1
    return answer