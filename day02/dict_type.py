adict = {"username":"yansl","password":"123456"}
bdict = {'5':"yansl","password":[2,5]}

def dict_sel():
    print(adict['username'])
    print(bdict['5'])
    b = bdict['password']
    print(b)
def dict_del():
    adict.pop('password')
    print(adict)
def dict_add():
    adict.update(bdict)
    print(adict)
    cdict = dict(adict,**bdict)
    print(cdict)


if __name__ == '__main__':
    # dict_sel()
    # dict_del()
    dict_add()