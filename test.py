

a=["test.txt","test1.txt"]


def tel(b):
	for x in b:
		file=open(x,"r+")
		print file.read()


tel(a)