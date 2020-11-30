# 3-2) PN 변수 추가
# PN 변수를 추가한 데이터프레임을 csv 파일로 저장


# 카드데이터
card = pd.read_table('c:/data/card.txt')
card

# 업종(10) : 숙박, 일자별 이용금액
store10_amt = card.loc[card['MCT_CAT_CD'].apply(lambda x : x == 10)][['STD_DD','USE_CNT','USE_AMT']]
store10_amt = store10_amt.reset_index()
del store10_amt['index']
store10_amt = store10_amt.rename(columns = {'STD_DD' : '일자', 'USE_CNT' : '이용건수' ,'USE_AMT':'이용금액'})
store10_amt # 숙박 일자별 이용금액

# 업종(20, 21) : 레저관련, 일자별 이용금액
store20_21_amt = card.loc[card['MCT_CAT_CD'].apply(lambda x : x == 20 or x == 21)][['STD_DD','USE_CNT','USE_AMT']]
store20_21_amt = store20_21_amt.reset_index()
del store20_21_amt['index']
store20_21_amt = store20_21_amt.rename(columns = {'STD_DD' : '일자', 'USE_CNT' : '이용건수' ,'USE_AMT':'이용금액'})
store20_21_amt # 레저, 일자별 이용금액

# 업종(22) : 문화취미, 일자별 이용금액
store22_amt = card.loc[card['MCT_CAT_CD'].apply(lambda x : x == 22)][['STD_DD','USE_CNT','USE_AMT']]
store22_amt = store22_amt.reset_index()
del store22_amt['index']
store22_amt = store22_amt.rename(columns = {'STD_DD' : '일자', 'USE_CNT' : '이용건수' ,'USE_AMT':'이용금액'})
store22_amt

# 업종(70) : 의료기관, 일자별 이용금액
store70_amt = card.loc[card['MCT_CAT_CD'].apply(lambda x : x == 70)][['STD_DD','USE_CNT','USE_AMT']]
store70_amt = store70_amt.reset_index()
del store70_amt['index']
store70_amt =store70_amt.rename(columns = {'STD_DD' : '일자', 'USE_CNT' : '이용건수' ,'USE_AMT':'이용금액'})
store70_amt

# 업종(71) : 보건위생, 일자별 이용금액
store71_amt = card.loc[card['MCT_CAT_CD'].apply(lambda x : x == 71)][['STD_DD','USE_CNT','USE_AMT']]
store71_amt = store71_amt.reset_index()
del store71_amt['index']
store71_amt =store71_amt.rename(columns = {'STD_DD' : '일자', 'USE_CNT' : '이용건수' ,'USE_AMT':'이용금액'})
store71_amt

# 업종(80, 81) : 요식업소,음료식품 일자별 이용금액
store80_81_amt = card.loc[card['MCT_CAT_CD'].apply(lambda x : x == 80 or x == 81)][['STD_DD','USE_CNT','USE_AMT']]
store80_81_amt = store80_81_amt.reset_index()
del store80_81_amt['index']
store80_81_amt = store80_81_amt.rename(columns = {'STD_DD' : '일자', 'USE_CNT' : '이용건수' ,'USE_AMT':'이용금액'})



# 오프라인 숙박 PN 컬럼 추가 ===============================================================

data = store10_amt[['일자','이용건수','이용금액']]
data = data.reset_index()
del data['index']

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


# 오프라인 문화취미 PN 컬럼 추가 ===============================================================
data = store22_amt[['일자','이용건수','이용금액']]
data = data.reset_index()
del data['index']

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


# 오프라인 식품 PN 컬럼 추가 ================================================================ 
data = store80_81_amt[['일자','이용건수','이용금액']]
data = data.reset_index()
del data['index']
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


# 오프라인 의료기관 PN 컬럼 추가 ================================================================ 
data= store70_amt[['일자','이용건수','이용금액']]
data = data.reset_index()
del data['index']
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



# 오프라인 보건위생 PN 컬럼 추가 ================================================================ 
data= store71_amt[['일자','이용건수','이용금액']]
data = data.reset_index()
del data['index']
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


# 오프라인 레저 PN 컬럼 추가 ================================================================ 
data = store20_21_amt[['일자','이용건수','이용금액']]
data = data.reset_index()
del data['index']
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




# 물류 데이터

mul = pd.read_excel('c:/data/mul.xlsx')
mul


# 온라인 문화취미(도서음반) PN 컬럼 추가 ================================================================ 
data = mul[['DL_YMD','DL_GD_LCLS_NM','DL_GD_LCLS_CD','INVC_CONT']]
data = data.loc[data['DL_GD_LCLS_CD'].apply(lambda x : x  == 12)][['DL_YMD','INVC_CONT']]
data = data.reset_index()
del data['index']
data.columns=['DATE','CN']

PN=[]
for i in data['DATE']:
    if str(i).startswith('1902'):
        PN.append(-0.448069969813029)
    elif str(i).startswith('1903'):
        PN.append(0.1945506234963735)
    elif str(i).startswith('1904'):
        PN.append(-0.02406144142150879)
    elif str(i).startswith('1905'):
        PN.append(-0.4979627847671509)
    elif str(i).startswith('2002'):
        PN.append(-0.12741482257843018)
    elif str(i).startswith('2003'):
        PN.append(0.1476357335394079)
    elif str(i).startswith('2004'):
        PN.append(0.43579452236493427)
    else:
        PN.append(0.14210561513900757)

data['PN']=PN
data.to_csv("C:/data/on_cul.csv", mode='w', index=False, encoding='utf-8')    


# 온라인 숙박(가구) PN 컬럼 추가 ================================================================ 
data = mul[['DL_YMD','DL_GD_LCLS_NM','DL_GD_LCLS_CD','INVC_CONT']]
data = data.loc[data['DL_GD_LCLS_CD'].apply(lambda x : x  == 10)][['DL_YMD','INVC_CONT']]
data = data.reset_index()
del data['index']
data.columns=['DATE','CN']

PN=[]
for i in data['DATE']:
    if str(i).startswith('1902'):
        PN.append(-0.1298816885266985)
    elif str(i).startswith('1903'):
        PN.append(-0.24523608173642839)
    elif str(i).startswith('1904'):
        PN.append(-0.5726537959916251)
    elif str(i).startswith('1905'):
        PN.append(-0.5188040807843208)
    elif str(i).startswith('2002'):
        PN.append(-0.10184521675109863)
    elif str(i).startswith('2003'):
        PN.append(0.7370842893918356)
    elif str(i).startswith('2004'):
        PN.append(-0.5253404080867767)
    else:
        PN.append(-0.5076049500041537)

data['PN']=PN
data.to_csv("C:/data/on_acco.csv", mode='w', index=False, encoding='utf-8')


# 온라인 보건위생(생활건강) PN 컬럼 추가 ================================================================ 
data = mul[['DL_YMD','DL_GD_LCLS_NM','DL_GD_LCLS_CD','INVC_CONT']]
data = data.loc[data['DL_GD_LCLS_CD'].apply(lambda x : x  == 15)][['DL_YMD','INVC_CONT']]
data = data.reset_index()
del data['index']
data.columns=['DATE','CN']

PN=[]
for i in data['DATE']:
    if str(i).startswith('1902'):
        PN.append(0.0242919921875)
    elif str(i).startswith('1903'):
        PN.append(-0.2546436531203134)
    elif str(i).startswith('1904'):
        PN.append(-0.25560569763183594)
    elif str(i).startswith('1905'):
        PN.append(0.4311133995652199)
    elif str(i).startswith('2002'):
        PN.append(-0.5093494653701782)
    elif str(i).startswith('2003'):
        PN.append(-0.4577632631574358)
    elif str(i).startswith('2004'):
        PN.append(-0.4161640836132897)
    else:
        PN.append(-0.06528772115707397)
      
data['PN']=PN
data.to_csv("C:/data/on_sani.csv", mode='w', index=False, encoding='utf-8')


# 온라인 레저(스포츠, 레저) PN 컬럼 추가 ================================================================ 
data  = mul[['DL_YMD','DL_GD_LCLS_NM','DL_GD_LCLS_CD','INVC_CONT']]
data = data.loc[data['DL_GD_LCLS_CD'].apply(lambda x : x  == 16)][['DL_YMD','INVC_CONT']]
data = data.reset_index()
del data['index']
data.columns=['DATE','CN']

PN=[]
for i in data['DATE']:
    if str(i).startswith('1902'):
        PN.append(0.29600413356508526)
    elif str(i).startswith('1903'):
        PN.append(-0.036042352517445884)
    elif str(i).startswith('1904'):
        PN.append(0.3428010770252773)
    elif str(i).startswith('1905'):
        PN.append(0.7659961325781686)
    elif str(i).startswith('2002'):
        PN.append(0.7704757792609078)
    elif str(i).startswith('2003'):
        PN.append(0.7231104969978333)
    elif str(i).startswith('2004'):
        PN.append(0.373626138482775)
    else:
        PN.append(0.35270217061042786)

data['PN']=PN
data.to_csv("C:/data/on_lei.csv", mode='w', index=False, encoding='utf-8')


# 온라인 식품(음식) PN 컬럼 추가 ================================================================ 
data  = mul[['DL_YMD','DL_GD_LCLS_NM','DL_GD_LCLS_CD','INVC_CONT']]
data = data.loc[data['DL_GD_LCLS_CD'].apply(lambda x : x  == 17)][['DL_YMD','INVC_CONT']]
data = data.reset_index()
del data['index']
data.columns=['DATE','CN']

PN=[]
for i in data['DATE']:
    if str(i).startswith('1902'):
        PN.append(0.48842278122901917)
    elif str(i).startswith('1903'):
        PN.append(0.4787071645259857)
    elif str(i).startswith('1904'):
        PN.append(0.5413034345422473)
    elif str(i).startswith('1905'):
        PN.append(-0.06888024674521552)
    elif str(i).startswith('2002'):
        PN.append(-0.017809921503067018)
    elif str(i).startswith('2003'):
        PN.append(-0.31325842227254597)
    elif str(i).startswith('2004'):
        PN.append(-0.06520995828840467)
    else:
        PN.append(-0.001237014929453532)

data['PN']=PN
data.to_csv("C:/data/on_food.csv", mode='w', index=False, encoding='utf-8')