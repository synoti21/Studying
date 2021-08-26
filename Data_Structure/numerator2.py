def card_conv(x:int, r:int) ->str:
    d=''
    dchar = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    n = len(str(x))
    print(f'{r:2} | {x:{n}}')
    
    while x>0:
        print('   +' + (n+2)*'-')
        d+= dchar[x%r]
        x//=r

    return d[::-1]

if __name__ == '__main__':

    num = int(input("변환할 값을 입력하시오"))
    conv_num = int(input("어떤 n지수로 변환하시겠습니까?"))

    
    
