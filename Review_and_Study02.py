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

print(ln1)
print("==[ 셋 ]==\n")
# set
# 중괄호 { }로 감싼 값의 묶음
# 리스트를 셋으로 감싸면 중복 제거
# 방법 1/
셋1 = {"값1", "값2", "값2", "값1", "값1", "값2", "값1"}
print("셋1 :", 셋1)  # {'값1', '값2'}

# 방법 2/ (실무에서 훨씬 잦음)
리스트 = ["값1", "값2", "값2", "값1", "값1", "값2", "값1"]
셋2 = set(리스트)
print("셋2 :", 셋2)  # {'값1', '값2'}

print(ln1)
print("--[ 빈 셋 만들기 ]--\n")
# 빈 중괄호 {}는 셋이 아니라 딕셔너리
#  빈 셋은 반드시 set()으로 만들기

empty_list = []
print(type(empty_list))  # <class 'list'> 리스트

empty_tuple = ()
print(type(empty_tuple))  # <class 'tuple'> 튜플

empty_set = {}
print(type(empty_set))  # <class 'dict'> 딕셔너리

real_empty_set = set()
print(type(real_empty_set))  # <class 'set'> 셋

print(ln1)
print("--[ .add ]--\n")
A = {"a1", "a2", "a3", "a4"}
print(A)
A.add("a3")  # 이미 존재하는 값 무시
A.add("a5")
print(A)

print(ln1)
print("--[ in ]--\n")
# 값이 셋(또는 리스트, 튜플, 문자열)안에 있으면 True, 없으면 False

A = {"a1", "a2", "a3", "a4"}
print("a3" in A)  # True
print("A3" in A)  # False
print("A5" in A)  # False

# 활용 예
if "a4" in A:
    print("a4 존재")

print(ln1)
print("--[ sorted ]--\n")
# 셋을 정렬 (결과 : 정렬된 리스트)

A = {"a2", "a4", "a1", "a3"}
st_a = sorted(A)
print(st_a)  # ['a1', 'a2', 'a3', 'a4'] ()
print(type(st_a))

# 중복 제거
B = {"a2", "a2", "a1", "a3"}  # a2가 2개
print(sorted(set(B)))  # ['a1', 'a2', 'a3'] (중복된 a2 제거, 정렬)

print(ln1)
print("--[ .union ]--\n")
# 두 셋을 합쳐 중복없는 전체 목록으로 만들기
A = {"a1", "a3", "a4", "a6"}
B = {"a5", "a2", "a4", "a1"}
print(sorted(A.union(B)))
print(sorted(B.union(A)))
print(sorted(A | B))

# 결과 : ['a1', 'a2', 'a3', 'a4', 'a5', 'a6']

print(ln1)
print("--[ .intersection ]--\n")
# 두 셋에 공통으로 들어있는 값만 남기기
print(sorted(A.intersection(B)))
print(sorted(B.intersection(A)))
print(sorted(A & B))

# 결과 : ['a1', 'a4']
