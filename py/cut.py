# -*- coding: utf-8 -*-
# 切片
    L = ["yellow", "red", "green", "blue", "purple", "white", "black"]
    print(L[0:3])
    print(L[:3])
    print(L[2:3])
    print(L[:-1])
    print(L[-3:-1])

    S = '123456789'
    print(S[0:3])
    print(S[0::3])
    
#切片包含起始值位置， [x,y] x <= value < y

#利用切片操作，实现一个trim()函数，去除字符串首尾的空格，注意不要调用str的strip()方法：
def trim(s):
    length = len(s)
    count = 0
    while (count < length):# 判断条件错误示例:(count < len(s)), 原因在于字符串 s 在循环中动态被截取 谨记!
        if s[:1].isspace(): # 判断第0个字符否为 空格
            s = s[1:]
        elif s[-1:].isspace(): # 判断最后字符是否为 空格
            s = s[:-1]
        count += 1
    return s
    
if trim('hello  ') != 'hello':
    print('测试失败1!')
elif trim('  hello') != 'hello':
    print('测试失败2!')
elif trim('  hello  ') != 'hello':
    print('测试失败3!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败4!')
elif trim('') != '':
    print('测试失败5!')
elif trim('    ') != '':
    print('测试失败6!')
else:
    print('测试成功!')