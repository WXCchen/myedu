import os
pwd = os.getcwd()

if __name__ == '__main__':
    print(pwd)

    b = os.path.abspath('..')
    print(b)
    
    os.path.abspath('../..')
    print(c)
