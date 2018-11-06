# 获取字母对应在字母表中的位置，从0开始计数
def Cal_loc(a):
    allStr = 'abcdefghijklmnopqrstuvwxyz'
    return allStr.find(a)

# 由 character 1 计算得到数字AB,A+B
def Cal_AB(cha1):
    lis = map(Cal_loc, cha1)
    tmp_ab = sum(lis)%100
    AB = '0'+str(tmp_ab) if len(str(tmp_ab)) == 1 else str(tmp_ab)
    A_B = int(AB[0])+int(AB[1])
    return AB, A_B

# 特征2位移A+B位
def Shift_cha2(cha2, A_B):
    Pri_Table = 'AzByCxDwEvFuGtHsIrJqKpLoMnNmOlPkQjRiShTgUfVeWdXcYbZa'
    lis = list(map(Cal_loc, cha2))
    for i,j in enumerate(lis):
        lis[i] = Pri_Table[(j + A_B)%52]
    return lis

# 密码生成
def Password_generate(cha1, cha2, cha3):
    AB, A_B = Cal_AB(cha1)
    letter = Shift_cha2(cha2, A_B)
    letter.insert(int(AB[1]), cha3)
    c = ''
    for i in letter:
        c += str(i)
    password = c + AB
    return password

print('''
    密码由输入的特征计算得到，请务必记住自己输入的两组特征
    建议 特征1 与目标站域名相关
    建议 特征2 自己设置固定的字符串
''')

cha1 = input("请输入特征1：")
cha2 = input("请输入特征2：")
cha2 = 'chenchuan' if not len(cha2) else cha2
cha3 = input("是否将‘.’加入密码中，默认加入，若不加入，则输入no\n--->")
cha3 = '.' if not len(cha3) else ''
password = Password_generate(cha1, cha2, cha3)
print('密码：\n', password)