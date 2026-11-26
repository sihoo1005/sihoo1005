"""사용자가 입력한 정수의 구구단을 출력합니다."""


def gugudan(dan):
    """dan에 해당하는 구구단을 1부터 9까지 출력합니다."""
    for number in range(1, 10):
        print(f"{dan} x {number} = {dan * number}")


def main():
    while True:
        try:
            dan = int(input("몇 단을 입력할까요? "))
        except ValueError:
            print("정수를 입력해 주세요. 예: 2, 7, 9")
            continue

        print(f"\n[ {dan}단 ]")
        gugudan(dan)
        break


if __name__ == "__main__":
    main()
