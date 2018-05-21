# class counter:
#     a='+'
#     b='-'
#     c='*'
#     d='/'
#     def __init__(self,a,b,c,d):
#         self.a=a
#         self.b=b
#         self.c=c
#         self.d=d
#     def plus_jia(self):
#         print(self.d)
#
# x=counter
# x.plus_jia()
class cat:
    def __init__(self,a,man,b):
        self.a=a
        self.man=man
        self.b=b
    def add_(self):
        if self.man=='+':
            print(self.a+self.b)
    def ad_(self):
        if self.man=='-':
            print(self.a-self.b)
    def dd_(self):
        if self.man=='*':
            print(self.a*self.b)
    def adda_(self):
        if self.man=='/':
            print(self.a/self.b)
s=cat(1000,'*',265)
s.add_()
s.ad_()
s.dd_()
s.adda_()