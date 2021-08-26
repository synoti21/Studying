#binary search
from typing import Any, Sequence

def bin_search(seq: Sequence, key: int) -> int:
    pl = 0
    pr = len(seq)-1

    print('   |', end='')
    for i in range(len(seq)):
        print(f'{i:4}', end='')
    print()
    print('---+' + (4*len(seq)+2)*'-')
    
    while True:
        pc = (pl+pr)//2
    
        print('   |', end='')
        if pl!=pc:
            print((pl*4+1)*' '+'<-'+((pc-pl)*4)*' '+'+',end='')
        else:
            print((pc*4+1)*' '+'<+',end='')
        if pc!=pr:
            print(((pr-pc)*4-2)*' '+'->')
        else:
            print('->')
        print(f'{pc:3}|',end='')
        for i in range(len(seq)):
            print(f'{seq[i]:4}',end='')
        print('\n   |')
        if seq[pc] == key :
            return pc
        elif seq[pc] > key:
            pr = pc-1
        else:
            pl = pc+1
        if pl > pr: #reaching the limit
            break
    return -1

if __name__ == '__main__':
    num = int(input("원소 수를 입력하시오."))
    x = [None] * num
    for i in range(num):
        x[i] = int(input(f'x[{i}] = '))
    ky = int(input("찾고자 하는 원소를 입력하시오"))
    n = bin_search(x, ky)

    if n == -1:
        print('찾고자 하는 원소가 없습니다.')
    else:
        print(f'원소 {ky}는 x[{n}]에 있습니다.')

