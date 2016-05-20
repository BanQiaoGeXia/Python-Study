#coding=utf-8

'''
   这里说明装饰器函数应用
   这里用四个DEMO 由浅到深说明装饰器的应用
   在函数前面用装饰器函数装饰
   这时会优先执行装饰器函数的功能
   在装饰器内部调用被装饰函数
'''

import time

'''
def timefun(func):          #这就是传说中的装饰器函数
    def wrappendfunc():     #装饰器函数启时声明这个函数
        print "%s called at %s"%(func.__name__,time.ctime())
                            #装饰器内部函数做了很多奇奇怪怪的事情
                            #并在合适的时机调用被装饰函数  并不局限于返回时刻
        return func()       #此demo中  在结束时执行的被装饰函数
    return wrappendfunc     #结束时返回调用内部函数

@timefun                    #装饰器函数正在装饰doIt函数
def doIt():
    print 'fighting for glory !!!!!'

doIt()                      #正常调用 他却已经在不经意间被装饰了
time.sleep(2)
doIt()  
'''

'''
def timefun(func):  
    def wrappedfunc(say):   #在这里我们慷慨的给他参数
        print "%s called at %s"%(func.__name__,time.ctime)  #添加名称时间装饰品
        print 'you have been killed !!'
                        #注意 被装饰函数可以在装饰器内部函数任意位置被执行  并不局限于末尾
        return func(say)#依然在返回时执行被调用函数  
    return wrappedfunc  #继续在声明了内部函数之后反过去执行他

@timefun                #装饰器有开始装饰sayIt函数了
def sayIt(say):         #这次 被装饰函数需要一个参数
    print say

words = "I'm the shadow walker !!!!"

sayIt(words)            #那么～～给他参数！！
time.sleep(2)
sayIt('Ha~~~~~~~~')     #我们尝试赋予不同参数 完美运行！！
'''

'''
def timefun_arg(pre = 'Warning'):   #由于装饰器有参数  在这里多套一层 为了拿到装饰器的参数
    def timefun(func):              #这是第一层 拿到了被装饰函数
        def wrappedfunc(say):       #这是第二层 拿到了被装饰函数的参数
            print "%s called at %s %s"%(func.__name__,time.ctime(),pre)
                                    #我们在最内层 能用到所有外层拿到的参数
            return func(say)        #话不多说  执行被装饰函数
        return wrappedfunc          #拿到了被装饰函数 为了在内二层执行他  
    return timefun                  #拿到装饰器的参数后 执行内部第一层

@timefun_arg('Action!')             #装饰器正在装饰  这次装饰器也要参数   给他！！！
def boom(say):
    print say
                                    #逐层拿取各种参数  在最内层统一应用
boom('Tranformers standing by ！！！')
time.sleep(2)
boom('Super man is already in the position !!!')
#到这里 可能会略显蛋疼 不过不要担心 最后一个更蛋疼
'''

#Don't worry 越蛋疼越神奇
                                    
def logged(when):
    def log(f,*args,**kargs):
        print "fun:%s  args:%r  kargs:%r"%(f,args,kargs)

    def pre_logged(f):
        def wrapper(*args,**kargs):
            log(f,*args,**kargs)
            return f(*args,**kargs)
        return wrapper

    def post_logged(f):
        def wrapper(*args,**kargs):
            now = time.time()
            try:
                return f(*args,**kargs)
            finally:
                log(f,*args,**kargs)
                print "time delta:%s"%(time.time()-now)
        return wrapper
    try:
        return {"pre":pre_logged,"post":post_logged}[when]
    except KeyError,e:
        raise ValueError(e),'must be "pre" or "post"'

@logged("pre")
def fun(name):
    print "BOOM SHAKALAKA ,",name

fun("Bumblebee")
