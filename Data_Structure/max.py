#시퀀스 원소의 최댓값 출력하기

from typing import Any, Sequence

def max_of(a: Sequence) -> Any:
    maximum=a[0]
    for i in range(1,len(a)):
        if a[i] > maximum: maximum=a[i]
    return maximum

if __name__ == '__main__': #이 파일을 직접 실행했을때만 if구문이 실행
    print('배열의 최댓값을 구합니다')
    n=int(input('원소의 갯수를 적으시오'))
    x=[None]*n

    for i in range(n):
        x[i] = int(input(f'x[{i}]값을 입력하세요'))
    print(f'최댓값은 {max_of(x)} 입니다.')

