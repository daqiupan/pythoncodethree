from time import ctime,sleep
class Demo:
    def music(self,music):
        for i in range(3):
            print('i was listening to%s.%s'%(music,ctime()))
            sleep(1)
    def movie(self,movie):
        for i in range(3):
            print('i was at the %s!%s'%(movie,ctime()))
            sleep(5)
print()
if __name__=='__main__':
    d=Demo()
    d.music('演员  ')
    d.movie('大邱叔叔世界6  ')
    print('结束时间 %s'%ctime())