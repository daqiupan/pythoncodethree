import sys
import xlrd
class ReadExcel:
    def get_sheet(self,path,index=0):
        book = xlrd.open_workbook(path)
        sheet = book.sheets()[index]
        return sheet


s = ReadExcel().get_sheet(r'D:\shuju.xlsx')
# for i in range(s.nrows):
#     for j in range(s.ncols):
#         print(s.cell(i,j).value)
for i in range(s.nrows):
    li = s.row_values(i)
    newli=li[0:7]
    __import__('cases.'+li[0])#动态引入
    mod=sys.modules['cases.'+li[0]]#内容储存，导入模块
    obj=getattr(mod,li[0])#根据li来获取到类
    mtd=getattr(obj(),li[0])
    mtd(newli,li[-1])#驱动方法执行，传入测试参数和预期结果