import csv

#写入药物-靶点对到新csv中

file = open("interactions.csv",encoding="UTF-8")
Info = csv.reader(file)
result = []
for row in Info:
	result.append((row[0],row[5]))
file.close()
f = open('drug_target.csv','w',newline = '',encoding="utf-8")
writer = csv.writer(f)
for i in result:
	writer.writerow(i)
f.close()