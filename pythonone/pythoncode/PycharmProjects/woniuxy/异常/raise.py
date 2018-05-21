try:
    name=input('输入变量名称：')
    if name.isdigit():
        raise NameError('bad name!')
except Exception as e:
    print(e)