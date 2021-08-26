#reversing the elements of list

from typing import Any, MutableSequence

def reverse_array(a: MutableSequence) -> None:
    n = len(a)
    for i in range(n // 2):
        a[i], a[n-i-1] = a[n-i-1], a[i]
        
        


if __name__ == '__main__':  

    n = int(input('Type the number of elements : '))
    x = [None]*n
    for i in range(n):
        x[i] = int(input(f'Type the element of x[{i}] : '))

    print("Reversing the array")

    reverse_array(x)

    for i in range(n):
        print(f'x[{i}] = {x[i]}')
    
