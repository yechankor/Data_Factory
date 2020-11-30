import pandas as pd

## 오프라인 숙박 =====================================================
data = pd.read_csv("C:/data/off_acco.csv", sep=',', encoding='utf-8')
data.columns=['DATE','CN','AMT']
PN=[]
for i in data['DATE']:
    if str(i)[0:6]== '201902':
        PN.append(-0.1298816885266985)
    elif str(i)[0:6]== '201903':
        PN.append(-0.24523608173642839)
    elif str(i)[0:6]== '201904':
        PN.append(-0.5726537959916251)
    elif str(i)[0:6]== '201905':
        PN.append(-0.5188040807843208)
    elif str(i)[0:6]== '202002':
        PN.append(-0.10184521675109863)
    elif str(i)[0:6]== '202003':
        PN.append(0.7370842893918356)
    elif str(i)[0:6]== '202004':
        PN.append(-0.5253404080867767)
    else:
        PN.append(-0.5076049500041537)

data['PN']=PN
data.to_csv("C:/data/off_acco.csv", mode='w', index=False, encoding='utf-8')        

## 오프라인 문화취미 =====================================================
data = pd.read_csv("C:/data/off_cul.csv", sep=',', encoding='utf-8')
data.columns=['DATE','CN','AMT']
PN=[]
for i in data['DATE']:
    if str(i)[0:6]== '201902':
        PN.append(-0.448069969813029)
    elif str(i)[0:6]== '201903':
        PN.append(0.1945506234963735)
    elif str(i)[0:6]== '201904':
        PN.append(-0.02406144142150879)
    elif str(i)[0:6]== '201905':
        PN.append(-0.4979627847671509)
    elif str(i)[0:6]== '202002':
        PN.append(-0.12741482257843018)
    elif str(i)[0:6]== '202003':
        PN.append(0.1476357335394079)
    elif str(i)[0:6]== '202004':
        PN.append(0.43579452236493427)
    else:
        PN.append(0.14210561513900757)

data['PN']=PN
data.to_csv("C:/data/off_cul.csv", mode='w', index=False, encoding='utf-8')        

## 오프라인 식품 =====================================================
data = pd.read_csv("C:/data/off_food.csv", sep=',', encoding='utf-8')
data.columns=['DATE','CN','AMT']
PN=[]
for i in data['DATE']:
    if str(i)[0:6]== '201902':
        PN.append(0.48842278122901917)
    elif str(i)[0:6]== '201903':
        PN.append(0.4787071645259857)
    elif str(i)[0:6]== '201904':
        PN.append(0.5413034345422473)
    elif str(i)[0:6]== '201905':
        PN.append(-0.06888024674521552)
    elif str(i)[0:6]== '202002':
        PN.append(-0.017809921503067018)
    elif str(i)[0:6]== '202003':
        PN.append(-0.31325842227254597)
    elif str(i)[0:6]== '202004':
        PN.append(-0.06520995828840467)
    else:
        PN.append(-0.001237014929453532)

data['PN']=PN
data.to_csv("C:/data/off_food.csv", mode='w', index=False, encoding='utf-8')

## 오프라인 의료기관 =====================================================
data = pd.read_csv("C:/data/off_medi.csv", sep=',', encoding='utf-8')
data.columns=['DATE','CN','AMT']
PN=[]
for i in data['DATE']:
    if str(i)[0:6]== '201902':
        PN.append(0.041013479232788086)
    elif str(i)[0:6]== '201903':
        PN.append(-0.0163763165473938)
    elif str(i)[0:6]== '201904':
        PN.append(0.2669769287109375)
    elif str(i)[0:6]== '201905':
        PN.append(0.17681125402450562)
    elif str(i)[0:6]== '202002':
        PN.append(-0.54629235714674)
    elif str(i)[0:6]== '202003':
        PN.append(-0.07592485348383586)
    elif str(i)[0:6]== '202004':
        PN.append(-0.18886275724931198)
    else:
        PN.append(-0.29306992292404177)
        
data['PN']=PN
data.to_csv("C:/data/off_medi.csv", mode='w', index=False, encoding='utf-8')

## 오프라인 보건위생 =====================================================
data = pd.read_csv("C:/data/off_sani.csv", sep=',', encoding='utf-8')
data.columns=['DATE','CN','AMT']
PN=[]
for i in data['DATE']:
    if str(i)[0:6]== '201902':
        PN.append(0.0242919921875)
    elif str(i)[0:6]== '201903':
        PN.append(-0.2546436531203134)
    elif str(i)[0:6]== '201904':
        PN.append(-0.25560569763183594)
    elif str(i)[0:6]== '201905':
        PN.append(0.4311133995652199)
    elif str(i)[0:6]== '202002':
        PN.append(-0.5093494653701782)
    elif str(i)[0:6]== '202003':
        PN.append(-0.4577632631574358)
    elif str(i)[0:6]== '202004':
        PN.append(-0.4161640836132897)
    else:
        PN.append(-0.06528772115707397)
      
data['PN']=PN
data.to_csv("C:/data/off_sani.csv", mode='w', index=False, encoding='utf-8')

## 오프라인 레저 =====================================================
data = pd.read_csv("C:/data/off_lei.csv", sep=',', encoding='utf-8')
data.columns=['DATE','CN','AMT']
PN=[]
for i in data['DATE']:
    if str(i)[0:6]== '201902':
        PN.append(0.29600413356508526)
    elif str(i)[0:6]== '201903':
        PN.append(-0.036042352517445884)
    elif str(i)[0:6]== '201904':
        PN.append(0.3428010770252773)
    elif str(i)[0:6]== '201905':
        PN.append(0.7659961325781686)
    elif str(i)[0:6]== '202002':
        PN.append(0.7704757792609078)
    elif str(i)[0:6]== '202003':
        PN.append(0.7231104969978333)
    elif str(i)[0:6]== '202004':
        PN.append(0.373626138482775)
    else:
        PN.append(0.35270217061042786)

data['PN']=PN
data.to_csv("C:/data/off_lei.csv", mode='w', index=False, encoding='utf-8')



## 온라인 숙박 =====================================================
data = pd.read_csv("C:/data/on_acco.csv", sep=',', encoding='utf-8')
data.columns=['DATE','CN']
PN=[]
for i in data['DATE']:
    if str(i)[0:6]== '201902':
        PN.append(-0.1298816885266985)
    elif str(i)[0:6]== '201903':
        PN.append(-0.24523608173642839)
    elif str(i)[0:6]== '201904':
        PN.append(-0.5726537959916251)
    elif str(i)[0:6]== '201905':
        PN.append(-0.5188040807843208)
    elif str(i)[0:6]== '202002':
        PN.append(-0.10184521675109863)
    elif str(i)[0:6]== '202003':
        PN.append(0.7370842893918356)
    elif str(i)[0:6]== '202004':
        PN.append(-0.5253404080867767)
    else:
        PN.append(-0.5076049500041537)

data['PN']=PN
data.to_csv("C:/data/on_acco.csv", mode='w', index=False, encoding='utf-8')        

## 온라인 문화취미 =====================================================
data = pd.read_csv("C:/data/on_cul.csv", sep=',', encoding='utf-8')
data.columns=['DATE','CN']
PN=[]
for i in data['DATE']:
    if str(i)[0:6]== '201902':
        PN.append(-0.448069969813029)
    elif str(i)[0:6]== '201903':
        PN.append(0.1945506234963735)
    elif str(i)[0:6]== '201904':
        PN.append(-0.02406144142150879)
    elif str(i)[0:6]== '201905':
        PN.append(-0.4979627847671509)
    elif str(i)[0:6]== '202002':
        PN.append(-0.12741482257843018)
    elif str(i)[0:6]== '202003':
        PN.append(0.1476357335394079)
    elif str(i)[0:6]== '202004':
        PN.append(0.43579452236493427)
    else:
        PN.append(0.14210561513900757)

data['PN']=PN
data.to_csv("C:/data/off_cul.csv", mode='w', index=False, encoding='utf-8')        

## 온라인 식품 =====================================================
data = pd.read_csv("C:/data/on_food.csv", sep=',', encoding='utf-8')
data.columns=['DATE','CN']
PN=[]
for i in data['DATE']:
    if str(i)[0:6]== '201902':
        PN.append(0.48842278122901917)
    elif str(i)[0:6]== '201903':
        PN.append(0.4787071645259857)
    elif str(i)[0:6]== '201904':
        PN.append(0.5413034345422473)
    elif str(i)[0:6]== '201905':
        PN.append(-0.06888024674521552)
    elif str(i)[0:6]== '202002':
        PN.append(-0.017809921503067018)
    elif str(i)[0:6]== '202003':
        PN.append(-0.31325842227254597)
    elif str(i)[0:6]== '202004':
        PN.append(-0.06520995828840467)
    else:
        PN.append(-0.001237014929453532)

data['PN']=PN
data.to_csv("C:/data/on_food.csv", mode='w', index=False, encoding='utf-8')


## 온라인 보건위생 =====================================================
data = pd.read_csv("C:/data/on_sani.csv", sep=',', encoding='utf-8')
data.columns=['DATE','CN']
PN=[]
for i in data['DATE']:
    if str(i)[0:6]== '201902':
        PN.append(0.0242919921875)
    elif str(i)[0:6]== '201903':
        PN.append(-0.2546436531203134)
    elif str(i)[0:6]== '201904':
        PN.append(-0.25560569763183594)
    elif str(i)[0:6]== '201905':
        PN.append(0.4311133995652199)
    elif str(i)[0:6]== '202002':
        PN.append(-0.5093494653701782)
    elif str(i)[0:6]== '202003':
        PN.append(-0.4577632631574358)
    elif str(i)[0:6]== '202004':
        PN.append(-0.4161640836132897)
    else:
        PN.append(-0.06528772115707397)
      
data['PN']=PN
data.to_csv("C:/data/on_sani.csv", mode='w', index=False, encoding='utf-8')

## 온라인 레저 =====================================================
data = pd.read_csv("C:/data/on_lei.csv", sep=',', encoding='utf-8')
data.columns=['DATE','CN']
PN=[]
for i in data['DATE']:
    if str(i)[0:6]== '201902':
        PN.append(0.29600413356508526)
    elif str(i)[0:6]== '201903':
        PN.append(-0.036042352517445884)
    elif str(i)[0:6]== '201904':
        PN.append(0.3428010770252773)
    elif str(i)[0:6]== '201905':
        PN.append(0.7659961325781686)
    elif str(i)[0:6]== '202002':
        PN.append(0.7704757792609078)
    elif str(i)[0:6]== '202003':
        PN.append(0.7231104969978333)
    elif str(i)[0:6]== '202004':
        PN.append(0.373626138482775)
    else:
        PN.append(0.35270217061042786)

data['PN']=PN
data.to_csv("C:/data/on_lei.csv", mode='w', index=False, encoding='utf-8')