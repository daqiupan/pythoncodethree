import  xlrd
class read:
    def get_msg(self):
        book=xlrd.open_workbook(r'D:\shuju.xlsx')
        sheet=book.sheets()[0]
        return sheet
if __name__=='__main__':
    s=read().get_msg()
    # print(s)
    # print(s.nrows)
    # print(s.cell(3,1).value)

    for i in range(s.nrows):
        # for j in range(s.ncols):
            # print(s.cell(i,j).value,'\t',end='')
        # print('')
        li=s.row_values(i)
        print(li)
