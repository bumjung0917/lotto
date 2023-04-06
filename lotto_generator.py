#2023243062 김범중
# 로또번호 추출기 프로젝트
import random

# 로또 추첨기 함수 정의 
def lotto_generator():
    numbers = random.sample(range(1, 46), 6)
    numbers.sort()
    return numbers

answer = input("로또번호추출기를 실행하시겠습니까? (Y/N)");

if answer == "Y" :     
    # 추첨할 로또 장 수 입력
    num_of_lotto = int(input("추첨할 로또 장 수를 입력하세요.: "))

    # 입력한 로또 장 수 만큼 로또 번호 추첨
    for i in range(num_of_lotto):
        print(f"{i+1}번째 로또 번호는 다음과 같습니다.:")
        print(lotto_generator())
    print("로또번호를 성공적으로 뽑았습니다.")

elif answer == "N" :
    print("추출기를 종료하겠습니다.")
    
else :
    print("잘못입력하셨습니다.")
