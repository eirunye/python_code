# with open('io.txt', 'r') as f:
#     print(f.read())

#
# f = open('gbk.txt', 'r', 'utf-8')
# print(f.read())


# StringIO

# from io import StringIO
#
# f = StringIO()
# a = f.write("hello")
# print(a)
#
# print(f.write(' '))
#
# print(f.write("world!"))
#
# print(f.getvalue())  # 获取缓存的数据

# StringIO  bytesIO

from io import StringIO

f = StringIO(" Hello !\nHi!\nGood bye!")
while True:
	s = f.readline()
	if s == '':
		break
	print(s.strip())



from io import BytesIO

ff = BytesIO()
print(ff.write('中文'.encode('utf-8')))
print(ff.getvalue())

