#linear search , using sentinel

from typing import Any, Sequence
import copy

def lin_search(seq: Sequence, key: Any) -> int:
    a = copy.deepcopy(seq)
    a.append(key)
    i=0
    while True:
        if a[i] == key:
           break
        i+=1
    return -1 if i == len(seq) else i

if __name__ == '__main__':
    num = int(input("원소수를 입력하시오"))
    x = [None]*num
    for i in range(num):
        x[i] = int(input(f'x[{i}] = '))
    keys = int(input("찾고자 하는 원소를 입력하시오"))
    n = lin_search(x,keys)
    if n == -1:
        print("찾고자 하는 원소가 없습니다")
    else:
        print(f'원소 {keys}은 x[{n}]에 있습니다')
    
        
           
