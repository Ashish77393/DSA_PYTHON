def Swap(a,b):
    print(f'before swap a={a} and b={b}')
    a = a ^ b
    b = a ^ b
    a = a ^ b
    print(f'after swap a={a} and b={b}')
a=10
b=20
Swap(a,b)