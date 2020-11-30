# 4-1) COVID 데이터 확인

import urllib.request as ul
import xmltodict
import json
import urllib.request as req
from urllib.request import urlopen
import collections
from bs4 import BeautifulSoup
import re
import pandas as pd
import numpy as np
from numpy import nan as na
from pandas import Series, DataFrame
import requests


'''
#코로나 관련 api 데이터 불러오기 ==================================================================
url = 'http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19InfStateJson?serviceKey=XeJGjpN7Je52s%2Fv39kkPFHksdN0vpWoxItodj0U%2BUkM3QFuJyOZdSSwPLOdfs2W41JUDQqirDfGBOmku5lw9wg%3D%3D&pageNo=1&numOfRows=1000&startCreateDt=20200101&endCreateDt=20200901'
request = ul.Request(url)
response = ul.urlopen(request)
rescode = response.getcode()
if(rescode == 200):
    responseData = response.read()
    rD = xmltodict.parse(responseData)
    rDJ = json.dumps(rD) # dict 형식을 json형식으로 변환
    rDD = json.loads(rDJ) # json 형식을 dict 형식으로 변환
    print(rDD)
    w_data = rDD['response']['body']['items']['item']

corona = pd.DataFrame(w_data)
corona = pd.DataFrame(corona)
corona = corona.sort_index(by='stateDt')
corona = corona.reset_index(drop=True)
corona = corona.fillna(0)
corona = corona.loc[:, ['stateDt', 'decideCnt']]
corona.to_excel('c:/data/corona1.xlsx', index=False)
'''

# covid 변수에 필요한 확진자수 데이터 뽑아오기
covid = pd.read_excel('c:/data/corona1.xlsx')
covid = covid.rename(columns={'stateDt':'기준 일', 'decideCnt':'확진자 수'})
covid = covid.loc[covid['기준 일'].apply(lambda  x : 20200201 <= x <= 20200531)]
covid = covid.drop([4, 7, 9, 10, 11, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 33, 35, 37, 39, 40, 42, 44, 46, 48, 50, 52, 54, 56, 57, 58, 82, 92, 116, 117]).values # 특정 행만 삭제
covid = pd.DataFrame(covid)
covid = covid.rename(columns = {0:'DATE', 1:'COVID'})
covid.to_csv('c:/data/covid.csv')