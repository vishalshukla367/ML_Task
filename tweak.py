import os
file = open('usr/mlcnn/main.py','r+')
l = []
for lines in file:
	l.append(lines)

os.system("echo '' | tee main.py")
l.insert(l.index('add_layer(model)\n')+1,'add_layer(model)\n')
file.writelines(l)


