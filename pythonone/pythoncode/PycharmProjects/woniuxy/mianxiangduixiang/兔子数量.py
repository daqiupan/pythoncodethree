a,b=0,1
for i in range(1,13):
    print('第%s个月，有%s对兔子'%(i,b))
    a,b=b,a+b


class Rib:
    month=0
    def gr(self):
        self.month += 1
    def bir(self,li):
        li.append(Rib())

li = [Rib()]
for j in range(12):
    for i in li:
        if i.month<3:
            i.gr()
        if i.month>=3:
            i.bir(li)
            i.gr()
    print(len(li))
