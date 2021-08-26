from max import*

n=int(input('원소수를 입력하시오.'))

x=[None]*n

for i in range(n):
    x[i]=int(input(f'x[{i}]의 원소를 입력하세요.'))

print(f'x의 최댓값은 {max_of(x)}입니다.')
