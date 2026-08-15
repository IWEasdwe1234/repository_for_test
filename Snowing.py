# = = = = = = = = = = = = = = = = = = = =

# 실행 방법
# 1. F5 또는 Ctrl + F5
# 2. 우측 위 재생 아이콘
# 3. 전체 선택(Ctrl + A) 후 Shfit + Enter

# 중지 방법
# 실행중인 터미널 종료 (쓰래기통 아이콘 or 마우스 휠버튼)
# 실행중인 터미널 클릭 후 Ctrl + C

# = = = = = = = = = = = = = = = = = = = =

import os
import time
import random

snow = []

while True:
    # 현재 터미널 크기 확인
    width, height = os.get_terminal_size()

    # 새로운 눈 생성
    if random.random() < 0.9:
        for _ in range(5):
            snow.append([random.randint(0, width - 1), 0])

    # 화면 지우기
    os.system("cls")

    # 현재 터미널 크기만큼 빈 화면 만들기
    screen = [[" " for _ in range(width)] for _ in range(height)]

    # 눈을 아래로 이동
    for s in snow:
        s[1] += 1

        # 터미널 화면 안에 있는 눈만 표시
        if s[1] < height and s[0] < width:
            screen[s[1]][s[0]] = "❄️"
            # screen[s[1]][s[0]] = "💧"
            # screen[s[1]][s[0]] = "🩸"
            # screen[s[1]][s[0]] = "⚡"
            # screen[s[1]][s[0]] = "🔥"
            # screen[s[1]][s[0]] = "💮"

    # 화면 출력
    for row in screen:
        print("".join(row))

    # 화면 아래로 떨어진 눈 제거
    snow = [s for s in snow if s[1] < height]

    # 눈이 떨어지는 속도
    time.sleep(0.08)
