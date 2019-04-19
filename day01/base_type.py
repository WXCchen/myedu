# def test1():
#     print('test1')
# def test2():
#     print('test2')
# def test3():
#     print('test3')
# if __name__ == '__main__':
#    test3()
#    test1()
#    test2()



# def int_demo():
#     aint = 5
#     print(aint)
#     print(type(aint))
# if __name__ == '__main__':
#     int_demo()

def str_demo():
    astr = '1223abc'
    print(astr)
    print(type(astr))
def float_demo():
    aflo = 0.123
    print(aflo)
    print(type(aflo))

def add_demo(a,b):
    print(a+b)


def type_zhuanhuan():
    aint = 45
    print(type(str(aint)))
    print (type(int(aint)))

def str_join():
    a = 123
    b = '你好'
    c = 0.47964
    print(str(a)+b+str(c))
    print('%s %s %s'%(a,b,c))

def jianfa_demo(a,b):
    c = a - b
    return c
if __name__ == '__main__':
    # str_demo
    # float_demo()
    # add_demo(465,4545)
    # type_zhuanhuan()
    # str_join()
    c = jianfa_demo(6,2)
    d = add_demo(6,2)
    print(c)
    print(d)
