#balance : 초기 잔액을 설정하는 변수를 초기화 해주세요
# 금액은 여러분 마음대로

balance = 10000

while True:
    num = input("ddd (1.입금, 2.출금, 3.영수증 보기, 4.종료) : ")

    if num == '4': # 4번 종료
        break # 종료

    if num == '1': # 입금 기능 구현 -> feat/deposit 브랜치에서 작업
        deposit_amount = int(input('입금할 금액을 입력해 주세요: ')) # str:5000 -> int() -> int:5000
        balance += deposit_amount # blance(15,000) = blance(10000) + deposit_amount(5000)
        print(f'입금하신 금액은 {deposit_amount}원이고, 현재 잔액은 {balance}원 입니다.')
    
    
    if num == '2': # 
        pass
    
    if num == '3':
        pass
# 코드는 위에서부터 아래로 실행



print(f'서비스를 종료합니다. 현재 잔액은 {balance}원 입니다.')
