#mutable Sequence 역순으로 정렬 (변경 가능한 정렬)

from typing import Any, MutableSequence

def reverse_array(a: MutableSequence) -> None:
    n = len(a)
    for i in range(n//2):
        a[i], a[n-i-1] = a[n-i-1], a[i]


if __name__ == '__main__':
    print('배열 함수를 역순으로 정렬')
    nx = int(input('원소수를 입력'))
    x = [None]*nx
    for i in range(nx):
        x[i] = int(input(f'x[{i}]의 원소를 입력'))

    print("원래의 x")
    for i in range(nx):
        print(f'x[{i}] = {x[i]}')
    reverse_array(x)
    print('역순 정렬')

    for i in range(nx):
        print(f'x[{i}] = {x[i]}')

    
        
    
