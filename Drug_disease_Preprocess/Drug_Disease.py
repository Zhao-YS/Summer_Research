
#读取药物适应症信息
f = open("P1-05-Drug_disease.txt","r")
lines = f.readlines()
f.close()

flag = 0
result = ["Drug_name, Disease, Clinical_status\n"]

#注意忽略第一个DRUGNAME标签，这里是模式的定义，不是实际的信息
for line in lines:
	if 'DRUGNAME' in line and 'Name' not in line:
		flag = 1
		Drugname = ""
		Drugname_list = line.split()[2:]
		if len(Drugname_list) == 1:
			Drugname = Drugname_list[0]
		else:
			for i in Drugname_list:
				Drugname = Drugname + i + " "
			Drugname = Drugname[:-1]
	if 'INDICATI' in line and flag == 1:
		Info = line.split()
		Disease_name = ""
		Front_loc = Info.index('INDICATI')
		Back_loc = Info.index('[ICD-11:')
		for i in range(Front_loc+1, Back_loc):
			if Front_loc + 2 == Back_loc:
				Disease_name = Info[i]
			else:
				Disease_name = Info[i]+" "
		if " " in Disease_name:
			Disease_name = Disease_name[:-1]
		for info in Info:
			if ']' in info:
				Cl_status = info[:-1]
		result.append(Drugname + ","+Disease_name+","+Cl_status+"\n")

f = open("Drug_disease.csv","w")
for line in result:
	f.write(line)
f.close()