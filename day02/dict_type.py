import json


adict = {"username":"yansl","password":"123456"}
bdict = {'5':"yansl","password":[2,5]}
cdict_str = '{"username":"yansl","password":[2,5]}'
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
def dict_add1():
    adict['sex'] = '女'
    print(adict)

def dict2str():
    print(type(adict))
    adict_str = json.dumps(adict)
    print(adict_str)
    print(type(adict_str))

def str2dict():
    print(type(cdict_str))
    cdict = json.loads(cdict_str)
    print(cdict)
    print(type(cdict))


if __name__ == '__main__':
    # dict_sel()
    # dict_del()
    # dict_add()
    # dict_add1()
    # dict2str()
    str2dict()
