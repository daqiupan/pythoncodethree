# class student:
#     a='name'
#     b='technical'
#     def print_stu_info(self):
#         print("学生%s,已经就读于本学%s专业"%(self.a,self.b))
# student().print_stu_info()

class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def print_score(self):
        print('%s : %s' %(self.name, self.score))
    def get_grade(self):
        level = self.score // 10
        {
           10: lambda: print('perfect'),
            9: lambda: print('A'),
            8: lambda: print('B'),
            7: lambda: print('C'),
            6: lambda: print('D'),
        }.get(level)()
std1 = Student('Jason', 80)
Student.get_grade(std1)