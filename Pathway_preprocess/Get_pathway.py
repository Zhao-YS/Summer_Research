import lxml
from lxml import etree
#读取xml
f=open('full_database.xml','r')
text=f.read()
#得到根节点
xml=etree.fromstring(text.encode('utf-8'))
root_tree = xml.getroottree()
root = root_tree.getroot()



Drug_path = "/*/*["
name_path = "]/*[local-name()='name']/text()"
p_path = "]/*[local-name()='pathways']/*/*[local-name()='name']/text()"
Id_path = "]/*[local-name()='pathways']/*/*[local-name()='smpdb-id']/text()"
Cate_path = "]/*[local-name()='pathways']/*/*[local-name()='category']/text()"
result = ["Drug_name,Pathway_name,smpdb-id,category\n"]
for i in range(1,len(root)):
    name = xml.xpath(Drug_path+str(i)+name_path)[0]
    pathways = xml.xpath(Drug_path+str(i)+p_path)
    Ids = xml.xpath(Drug_path+str(i)+Id_path)
    Cates = xml.xpath(Drug_path+str(i)+Cate_path)
    if len(pathways) > 0:
        for i in range(0,len(pathways)):
            result.append(name+','+pathways[i]+','+Ids[i]+','+Cates[i]+'\n')



f = open("Drug_Pathways.csv", 'w')
for line in result:
    f.write(line)
f.close()





