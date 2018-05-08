# -*- coding: utf-8 -*-
# 列表生成式
# 练习
# 如果list中既包含字符串，又包含整数，由于非字符串类型没有lower()方法，所以列表生成式会报错：

L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s, str)]

print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')
    
    
# 多练练
L3 = [m + n for m in 'ABC' for n in 'XYZ']
print(L3)

# 列出目录下的所有文件和目录名
import os # 导入os模块
L4 = [d for d in os.listdir('D:/')] # 打印出来好多 显示隐藏文件后都看不到的东西..中毒了?
print(L4)