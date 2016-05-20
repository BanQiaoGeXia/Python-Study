#coding=utf_-8

'''
    counter是一个闭包函数  调用这个函数时
    他声明他的内部函数  并把这个内部函数以返回值的形式返回
    返回的这个内部函数相当于一个实例化的对象
    他对counter内部变量的操作不会与其他函数冲突
    孤认为十分神奇
'''

def counter(start = 0):     #这是一个闭包函数
    count = [start]         #相当于 counter类  有一个成员变量counter
    def incr():             #有一个incr方法
        count[0] += 1
        return count[0]
    return incr             #返回这个方法

c1 = counter(10)            #此处相当于初始化一个counter对象
c2 = counter(20)

for i in range(5):          #此处是c1对象的操作
    print c1()
print "--I'm beautiful line--"
for i in range(5):          #此处是c2对象的操作
    print c2()          
                            #他们操作的变量互不冲突
