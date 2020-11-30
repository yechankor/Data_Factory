# 3-3) 날짜 중복 제거

import pandas as pd
from pandas import Series, DataFrame

## 오프라인 숙박 =====================================================
data = pd.read_csv("C:/data/off_acco.csv", sep=',', encoding='utf-8')
date=data['DATE'].unique()
pn=data['PN'].groupby(data['DATE']).mean().reset_index(drop=True)
cn=data['CN'].groupby(data['DATE']).sum().reset_index(drop=True)
data=DataFrame({'DATE':date, 'PN':pn, 'CN':cn})
data.to_csv("C:/data/off_acco.csv", mode='w', index=False, encoding='utf-8')        

## 오프라인 문화취미 =====================================================
data = pd.read_csv("C:/data/off_cul.csv", sep=',', encoding='utf-8')
date=data['DATE'].unique()
pn=data['PN'].groupby(data['DATE']).mean().reset_index(drop=True)
cn=data['CN'].groupby(data['DATE']).sum().reset_index(drop=True)
data=DataFrame({'DATE':date, 'PN':pn, 'CN':cn})
data.to_csv("C:/data/off_cul.csv", mode='w', index=False, encoding='utf-8')        

## 오프라인 식품 =====================================================
data = pd.read_csv("C:/data/off_food.csv", sep=',', encoding='utf-8')
date=data['DATE'].unique()
pn=data['PN'].groupby(data['DATE']).mean().reset_index(drop=True)
cn=data['CN'].groupby(data['DATE']).sum().reset_index(drop=True)
data=DataFrame({'DATE':date, 'PN':pn, 'CN':cn})
data.to_csv("C:/data/off_food.csv", mode='w', index=False, encoding='utf-8')

## 오프라인 의료기관 =====================================================
data = pd.read_csv("C:/data/off_medi.csv", sep=',', encoding='utf-8')
date=data['DATE'].unique()
pn=data['PN'].groupby(data['DATE']).mean().reset_index(drop=True)
cn=data['CN'].groupby(data['DATE']).sum().reset_index(drop=True)
data=DataFrame({'DATE':date, 'PN':pn, 'CN':cn})
data.to_csv("C:/data/off_medi.csv", mode='w', index=False, encoding='utf-8')

## 오프라인 보건위생 =====================================================
data = pd.read_csv("C:/data/off_sani.csv", sep=',', encoding='utf-8')
date=data['DATE'].unique()
pn=data['PN'].groupby(data['DATE']).mean().reset_index(drop=True)
cn=data['CN'].groupby(data['DATE']).sum().reset_index(drop=True)
data=DataFrame({'DATE':date, 'PN':pn, 'CN':cn})
data.to_csv("C:/data/off_sani.csv", mode='w', index=False, encoding='utf-8')

## 오프라인 레저 =====================================================
data = pd.read_csv("C:/data/off_lei.csv", sep=',', encoding='utf-8')
date=data['DATE'].unique()
pn=data['PN'].groupby(data['DATE']).mean().reset_index(drop=True)
cn=data['CN'].groupby(data['DATE']).sum().reset_index(drop=True)
data=DataFrame({'DATE':date, 'PN':pn, 'CN':cn})
data.to_csv("C:/data/off_lei.csv", mode='w', index=False, encoding='utf-8')


## 온라인 숙박 =====================================================
data = pd.read_csv("C:/data/on_acco.csv", sep=',', encoding='utf-8')
date=data['DATE'].unique()
pn=data['PN'].groupby(data['DATE']).mean().reset_index(drop=True)
cn=data['CN'].groupby(data['DATE']).sum().reset_index(drop=True)
data=DataFrame({'DATE':date, 'PN':pn, 'CN':cn})
data.to_csv("C:/data/on_acco.csv", mode='w', index=False, encoding='utf-8')        

## 온라인 문화취미 =====================================================
data = pd.read_csv("C:/data/on_cul.csv", sep=',', encoding='utf-8')
date=data['DATE'].unique()
pn=data['PN'].groupby(data['DATE']).mean().reset_index(drop=True)
cn=data['CN'].groupby(data['DATE']).sum().reset_index(drop=True)
data=DataFrame({'DATE':date, 'PN':pn, 'CN':cn})
data.to_csv("C:/data/on_cul.csv", mode='w', index=False, encoding='utf-8')        

## 온라인 식품 =====================================================
data = pd.read_csv("C:/data/on_food.csv", sep=',', encoding='utf-8')
date=data['DATE'].unique()
pn=data['PN'].groupby(data['DATE']).mean().reset_index(drop=True)
cn=data['CN'].groupby(data['DATE']).sum().reset_index(drop=True)
data=DataFrame({'DATE':date, 'PN':pn, 'CN':cn})
data.to_csv("C:/data/on_food.csv", mode='w', index=False, encoding='utf-8')

## 온라인 보건위생 =====================================================
data = pd.read_csv("C:/data/on_sani.csv", sep=',', encoding='utf-8')
date=data['DATE'].unique()
pn=data['PN'].groupby(data['DATE']).mean().reset_index(drop=True)
cn=data['CN'].groupby(data['DATE']).sum().reset_index(drop=True)
data=DataFrame({'DATE':date, 'PN':pn, 'CN':cn})
data.to_csv("C:/data/on_sani.csv", mode='w', index=False, encoding='utf-8')

## 온라인 레저 =====================================================
data = pd.read_csv("C:/data/on_lei.csv", sep=',', encoding='utf-8')
date=data['DATE'].unique()
pn=data['PN'].groupby(data['DATE']).mean().reset_index(drop=True)
cn=data['CN'].groupby(data['DATE']).sum().reset_index(drop=True)
data=DataFrame({'DATE':date, 'PN':pn, 'CN':cn})
data.to_csv("C:/data/on_lei.csv", mode='w', index=False, encoding='utf-8')