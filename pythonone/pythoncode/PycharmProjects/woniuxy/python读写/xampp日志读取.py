import  glob,os
# cat=glob.glob(r'C:\Xampp\apache\logs\*.log')
# cat=file.read()
# print(cat)
cat1=os.listdir(r'C:\Xampp\apache\logs')
for i in cat1:
    f=open(i)
    li=f.readlines()
    print(li)
cat2=open(r'C:\Users\Administrator\Desktop\daqiu.txt','r+')

# file=open(r'C:\Users\Administrator\Desktop\daqiu.txt','r+')
# cat1.seek(0)
# file=open(r'C:\Xampp\apache\logs','r+',encoding='utf8')
# file.write(r'C:\Users\Administrator\Desktop\daqiu.txt')
# cer=file.read()
# print(cer)
file.close()