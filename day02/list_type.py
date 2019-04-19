def list_sel(a):
    print(a[2])
    print(a[1:3])
    print(a[4:7])
def list_del():
    alist  = ['a', 7, 'hello', '8', 'fyfy', '你好']
    alist.pop()
    print(alist)
    alist.pop(0)
    print(alist)

    blist = alist[:-3]
    print(blist)

    alist.append('4564')

def list_update():
    alist = ['a', 7, 'hello', '8', 'fyfy', '你好']
    alist[0] = 5
    print(alist)


if __name__ == '__main__':
    alist = ['a',7,'hello','8','fyfy','你好']
    # list_sel(alist)
    # list_del()
    # list_update()
    print(len(alist))
