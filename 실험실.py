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

a = 30
b = "20"
c = "이십"

# print(a + b) # TypeError: unsupported operand type(s) for +: 'int' and 'str'
print(a + int(b))  # 50
print(a + int(c))  # ValueError: invalid literal for int() with base 10: '이십'
