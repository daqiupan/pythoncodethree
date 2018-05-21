# import random
# class Autopeiple:
#     GameDic={'石头':'剪刀','剪刀':'布','布':'石头'}
#     a='石头'
#     b='剪刀'
#     c='布'
#     def __init__(self,a,b,c):
#         self.a=a
#         self.b=b
#         self.c=c
#     def shitou(self):
#         if self.a==
#             print('')

# import random
# guess_list = ["石头","剪刀","布"]
# guize = [["布","石头"],["石头","剪刀"],["剪刀","布"]]
# while True:
#     computer = random.choice(guess_list)
#     people =  input('请输入：石头,剪刀,布\n').strip()
#     if people not in  guess_list:
#         people =  input('重新请输入：石头,剪刀,布\n').strip()
#         continue
#     if computer ==  people:
#         print("平手，再玩一次！")
#     elif [computer,people] in guize :
#         print("电脑获胜！")
#     else:
#         print("人获胜！")
#         break
