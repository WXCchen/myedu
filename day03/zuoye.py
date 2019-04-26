#计算1到50之间的奇数和
def jishu_add():
    sum = 0
    for i in range(1,51):
        if i % 2 == 1:
            sum = sum+i
    print(sum)

#写for循环打印九九乘法表
def chenfabiao():
    for i in range(1,10):
        for j in range(1,i+1):
            print('%s * %s = %s'%(j,i,j*i),end='   ')
        print('')

#输入两个数求这两个数之间的偶数和
def oushu_add(a,b):
    sum = 0
    if a<b:
        for i in range(a,b):
            if i %2 ==0:
                sum = sum+i
    elif a>b:
        for i in range(b,a):
            if i %2 ==0:
                sum = sum+i
    else:
        print('a和b相等')
    print(sum)


if __name__ == '__main__':
    # jishu_add()
    chenfabiao()
    # oushu_add(1,20)