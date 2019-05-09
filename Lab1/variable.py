import sys
import ctypes
i = 10
print(hex(id(i)))


word = 'hello sagar!!'
print(id(word))

i = [1, 2, 3, 4]
j = i
print(sys.getrefcount(i))





