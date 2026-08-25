ln1 = f"\n{"=" * 20}\n"
ln2 = f"\n{"= " * 10}\n"

# [환경 설정] 한글 폰트 설정 및 필수 라이브러리 로드
# macOS, Windows, Linux, Google Colab 환경에 맞춰 한글 깨짐 없이 동작하도록 자동 감지 설정합니다.

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

# --------


plt.plot([1, 2, 3], [10, 20, 15])
plt.show()
