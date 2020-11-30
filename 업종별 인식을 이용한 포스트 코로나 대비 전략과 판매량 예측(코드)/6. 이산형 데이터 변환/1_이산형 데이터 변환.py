off_data=pd.read_csv("C:/data/off_data.csv", encoding='utf-8')
on_data=pd.read_csv("C:/data/on_data.csv", encoding='utf-8')

## 연속형 데이터를 이산형 데이터로 변환

## CN변수: 이전보다 50%이상 감소/증가한 경우 1, 그렇지 않은 경우 0
## PN변수: 음수인 경우 0, 양수인 경우 1로 분류
## COVID 변수: 0인 경우 0으로, 0이외의 값 중 50%분위값 10019를 기준으로 1,2로 분류
np.percentile(off_data['COVID'][off_data['COVID']!=0],50)


## 오프라인 숙박==========================================================================
data=pd.read_csv("C:/data/off_acco.csv", encoding='utf-8')

# 이산형 변수로 변환
cn=data['CN']
new_cn=[]
for i in range(len(cn)):
    if i==0:
        new_cn.append(0)
    elif ((cn[i]-cn[i-1])/cn[i-1] >= 0.10) | ((cn[i]-cn[i-1])/cn[i-1] <= -0.10):
        new_cn.append(1)
    else:
        new_cn.append(0)
   
sum(new_cn)
len(new_cn)

new_pn=[]
for i in range(len(data['PN'])):
    if data['PN'][i]>0:
        new_pn.append(1)
    else:
        new_pn.append(0)
        
new_covid=[]
for i in range(len(data['COVID'])):
    if data['COVID'][i]==0:
        new_covid.append(0)
    elif data['COVID'][i]>=10019:
        new_covid.append(2)
    else:
        new_covid.append(1)
        
data['CN']=new_cn
data['PN']=new_pn
data['COVID']=new_covid

# 데이터 프레임 행을 랜덤하게 섞기
data=data.sample(frac=1).reset_index(drop=True)

train=data[:int(len(data)*0.6)]
test=data[int(len(data)*0.6):]

train.to_csv("C:/data/off_acco(train).csv")
test.to_csv("C:/data/off_acco(test).csv")


## 오프라인 문화취미 ==========================================================================
data=pd.read_csv("C:/data/off_cul.csv", encoding='utf-8')

# 이산형 변수로 변환
cn=data['CN']
new_cn=[]
for i in range(len(cn)):
    if i==0:
        new_cn.append(0)
    elif ((cn[i]-cn[i-1])/cn[i-1] >= 0.10) | ((cn[i]-cn[i-1])/cn[i-1] <= -0.10):
        new_cn.append(1)
    else:
        new_cn.append(0)
   
sum(new_cn)
len(new_cn)

new_pn=[]
for i in range(len(data['PN'])):
    if data['PN'][i]>0:
        new_pn.append(1)
    else:
        new_pn.append(0)
        
new_covid=[]
for i in range(len(data['COVID'])):
    if data['COVID'][i]==0:
        new_covid.append(0)
    elif data['COVID'][i]>=10019:
        new_covid.append(2)
    else:
        new_covid.append(1)
        
data['CN']=new_cn
data['PN']=new_pn
data['COVID']=new_covid

# 데이터 프레임 행을 랜덤하게 섞기
data=data.sample(frac=1).reset_index(drop=True)

train=data[:int(len(data)*0.6)]
test=data[int(len(data)*0.6):]

train.to_csv("C:/data/off_cul(train).csv")
test.to_csv("C:/data/off_cul(test).csv")


## 오프라인 식품==========================================================================
data=pd.read_csv("C:/data/off_food.csv", encoding='utf-8')

# 이산형 변수로 변환
cn=data['CN']
new_cn=[]
for i in range(len(cn)):
    if i==0:
        new_cn.append(0)
    elif ((cn[i]-cn[i-1])/cn[i-1] >= 0.10) | ((cn[i]-cn[i-1])/cn[i-1] <= -0.10):
        new_cn.append(1)
    else:
        new_cn.append(0)
   
sum(new_cn)
len(new_cn)

new_pn=[]
for i in range(len(data['PN'])):
    if data['PN'][i]>0:
        new_pn.append(1)
    else:
        new_pn.append(0)
        
new_covid=[]
for i in range(len(data['COVID'])):
    if data['COVID'][i]==0:
        new_covid.append(0)
    elif data['COVID'][i]>=10019:
        new_covid.append(2)
    else:
        new_covid.append(1)
        
data['CN']=new_cn
data['PN']=new_pn
data['COVID']=new_covid

# 데이터 프레임 행을 랜덤하게 섞기
data=data.sample(frac=1).reset_index(drop=True)

train=data[:int(len(data)*0.6)]
test=data[int(len(data)*0.6):]

train.to_csv("C:/data/off_food(train).csv")
test.to_csv("C:/data/off_food(test).csv")


## 오프라인 레저==========================================================================
data=pd.read_csv("C:/data/off_lei.csv", encoding='utf-8')

# 이산형 변수로 변환
cn=data['CN']
new_cn=[]
for i in range(len(cn)):
    if i==0:
        new_cn.append(0)
    elif ((cn[i]-cn[i-1])/cn[i-1] >= 0.10) | ((cn[i]-cn[i-1])/cn[i-1] <= -0.10):
        new_cn.append(1)
    else:
        new_cn.append(0)
   
sum(new_cn)
len(new_cn)

new_pn=[]
for i in range(len(data['PN'])):
    if data['PN'][i]>0:
        new_pn.append(1)
    else:
        new_pn.append(0)
        
new_covid=[]
for i in range(len(data['COVID'])):
    if data['COVID'][i]==0:
        new_covid.append(0)
    elif data['COVID'][i]>=10019:
        new_covid.append(2)
    else:
        new_covid.append(1)
        
data['CN']=new_cn
data['PN']=new_pn
data['COVID']=new_covid

# 데이터 프레임 행을 랜덤하게 섞기
data=data.sample(frac=1).reset_index(drop=True)

train=data[:int(len(data)*0.6)]
test=data[int(len(data)*0.6):]

train.to_csv("C:/data/off_lei(train).csv")
test.to_csv("C:/data/off_lei(test).csv")


## 오프라인 의료==========================================================================
data=pd.read_csv("C:/data/off_medi.csv", encoding='utf-8')

# 이산형 변수로 변환
cn=data['CN']
new_cn=[]
for i in range(len(cn)):
    if i==0:
        new_cn.append(0)
    elif ((cn[i]-cn[i-1])/cn[i-1] >= 0.10) | ((cn[i]-cn[i-1])/cn[i-1] <= -0.10):
        new_cn.append(1)
    else:
        new_cn.append(0)
   
sum(new_cn)
len(new_cn)

new_pn=[]
for i in range(len(data['PN'])):
    if data['PN'][i]>0:
        new_pn.append(1)
    else:
        new_pn.append(0)
        
new_covid=[]
for i in range(len(data['COVID'])):
    if data['COVID'][i]==0:
        new_covid.append(0)
    elif data['COVID'][i]>=10019:
        new_covid.append(2)
    else:
        new_covid.append(1)
        
data['CN']=new_cn
data['PN']=new_pn
data['COVID']=new_covid

# 데이터 프레임 행을 랜덤하게 섞기
data=data.sample(frac=1).reset_index(drop=True)

train=data[:int(len(data)*0.6)]
test=data[int(len(data)*0.6):]

train.to_csv("C:/data/off_medi(train).csv")
test.to_csv("C:/data/off_medi(test).csv")


## 오프라인 보건위생==========================================================================
data=pd.read_csv("C:/data/off_sani.csv", encoding='utf-8')

# 이산형 변수로 변환
cn=data['CN']
new_cn=[]
for i in range(len(cn)):
    if i==0:
        new_cn.append(0)
    elif ((cn[i]-cn[i-1])/cn[i-1] >= 0.10) | ((cn[i]-cn[i-1])/cn[i-1] <= -0.10):
        new_cn.append(1)
    else:
        new_cn.append(0)
   
sum(new_cn)
len(new_cn)

new_pn=[]
for i in range(len(data['PN'])):
    if data['PN'][i]>0:
        new_pn.append(1)
    else:
        new_pn.append(0)
        
new_covid=[]
for i in range(len(data['COVID'])):
    if data['COVID'][i]==0:
        new_covid.append(0)
    elif data['COVID'][i]>=10019:
        new_covid.append(2)
    else:
        new_covid.append(1)
        
data['CN']=new_cn
data['PN']=new_pn
data['COVID']=new_covid

# 데이터 프레임 행을 랜덤하게 섞기
data=data.sample(frac=1).reset_index(drop=True)

train=data[:int(len(data)*0.6)]
test=data[int(len(data)*0.6):]

train.to_csv("C:/data/off_sani(train).csv")
test.to_csv("C:/data/off_sani(test).csv")



## 온라인 숙박==========================================================================
data=pd.read_csv("C:/data/on_acco.csv", encoding='utf-8')

# 이산형 변수로 변환
cn=data['CN']
new_cn=[]
for i in range(len(cn)):
    if i==0:
        new_cn.append(0)
    elif ((cn[i]-cn[i-1])/cn[i-1] >= 0.10) | ((cn[i]-cn[i-1])/cn[i-1] <= -0.10):
        new_cn.append(1)
    else:
        new_cn.append(0)
   
sum(new_cn)
len(new_cn)

new_pn=[]
for i in range(len(data['PN'])):
    if data['PN'][i]>0:
        new_pn.append(1)
    else:
        new_pn.append(0)
        
new_covid=[]
for i in range(len(data['COVID'])):
    if data['COVID'][i]==0:
        new_covid.append(0)
    elif data['COVID'][i]>=10019:
        new_covid.append(2)
    else:
        new_covid.append(1)
        
data['CN']=new_cn
data['PN']=new_pn
data['COVID']=new_covid

# 데이터 프레임 행을 랜덤하게 섞기
data=data.sample(frac=1).reset_index(drop=True)

train=data[:int(len(data)*0.6)]
test=data[int(len(data)*0.6):]

train.to_csv("C:/data/on_acco(train).csv")
test.to_csv("C:/data/on_acco(test).csv")


## 온라인 문화취미 ==========================================================================
data=pd.read_csv("C:/data/on_cul.csv", encoding='utf-8')

# 이산형 변수로 변환
cn=data['CN']
new_cn=[]
for i in range(len(cn)):
    if i==0:
        new_cn.append(0)
    elif ((cn[i]-cn[i-1])/cn[i-1] >= 0.10) | ((cn[i]-cn[i-1])/cn[i-1] <= -0.10):
        new_cn.append(1)
    else:
        new_cn.append(0)
   
sum(new_cn)
len(new_cn)

new_pn=[]
for i in range(len(data['PN'])):
    if data['PN'][i]>0:
        new_pn.append(1)
    else:
        new_pn.append(0)
        
new_covid=[]
for i in range(len(data['COVID'])):
    if data['COVID'][i]==0:
        new_covid.append(0)
    elif data['COVID'][i]>=10019:
        new_covid.append(2)
    else:
        new_covid.append(1)
        
data['CN']=new_cn
data['PN']=new_pn
data['COVID']=new_covid

# 데이터 프레임 행을 랜덤하게 섞기
data=data.sample(frac=1).reset_index(drop=True)

train=data[:int(len(data)*0.6)]
test=data[int(len(data)*0.6):]

train.to_csv("C:/data/on_cul(train).csv")
test.to_csv("C:/data/on_cul(test).csv")


## 온라인 식품==========================================================================
data=pd.read_csv("C:/data/on_food.csv", encoding='utf-8')

# 이산형 변수로 변환
cn=data['CN']
new_cn=[]
for i in range(len(cn)):
    if i==0:
        new_cn.append(0)
    elif ((cn[i]-cn[i-1])/cn[i-1] >= 0.10) | ((cn[i]-cn[i-1])/cn[i-1] <= -0.10):
        new_cn.append(1)
    else:
        new_cn.append(0)
   
sum(new_cn)
len(new_cn)

new_pn=[]
for i in range(len(data['PN'])):
    if data['PN'][i]>0:
        new_pn.append(1)
    else:
        new_pn.append(0)
        
new_covid=[]
for i in range(len(data['COVID'])):
    if data['COVID'][i]==0:
        new_covid.append(0)
    elif data['COVID'][i]>=10019:
        new_covid.append(2)
    else:
        new_covid.append(1)
        
data['CN']=new_cn
data['PN']=new_pn
data['COVID']=new_covid

# 데이터 프레임 행을 랜덤하게 섞기
data=data.sample(frac=1).reset_index(drop=True)

train=data[:int(len(data)*0.6)]
test=data[int(len(data)*0.6):]

train.to_csv("C:/data/on_food(train).csv")
test.to_csv("C:/data/on_food(test).csv")


## 온라인 레저==========================================================================
data=pd.read_csv("C:/data/on_lei.csv", encoding='utf-8')

# 이산형 변수로 변환
cn=data['CN']
new_cn=[]
for i in range(len(cn)):
    if i==0:
        new_cn.append(0)
    elif ((cn[i]-cn[i-1])/cn[i-1] >= 0.10) | ((cn[i]-cn[i-1])/cn[i-1] <= -0.10):
        new_cn.append(1)
    else:
        new_cn.append(0)
   
sum(new_cn)
len(new_cn)

new_pn=[]
for i in range(len(data['PN'])):
    if data['PN'][i]>0:
        new_pn.append(1)
    else:
        new_pn.append(0)
        
new_covid=[]
for i in range(len(data['COVID'])):
    if data['COVID'][i]==0:
        new_covid.append(0)
    elif data['COVID'][i]>=10019:
        new_covid.append(2)
    else:
        new_covid.append(1)
        
data['CN']=new_cn
data['PN']=new_pn
data['COVID']=new_covid

# 데이터 프레임 행을 랜덤하게 섞기
data=data.sample(frac=1).reset_index(drop=True)

train=data[:int(len(data)*0.6)]
test=data[int(len(data)*0.6):]

train.to_csv("C:/data/on_lei(train).csv")
test.to_csv("C:/data/on_lei(test).csv")


## 온라인 보건위생==========================================================================
data=pd.read_csv("C:/data/on_sani.csv", encoding='utf-8')

# 이산형 변수로 변환
cn=data['CN']
new_cn=[]
for i in range(len(cn)):
    if i==0:
        new_cn.append(0)
    elif ((cn[i]-cn[i-1])/cn[i-1] >= 0.10) | ((cn[i]-cn[i-1])/cn[i-1] <= -0.10):
        new_cn.append(1)
    else:
        new_cn.append(0)
   
sum(new_cn)
len(new_cn)

new_pn=[]
for i in range(len(data['PN'])):
    if data['PN'][i]>0:
        new_pn.append(1)
    else:
        new_pn.append(0)
        
new_covid=[]
for i in range(len(data['COVID'])):
    if data['COVID'][i]==0:
        new_covid.append(0)
    elif data['COVID'][i]>=10019:
        new_covid.append(2)
    else:
        new_covid.append(1)
        
data['CN']=new_cn
data['PN']=new_pn
data['COVID']=new_covid

# 데이터 프레임 행을 랜덤하게 섞기
data=data.sample(frac=1).reset_index(drop=True)

train=data[:int(len(data)*0.6)]
test=data[int(len(data)*0.6):]

train.to_csv("C:/data/on_sani(train).csv")
test.to_csv("C:/data/on_sani(test).csv")