import pandas as pd
from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit.Chem import MACCSkeys
from rdkit.Chem import DataStructs
from rdkit.Chem import Draw

#向2048位bit编码中添加逗号，以存入csv格式
def comma(s):
	result = ""
	for i in range(0,len(s)):
		result = result + "," + s[i]
	return result

#Get SMILEs & Morgan-fingerprint
suppl = Chem.SDMolSupplier('structures.sdf')
mols = [x for x in suppl if x is not None]
Fingerprints = []
SMILEs = []
mol_list = []
for mol in mols:
	mol_list.append(mol)
	name = mol.GetProp('GENERIC_NAME')
	name = name.replace(",", "_")
	Morgan = AllChem.GetMorganFingerprintAsBitVect(mol,2,nBits=2048)
	Fingerprint = comma(Morgan.ToBitString())
	Fingerprints.append(name+Fingerprint)
	smile = Chem.MolToSmiles(mol)
	SMILEs.append(name+','+Chem.MolToSmiles(mol))

#保存SMILEs与Fingerprint到文件
f1 = open("Drug_SMILEs.csv", 'w')
f1.write("Name,SMILEs\n")
f2 = open("Drug_Fingerprints.csv", 'w')
for i in range(0,len(SMILEs)):
	f1.write(SMILEs[i]+'\n')
	f2.write(Fingerprints[i]+'\n')
f1.close()
f2.close()