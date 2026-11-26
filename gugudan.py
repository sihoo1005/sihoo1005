# 입력한 숫자의 구구단을 출력하는 함수
def gugudan(dan):
    for i in range(1, 10):
        print(dan, "x", i, "=", dan * i)


dan = int(input("몇 단을 입력할까요? "))
gugudan(dan)
