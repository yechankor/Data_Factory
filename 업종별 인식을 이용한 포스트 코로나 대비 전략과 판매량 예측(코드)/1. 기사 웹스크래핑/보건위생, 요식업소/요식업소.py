from urllib.request import urlopen
from konlpy.tag import Okt 
okt=Okt()
from selenium import webdriver
from urllib.parse import quote
import csv


### 요식업소 ################################################
## 검색 키워드: 요식업소, 커피전문점, 주점
quote('요식업')
quote('커피전문점')
quote('주점')

## 2019년 1월 
file=open("C:/data/food201901.csv","r")
data=file.read()
data=data.replace('\n',' ')
data=data.replace('\t',' ')
data=data.replace('<U+00A0>',' ')
data=data.split('.')
file.close()
# 토큰화
food201901=[]
for i in data:
    food201901.append(okt.morphs(i))
print(food201901)


## 2019년 2월
# R에서 만든 파일 리스트로 읽기
file=open("C:/data/food201902.csv","r")
data=file.read()
data=data.replace('\n',' ')
data=data.replace('\t',' ')
data=data.replace('<U+00A0>',' ')
data=data.split('.')
file.close()
# 토큰화
food201902=[]
for i in data:
    food201902.append(okt.morphs(i))
print(food201902)


## 2019년 3월 
file=open("C:/data/food201903.csv","r")
data=file.read()
data=data.replace('\n',' ')
data=data.replace('\t',' ')
data=data.replace('<U+00A0>',' ')
data=data.split('.')
file.close()
# 토큰화
food201903=[]
for i in data:
    food201903.append(okt.morphs(i))
print(food201903)


## 2019년 4월 
file=open("C:/data/food201904.csv","r")
data=file.read()
data=data.replace('\n',' ')
data=data.replace('\t',' ')
data=data.replace('<U+00A0>',' ')
data=data.split('.')
file.close()
# 토큰화
food201904=[]
for i in data:
    food201904.append(okt.morphs(i))
print(food201904)


## 2019년 5월 
file=open("C:/data/food201905.csv","r")
data=file.read()
data=data.replace('\n',' ')
data=data.replace('\t',' ')
data=data.replace('<U+00A0>',' ')
data=data.split('.')
file.close()
# 토큰화
food201905=[]
for i in data:
    food201905.append(okt.morphs(i))
print(food201905)


## 2020년 1월 
file=open("C:/data/food202001.csv","r")
data=file.read()
data=data.replace('\n',' ')
data=data.replace('\t',' ')
data=data.replace('<U+00A0>',' ')
data=data.split('.')
file.close()
# 토큰화
food202001=[]
for i in data:
    food202001.append(okt.morphs(i))
print(food202001)


## 2020년 2월
file=open("C:/data/food202002.csv","r")
data=file.read()
data=data.replace('\n',' ')
data=data.replace('\t',' ')
data=data.replace('<U+00A0>',' ')
data=data.split('.')
file.close()
# 토큰화
food202002=[]
for i in data:
    food202002.append(okt.morphs(i))
print(food202002)


## 2020년 3월 
file=open("C:/data/food202003.csv","r")
data=file.read()
data=data.replace('\n',' ')
data=data.replace('\t',' ')
data=data.replace('<U+00A0>',' ')
data=data.split('.')
file.close()
# 토큰화
food202003=[]
for i in data:
    food202003.append(okt.morphs(i))
print(food202003)


## 2020년 4월 
file=open("C:/data/food202004.csv","r")
data=file.read()
data=data.replace('\n',' ')
data=data.replace('\t',' ')
data=data.replace('<U+00A0>',' ')
data=data.split('.')
file.close()
# 토큰화
food202004=[]
for i in data:
    food202004.append(okt.morphs(i))
print(food202004)


## 2019년 5월 
file=open("C:/data/food202005.csv","r")
data=file.read()
data=data.replace('\n',' ')
data=data.replace('\t',' ')
data=data.replace('<U+00A0>',' ')
data=data.split('.')
file.close()
# 토큰화
food202005=[]
for i in data:
    food202005.append(okt.morphs(i))
print(food202005)