class person():
    def make_money(self):
        print('一百万')
class teacher():
    def make_money(self):
        print('五百万')
class student():
    def make_money(self):
        print('一千万')
#3###
teacher().make_money()
class class_room:
    t=teacher()
    s=student()
    def teach(self):
        pass
class_room.s.make_money()
class_room.t.make_money()

class car:
    def wheels(self,number):
        print('this car has %s wheels'%(number))
    def wheels(self,number,brand):
        print('this car has %s %s wheels'%(number,brand))
car().wheels(3,2)