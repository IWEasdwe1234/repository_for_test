# = = = = = = = = = = = = = = = = = = = =

# 여기에서는 코드를 실행했을 때 어떤 결과가 나오는지 실험

# 실험 이후 주석문으로 변경 ( Ctrl + / )

# = = = = = = = = = = = = = = = = = = = =

# 변수 이름을 한글로 사용하기

# 변수이름 = "변수 값"
# print("\n한글을 사용한 변수 출력\n")
# print(변수이름)

# 물결 = "~"
# 한줄 = "-"
# 두줄 = "= "

# 길이 = int(20)

# print(f"\n{물결*길이}\n")
# print(f"\n{한줄*길이}\n")
# print(f"\n{두줄*길이}\n")

# = = = = = = = = = = = = = = = = = = = =

# a = 30
# b = "20"
# c = "이십"

# # print(a + b) # TypeError: unsupported operand type(s) for +: 'int' and 'str'
# print(a + int(b))  # 50
# print(a + int(c))  # ValueError: invalid literal for int() with base 10: '이십'

# = = = = = = = = = = = = = = = = = = = =

# 과일 = ["사과", "딸기", "포도", "거봉", "복숭아", "자두", "배"]
# 조인 = "/ ".join(과일), "-".join(과일)
# print(조인)

# 과일1차분류 = 과일.copy()  # 원본 리스트 보호
# 과일1차분류.append("수박")  # 임의의 값("수박") 맨 뒤에 추가
# print(과일1차분류)  # 복사된 리스트 수정 확인
# print(과일1차분류.index("수박"))  # 임의의 값 위치 확인
# print(len(과일1차분류))  # 수정한 리스트 길이 확인
# print(f"{len(과일1차분류)} == {과일1차분류.index("수박")+1}")
# # 임의의 값을 맨뒤로 보내고 해당 값의 인덱스 번호 + 1은 전체 길이와 같음
# print(과일)  # 원본 리스트 변화 확인

# = = = = = = = = = = = = = = = = = = = =

# for 단 in range(1, 10):  # 1단 ~ 9단
#     print(f"\n{"= "*5}\n\n{단} 단\n")  # 구분선
#     for 수 in range(1, 10):  # 단과 곱할 숫자 1~9
#         print(f"{단} x {수} = {단 * 수}")

# = = = = = = = = = = = = = = = = = = = =

# 파이썬에서 유튜브 추출

# bash에서 다음 실행
# https://ffmpeg.org/ 미리 설치
# pip install yt-dlp
# import yt_dlp
# 다운로드 옵션 설정
# ydl_opts = {
#     'format': 'bestvideo+bestaudio/best',  # 최고 화질 비디오와 오디오 병합
#     'outtmpl': '%(title)s.%(ext)s',       # 저장할 파일명 (영상 제목.확장자)
# }
# 다운로더 객체 생성 및 실행
# with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#     urls = ['https://youtube.com']
#     ydl.download(urls)

# print("다운로드가 완료되었습니다.")

# -------------

# 오디오 추출을 위한 옵션 설정
# ydl_opts = {
#     # 최상의 오디오 음질을 선택
#     'format': 'bestaudio/best',

#     # 저장할 파일명 설정 (영상 제목.확장자)
#     'outtmpl': '%(title)s.%(ext)s',

#     # 다운로드 후 후처리(변환) 작업 설정
#     'postprocessors': [{
#         'key': 'FFmpegExtractAudio',
#         'preferredcodec': 'mp3',    # mp3 포맷으로 변환
#         'preferredquality': '192',  # 음질 설정 (192kbps 또는 최고음질은 320)
#     }],
# }

# # 다운로드 실행
# with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#     urls = ['https://youtube.com']
#     ydl.download(urls)

# print("MP3 음원 추출이 완료되었습니다.")

# = = = = = = = = = = = = = = = = = = = =
