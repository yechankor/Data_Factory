# 4-2) COVID 변수 추가

covid=pd.read_csv('c:/data/covid.csv')

#오프라인 숙박 COVID 컬럼 추가 =======================================================
off_acc = pd.read_csv('c:/data/off_acco.csv')
off_acc1 = off_acc[121:]
off_acco2020 = pd.merge(off_acc1, covid)
off_acc2 = off_acc[0:121]
off_acc1 = pd.concat([off_acc2, off_acco2020], join='outer').fillna(0)
off_acc1 = off_acc1.astype({'COVID' : 'int'})
off_acc1 = off_acc1[['DATE', 'PN', 'CN', 'COVID']]
off_acc1.to_csv('c:/data/off_acc1.csv')
off_acc1.reset_index(drop=True, inplace=True)
off_acc1.to_csv('c:/data/off_acc1.csv',index=False)
off_acc1

#오프라인 문화취미 COVID 컬럼 추가 =======================================================
off_cul = pd.read_csv('c:/data/off_cul.csv')
off_cul1 = off_cul.reset_index()
off_cul2 = off_cul1[121:]
off_cul2 = off_cul2.reset_index(drop=True)
off_cul3 = pd.merge(off_cul2, covid, left_index=True, right_index=True)
del off_cul3['DATE_x']
off_cul3 = off_cul3[['DATE_y', 'PN', 'CN', 'COVID']]
off_cul3 = off_cul3.rename(columns={'DATE_y':'DATE', 'PN':'PN', 'CN':'CN', 'COVID':'COVID'})
off_cul4 = off_cul1[:121]
off_cul5 = pd.concat([off_cul4, off_cul3], join='outer').fillna(0)
off_cul5 = off_cul5[['DATE', 'PN', 'CN', 'COVID']]
off_cul5 = off_cul5.astype({'COVID' : 'int'})
off_cul5.reset_index(drop=True, inplace=True)
off_cul5.to_csv("c:/data/off_cul1.csv")
off_cul5

#오프라인 식품 COVID 컬럼 추가 =======================================================
off_food = pd.read_csv('c:/data/off_food.csv')
off_food1 = off_food[121:]
off_food2020 = pd.merge(off_food1, covid)
off_food1 = off_food[:121]
off_food2 = pd.concat([off_food1, off_food2020], join='outer').fillna(0)
off_food2 = off_food2[['DATE', 'PN', 'CN', 'COVID']]
off_food2 = off_food2.astype({'COVID' : 'int'})
off_food2.reset_index(drop=True, inplace=True)
off_food2.to_csv("c:/data/off_food2.csv")
off_food2

#오프라인 레저 COVID 컬럼 추가 =======================================================
off_lei = pd.read_csv('c:/data/off_lei.csv')
off_lei1 = off_lei[121:]
off_lei2 = pd.merge(off_lei1, covid)
off_lei3 = off_lei[:121]
off_lei3 = pd.concat([off_lei3, off_lei2], join='outer').fillna(0)
off_lei3 = off_lei3[['DATE', 'PN', 'CN', 'COVID']]
off_lei3 = off_lei3.astype({'COVID' : 'int'})
off_lei3.reset_index(drop=True, inplace=True)
off_lei3.to_csv('c:/data/off_lei1.csv')
off_lei3

#오프라인 의료기관 COVID 컬럼 추가 =======================================================
off_medi = pd.read_csv('c:/data/off_medi.csv')
off_medi0 = off_medi[121:]
off_medi1 = pd.merge(off_medi, covid)
off_medi2 = off_medi[:121]
off_medi3 = pd.concat([off_medi2, off_medi1], join='outer').fillna(0)
off_medi3 = off_medi3[['DATE', 'PN', 'CN', 'COVID']]
off_medi3 = off_medi3.astype({'COVID' : 'int'})
off_medi3.reset_index(drop=True, inplace=True)
off_medi3.to_csv('c:/data/off_medi1.csv',index=False)
off_medi3

#오프라인 보건위생 COVID 컬럼 추가 =======================================================
off_sani = pd.read_csv('c:/data/off_sani.csv')
off_sani1 = off_sani[121:]
off_sani1 = off_sani1.reset_index(drop=True)
off_sani2 = pd.merge(off_sani1, covid)
off_sani3 = off_sani[:121]
off_sani3 = pd.concat([off_sani3, off_sani2], join='outer').fillna(0)
off_sani3 = off_sani3[['DATE', 'PN', 'CN', 'COVID']]
off_sani3 = off_sani3.astype({'COVID' : 'int'})
off_sani3.reset_index(drop=True, inplace=True)
off_sani3.to_csv("c:/data/off_sani1.csv",index=False)
off_sani3

#온라인 숙박 COVID 컬럼 추가 =======================================================
on_acc = pd.read_csv('c:/data/on_acco.csv')
on_acc1 = on_acc[121:]
on_acc1 = on_acc1.reset_index(drop=True)
on_acc2 = pd.merge(on_acc1, covid, left_index=True, right_index=True)
del on_acc2['DATE_y']
on_acc2 = on_acc2.rename(columns={'DATE_x':'DATE', 'PN':'PN', 'CN':'CN'})
on_acc2 = on_acc2[['DATE', 'PN', "CN", 'COVID']]
on_acc3 = on_acc[:121]
on_acc3 = pd.concat([on_acc3, on_acc2], join='outer').fillna(0)
on_acc3 = on_acc3[['DATE', 'PN', 'CN', 'COVID']]
on_acc3 = on_acc3.astype({'COVID' : 'int'})
on_acc3.reset_index(drop=True, inplace=True)
on_acc3.to_csv("c:/data/on_acc1.csv", index=False)
on_acc3

#온라인 문화취미 COVID 컬럼 추가 =======================================================
on_cul = pd.read_csv('c:/data/on_cul.csv')
on_cul1 = on_cul.reset_index()
on_cul2 = on_cul1[120:]
on_cul2 = on_cul2.reset_index(drop=True)
on_cul3 = pd.merge(on_cul2, covid, left_index=True, right_index=True)
del on_cul3['DATE_y']
on_cul3 = on_cul3.rename(columns = {'DATE_x':'DATE', 'CN':'CN', 'PN':'PN', 'COVID':'COVID'})
on_cul4 = on_cul1[:120]
on_cul4= on_cul4.reset_index(drop=True)
on_cul5 = pd.concat([on_cul4, on_cul3],).fillna(0)
on_cul5 = on_cul5[['DATE', 'PN', 'CN', 'COVID']]
on_cul5 = on_cul5.astype({'COVID' : 'int'})
on_cul5 = on_cul5.reset_index(drop=True)
on_cul5.to_csv("c:/data/on_cul1.csv",index=False)
on_cul5

#온라인 식품 COVID 컬럼 추가 =======================================================
on_food = pd.read_csv('c:/data/on_food.csv')
on_food1 = on_food[121:]
on_food1 = on_food1.reset_index(drop=True)
on_food2 = pd.merge(on_food1, covid, left_index=True, right_index=True)
del on_food2['DATE_y']
on_food2 = on_food2.rename(columns = {'DATE_x':'DATE', 'CN':'CN', 'PN':'PN', 'COVID':'COVID'})
on_food3 = on_food[:121]
on_food4 = pd.concat([on_food3, on_food2], join = 'outer').fillna(0)
on_food4 = on_food4[['DATE', 'PN', 'CN', 'COVID']]
on_food4 = on_food4.astype({'COVID' : 'int'})
on_food4 = on_food4.reset_index(drop=True)
on_food4.to_csv('c:/data/on_food1.csv',index=False)
on_food4

#온라인 레저 COVID 컬럼 추가 =======================================================
on_lei = pd.read_csv('c:/data/on_lei.csv')
on_lei1 = on_lei[119:]
on_lei1 = on_lei1.reset_index(drop=True)
on_lei2 = pd.merge(on_lei1, covid, left_index=True, right_index=True)
del on_lei2['DATE_y']
on_lei2 = on_lei2.rename(columns = {'DATE_x':'DATE', 'CN':'CN', 'PN':'PN', 'COVID':'COVID'})
on_lei3 = on_lei[:119]
on_lei4 = pd.concat([on_lei3, on_lei2], join = 'outer').fillna(0)
on_lei4 = on_lei4[['DATE', 'PN', 'CN', 'COVID']]
on_lei4 = on_lei4.astype({'COVID' : 'int'})
on_lei4.reset_index(drop=True, inplace=True)
on_lei4.to_csv('c:/data/on_lei1.csv', index=False)
on_lei4

#온라인 보건위생 COVID 컬럼 추가 =======================================================
on_sani0 = pd.read_csv('c:/data/on_sani.csv')
on_sani1 = on_sani0[121:]
on_sani1 = on_sani1.reset_index(drop=True)
on_sani2 = pd.merge(on_sani1, covid, left_index=True, right_index=True)
del on_sani2['DATE_y']
on_sani2 = on_sani2.rename(columns = {'DATE_x':'DATE', 'CN':'CN', 'PN':'PN', 'COVID':'COVID'})
on_sani3 = on_sani0[:121]
on_sani4 = pd.concat([on_sani3, on_sani2], join = 'outer').fillna(0)
on_sani4 = on_sani4[['DATE', 'PN', 'CN', 'COVID']]
on_sani4 = on_sani4.astype({'COVID' : 'int'})
on_sani4.reset_index(drop=True, inplace=True)
on_sani4.to_csv('c:/data/on_sani1.csv', index=False)
on_sani4