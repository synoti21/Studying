from fixed_stack import FixedStack
from enum import Enum

Menu = Enum('Menu',['푸시','팝','피크','검색','덤프','종료'])

def select_menu() -> Menu:
    s = [f'({m.value}){m.name}' for m in Menu]
    while True:
        print(*s, sep='  ', end = '')
        n = int(input(': '))
        if 1 <= n <= len(Menu):
            return Menu(n)

s = FixedStack(64)
while True:
    print(f'현재 데이터 개수 : {len(s)} / {s.capacity}')
    menu = select_menu()

    if menu == Menu.푸시:
        value = input("데이터를 입력하세요 : ")
        try:
            s.push(value)
        except FixedStack.Full:
            print("스택이 가득 차 있습니다.")

    elif menu == Menu.팝:
        try:
            value = s.pop()
            print(f'팝한 데이터는 {value}입니다.')
        except FixedStack.Empty:
            print("스택이 비어있습니다")

    elif menu == Menu.피크:
        try:
            value = s.peek()
            print(f'피크한 데이터는 {value}입니다')
        except FixedStack.Empty:
            print("스택이 비어있습니다.")
    
    elif menu == Menu.검색:
        value = input("검색할 데이터를 입력하세요")
        if value in s:
            print(f'{s.count(value)}개 포함되고, 맨 앞의 위치는 {s.find(value)}입니다.')
        else:
            print("찾는 데이터가 없습니다")

    elif menu == Menu.덤프:
        s.dump()

    else:
        break
            
        
        