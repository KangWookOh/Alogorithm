import re

def solution(files):
    # 1. 파일 이름을 머리, 번호, 꼬리 부분으로 나누는 함수
    def split_filename(filename):
        # 정규 표현식을 사용해 파일 이름 나누기
        match = re.match(r'([a-zA-Z-\s.]+)(\d{1,5})(.*)', filename)
        return match.groups()

    # 2. 파일 이름을 정렬하는 함수
    def sort_key(filename):
        head, number, tail = split_filename(filename)
        return (head.lower(), int(number))

    # 3. 파일 목록 정렬하기
    return sorted(files, key=sort_key)

# 테스트
files = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
result = solution(files)
print(result)