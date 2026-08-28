import platform
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import pandas as pd
import numpy as np

try:
    import seaborn as sns
except ImportError:
    pass

# 운영체제(OS)별 한글 폰트 자동 설정
system_name = platform.system()
if system_name == "Darwin":  # macOS
    plt.rcParams["font.family"] = "AppleGothic"
    plt.rcParams["font.sans-serif"] = [
        "AppleGothic",
        "Apple SD Gothic Neo",
        "NanumGothic",
        "DejaVu Sans",
    ]
elif system_name == "Windows":  # Windows
    plt.rcParams["font.family"] = "Malgun Gothic"
    plt.rcParams["font.sans-serif"] = ["Malgun Gothic", "NanumGothic", "DejaVu Sans"]
else:  # Linux / Google Colab
    try:
        nanum_fonts = [f.name for f in fm.fontManager.ttflist if "Nanum" in f.name]
        if nanum_fonts:
            plt.rcParams["font.family"] = nanum_fonts[0]
        else:
            import subprocess

            subprocess.run(
                ["apt-get", "install", "-y", "fonts-nanum"],
                check=False,
                stdout=subprocess.DEVNULL,
            )
            fm.fontManager.addfont("/usr/share/fonts/truetype/nanum/NanumGothic.ttf")
            plt.rcParams["font.family"] = "NanumGothic"
    except Exception:
        pass
    plt.rcParams["font.sans-serif"] = ["NanumGothic", "DejaVu Sans"]

# 마이너스 기호 깨짐 방지 및 Seaborn 폰트 동기화
plt.rcParams["axes.unicode_minus"] = False
try:
    if "sns" in locals():
        sns.set_theme(style="whitegrid", font=plt.rcParams["font.family"])
except Exception:
    pass

print(f'✅ 환경 설정 완료! 현재 적용된 폰트: {plt.rcParams["font.family"]}')


# ------------------------------------------------------------------------------

# 실습 1. 막대 그래프 직접 그리기

# 목표

# 범주별 값을 막대로 비교하고 색·방향을 바꿔 강조

# 단계
# groupby로 설비별 평균 온도를 구해 막대로 그리기
# 색 리스트로 가장 뜨거운 설비만 강조하고 너비 조절
# barh로 가로 막대로 바꾸고 제목·축 이름 붙이기

# 예상 결과
# 설비별 평균 온도 막대(C호기 최고), 색·가로 변형

df = pd.read_csv("zip/17_열처리.csv")

avg = df.groupby("배치")["온도"].mean()
print(avg.head())

plt.figure(figsize=(8, 4))
plt.bar(avg.index, avg.values, color=["#8c8c8c", "#8c8c8c", "#d00000"], width=0.4)

plt.title("배치별 평균온도")
plt.ylabel("온도")
plt.show()

plt.figure(figsize=(8, 4))
plt.barh(avg.index, avg.values, color=["#8c8c8c", "#8c8c8c", "#d00000"], height=0.4)

plt.title("배치별 평균온도")
plt.ylabel("온도")
plt.show()

# ------------------------------------------------------------------------------

# 실습 2. 범주별 집계 막대 그래프

# 개수·평균을 집계해 범주별로 막대 비교

# 목표
# value_counts·groupby로 집계한 값을 막대로 비교

# 단계
# 상태 열의 개수를 세어 막대로 그리기
# 구역으로 그룹을 나눠 평균 진동을 막대로 그리기
# 제목·축 이름을 붙여 완성

# 예상 결과
# 상태 정상 17·점검 4, 구역별 평균 진동 비교

status = df["상태"].value_counts()
print(status.head())
plt.figure(figsize=(8, 4))
plt.bar(status.index, status.values, color=["#8c8c8c", "#f00a0a"], width=0.6)
plt.title("상태별 개수")
plt.ylabel("개수")
plt.show()


sections = df.groupby("배치")["OP값"].mean()
print(sections.head())

plt.figure(figsize=(8, 4))
plt.bar(
    sections.index, sections.values, color=["#ffacac", "#8c8c8c", "#8c8c8c"], width=0.5
)
plt.title("구역별 평균 진동")
plt.ylabel("진동")
plt.show()

# ------------------------------------------------------------------------------

# 실습 3. 히스토그램 직접 그리기

# 온도 분포를 히스토그램으로, bins로 구간 조절

# 목표
# 숫자 분포를 히스토그램으로 그리고 bins로 구간 조절

# 단계
# 온도 열을 hist로 그려 자동 구간 분포 확인
# bins를 작게·크게 바꿔 구간 수에 따른 모양 비교
# 제목·축 이름을 붙여 완성

# 예상 결과
# 온도 구간별 개수 분포, bins 5·20의 모양 차이

plt.figure(figsize=(8, 4))
plt.hist(df["온도"], bins=4)
plt.xlabel("온도")
plt.ylabel("설비수")
plt.show()

plt.figure(figsize=(8, 4))
plt.hist(df["온도"], bins=44)
plt.xlabel("온도")
plt.ylabel("설비수")
plt.show()

# ------------------------------------------------------------------------------

# 실습 4. 센서값 분포 히스토그램

# 분포를 그리고 평균·표준편차·이상 설비로 해석

# 목표
# 분포를 그리고 평균·표준편차와 이상 설비로 해석

# 단계
# 온도 분포를 히스토그램으로 그리기
# 평균과 표준편차를 구해 분포의 중심·퍼짐과 비교
# 조건 필터링으로 정상 범위를 벗어난 설비 수 확인

# 예상 결과
# 온도 평균 70.0·표준편차 5.6, 78 이상 설비 2대

print(df["온도"].mean())
print(df["온도"].std())

hight = df[df["온도"] >= 862]
print(len(hight))

plt.figure(figsize=(8, 4))
plt.hist(df["온도"], bins=8)
plt.xlabel("온도")
plt.ylabel("설비수")
plt.show()

# ------------------------------------------------------------------------------

# 실습 5. 산점도로 센서 간 관계 분석

# 온도-진동 산점도에 상태별 색·기준선 추가

# 목표
# 두 변수 산점도에 상태별 색과 임계 기준선 추가 단계

# 온도와 진동을 산점도로 찍어 관계 확인
# 상태를 색으로 매핑해 점검·정상을 색으로 구분
# axhline으로 진동 임계 기준선 그리기

# 예상 결과
# 온도↑ 진동↑ 양의 관계, 상태별 색·기준선 표시

plt.figure(figsize=(8, 4))

colors = df["상태"].map({"정상": "#00f0f0", "승온": "#cc0000"})
plt.scatter(df["온도"], df["OP값"], color=colors, alpha=0.4)

plt.axhline(y=90.0, color="#ff0000", linestyle="--")  # 기준선
plt.xlabel("온도")
plt.ylabel("진동")
plt.show()

# ------------------------------------------------------------------------------

# 실습 6.
# 앞서 온도와 OP값(소음) 산포도를 참고해 온도와 CP값(진동) 산포도도 만들고 관계를 분석 판단해보세요.

import matplotlib.pyplot as plt
import pandas as pd

plt.figure(figsize=(8, 4))

colors = df["상태"].map({"정상": "#00f0f0", "승온": "#cc0000"})

plt.scatter(df["온도"], df["CP값"], color=colors, alpha=0.4)

plt.xlabel("온도")
plt.ylabel("진동")
plt.title("온도와 CP값(진동) 산점도")
plt.show()

# ------------------------------------------------------------------------------

# 실습 7.
# zip/17_열처리_공정.csv

# 전체 shape 확인
# 결측이 얼마 있는지 확인
# 결측을 평균값으로 메꾸기

from numpy._core import numeric

df_wide = pd.read_csv("zip/17_열처리_공정.csv")
print(df_wide.shape)
print(df_wide.isna().sum().sum())
df_wide2 = df_wide.fillna(df_wide.mean(numeric_only=True))
print(df_wide2.isna().sum().sum())

# ------------------------------------------------------------------------------

# 실습 8. 시각화 리포트 완성과 저장

# 분포·범주·관계를 2×2 한 화면에 모아 저장

# 목표
# 분포·범주·관계 그래프를 2×2로 모아 리포트로 저장

# 단계
# figure와 subplot으로 2×2 칸을 만들기
# 각 칸에 분포·범주·관계·판정 그래프를 그리고 제목 달기
# tight_layout으로 정리하고 이미지 파일로 저장

# 예상 결과
# 센서 분포·라인 개수·관계·판정을 담은 2×2 리포트 저장

plt.figure(figsize=(12, 12))
plt.suptitle("종합 리포트")

plt.subplot(2, 2, 1)
plt.plot([1, 2, 3, 4, 5], [10, 25, 20, 40, 30])
plt.title("선그래프")

plt.subplot(2, 2, 2)
plt.bar([1, 2, 3, 4, 5], [10, 25, 20, 40, 30])
plt.title("막대그래프")

plt.subplot(2, 2, 3)
plt.hist([10, 25, 20, 40, 30])
plt.title("히스토그램")

plt.subplot(2, 2, 4)
plt.scatter([1, 2, 3, 4, 5], [10, 25, 20, 40, 30])
plt.title("산포도")

plt.show()

# ------------------------------------------------------------------------------
