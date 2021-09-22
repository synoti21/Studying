from Fixedqueue import FixedQueue
from enum import Enum

Menu = Enum('Menu', ['인큐','디큐','피크','검색','덤프','종료'])

def select_menu() -> Menu:
    s = [f'({m.value}){m.name}'for m in Menu]
    while True:
        print(*s,sep='   ', end = '')
        n = int(input(": "))
        if 1 <= n <= len(Menu):
            return Menu(n)

q =FixedQueue(64)

while True:
    print(f'현재 데이터 개수 : {len(q)} / {q.capacity}')
    menu = select_menu()

    if menu == Menu.인큐:
        x = int(input("입력할 데이터를 입력하세요:"))
        try:
            q.enque(x)
        except FixedQueue.Full:
            print("큐가 가득찼습니다.")
        
    elif menu == Menu.디큐:
        try:
            x = q.deque()
            print(f'디큐한 데이터는 {x}입니다.')
        except FixedQueue.Empty:
            print("큐가 비었습니다.")
    
    elif menu == Menu.피크:
        try:
            x = q.peek()
            print(f'피크한 데이터는 {x} 입니다.')
        except FixedQueue.Empty:
            print("큐가 비었습니다.")
    
    elif menu == Menu.검색:
        x = int(input("검색할 데이터를 입력하세요"))
        if x in q:
            print(f'{q.count(x)}개 포합되고, 맨 앞의 위치는 {q.find(x)}입니다.')
        else:
            print("검색값을 찾을 수 없습니다.")
    
    elif menu == Menu.덤프:
        q.dump()
    
    else:
        break