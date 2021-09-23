from fixed_stack import FixedStack

'''def rec(n : int) -> int:
    if n > 0 :
        rec(n - 1)
        print(n)
        rec(n - 2)'''

'''def rec(n : int ) -> int:   #replaced tail recursion
    while n > 0:
        rec(n-1) # can't replace n = n-1 (needs to temporaily save n to print(n))
        print(n)
        n = n-2  # rec(n-2) => update n to n-2 and go to start point'''


def rec(n : int) -> int:
    s = FixedStack(n)
    while True:
        if n > 0 :
            s.push(n)
            n = n-1
            continue
        if not s.is_empty():
            n = s.pop()
            print(n)
            n = n-2
            continue
        break


x = int(input("x : "))
rec(x)


