#balance : 초기 잔액을 설정하는 변수를 초기화 해주세요
# 금액은 여러분 마음대로

balance = 10000
# 초기화는 맨 위에 미리만들기, 특정값이나 빈값을 입력
receipts = []

while True:
    num = input("사용하실 기능의 번호를 선택해주세요 (1.입금, 2.출금, 3.영수증 보기, 4.종료) : ")

    if num == '4': # 4번 종료
        break # 종료

    if num == '1': # 입금 기능 구현 -> feat/deposit 브랜치에서 작업
        deposit_amount = int(input('입금할 금액을 입력해주세요: ')) # str:5000 -> int() -> int:5000
        balance += deposit_amount # blance(15,000) = blance(10000) + deposit_amount(5000)
        # 입금 계산 후 영수증 자리 출력 전, 후
        print(f'입금하신 금액은 {deposit_amount}원이고, 현재 잔액은 {balance}원 입니다.')
        # 입금 계산 후 영수증 자리 출력 전, 후
        # 보안 -> '입금', deposit_amount -> 튜플로 만들기
        receipts.append(('입금', deposit_amount, balance))


    
    if num == '2': # 
        withdraw_amount = int(input('출금할 금액을 입력해주세요: '))
        withdraw_amount = min(balance, withdraw_amount)
        balance -= withdraw_amount
        print(f'출금하신 금액은 {withdraw_amount}원이고, 현재 잔액은 {balance}원 입니다.')
        receipts.append(('출금', withdraw_amount, balance))


    if num == '3':
        if receipts:
            for i in receipts:
                print(f"{i[0]}: {i[1]}원 | 잔액: {i[2]}")
        else:
            print(f"영수증 내역이 없습니다.")


# 코드는 위에서부터 아래로 실행



print(f'서비스를 종료합니다. 현재 잔액은 {balance}원 입니다.')
