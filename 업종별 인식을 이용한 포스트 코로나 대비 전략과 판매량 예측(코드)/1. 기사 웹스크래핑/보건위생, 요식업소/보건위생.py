from urllib.request import urlopen
from konlpy.tag import Okt 
okt=Okt()
from selenium import webdriver
from urllib.parse import quote
import csv


## RSTUDIO에서 Rselenium 자동화로 키워드별 중앙일보 기사 스크래핑하고 저장
## 저장된 파일을 리스트로 읽고 토큰화

### 보건위생 ################################################
## 검색 키워드: 보건위생, 마스크
quote('보건위생')
quote('마스크')

## 2019년 1월 
file = open("C:/data/health201901.csv","r")
data=file.read()
data=data.replace('\n',' ')
data=data.replace('\t',' ')
data=data.replace('<U+00A0>',' ')
data=data.split('.')
file.close()
# 토큰화
health201901=[]
for i in data:
    health201901.append(okt.morphs(i))
print(health201901)


## 2019년 2월
file=open("C:/data/health201902.csv","r")
data=file.read()
data=data.replace('\n',' ')
data=data.replace('\t',' ')
data=data.replace('<U+00A0>',' ')
data=data.split('.')
file.close()
# 토큰화
health201902=[]
for i in data:
    health201902.append(okt.morphs(i))
print(health201902)


## 2019년 3월 
file=open("C:/data/health201903.csv","r")
data=file.read()
data=data.replace('\n',' ')
data=data.replace('\t',' ')
data=data.replace('<U+00A0>',' ')
data=data.split('.')
file.close()
# 토큰화
health201903=[]
for i in data:
    health201903.append(okt.morphs(i))
print(health201903)


## 2019년 4월 
file=open("C:/data/health201904.csv","r")
data=file.read()
data=data.replace('\n',' ')
data=data.replace('\t',' ')
data=data.replace('<U+00A0>',' ')
data=data.split('.')
file.close()
# 토큰화
health201904=[]
for i in data:
    health201904.append(okt.morphs(i))
print(health201904)


## 2019년 5월 
file=open("C:/data/health201905.csv","r")
data=file.read()
data=data.replace('\n',' ')
data=data.replace('\t',' ')
data=data.replace('<U+00A0>',' ')
data=data.split('.')
file.close()
# 토큰화
health201905=[]
for i in data:
    health201905.append(okt.morphs(i))
print(health201905)


## 2020년 1월 
file=open("C:/data/health202001.csv","r")
data=file.read()
data=data.replace('\n',' ')
data=data.replace('\t',' ')
data=data.replace('<U+00A0>',' ')
data=data.split('.')
file.close()
# 토큰화
health202001=[]
for i in data:
    health202001.append(okt.morphs(i))
print(health202001)


## 2020년 2월
file=open("C:/data/health202002.csv","r")
data=file.read()
data=data.replace('\n',' ')
data=data.replace('\t',' ')
data=data.replace('<U+00A0>',' ')
data=data.split('.')
file.close()
# 토큰화
health202002=[]
for i in data:
    health202002.append(okt.morphs(i))
print(health202002)


## 2020년 3월 
file=open("C:/data/health202003.csv","r")
data=file.read()
data=data.replace('\n',' ')
data=data.replace('\t',' ')
data=data.replace('<U+00A0>',' ')
data=data.split('.')
file.close()
# 토큰화
health202003=[]
for i in data:
    health202003.append(okt.morphs(i))
print(health202003)


## 2020년 4월 
file=open("C:/data/health202004.csv","r")
data=file.read()
data=data.replace('\n',' ')
data=data.replace('\t',' ')
data=data.replace('<U+00A0>',' ')
data=data.split('.')
file.close()
# 토큰화
health202004=[]
for i in data:
    health202004.append(okt.morphs(i))
print(health202004)


## 2019년 5월 
file=open("C:/data/health202005.csv","r")
data=file.read()
print(data)
data=data.replace('\n',' ')
data=data.replace('\t',' ')
data=data.replace('<U+00A0>',' ')
data=data.split('.')
file.close()
# 토큰화
health=[]
for i in data:
    health.append(okt.morphs(i))
print(health)








