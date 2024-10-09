def max_meeting_attendees(meetings):
    # 시작 시간을 기준으로 회의 정렬
    meetings.sort(key=lambda x: x[0])
    n = len(meetings)

    # dp[i]는 i번째 회의까지 고려했을 때의 최대 인원
    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        # 현재 회의를 선택하지 않는 경우
        dp[i] = dp[i-1]

        # 현재 회의와 겹치지 않는 이전 회의 찾기
        j = i - 1
        while j > 0 and meetings[j-1][1] > meetings[i-1][0]:
            j -= 1

        # 현재 회의를 선택하는 경우
        dp[i] = max(dp[i], dp[j] + meetings[i-1][2])

    return dp[n]

# 입력 처리
n = int(input())
meetings = []
for _ in range(n):
    start, end, attendees = map(int, input().split())
    meetings.append((start, end, attendees))

# 결과 출력
print(max_meeting_attendees(meetings))