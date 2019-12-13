from ctypes import cdll
from ctypes import *

# 调用c++ 函数
testdll = cdll.LoadLibrary('D:\pyextend\pyextend.dll')
print(testdll.sum(1, 3))

# 传入字符串列表给c++ 调用
str1 = c_char_p(bytes("nihao", 'utf-8'))
str2 = c_char_p(bytes("shijie", 'utf-8'))

a = (c_char_p * 2)(str1, str2)
testdll.get_str_list(2, a)

# 传入列表给c++ 调用
b= (c_int64 * 4)(400, 10, 500, 0)
testdll.get_int_list(4, b)

# 传入python函数给c++ 调用
def testfunc():
	print('hello world')


CALLFUNC = CFUNCTYPE(None)
p = CALLFUNC(testfunc)

testdll.call_func(p)