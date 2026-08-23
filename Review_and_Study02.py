ln1 = f"\n{"=" * 20}\n"
ln2 = f"\n{"= " * 10}\n"
# 튜플
# 소괄호 안에 값을 쉼표로 구분해 묶으면 튜플이 만들어진다
# 튜플은 값을 바꿀 수 없다
# 리스트처럼 append·remove·sort 같은 수정용 메서드가 아예 없다
# 튜플이 가진 메서드는 딱 두 개, count와 index뿐
# 내장 함수 len을 더한 셋이 튜플을 다루는 도구 전부
#  "몇 개인가 · 몇 번 나왔나 · 어디에 있나"라는 세 가지 질문을 모두 답할 수 있다.

print(ln1)
(78)  # 그냥 숫자
(78,)  # 튜플
print("\n==[ 튜플 ]==\n")
status = ("정상", "정상", "경고", "정상")
print(f"{len(status)} ← len\n")
print(f"{status.count("정상")} ← count\n")
print(f"{status.index("경고")} ← index\n")

print(ln2)
# 튜플 리스트, 언패킹
# 리스트의 각 요소가 튜플인 구조
튜플in리스트 = [
    ("값1, 1"),
    ("값2, 2"),
    ("값3, 3"),
    ("값4, 4"),
]
print("--[ 리스트 안의 튜플 ]--\n")
print(f"{len(튜플in리스트)}\n")
print(f"{튜플in리스트[0]}\n")
print(f"{튜플in리스트[0][1]}\n")
# 튜플에서 마지막값 뒤에 쉼표를 넣어도 에러가 발생하지 않음

print(ln1)
print("--[ 튜플 리스트 정렬 ]--\n")
# 튜플 리스트 정렬
# sorted
sensors = [(78, "모터온도"), (95, "베어링진동"), (32, "펌프압력")]
a = sorted(sensors)  # (작은 값 → 큰값)
b = sorted(sensors, reverse=False)  # (작은 값 → 큰값)
c = sorted(sensors, reverse=True)  # (큰값 → 작은 값)
print(f"sorted(sensors)\n{a}")
print(f"sorted(sensors, reverse=False)\n{b}")
print(f"sorted(sensors, reverse=True)\n{c}")
# a와 b의 결과값이 같음(작은 값 → 큰값)

print(ln2)
print(f"가장 큰 값\n{c[0]}")

print(ln2)
print("--[ 튜플 언패킹 ]--\n")

리스트 = [
    ("이름1", 30),
    ("이름2", 20),
    ("이름3", 40),
    ("이름4", 10),
]
for 이름, 값 in 리스트:
    기준값 = 30
    if 값 > 기준값:
        print(이름, "기준값 초과")
