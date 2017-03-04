import os

def print_directory_contents(sPath):

	print ("Directory", sPath)
	files = os.listdir(sPath)
	for file in files:
		#filePath = sPath+'/'+file
		filePath = os.path.join(sPath, file)
		fileIsDir = os.path.isdir(filePath)
		print(file, fileIsDir)
		if fileIsDir:
			print_directory_contents(filePath)
		else:
			print file


print_directory_contents('/Users/kumarn/Documents/_navin/_nk_only/_python')

#print(help(os))

l_mem = []
l = l_mem           # the third call
for i in range(3):
    l.append(i*i)

print(l)       

def f(x,l=[]):
    for i in range(x):
        l.append(i*i)
    print(l) 

f(2)
f(3,[3,2,1])
f(3)

# end of file