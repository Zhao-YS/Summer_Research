
import csv


#读入细胞系名称与Depmap-id的对应信息
name_File = open("output/cell_lines.csv","r")
CL_Info = csv.reader(name_File)
Ids = []
CL_names = []
for row in CL_Info:
	Ids.append(row[1])
	CL_names.append(row[0])
Ids = Ids[1:]
CL_names = CL_names[1:]
name_File.close()


#读入表达数据
expr_File = open("CCLE_expression.csv","r")
expr_Info = csv.reader(expr_File)
Dep_id = []
Info = []
for row in expr_Info:
	Info.append(row[1:])
	Dep_id.append(row[0])
Genes = Info[0]
Info = Info[1:]
Dep_id = Dep_id[1:]
expr_File.close()


#连接细胞系名称与表达数据
result = [tuple(['Cellline_Name']+Genes)]
for i in range(0,len(Ids)):
	if Ids[i]!='NA' and Ids[i] in Dep_id:
		result.append(tuple([CL_names[i]]+Info[Dep_id.index(Ids[i])]))
f = open('output/cell_line_exp.csv','w',newline = '')
writer = csv.writer(f)
for i in result:
	writer.writerow(i)
f.close()


