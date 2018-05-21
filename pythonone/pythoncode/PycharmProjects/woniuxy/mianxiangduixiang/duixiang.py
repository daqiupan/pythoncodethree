# class demo_class:
#     def __init__(self,name,age):
#         self.__name=name
#         self.age=age
#         def _print_info(self):
#             print('INTO:..%s..%s...\n'%(self.name,self.age))
# d=demo_class('wang',20)
# print(d.age)
# print(d.__name)
# # print(d._print_info())

class student:
    name='qiu'
    age=21
    course={'yuwen':'100','shuxue':'99','yingyu':'97'}
    def get_name(self):
        print("姓名为:%s"%(self.name))
    def get_age(self):
        print("年龄为：%d"%(self.age))
    def get_course(self):
        print("三门科目中的最高分数的课程为：%s"%(max(self.course)))
    def get_avg(self):
        s=sum()
        cat=3
        print("该学生的平均成绩为：%s"%((self.course.values())/cat))
x=student()
x.get_name()
x.get_age()
x.get_course()
x.get_avg()