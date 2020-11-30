import collections
import pandas as pd
import numpy as np
from numpy import nan as na
from pandas import Series, DataFrame
import urllib.request as req
from urllib.request import urlopen
from urllib.parse import quote # 아스키 문자로 변환해주는 함수
import json
from fake_useragent import UserAgent
import requests
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
import time
from selenium import webdriver
import re
import lxml.html
from bs4 import NavigableString
import urllib.request as req
from konlpy.tag import Okt
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import scale
from nltk import NaiveBayesClassifier
from nltk.tokenize import word_tokenize
import nltk
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB # 다항분포 나이브 베이즈 모델
from sklearn.metrics import accuracy_score #정확도 계산
pd.set_option("display.max_rows", 1400) # 보여지는 행 개수 조정
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from collections import Counter
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

pd.set_option("display.max_rows", 1500) # 보여지는 행 개수 조정
#====================================================================================
# 해리포터와 마법사의 돌

stone_df = pd.DataFrame(columns = ['review', 'score'])

stone_review_lst = []
stone_score_lst = []
for i in range(1, 160):
    url = 'https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn?code=30688&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false&page={}'
    li = url.format(i)
    res = req.urlopen(li)
    soup = BeautifulSoup(res, 'html.parser')
    review = soup.select('div.score_reple')
    score = soup.select('div.star_score')
    for j in review:
        stone_review_lst.append(j.find('span').get_text().strip())
    for k in score:
        stone_score_lst.append(k.find('em').get_text().strip())

stone_review_lst
stone_score_lst


stone_df['score'] = stone_score_lst
stone_df['review'] = stone_review_lst


stone_df.to_csv('c:/data/harry_stone.csv', encoding='utf-8', index=False)
stone_df = pd.read_csv('c:/data/harry_stone.csv')
stone_df = stone_df.dropna()
stone_df.reset_index(drop=True, inplace=True)
stone_df

harryporter_stone = stone_df

harryporter_stone = harryporter_stone.reset_index(drop=True)
harryporter_stone

harryporter_stone.to_csv('c:/data/harryporter_stone.csv', encoding='utf-8', index=False)
harryporter_stone = harryporter_stone.dropna(axis=0, how='any')
harryporter_stone = harryporter_stone.reset_index(drop=True)

harryporter_stone


harryporter_stone['review'] = harryporter_stone['review'].str.replace('!', '')
harryporter_stone['review'] = harryporter_stone['review'].str.replace('ㅠ', '')
harryporter_stone['review'] = harryporter_stone['review'].str.replace('ㅜ', '')
harryporter_stone['review'] = harryporter_stone['review'].str.replace('ㅡ', '')
harryporter_stone['review'] = harryporter_stone['review'].str.replace('ㅋ', '')
harryporter_stone['review'] = harryporter_stone['review'].str.replace('ㅎ', '')
harryporter_stone['review'] = harryporter_stone['review'].str.replace('.', '')
harryporter_stone['review'] = harryporter_stone['review'].str.replace('[-=+;:,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…♥♡》]', '')

harryporter_stone['review']


harryporter_stone.columns = ['리뷰', '평점']
harryporter_stone['긍정/부정'] = ''
harryporter_stone


harryporter_stone.loc[harryporter_stone['평점'] >= 7, '긍정/부정'] = '긍정'
harryporter_stone.loc[harryporter_stone['평점'] <= 6, '긍정/부정'] = '부정'

harryporter_stone

harryporter_stone = harryporter_stone.drop_duplicates()
harryporter_stone.to_csv('c:/data/harryporter_stone.csv', encoding='utf-8')
harryporter_stone


#====================================================================================
# 해리포터와 비밀의 방




room_df = pd.DataFrame(columns = ['review', 'score'])

room_review_lst = []
room_score_lst = []
for i in range(1, 150):
    url = 'https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn?code=33930&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false&page={}'
    li = url.format(i)
    res = req.urlopen(li)
    soup = BeautifulSoup(res, 'html.parser')
    review = soup.select('div.score_reple')
    score = soup.select('div.star_score')
    for j in review:
        room_review_lst.append(j.find('span').get_text().strip())
    for k in score:
        room_score_lst.append(k.find('em').get_text().strip())

room_review_lst
room_score_lst


room_df['score'] = room_score_lst
room_df['review'] = room_review_lst



room_df

room_df.to_csv('c:/data/room_df.csv', encoding='cp949', index=False)
room_df = pd.read_csv('c:/data/room_df.csv', encoding='cp949')
room_df
room_df = room_df.dropna()
room_df.reset_index(drop=True, inplace=True)
room_df
harryporter_room = room_df
harryporter_room


harryporter_room['review'] = harryporter_room['review'].str.replace('!!', '')
harryporter_room['review'] = harryporter_room['review'].str.replace('ㅠ', '')
harryporter_room['review'] = harryporter_room['review'].str.replace('ㅜ', '')
harryporter_room['review'] = harryporter_room['review'].str.replace('ㅋ', '')
harryporter_room['review'] = harryporter_room['review'].str.replace('ㅎ', '')
harryporter_room['review'] = harryporter_room['review'].str.replace('.', '')
harryporter_room['review'] = harryporter_room['review'].str.replace('[-=+;:,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…♥♡》]', '')

harryporter_room.columns = ['리뷰', '평점']
harryporter_room['긍정/부정'] = ''
harryporter_room = harryporter_room.reset_index(drop=True)

harryporter_room.loc[harryporter_room['평점'] >= 7, '긍정/부정'] = '긍정'
harryporter_room.loc[harryporter_room['평점'] <= 6, '긍정/부정'] = '부정'

harryporter_room.to_csv('c:/data/harryporter_room.csv', encoding='cp949')
harryporter_room

#====================================================================================
# 해리포터와 아즈카반의 죄수



azkaban_df = pd.DataFrame(columns = ['review', 'score'])

azkaban_review_lst = []
azkaban_score_lst = []
for i in range(1, 150):
    url = 'https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn?code=35546&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false&page={}'
    li = url.format(i)
    res = req.urlopen(li)
    soup = BeautifulSoup(res, 'html.parser')
    review = soup.select('div.score_reple')
    score = soup.select('div.star_score')
    for j in review:
        azkaban_review_lst.append(j.find('span').get_text().strip())
    for k in score:
        azkaban_score_lst.append(k.find('em').get_text().strip())

azkaban_review_lst
azkaban_score_lst


azkaban_df['score'] = azkaban_score_lst
azkaban_df['review'] = azkaban_review_lst

azkaban_df

azkaban_df.to_csv('c:/data/azkaban_df.csv', encoding='cp949', index=False)
azkaban_df = pd.read_csv('c:/data/azkaban_df.csv', encoding='cp949')
azkaban_df = azkaban_df.dropna()
azkaban_df.reset_index(drop=True, inplace=True)
azkaban_df

harryporter_azkaban = azkaban_df
harryporter_azkaban



harryporter_azkaban['review'] = harryporter_azkaban['review'].str.replace('!!', '')
harryporter_azkaban['review'] = harryporter_azkaban['review'].str.replace('ㅠ', '')
harryporter_azkaban['review'] = harryporter_azkaban['review'].str.replace('ㅜ', '')
harryporter_azkaban['review'] = harryporter_azkaban['review'].str.replace('.', '')
harryporter_azkaban['review'] = harryporter_azkaban['review'].str.replace('ㅋ', '')
harryporter_azkaban['review'] = harryporter_azkaban['review'].str.replace('ㅎ', '')
harryporter_azkaban['review'] = harryporter_azkaban['review'].str.replace('[-=+;:,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…♥♡》]', '')

harryporter_azkaban

harryporter_azkaban.columns = ['리뷰', '평점']
harryporter_azkaban['긍정/부정'] = ''
harryporter_azkaban


harryporter_azkaban.loc[harryporter_azkaban['평점'] >= 7, '긍정/부정'] = '긍정'
harryporter_azkaban.loc[harryporter_azkaban['평점'] <= 6, '긍정/부정'] = '부정'


harryporter_azkaban.to_csv('c:/data/harryporter_azkaban.csv', encoding='cp949')
harryporter_azkaban


#====================================================================================
# 해리포터와 불의 잔


fire_df = pd.DataFrame(columns = ['review', 'score'])

fire_review_lst = []
fire_score_lst = []
for i in range(1, 150):
    url = 'https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn?code=37883&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false&page={}'
    li = url.format(i)
    res = req.urlopen(li)
    soup = BeautifulSoup(res, 'html.parser')
    review = soup.select('div.score_reple')
    score = soup.select('div.star_score')
    for j in review:
        fire_review_lst.append(j.find('span').get_text().strip())
    for k in score:
        fire_score_lst.append(k.find('em').get_text().strip())

fire_review_lst
fire_score_lst


fire_df['score'] = fire_score_lst
fire_df['review'] = fire_review_lst


fire_df

fire_df.to_csv('c:/data/fire_df.csv', encoding='cp949', index=False)
fire_df = pd.read_csv('c:/data/fire_df.csv', encoding='cp949')
fire_df = fire_df.dropna()
fire_df.reset_index(drop=True, inplace=True)
fire_df

harryporter_fire = fire_df
harryporter_fire


harryporter_fire['review'] = harryporter_fire['review'].str.replace('!!', '')
harryporter_fire['review'] = harryporter_fire['review'].str.replace('ㅠ', '')
harryporter_fire['review'] = harryporter_fire['review'].str.replace('ㅜ', '')
harryporter_fire['review'] = harryporter_fire['review'].str.replace('.', '')
harryporter_fire['review'] = harryporter_fire['review'].str.replace('ㅋ', '')
harryporter_fire['review'] = harryporter_fire['review'].str.replace('ㅎ', '')
harryporter_fire['review'] = harryporter_fire['review'].str.replace('[-=+;:,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…♥♡》]', '')

harryporter_fire

harryporter_fire.columns = ['리뷰', '평점']
harryporter_fire['긍정/부정'] = ''
harryporter_fire

harryporter_fire.loc[harryporter_fire['평점'] >= 7, '긍정/부정'] = '긍정'
harryporter_fire.loc[harryporter_fire['평점'] <= 6, '긍정/부정'] = '부정'

harryporter_fire.to_csv('c:/data/harryporter_fire.csv', encoding='cp949')
harryporter_fire



#====================================================================================
# 해리포터와 불사조 기사단

phoenix_df = pd.DataFrame(columns = ['review', 'score'])

phoenix_review_lst = []
phoenix_score_lst = []
for i in range(1, 150):
    url = 'https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn?code=57095&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=1&page={}'
    li = url.format(i)
    res = req.urlopen(li)
    soup = BeautifulSoup(res, 'html.parser')
    review = soup.select('div.score_reple')
    score = soup.select('div.star_score')
    for j in review:
        phoenix_review_lst.append(j.find('span').get_text().strip())
    for k in score:
        phoenix_score_lst.append(k.find('em').get_text().strip())

phoenix_review_lst
phoenix_score_lst

phoenix_df['score'] = phoenix_score_lst
phoenix_df['review'] = phoenix_review_lst

phoenix_df

phoenix_df.to_csv('c:/data/phoenix_df.csv', encoding='cp949', index=False)
phoenix_df = pd.read_csv('c:/data/phoenix_df.csv', encoding='cp949')
phoenix_df = phoenix_df.dropna()
phoenix_df.reset_index(drop=True, inplace=True)
phoenix_df

harryporter_phoenix = phoenix_df
harryporter_phoenix


harryporter_phoenix['review'] = harryporter_phoenix['review'].str.replace('!!', '')
harryporter_phoenix['review'] = harryporter_phoenix['review'].str.replace('ㅠ', '')
harryporter_phoenix['review'] = harryporter_phoenix['review'].str.replace('ㅜ', '')
harryporter_phoenix['review'] = harryporter_phoenix['review'].str.replace('.', '')
harryporter_phoenix['review'] = harryporter_phoenix['review'].str.replace('ㅋ', '')
harryporter_phoenix['review'] = harryporter_phoenix['review'].str.replace('ㅎ', '')
harryporter_phoenix['review'] = harryporter_phoenix['review'].str.replace('[-=+;:,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…♥♡》]', '')

harryporter_phoenix

harryporter_phoenix.columns = ['리뷰', '평점']
harryporter_phoenix['긍정/부정'] = ''
harryporter_phoenix

harryporter_phoenix.loc[harryporter_phoenix['평점'] >= 7, '긍정/부정'] = '긍정'
harryporter_phoenix.loc[harryporter_phoenix['평점'] <= 6, '긍정/부정'] = '부정'

harryporter_phoenix.to_csv('c:/data/harryporter_phoenix.csv', encoding='cp949')
harryporter_phoenix



#====================================================================================
# 해리포터와 혼혈 왕자




prince_df = pd.DataFrame(columns = ['review', 'score'])

prince_review_lst = []
prince_score_lst = []
for i in range(1, 150):
    url = 'https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn?code=67900&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false&page={}'
    li = url.format(i)
    res = req.urlopen(li)
    soup = BeautifulSoup(res, 'html.parser')
    review = soup.select('div.score_reple')
    score = soup.select('div.star_score')
    for j in review:
        prince_review_lst.append(j.find('span').get_text().strip())
    for k in score:
        prince_score_lst.append(k.find('em').get_text().strip())

prince_review_lst
prince_score_lst


prince_df['score'] = prince_score_lst
prince_df['review'] = prince_review_lst


prince_df

prince_df.to_csv('c:/data/prince_df.csv', encoding='cp949', index=False)
prince_df = pd.read_csv('c:/data/prince_df.csv', encoding='cp949')
prince_df = prince_df.dropna()
prince_df.reset_index(drop=True, inplace=True)
prince_df

harryporter_prince = prince_df
harryporter_prince

harryporter_prince['review'] = harryporter_prince['review'].str.replace('!!', '')
harryporter_prince['review'] = harryporter_prince['review'].str.replace('ㅠ', '')
harryporter_prince['review'] = harryporter_prince['review'].str.replace('ㅜ', '')
harryporter_prince['review'] = harryporter_prince['review'].str.replace('.', '')
harryporter_prince['review'] = harryporter_prince['review'].str.replace('ㅡ', '')
harryporter_prince['review'] = harryporter_prince['review'].str.replace('ㅋ', '')
harryporter_prince['review'] = harryporter_prince['review'].str.replace('ㅎ', '')
harryporter_prince['review'] = harryporter_prince['review'].str.replace('[-=+;:,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…♥♡》]', '')

harryporter_prince.columns = ['리뷰', '평점']
harryporter_prince['긍정/부정'] = ''
harryporter_prince


harryporter_prince.loc[harryporter_prince['평점'] >= 7, '긍정/부정'] = '긍정'
harryporter_prince.loc[harryporter_prince['평점'] <= 6, '긍정/부정'] = '부정'


harryporter_prince.to_csv('c:/data/harryporter_prince.csv', encoding='cp949')
harryporter_prince


#====================================================================================
# 해리포터와 죽음의 성물1

deathly1_df = pd.DataFrame(columns = ['review', 'score'])

deathly1_review_lst = []
deathly1_score_lst = []
for i in range(1, 150):
    url = 'https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn?code=67901&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false&page={}'
    li = url.format(i)
    res = req.urlopen(li)
    soup = BeautifulSoup(res, 'html.parser')
    review = soup.select('div.score_reple')
    score = soup.select('div.star_score')
    for j in review:
        deathly1_review_lst.append(j.find('span').get_text().strip())
    for k in score:
        deathly1_score_lst.append(k.find('em').get_text().strip())

deathly1_review_lst
deathly1_score_lst


deathly1_df['score'] = deathly1_score_lst
deathly1_df['review'] = deathly1_review_lst

deathly1_df

deathly1_df.to_csv('c:/data/deathly1_df.csv', encoding='utf-8', index=False)
deathly1_df = pd.read_csv('c:/data/deathly1_df.csv', encoding='utf-8')
deathly1_df = deathly1_df.dropna()
deathly1_df.reset_index(drop=True, inplace=True)
deathly1_df


harryporter_deathly1 = deathly1_df


harryporter_deathly1['review'] = harryporter_deathly1['review'].str.replace('!!', '')
harryporter_deathly1['review'] = harryporter_deathly1['review'].str.replace('ㅠ', '')
harryporter_deathly1['review'] = harryporter_deathly1['review'].str.replace('ㅜ', '')
harryporter_deathly1['review'] = harryporter_deathly1['review'].str.replace('.', '')
harryporter_deathly1['review'] = harryporter_deathly1['review'].str.replace('ㅡ', '')
harryporter_deathly1['review'] = harryporter_deathly1['review'].str.replace('ㅋ', '')
harryporter_deathly1['review'] = harryporter_deathly1['review'].str.replace('ㄴ', '')
harryporter_deathly1['review'] = harryporter_deathly1['review'].str.replace('ㅎ', '')
harryporter_deathly1['review'] = harryporter_deathly1['review'].str.replace('ㅇ', '')
harryporter_deathly1['review'] = harryporter_deathly1['review'].str.replace('ㅅ', '')
harryporter_deathly1['review'] = harryporter_deathly1['review'].str.replace('[a-zA-Z]', '')
harryporter_deathly1['review'] = harryporter_deathly1['review'].str.replace('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…♥♡》]', '')
harryporter_deathly1['review'] = harryporter_deathly1['review'].str.replace('낙ㄷ누즈느디느놋즈지', '')
harryporter_deathly1['review'] = harryporter_deathly1['review'].str.replace('슈ㅡㅏ', '')
harryporter_deathly1['review'] = harryporter_deathly1['review'].str.replace('[^ㄱ-ㅎㅏ-ㅣ가-힣0-9 ]', '')

harryporter_deathly1

harryporter_deathly1.columns = ['리뷰', '평점']
harryporter_deathly1['긍정/부정'] = ''
harryporter_deathly1

harryporter_deathly1.loc[harryporter_deathly1['평점'] >= 7, '긍정/부정'] = '긍정'
harryporter_deathly1.loc[harryporter_deathly1['평점'] <= 6, '긍정/부정'] = '부정'

harryporter_deathly1.to_csv('c:/data/harryporter_deathly1.csv', encoding='cp949')

harryporter_deathly1

#=====================================================================================
#해리포터 죽음의 성물2

deathly2_df = pd.DataFrame(columns = ['review', 'score'])

deathly2_review_lst = []
deathly2_score_lst = []
for i in range(1, 150):
    url = 'https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn?code=47528&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false&page={}'
    li = url.format(i)
    res = req.urlopen(li)
    soup = BeautifulSoup(res, 'html.parser')
    review = soup.select('div.score_reple')
    score = soup.select('div.star_score')
    for j in review:
        deathly2_review_lst.append(j.find('span').get_text().strip())
    for k in score:
        deathly2_score_lst.append(k.find('em').get_text().strip())

deathly2_review_lst
deathly2_score_lst

deathly2_df['score'] = deathly2_score_lst
deathly2_df['review'] = deathly2_review_lst

deathly2_df

deathly2_df.to_csv('c:/data/deathly2_df.csv', encoding='utf-8', index=False)
deathly2_df = pd.read_csv('c:/data/deathly2_df.csv', encoding='utf-8')
deathly2_df = deathly2_df.dropna()
deathly2_df.reset_index(drop=True, inplace=True)
deathly2_df


harryporter_deathly2 = deathly2_df

harryporter_deathly2

harryporter_deathly2['review'] = harryporter_deathly2['review'].str.replace('!!', '')
harryporter_deathly2['review'] = harryporter_deathly2['review'].str.replace('ㅠ', '')
harryporter_deathly2['review'] = harryporter_deathly2['review'].str.replace('ㅜ', '')
harryporter_deathly2['review'] = harryporter_deathly2['review'].str.replace('.', '')
harryporter_deathly2['review'] = harryporter_deathly2['review'].str.replace('ㅋ', '')
harryporter_deathly2['review'] = harryporter_deathly2['review'].str.replace('ㅎ', '')
harryporter_deathly2['review'] = harryporter_deathly2['review'].str.replace('[a-zA-Z]', '')
harryporter_deathly2['review'] = harryporter_deathly2['review'].str.replace('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…♥♡》]', '')
harryporter_deathly2['review'] = harryporter_deathly2['review'].str.replace('낙ㄷ누즈느디느놋즈지', '')
harryporter_deathly2['review'] = harryporter_deathly2['review'].str.replace('슈ㅡㅏ', '')
harryporter_deathly2['review'] = harryporter_deathly2['review'].str.replace('[^ㄱ-ㅎㅏ-ㅣ가-힣0-9 ]', '')

harryporter_deathly2


harryporter_deathly2.columns = ['리뷰', '평점']
harryporter_deathly2['긍정/부정'] = ''
harryporter_deathly2


harryporter_deathly2.loc[harryporter_deathly2['평점'] >= 7, '긍정/부정'] = '긍정'
harryporter_deathly2.loc[harryporter_deathly2['평점'] <= 6, '긍정/부정'] = '부정'


harryporter_deathly2.to_csv('c:/data/harryporter_deathly2.csv', encoding='cp949')


harryporter_deathly2

#종합===========================================================================================

harryporter_stone = pd.read_csv('c:/data/harryporter_stone.csv', encoding='cp949', index_col=[0])
harryporter_room = pd.read_csv('c:/data/harryporter_room.csv', encoding='cp949',index_col=[0])
harryporter_azkaban = pd.read_csv('c:/data/harryporter_azkaban.csv', encoding='cp949', index_col=[0])
harryporter_fire = pd.read_csv('c:/data/harryporter_fire.csv', encoding='cp949', index_col=[0])
harryporter_phoenix = pd.read_csv('c:/data/harryporter_phoenix.csv', encoding='cp949', index_col=[0])
harryporter_prince = pd.read_csv('c:/data/harryporter_prince.csv', encoding='cp949', index_col=[0])
harryporter_deathly1 = pd.read_csv('c:/data/harryporter_deathly1.csv', encoding='cp949', index_col=[0])
harryporter_deathly2 = pd.read_csv('c:/data/harryporter_deathly2.csv', encoding='cp949', index_col=[0])

harryporter_stone = harryporter_stone.dropna()
harryporter_stone.isnull().sum().sum()
harryporter_room = harryporter_room.dropna()
harryporter_azkaban = harryporter_azkaban.dropna()
harryporter_fire = harryporter_fire.dropna()
harryporter_phoenix = harryporter_phoenix.dropna()
harryporter_prince = harryporter_prince.dropna()
harryporter_deathly1 = harryporter_deathly1.dropna()
harryporter_deathly2 = harryporter_deathly2.dropna()


harryporter_stone = harryporter_stone.reset_index(drop=True)
harryporter_room = harryporter_room.reset_index(drop=True)
harryporter_azkaban = harryporter_azkaban.reset_index(drop=True)
harryporter_fire = harryporter_fire.reset_index(drop=True)
harryporter_phoenix = harryporter_phoenix.reset_index(drop=True)
harryporter_prince = harryporter_prince.reset_index(drop=True)
harryporter_deathly1 = harryporter_deathly1.reset_index(drop=True)
harryporter_deathly2 = harryporter_deathly2.reset_index(drop=True)

harryporter_stone.to_csv('c:/data/harryporter_stone.csv', encoding='cp949')
harryporter_room.to_csv('c:/data/harryporter_room.csv', encoding='cp949')
harryporter_azkaban.to_csv('c:/data/harryporter_azkaban.csv', encoding='cp949')
harryporter_fire.to_csv('c:/data/harryporter_fire.csv', encoding='cp949')
harryporter_phoenix.to_csv('c:/data/harryporter_phoenix.csv', encoding='cp949')
harryporter_prince.to_csv('c:/data/harryporter_prince.csv', encoding='cp949')
harryporter_deathly1.to_csv('c:/data/harryporter_deathly1.csv', encoding='cp949')
harryporter_deathly2.to_csv('c:/data/harryporter_deathly2.csv', encoding='cp949')

harryporter_stone
harryporter_room
harryporter_azkaban
harryporter_fire
harryporter_phoenix
harryporter_prince
harryporter_deathly1
harryporter_deathly2


#harryporter_stone==========================================================================

# 정확도
cv = CountVectorizer()
x_train = cv.fit_transform(harryporter_stone['리뷰'])
x_train
y_train = harryporter_stone['긍정/부정']
encode_cv = x_train.toarray() 
cv.inverse_transform(encode_cv[0:2])
cv.get_feature_names()
nb = MultinomialNB()
nb.fit(x_train, y_train)
x_test = cv.transform(harryporter_stone['리뷰'])
y_predict = nb.predict(x_test)
accuracy_score(harryporter_stone['긍정/부정'], y_predict)

# NaiveBayes
stone_allword = set(word for i in harryporter_stone['리뷰'] for word in word_tokenize(i))
stone_allword
stone_data = harryporter_stone[['리뷰', '긍정/부정']].values.tolist()
stone_t = [({word : (word in word_tokenize(x[0])) for word in stone_allword}, x[1]) for x in stone_data]
stone_t

classifier = nltk.NaiveBayesClassifier.train(stone_t)
classifier.show_most_informative_features()


stop_word = []
with open('c:/data/stop_words.txt', 'r', encoding='utf-8') as s:
    for word in s:
        stop_word.append(word.strip())
stop_word
from konlpy.tag import Okt
pos = Okt()
def text_tokenizing(doc):
    return [word for word in pos.morphs(doc) if word not in stop_word and len(word) > 1]
contents_token = [text_tokenizing(i) for i in harryporter_stone['리뷰']]
contents_token[0:2]
contents = [' '.join(i) for i in contents_token]
contents[0:2]
X = contents
Y = harryporter_stone['긍정/부정']
X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size=0.2)
Counter(Y_train)
Counter(Y_test)
cv = CountVectorizer()
X_train = cv.fit_transform(X_train)
nb = MultinomialNB()
nb.fit(X_train, Y_train)
X_test = cv.transform(X_test)
print(classification_report(Y_test, nb.predict(X_test)))


#harryporter_room==========================================================================

# 정확도
cv = CountVectorizer()
x_train = cv.fit_transform(harryporter_room['리뷰'])
x_train
y_train = harryporter_room['긍정/부정']
encode_cv = x_train.toarray() 
cv.inverse_transform(encode_cv[0:2])
len(cv.get_feature_names())
nb = MultinomialNB()
nb.fit(x_train, y_train)
x_test = cv.transform(harryporter_room['리뷰'])
y_predict = nb.predict(x_test)
accuracy_score(harryporter_room['긍정/부정'], y_predict)

# NaiveBayes
harry_word = Okt()
room_allword = set(word for i in harryporter_room['리뷰'] for word in word_tokenize(i))
room_allword
room_data = harryporter_room[['리뷰', '긍정/부정']].values.tolist()
room_t = [({word : (word in word_tokenize(x[0])) for word in room_allword}, x[1]) for x in room_data]
room_t

classifier = nltk.NaiveBayesClassifier.train(room_t)
classifier.show_most_informative_features()


stop_word = []
with open('c:/data/stop_words.txt', 'r', encoding='utf-8') as s:
    for word in s:
        stop_word.append(word.strip())
stop_word
from konlpy.tag import Okt
pos = Okt()
def text_tokenizing(doc):
    return [word for word in pos.morphs(doc) if word not in stop_word and len(word) > 1]
contents_token = [text_tokenizing(i) for i in harryporter_room['리뷰']]
contents_token[0:2]
contents = [' '.join(i) for i in contents_token]
contents[0:2]
X = contents
Y = harryporter_room['긍정/부정']
X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size=0.2)
Counter(Y_train)
Counter(Y_test)
cv = CountVectorizer()
X_train = cv.fit_transform(X_train)
nb = MultinomialNB()
nb.fit(X_train, Y_train)
X_test = cv.transform(X_test)
print(classification_report(Y_test, nb.predict(X_test)))


#harryporter_azkaban==========================================================================

# 정확도
cv = CountVectorizer()
x_train = cv.fit_transform(harryporter_azkaban['리뷰'])
x_train
y_train = harryporter_azkaban['긍정/부정']
encode_cv = x_train.toarray()
cv.inverse_transform(encode_cv[0:2])
len(cv.get_feature_names())
nb = MultinomialNB()
nb.fit(x_train, y_train)
x_test = cv.transform(harryporter_azkaban['리뷰'])
y_predict = nb.predict(x_test)
accuracy_score(harryporter_azkaban['긍정/부정'], y_predict)

# NaiveBayes
azkaban_allword = set(word for i in harryporter_azkaban['리뷰'] for word in word_tokenize(i))
azkaban_allword
azkaban_data = harryporter_azkaban[['리뷰', '긍정/부정']].values.tolist()
azkaban_t = [({word : (word in word_tokenize(x[0])) for word in azkaban_allword}, x[1]) for x in azkaban_data]
azkaban_t

classifier = nltk.NaiveBayesClassifier.train(azkaban_t)
classifier.show_most_informative_features()


stop_word = []
with open('c:/data/stop_words.txt', 'r', encoding='utf-8') as s:
    for word in s:
        stop_word.append(word.strip())
stop_word
from konlpy.tag import Okt
pos = Okt()
def text_tokenizing(doc):
    return [word for word in pos.morphs(doc) if word not in stop_word and len(word) > 1]
contents_token = [text_tokenizing(i) for i in harryporter_azkaban['리뷰']]
contents_token[0:2]
contents = [' '.join(i) for i in contents_token]
contents[0:2]
X = contents
Y = harryporter_azkaban['긍정/부정']
X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size=0.2)
Counter(Y_train)
Counter(Y_test)
cv = CountVectorizer()
X_train = cv.fit_transform(X_train)
nb = MultinomialNB()
nb.fit(X_train, Y_train)
X_test = cv.transform(X_test)
print(classification_report(Y_test, nb.predict(X_test)))




#harryporter_fire==========================================================================

# 정확도
cv = CountVectorizer()
x_train = cv.fit_transform(harryporter_fire['리뷰'])
x_train
y_train = harryporter_fire['긍정/부정']
encode_cv = x_train.toarray()
cv.inverse_transform(encode_cv[0:2])
len(cv.get_feature_names())
nb = MultinomialNB()
nb.fit(x_train, y_train)
x_test = cv.transform(harryporter_fire['리뷰'])
y_predict = nb.predict(x_test)
accuracy_score(harryporter_fire['긍정/부정'], y_predict)


fire_allword = set(word for i in harryporter_fire['리뷰'] for word in word_tokenize(i))
fire_allword
fire_data = harryporter_fire[['리뷰', '긍정/부정']].values.tolist()
fire_t = [({word : (word in word_tokenize(x[0])) for word in fire_allword}, x[1]) for x in fire_data]
fire_t

classifier = nltk.NaiveBayesClassifier.train(fire_t)
classifier.show_most_informative_features()



stop_word = []
with open('c:/data/stop_words.txt', 'r', encoding='utf-8') as s:
    for word in s:
        stop_word.append(word.strip())
stop_word
from konlpy.tag import Okt
pos = Okt()
def text_tokenizing(doc):
    return [word for word in pos.morphs(doc) if word not in stop_word and len(word) > 1]
contents_token = [text_tokenizing(i) for i in harryporter_fire['리뷰']]
contents_token[0:2]
contents = [' '.join(i) for i in contents_token]
contents[0:2]
X = contents
Y = harryporter_fire['긍정/부정']
X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size=0.2)
Counter(Y_train)
Counter(Y_test)
cv = CountVectorizer()
X_train = cv.fit_transform(X_train)
nb = MultinomialNB()
nb.fit(X_train, Y_train)
X_test = cv.transform(X_test)
print(classification_report(Y_test, nb.predict(X_test)))
print(confusion_matrix(Y_test, nb.predict(X_test)))




#harryporter_phoenix==========================================================================

# 정확도
cv = CountVectorizer()
x_train = cv.fit_transform(harryporter_phoenix['리뷰'])
x_train
y_train = harryporter_phoenix['긍정/부정']
encode_cv = x_train.toarray()
cv.inverse_transform(encode_cv[0:2])
len(cv.get_feature_names())
nb = MultinomialNB()
nb.fit(x_train, y_train)
x_test = cv.transform(harryporter_phoenix['리뷰'])
y_predict = nb.predict(x_test)
accuracy_score(harryporter_phoenix['긍정/부정'], y_predict)


phoenix_allword = set(word for i in harryporter_phoenix['리뷰'] for word in word_tokenize(i))
phoenix_allword
phoenix_data = harryporter_phoenix[['리뷰', '긍정/부정']].values.tolist()
phoenix_t = [({word : (word in word_tokenize(x[0])) for word in phoenix_allword}, x[1]) for x in phoenix_data]
phoenix_t

classifier = nltk.NaiveBayesClassifier.train(phoenix_t)
classifier.show_most_informative_features()



stop_word = []
with open('c:/data/stop_words.txt', 'r', encoding='utf-8') as s:
    for word in s:
        stop_word.append(word.strip())
stop_word
from konlpy.tag import Okt
pos = Okt()
def text_tokenizing(doc):
    return [word for word in pos.morphs(doc) if word not in stop_word and len(word) > 1]
contents_token = [text_tokenizing(i) for i in harryporter_phoenix['리뷰']]
contents_token[0:2]
contents = [' '.join(i) for i in contents_token]
contents[0:2]
X = contents
Y = harryporter_phoenix['긍정/부정']
X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size=0.2)
Counter(Y_train)
Counter(Y_test)
cv = CountVectorizer()
X_train = cv.fit_transform(X_train)
nb = MultinomialNB()
nb.fit(X_train, Y_train)
X_test = cv.transform(X_test)
print(classification_report(Y_test, nb.predict(X_test)))
print(confusion_matrix(Y_test, nb.predict(X_test)))


#harryporter_prince==========================================================================

# 정확도
cv = CountVectorizer()
x_train = cv.fit_transform(harryporter_prince['리뷰'])
x_train
y_train = harryporter_prince['긍정/부정']
encode_cv = x_train.toarray()
cv.inverse_transform(encode_cv[0:2])
len(cv.get_feature_names())
nb = MultinomialNB()
nb.fit(x_train, y_train)
x_test = cv.transform(harryporter_prince['리뷰'])
y_predict = nb.predict(x_test)
accuracy_score(harryporter_prince['긍정/부정'], y_predict)

# NaiveBayes
prince_allword = set(word for i in harryporter_prince['리뷰'] for word in word_tokenize(i))
prince_allword
prince_data = harryporter_prince[['리뷰', '긍정/부정']].values.tolist()
prince_t = [({word : (word in word_tokenize(x[0])) for word in prince_allword}, x[1]) for x in prince_data]
prince_t
classifier = nltk.NaiveBayesClassifier.train(prince_t)
classifier.show_most_informative_features()


stop_word = []
with open('c:/data/stop_words.txt', 'r', encoding='utf-8') as s:
    for word in s:
        stop_word.append(word.strip())
stop_word
from konlpy.tag import Okt
pos = Okt()
def text_tokenizing(doc):
    return [word for word in pos.morphs(doc) if word not in stop_word and len(word) > 1]
contents_token = [text_tokenizing(i) for i in harryporter_prince['리뷰']]
contents_token[0:2]
contents = [' '.join(i) for i in contents_token]
contents[0:2]
X = contents
Y = harryporter_prince['긍정/부정']
X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size=0.2)
Counter(Y_train)
Counter(Y_test)
cv = CountVectorizer()
X_train = cv.fit_transform(X_train)
nb = MultinomialNB()
nb.fit(X_train, Y_train)
X_test = cv.transform(X_test)
print(classification_report(Y_test, nb.predict(X_test)))



#harryporter_deathly1==========================================================================

# 정확도
cv = CountVectorizer()
x_train = cv.fit_transform(harryporter_deathly1['리뷰'])
x_train
y_train = harryporter_deathly1['긍정/부정']
encode_cv = x_train.toarray()
cv.inverse_transform(encode_cv[0:2])
len(cv.get_feature_names())
nb = MultinomialNB()
nb.fit(x_train, y_train)
x_test = cv.transform(harryporter_deathly1['리뷰'])
y_predict = nb.predict(x_test)
accuracy_score(harryporter_deathly1['긍정/부정'], y_predict)

# NaiveBayes 
deathly1_allword = set(word for i in harryporter_deathly1['리뷰'] for word in word_tokenize(i))
deathly1_allword
deathly1_data = harryporter_deathly1[['리뷰', '긍정/부정']].values.tolist()
deathly1_t = [({word : (word in word_tokenize(x[0])) for word in deathly1_allword}, x[1]) for x in deathly1_data]
deathly1_t

classifier = nltk.NaiveBayesClassifier.train(deathly1_t)
classifier.show_most_informative_features()


stop_word = []
with open('c:/data/stop_words.txt', 'r', encoding='utf-8') as s:
    for word in s:
        stop_word.append(word.strip())
stop_word
from konlpy.tag import Okt
pos = Okt()
def text_tokenizing(doc):
    return [word for word in pos.morphs(doc) if word not in stop_word and len(word) > 1]
contents_token = [text_tokenizing(i) for i in harryporter_deathly1['리뷰']]
contents_token[0:2]
contents = [' '.join(i) for i in contents_token]
contents[0:2]
X = contents
Y = harryporter_deathly1['긍정/부정']
X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size=0.2)
Counter(Y_train)
Counter(Y_test)
cv = CountVectorizer()
X_train = cv.fit_transform(X_train)
nb = MultinomialNB()
nb.fit(X_train, Y_train)
X_test = cv.transform(X_test)
print(classification_report(Y_test, nb.predict(X_test)))


#harryporter_deathly2==========================================================================

# 정확도
cv = CountVectorizer()
x_train = cv.fit_transform(harryporter_deathly2['리뷰'])
x_train
y_train = harryporter_deathly2['긍정/부정']
encode_cv = x_train.toarray()
cv.inverse_transform(encode_cv[0:2])
len(cv.get_feature_names())
nb = MultinomialNB()
nb.fit(x_train, y_train)
x_test = cv.transform(harryporter_deathly2['리뷰'])
y_predict = nb.predict(x_test)
accuracy_score(harryporter_deathly2['긍정/부정'], y_predict)

# NaiveBayes 
deathly2_allword = set(word for i in harryporter_deathly2['리뷰'] for word in word_tokenize(i))
deathly2_allword
deathly2_data = harryporter_deathly2[['리뷰', '긍정/부정']].values.tolist()
deathly2_t = [({word : (word in word_tokenize(x[0])) for word in deathly2_allword}, x[1]) for x in deathly2_data]
deathly2_t

classifier = nltk.NaiveBayesClassifier.train(deathly2_t)
classifier.show_most_informative_features()

stop_word = []
with open('c:/data/stop_words.txt', 'r', encoding='utf-8') as s:
    for word in s:
        stop_word.append(word.strip())
stop_word
from konlpy.tag import Okt
pos = Okt()
def text_tokenizing(doc):
    return [word for word in pos.morphs(doc) if word not in stop_word and len(word) > 1]
contents_token = [text_tokenizing(i) for i in harryporter_deathly2['리뷰']]
contents_token[0:2]
contents = [' '.join(i) for i in contents_token]
contents[0:2]
X = contents
Y = harryporter_deathly2['긍정/부정']
X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size=0.2)
Counter(Y_train)
Counter(Y_test)
cv = CountVectorizer()
X_train = cv.fit_transform(X_train)
nb = MultinomialNB()
nb.fit(X_train, Y_train)
X_test = cv.transform(X_test)
print(classification_report(Y_test, nb.predict(X_test)))

text = pd.Series('이 영화 정말 재미없고 극혐이야')
z_test = cv.transform(text)
nb.predict(z_test)

text = pd.Series('이 영화 똥이야')
z_test = cv.transform(text)
nb.predict(z_test)