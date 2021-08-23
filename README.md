# ReadMe

## 开发环境

python: 3.8.8

pandas: 1.2.4

numpy: 1.19.5

matplotlib: 3.3.4

keras: 2.6.0

sklearn: 0.24.1

lxml: 4.6.3

rdkit: 2019.09.3

csv :1.0

## 文件说明

### DrugComb

- drugcombs_scored.csv

  药物协同作用原始数据，来源于DrugComb

### Drug_disease_Preprocess

- Drug_disease.csv

  Drug_Disease.py执行后得到的药物-适应症信息数据文件

- Drug_disease.py

  提取药物-适应症信息的python脚本

- P1-05-Drug_disease.txt

  药物-适应症，原始数据，来源于TTD数据库

### Drug_structrue_Preprocess

- 1.png

  SMILE_Fingerprint.py画出的SMILEs分子可视化结构

- Drug_FingerPrints.csv

  执行SMILE_Fingerprint.py后得到的药物-Morgan指纹编码数据

- Drug_SMILEs.csv

  执行SMILE_Fingerprint.py后得到的药物-SMILEs结构数据

- GPU.pbs

  RNN网络加速训练时调用计算集群的服务器脚本

- RNN.py

  RNN的搭建，训练以及评估的python实现

- SMILE_Fingerprint.py

  处理DrugBank中的原始分子结构数据，得到分子结构的SMILEs与Morgan指纹并输出

- structures.sdf

  分子结构原始数据，来源于DrugBank

### Drug_target_preprocess

- Drug_target.csv

  执行interaction.py后生成的药物-靶点数据

- interaction.py

  提取药物-靶点相关信息

- interactions.csv

  原始数据，来源于DGIdb

### Expression_Preprocess

#### output

- cell_line_exp.csv

  执行cell_line2Expression.py后得到，细胞系+表达量原始数据

- cell_lines.csv

  执行Name2Depmap.py后得到，细胞系原名与DepMap_IDs的对应表

- Exp_code.csv

  编码后的表达数据，执行Exp_Encode.py后得到

#### 当前目录

- cell_line2Expression.py

  将drugcombs中的细胞系通过Depmap-id与表达量连接

- drugcombs_scored.csv

  药物协同作用原始数据，来源于DrugComb，此处用于提取需要的细胞系

- Exp_Encode.py

  编码表达数据

- Manual_Search.csv

  人工标注的缺失信息的细胞系后续处理方法

- Name2Depmap.py

  将细胞系原名与Depmap-id关联

- sample_info.csv

  来源于CCLE数据库的原始数据，包含细胞系原名与Depmap-id的对应关系

### Pathway_preprocess

- Drug_Pathways.csv

  执行Get_pathway.py后得到的药物通路信息

- Get_pathway.py

  从大型中提取药物通路相关信息(大型xml文件无法上传github)