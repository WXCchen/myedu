class human (object):
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex
    def eatlunch(self):
        print('%s吃饭'%self.name)
    def sleep(self):
        print('%s睡觉'%self.name)

class Tester (human):
    def work(self):
        print('%s在测试'%self.name)
        self.eatlunch()
        self.sleep()


if __name__ == '__main__':
    # Human = human('Mary',20,'女')
    # Human.eatlunch()
    # Human.sleep()
    tester = Tester('Mary', 20, '女')
    tester.work()