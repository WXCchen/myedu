alist = ['哈','喽','wo','de',1,2,3]
def for_demo():
    for i in range(3):
        print(i)
        print('想放假')
def for_demo1():
    for i in range(3,6):
        print(i)
    for i in range(7,10):
        print(i)
def for_demo2():
    for i in range(3,10,2):
        print(i)
def for_list():
    for i in alist:
        print(i)
# def for_list2():
#     a = len(alist)
#     for i in range(a):
#         print(alist[i])
if __name__ == '__main__':
    # for_list2()
    # for_demo()
    # for_demo1()
    # for_demo2()