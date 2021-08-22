import csv
import numpy as np

#import expression data
f = open('output/cell_line_exp.csv','r')
expr_Data = csv.reader(f)
Info = []
Names = []
for row in expr_Data:
	Info.append(row[1:])
	Names.append(row[0])
codes = []
Gene = Info[0]
#取最大值下标并编码，重复1500次
for i in range(1,len(Info)):
	data = np.array(Info[i])
	code = np.zeros((len(Info[i])))
	for j in range(0,1500):
		max_loc = np.argmax(data)
		code[max_loc] = 1
		data[max_loc] = -1
	code = code.astype(np.int)
	codes.append(list(code))
#写入csv文件
result = [tuple(['cell_line']+Gene)]
Names = Names[1:]
for i in range(0,len(Names)):
	result.append(([Names[i]]+codes[i]))
file = open('output/Exp_code.csv','w',newline='')
writer = csv.writer(file)
for i in result:
	writer.writerow(i)
f.close()
file.close()
