import queue
import threading
import time


# 同步锁
class MyThread(threading.Thread):
    # 必须保证使用公共的lock对象（成员变量）
    # threading.Lock().acquire()
    # threading.Lock().release()
    # 以上的写法会报错  release unlocked lock （释放了没有锁定的锁对象）
    threadLock = threading.Lock()

    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print("开启线程： " + self.name)
        # 获取锁，用于线程同步
        self.threadLock.acquire()  # 当正确使用了锁对象后 ，程序结果 ：先把线程1 的结果全部打印  再打印线程2的
        self.print_time(self.name, self.counter, 3)
        # 释放锁，开启下一个线程
        self.threadLock.release()

    def print_time(self, threadName, delay, counter):
        while counter:
            time.sleep(delay)
            print("%s: %s" % (threadName, counter))
            counter -= 1


# FIFO（先入先出)队列Queue（队列都是基于同步实现的）
# LIFO（后入先出）队列LifoQueue
# 优先级队列 PriorityQueue。
class MyQueue(threading.Thread):
    # 声明队列长度
    # workQueue = queue.Queue(10)
    # workQueue = queue.LifoQueue(10)
    workQueue = queue.PriorityQueue(10)
    # 公共锁
    queueLock = threading.Lock()
    printLock = threading.Lock()
    counter = 5
    def __init__(self, threadName):
        threading.Thread.__init__(self)
        self.threadName = threadName

    def run(self):
        print("开启线程%s" % (self.threadName))
        self.print_thread_in_queue(self.threadName)
        print("关闭线程%s" % (self.threadName))

    def print_thread_in_queue(self ,name):
        while self.counter:
            self.queueLock.acquire()
            if not self.workQueue.empty():
                data = self.workQueue.get()
                self.queueLock.release()
                print("%s 执行 %s" % (name, data))
            else:
                self.queueLock.release()
            self.counter -=1
            time.sleep(2)

if __name__ == '__main__':
    # 同步锁test
    # thread1 = MyThread(1, "Thread-1", 1)
    # thread2 = MyThread(2, "Thread-2", 1)
    # # 开启新线程
    # thread1.start()
    # thread2.start()
    # threads = []
    # # 添加线程到线程列表
    # threads.append(thread1)
    # threads.append(thread2)
    # # 等待所有线程完成
    # for t in threads:
    #     t.join()
    # print("退出主线程")
    # queue测试
    threads = []
    nameList = ["One", "Two", "Three", "Four", "Five"]
    # 公共队列
    # 线程名列表
    ThreadList = ["thread-01", "thread-02", "thread-03"]
    # for word in nameList:
    #     MyQueue.workQueue.put(word)
    # 源码详解http://blog.csdn.net/liu2012huan/article/details/53264162
    MyQueue.workQueue._put((2,"One"))
    MyQueue.workQueue._put((4,"Two"))
    MyQueue.workQueue._put((5,"Three"))
    MyQueue.workQueue._put((1,"Four"))
    MyQueue.workQueue._put((3,"Five"))
    for name in ThreadList:
        myqueue = MyQueue(name)
        myqueue.start()
        threads.append(myqueue)
    for td in threads:
        td.join()
    print("全部退出")

