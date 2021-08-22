import csv

#import celllines & remove duplicates
f = open('drugcombs_scored.csv','r')
celllines = csv.reader(f)
Info = []
for row in celllines:
	Info.append(row[3])
Info = list(set(Info[1:]))
f.close()

#Match the cell-line names to Depmap-id
data = []
Depf = open('sample_info.csv','r')
DepMap_Info = csv.reader(Depf)
DepMap_IDs = []
CL_Names = []
for row in DepMap_Info:
	DepMap_IDs.append(row[0])
	CL_Names.append(row[1]+row[2]+row[3]+row[4])
Depf.close()
result = [("cell_Line_Name","DepMap_IDs")]
for name in Info:

	flag = False
	for i in range(0,len(CL_Names)):
		if name in CL_Names[i]:
			result.append((name,DepMap_IDs[i]))
			flag = True
			break
	if flag == False and '-' in name:
		loc = name.index('-')
		name = name[:loc] + name[loc+1:]
		for i in range(0,len(CL_Names)):
			if name in CL_Names[i]:
				result.append((name,DepMap_IDs[i]))
				flag = True
				break
	if flag == False:
		result.append((name,'NA'))
		print(name)
f = open('output/cell_lines.csv','w',newline='')
writer = csv.writer(f)
for i in result:
	writer.writerow(i)
f.close()