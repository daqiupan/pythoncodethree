while True:
    try:
        x=int(input("输入："))
        break
    except ValueError as e:
        print("错误输入",e)
    finally:
        print('运行成功')