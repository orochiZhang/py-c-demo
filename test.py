from ctypes import cdll

testdll = cdll.LoadLibrary('test.dll')
print(testdll.sum(1, 3))
# testso = cdll.LoadLibrary('/home/test.so')
# print(testso.sum(1, 3))