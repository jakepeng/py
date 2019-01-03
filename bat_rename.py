import os

#os.chdir('C:\\Users\\Jake.WIN-7M5O4J7N5L2\\Desktop\\新建文件夹')
os.chdir('D:\\Video\\新建文件夹')
files = os.listdir()

for e in files:
	#(name, ext) = os.path.splitext(e)
	os.rename(e, e.replace('_sub0', ''))