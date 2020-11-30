import datetime
import math
from wordcloud import WordCloud, STOPWORDS
import collections
import pandas as pd
import numpy as np
from numpy import nan as na
from pandas import Series, DataFrame
import wordcloud
import statsmodels.api as sm
import statsmodels.formula.api as smf
import matplotlib.pylab as plt
from matplotlib import font_manager, rc # 한글 깨질 때
font_name = font_manager.FontProperties(fname='c:\windows/fonts/malgun.ttf').get_name() # 한글 폰트 설정법
rc('font', family=font_name) # 한글 폰트 설정법
import matplotlib.font_manager as fm
from bs4 import BeautifulSoup
from bs4 import NavigableString
from konlpy.tag import Okt
pos = Okt()
import glob
from pandas import *
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
import sklearn.metrics as metrics
import numpy as np
import scipy.stats as stats
import pandas_datareader.data as web
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
from sklearn.neighbors import KNeighborsClassifier
from urllib.request import urlopen
from urllib.parse import quote # 아스키 문자로 변환해주는 함수
import json
from fake_useragent import UserAgent
import requests
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from matplotlib import rc
from sklearn.feature_extraction.text import CountVectorizer
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
from sklearn.preprocessing import StandardScaler
from collections import Counter
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules
import urllib
from sklearn.tree import DecisionTreeClassifier
import pydotplus
import tensorflow as tf
import graphviz
from sklearn.tree import export_graphviz
from IPython.display import Image
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from scipy import stats
from sklearn import linear_model
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import re
from sklearn.ensemble import GradientBoostingRegressor 
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer
from collections import Counter
from sklearn.datasets import load_iris
import seaborn as sns
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import Ridge, RidgeCV, Lasso, LassoCV, ElasticNet,ElasticNetCV
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
import numpy as np
from gensim.models.word2vec import Word2Vec
import pandas as pd
#===================================================================================================================
# 네이버 트랜드 검색 api

client_id = "a7sewAJZVT2hdTz17pJQ"
client_secret = "1dstmcRYya"

url = "https://openapi.naver.com/v1/datalab/search";
body = {
    'startDate' : '2016-01-01',
    'endDate' : '2016-12-31',
    'timeUnit' : 'month',        # input : [date, week, month]
    'keywordGroups' : [         #
        {'groupName': '여드름','keywords': ['여드름']},
        ],
}
body = json.dumps(body)
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
request.add_header("Content-Type","application/json")
response = urllib.request.urlopen(request, data=body.encode("utf-8"))
data = json.loads(response.read().decode('utf-8'))

tmp = pd.DataFrame(data['results'])
print(tmp)

res = data['results'][0]['data']
acne_naver = pd.DataFrame(res)


client_id = "a7sewAJZVT2hdTz17pJQ"
client_secret = "1dstmcRYya"

url = "https://openapi.naver.com/v1/datalab/search";
body = {
    'startDate' : '2017-01-01',
    'endDate' : '2017-12-31',
    'timeUnit' : 'month',        # input : [date, week, month]
    'keywordGroups' : [         #
        {'groupName': '여드름','keywords': ['여드름']},
        ],
}
body = json.dumps(body)
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
request.add_header("Content-Type","application/json")
response = urllib.request.urlopen(request, data=body.encode("utf-8"))
data = json.loads(response.read().decode('utf-8'))

tmp = pd.DataFrame(data['results'])
print(tmp)

res1 = data['results'][0]['data']
acne_naver1 = pd.DataFrame(res1)


client_id = "a7sewAJZVT2hdTz17pJQ"
client_secret = "1dstmcRYya"

url = "https://openapi.naver.com/v1/datalab/search";
body = {
    'startDate' : '2018-01-01',
    'endDate' : '2018-12-31',
    'timeUnit' : 'month',        # input : [date, week, month]
    'keywordGroups' : [         #
        {'groupName': '여드름','keywords': ['여드름']},
        ],
}
body = json.dumps(body)
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
request.add_header("Content-Type","application/json")
response = urllib.request.urlopen(request, data=body.encode("utf-8"))
data = json.loads(response.read().decode('utf-8'))

tmp = pd.DataFrame(data['results'])
print(tmp)

res2 = data['results'][0]['data']
acne_naver2 = pd.DataFrame(res2)


client_id = "a7sewAJZVT2hdTz17pJQ"
client_secret = "1dstmcRYya"

url = "https://openapi.naver.com/v1/datalab/search";
body = {
    'startDate' : '2019-01-01',
    'endDate' : '2019-12-31',
    'timeUnit' : 'month',        # input : [date, week, month]
    'keywordGroups' : [         #
        {'groupName': '여드름','keywords': ['여드름']},
        ],
}
body = json.dumps(body)
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
request.add_header("Content-Type","application/json")
response = urllib.request.urlopen(request, data=body.encode("utf-8"))
data = json.loads(response.read().decode('utf-8'))

tmp = pd.DataFrame(data['results'])
print(tmp)

res3 = data['results'][0]['data']
acne_naver3 = pd.DataFrame(res3)


client_id = "a7sewAJZVT2hdTz17pJQ"
client_secret = "1dstmcRYya"

url = "https://openapi.naver.com/v1/datalab/search";
body = {
    'startDate' : '2020-01-01',
    'endDate' : '2020-02-28',
    'timeUnit' : 'month',        # input : [date, week, month]
    'keywordGroups' : [         #
        {'groupName': '여드름','keywords': ['여드름']},
        ],
}
body = json.dumps(body)
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
request.add_header("Content-Type","application/json")
response = urllib.request.urlopen(request, data=body.encode("utf-8"))
data = json.loads(response.read().decode('utf-8'))

tmp = pd.DataFrame(data['results'])
print(tmp)

res4 = data['results'][0]['data']
acne_naver4 = pd.DataFrame(res4)
acne_naver5 = pd.concat([acne_naver, acne_naver1, acne_naver2, acne_naver3, acne_naver4], axis=0)
acne_naver5 = acne_naver5.drop('period', axis=1)
acne_naver5.to_csv('c:/data/final/acne_naver5.csv', encoding='cp949', index=False)
acne_naver5.reset_index(drop=True, inplace=True)


acne_naver5['date'] = ['2016-01-01', '2016-02-01', '2016-03-01', '2016-04-01', '2016-05-01', '2016-06-01', '2016-07-01', '2016-08-01', '2016-09-01', '2016-10-01', '2016-11-01', '2016-12-01',
                    '2017-01-01', '2017-02-01', '2017-03-01', '2017-04-01', '2017-05-01', '2017-06-01', '2017-07-01', '2017-08-01', '2017-09-01', '2017-10-01', '2017-11-01', '2017-12-01',
                    '2018-01-01', '2018-02-01', '2018-03-01', '2018-04-01', '2018-05-01', '2018-06-01', '2018-07-01', '2018-08-01', '2018-09-01', '2018-10-01', '2018-11-01', '2018-12-01',
                    '2019-01-01', '2019-02-01', '2019-03-01', '2019-04-01', '2019-05-01', '2019-06-01', '2019-07-01', '2019-08-01', '2019-09-01', '2019-10-01', '2019-11-01', '2019-12-01',
                    '2020-01-01', '2020-02-01']

acne_naver5.set_index('date', inplace=True)

acne_naver5

embedding_model = Word2Vec(acne_naver5, size=100, window = 2, min_count=50, workers=4, iter=100, sg=1)


sns.lineplot(data=acne_naver5, markers=True, sizes=[5, 6, 7, 8, 9])
plt.xticks(np.arange(1, len(acne_naver['period']), 1), labels=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], fontsize=18)
plt.yticks(np.arange(0, 120, 20), fontsize=18)
plt.xlabel('1월 ~ 12월', fontsize=20)
plt.ylabel('검색 수치', fontsize=20)
plt.title('2016 ~ 2020 <여드름> 검색 트렌드', fontsize=24)
plt.legend(['2016', '2017', '2018', '2019', '2020'], fontsize=20)
plt.grid(True)
plt.savefig('naver_trand.png')

plt.plot(acne_naver5['ratio'])




#===================================================================================================================
# 네이버 지식인 api

    client_id = "C2QUU8idCr59BHXMN1qx"
    client_secret = "s62CxCE2rP"

    q = urllib.parse.quote('여드름')
    idx = 0
    display = 100
    start = 1
    end = 1000
    sort = 'sim'

    in_df = pd.DataFrame(columns=('title', 'description'))

    for i in range(start, end, display):
        url = "https://openapi.naver.com/v1/search/kin?query=" + q \
            + '&display=' + str(display) \
            + '&start=' + str(i) \
            + '&sort=' + sort

    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if(rescode==200): # 정상적으로 코드를 받으면 200 표시
        response_body = response.read()
        response_dict = json.loads(response_body.decode('utf-8'))
        items = response_dict['items']
        for i_index in range(0, len(items)):
            remove_tag = re.compile('[^가-힣 ]')
            title = re.sub(remove_tag, '', items[i_index]['title'])
            description = re.sub(remove_tag, '', items[i_index]['description'])
            in_df.loc[idx] = [title, description]
            idx += 1
    else:
        print("Error Code:" + rescode)

    jisik = pd.DataFrame(columns = ['description'])
    jisik['description'] = in_df['description']

    jisik.to_csv('c:/data/final/jisik.csv', encoding='cp949', index=False)
    jisik = pd.read_csv('c:/data/final/jisik.csv', encoding='cp949', header=0, names=['description'])
    jisik


    stop_word = []
    with open('c:/data/stop_words.txt', 'r', encoding='utf-8') as s:
        for word in s:
            stop_word.append(word.strip())
    stop_word
    from konlpy.tag import Okt
    pos = Okt()
    def text_tokenizing(doc):
        return [word for word in pos.nouns(doc) if word not in stop_word and len(word) > 1]
    contents_token = [text_tokenizing(i) for i in jisik['description']]
    contents_token[0:2]
    contents = [' '.join(i) for i in contents_token]
    split = ''
    contents = split.join(contents)
    contents = contents.split()
    contents1 = Counter(contents)
    contents1 = contents1.most_common(100)
    contents = np.array(contents1)

contents.drop([contents.index[5], contents.index[10], contents.index[14], contents.index[16], contents.index[17]],inplace=True)


g = sns.barplot(x=contents[0], y=contents[1], data=contents, ci=None)
ax = g
for i in ax.patches:
    ax.annotate('%.0f' % i.get_height(), (i.get_x() + i.get_width()/2, i.get_height()-30), ha='center', va='center', fontsize=10, color='black', xytext=(0, 10), textcoords='offset points')
plt.xticks(fontsize=12, rotation=45)
plt.xlabel('단어',fontsize=12)
plt.ylabel('cnt', fontsize=12)
plt.show()



# wordcloud
WordCloud(font_path='c://windows//fonts//malgunbd.ttf', width = 500,height = 500,background_color = 'white',stopwords = 
STOPWORDS).generate(str(contents))
plt.figure(figsize = (10, 10),facecolor = 'k',edgecolor = 'k')
plt.imshow(wordcloud, interpolation = 'nearest')
plt.axis('off')
plt.tight_layout(pad=0)
plt.show()   



acne_df110_2016 = acne_df110.loc[0:11].sum(axis=0)
acne_df110_2017 = acne_df110.loc[12:23].sum(axis=0)
acne_df110_2018 = acne_df110.loc[24:35].sum(axis=0)
acne_df110_2019 = acne_df110.loc[36:47].sum(axis=0)
acne_df110_2020 = acne_df110.loc[48:].sum(axis=0)
acne_df110_2016 = pd.DataFrame(acne_df110_2016)
acne_df110_2017 = pd.DataFrame(acne_df110_2017)
acne_df110_2018 = pd.DataFrame(acne_df110_2018)
acne_df110_2019 = pd.DataFrame(acne_df110_2019)
acne_df110_2020 = pd.DataFrame(acne_df110_2020)

acne_df110_sum = pd.concat([acne_df110_2016, acne_df110_2017, acne_df110_2018, acne_df110_2019, acne_df110_2020], axis=0)

acne_df110_sum['year'] = [2016, 2016, 2017, 2017, 2018, 2018,2019, 2019, 2020,2020]
acne_df110_sum['sex'] = ['man', 'woman', 'man', 'woman', 'man', 'woman', 'man', 'woman', 'man', 'woman']
acne_df110_sum
acne_df110_sum = acne_df110_sum.reset_index(drop=True, inplace=True)
acne_df110_sum
acne_sex = acne_df110_sum.sort_values(by=['년도'])

p3 = sns.set_palette('deep', 5)
q = sns.barplot(data=acne_df110_sum, x='year', y=0, hue='sex', palette=p3)
ax = q
for i in ax.patches:
    ax.annotate('%.0f' % i.get_height(), (i.get_x() + i.get_width()/2, i.get_height()-30), ha='center', va='center', fontsize=10, color='black', xytext=(0, 10), textcoords='offset points')
plt.xticks(fontsize=12)
plt.xlabel('연도별',fontsize=12)
plt.ylabel('환자 수', fontsize=12)

#===================================================================================================================
# 네이버 뉴스 api

client_id = "C2QUU8idCr59BHXMN1qx"
client_secret = "s62CxCE2rP"

q = urllib.parse.quote('여드름')
idx = 0
display = 100
start = 1
end = 1000
sort = 'sim'

in_df = pd.DataFrame(columns=('title', 'description'))

for i in range(start, end, display):
  url = "https://openapi.naver.com/v1/search/news?query=" + q \
        + '&display=' + str(display) \
        + '&start=' + str(i) \
        + '&sort=' + sort

  request = urllib.request.Request(url)
  request.add_header("X-Naver-Client-Id",client_id)
  request.add_header("X-Naver-Client-Secret",client_secret)
  response = urllib.request.urlopen(request)
  rescode = response.getcode()
  if(rescode==200): # 정상적으로 코드를 받으면 200 표시
      response_body = response.read()
      response_dict = json.loads(response_body.decode('utf-8'))
      items = response_dict['items']
      for i_index in range(0, len(items)):
        remove_tag = re.compile('[^가-힣 ]')
        title = re.sub(remove_tag, '', items[i_index]['title'])
        description = re.sub(remove_tag, '', items[i_index]['description'])
        in_df.loc[idx] = [title, description]
        idx += 1
  else:
      print("Error Code:" + rescode)

news = pd.DataFrame(columns = ['description'])
news['description'] = in_df['description']



stop_word = []
with open('c:/data/stop_words.txt', 'r', encoding='utf-8') as s:
    for word in s:
        stop_word.append(word.strip())
stop_word
from konlpy.tag import Okt
pos = Okt()
def text_tokenizing(doc):
    return [word for word in pos.nouns(doc) if word not in stop_word and len(word) > 1]
contents_token = [text_tokenizing(i) for i in news['description']]
contents = [' '.join(i) for i in contents_token]
split = ''
news_contents = split.join(contents)
news_contents = news_contents.split()

news_contents
news_contents1 = Counter(news_contents)
news_contents1 = news_contents1.most_common(20)
news_contents = pd.DataFrame(news_contents1)

news_contents.drop([news_contents.index[10], news_contents.index[16]], inplace=True)

g = sns.barplot(x=news_contents[0], y=news_contents[1], data=news_contents)
ax = g
for i in ax.patches:
    ax.annotate('%.0f' % i.get_height(), (i.get_x() + i.get_width()/2, i.get_height()-30), ha='center', va='center', fontsize=10, color='black', xytext=(0, 10), textcoords='offset points')
plt.xticks(fontsize=12, rotation=45)
plt.xlabel('단어',fontsize=12)
plt.ylabel('cnt', fontsize=12)
plt.show()
plt.savefig('new_count.png')



wordcloud = WordCloud(font_path='c://windows//fonts//malgunbd.ttf', width = 900,height = 900,background_color = 'white',stopwords = 
STOPWORDS).generate(str(news_contents))
fig = plt.figure(figsize = (10, 30),facecolor = 'k',edgecolor = 'k')
plt.imshow(wordcloud, interpolation = 'nearest')
plt.axis('off')
plt.tight_layout(pad=0)
plt.show()   



#===========================================================================================
# L70 ~ L709, L730 여드름 질병코드

acnes_2016 = pd.read_csv('c:/data/final/medi_2016.csv', encoding='CP949')
acnes_2016 = acnes_2016.groupby('연령군').sum()
acnes_2016 = acnes_2016.drop(['진료년도'], axis=1)
acnes_2016.reset_index(inplace=True)
acnes_2016.to_csv('c:/data/final/l2016.csv', encoding='CP949', index=False)

acnes_2017 = pd.read_csv('c:/data/final/medi_2017.csv', encoding='CP949')
acnes_2017 = acnes_2017.groupby('연령군').sum()
acnes_2017 = acnes_2017.drop(['진료년도'], axis=1)
acnes_2017.reset_index(inplace=True)
acnes_2017.to_csv('c:/data/final/l2017.csv', encoding='CP949', index=False)

acnes_2018 = pd.read_csv('c:/data/final/medi_2018.csv', encoding='CP949')
acnes_2018 = acnes_2018.groupby('연령군').sum()
acnes_2018 = acnes_2018.drop(['진료년도'], axis=1)
acnes_2018.reset_index(inplace=True)
acnes_2018.to_csv('c:/data/final/l2018.csv', encoding='CP949', index=False)


acne_2016 = pd.read_csv('c:/data/final/l2016.csv', encoding='cp949')
acne_2017 = pd.read_csv('c:/data/final/l2017.csv', encoding='cp949')
acne_2018 = pd.read_csv('c:/data/final/l2018.csv', encoding='cp949')


medi_1618 = pd.read_csv('c:/data/final/medi_2013_18.csv', encoding='cp949')
medi0131 = medi_1618.loc[medi_1618['행위코드'].isin(['N0131', 'N0132', 'N0133'])]

medi0131.drop(medi0131[medi0131['진료년도'].isin([2013, 2014, 2015])].index, inplace=True)

medi0131.drop(medi0131[medi0131['의료기관종별'].isin(['요양병원', '치과병원', '보건의료원'])].index, inplace=True)
medi0131
hos_medi0131 = medi0131.groupby('의료기관종별').sum()
hos_medi_acne = hos_medi0131.drop('진료년도', axis=1)

#의료기관별 건수
hos_medi_acne

year_medi_acne = medi0131.groupby('진료년도').sum()

#년도별 건수
year_medi_acne


#======================================================================================================================================


l70 = pd.read_excel('c:/data/final/l70_외래.xls', encoding='cp949')
l70

l70.rename(columns = {'환자수':'환자수.0'}, inplace=True)

cnt = 0
l = []
for i in range(0, 36):
    l.append(l70['환자수.{}'.format(i)])
    cnt += 1

l70 = pd.DataFrame(l)
l70 = l70.drop([2,3, 5], axis=1)
l70.columns = ['총합', '남성', '여성']

l70.loc[l70['남성'] == '-', '남성'] = 0
l70.loc[l70['여성'] == '-', '여성'] = 0
l70
l70 = l70.astype(int)

l70 = l70.rename(index = {'환자수.0':'2016_1', '환자수.1':'2016_2', '환자수.2':'2016_3',  '환자수.3':'2016_4', '환자수.4':'2016_5',
                             '환자수.5':'2016_6', '환자수.6':'2016_7', '환자수.7':'2016_8',
                              '환자수.8':'2016_9', '환자수.9':'2016_10', '환자수.10':'2016_11', '환자수.11':'2016_12',
                               '환자수.12':'2017_1', '환자수.13':'2017_2', '환자수.14':'2017_3', '환자수.15':'2017_4',
                                '환자수.16':'2017_5', '환자수.17':'2017_6', '환자수.18':'2017_7', '환자수.19':'2017_8',
                                 '환자수.20':'2017_9', '환자수.21':'2017_10', '환자수.22':'2017_11', '환자수.23':'2017_12',
                                  '환자수.24':'2018_1', '환자수.25':'2018_2', '환자수.26':'2018_3', '환자수.27':'2018_4',
                                   '환자수.28':'2018_5', '환자수.29':'2018_6', '환자수.30':'2018_7', '환자수.31':'2018_8',
                                    '환자수.32':'2018_9', '환자수.33':'2018_10', '환자수.34':'2018_11', '환자수.35':'2018_12',
                                    '환자수.36':'2019_1', '환자수.37':'2019_2', '환자수.38':'2019_3', '환자수.39':'2019_4',
                                    '환자수.40':'2019_5', '환자수.41':'2019_6', '환자수.42':'2019_7', '환자수.43':'2019_8',
                                    '환자수.44':'2019_9', '환자수.45':'2019_10', '환자수.46':'2019_11', '환자수.47':'2019_12',
                                    '환자수.48':'2020_1', '환자수.49':'2020_2', '환자수.50':'2020_3', '환자수.51':'2020_4',
                                    '환자수.52':'2020_5', '환자수.53':'2020_6', '환자수.54':'2020_7', '환자수.55':'2020_8',
                                    '환자수.56':'2020_9'})

l70
plt.plot(l70['여성'])

#======================================================================================================================================


l700 = pd.read_excel('c:/data/final/l700_외래.xls', encoding='cp949')


l700.rename(columns = {'환자수':'환자수.0'}, inplace=True)

cnt = 0
l = []
for i in range(0, 36):
    l.append(l700['환자수.{}'.format(i)])
    cnt += 1

l700 = pd.DataFrame(l)
l700 = l700.drop([2,3, 5], axis=1)
l700.columns = ['총합', '남성', '여성']

l700.loc[l700['남성'] == '-', '남성'] = 0
l700.loc[l700['여성'] == '-', '여성'] = 0
l700
l700 = l700.astype(int)

l700 = l700.rename(index = {'환자수.0':'2016_1', '환자수.1':'2016_2', '환자수.2':'2016_3',  '환자수.3':'2016_4', '환자수.4':'2016_5',
                             '환자수.5':'2016_6', '환자수.6':'2016_7', '환자수.7':'2016_8',
                              '환자수.8':'2016_9', '환자수.9':'2016_10', '환자수.10':'2016_11', '환자수.11':'2016_12',
                               '환자수.12':'2017_1', '환자수.13':'2017_2', '환자수.14':'2017_3', '환자수.15':'2017_4',
                                '환자수.16':'2017_5', '환자수.17':'2017_6', '환자수.18':'2017_7', '환자수.19':'2017_8',
                                 '환자수.20':'2017_9', '환자수.21':'2017_10', '환자수.22':'2017_11', '환자수.23':'2017_12',
                                  '환자수.24':'2018_1', '환자수.25':'2018_2', '환자수.26':'2018_3', '환자수.27':'2018_4',
                                   '환자수.28':'2018_5', '환자수.29':'2018_6', '환자수.30':'2018_7', '환자수.31':'2018_8',
                                    '환자수.32':'2018_9', '환자수.33':'2018_10', '환자수.34':'2018_11', '환자수.35':'2018_12',
                                    '환자수.36':'2019_1', '환자수.37':'2019_2', '환자수.38':'2019_3', '환자수.39':'2019_4',
                                    '환자수.40':'2019_5', '환자수.41':'2019_6', '환자수.42':'2019_7', '환자수.43':'2019_8',
                                    '환자수.44':'2019_9', '환자수.45':'2019_10', '환자수.46':'2019_11', '환자수.47':'2019_12',
                                    '환자수.48':'2020_1', '환자수.49':'2020_2', '환자수.50':'2020_3', '환자수.51':'2020_4',
                                    '환자수.52':'2020_5', '환자수.53':'2020_6', '환자수.54':'2020_7', '환자수.55':'2020_8',
                                    '환자수.56':'2020_9'})

l700

plt.plot(l700['여성'])

#======================================================================================================================================


l701 = pd.read_excel('c:/data/final/l701_외래.xls', encoding='cp949')

l701.rename(columns = {'환자수':'환자수.0'}, inplace=True)
l701.info()

cnt = 0
l = []
for i in range(0, 36):
    l.append(l701['환자수.{}'.format(i)])
    cnt += 1

l701 = pd.DataFrame(l)
l701 = l701.drop([2,3, 5, 6], axis=1)
l701.columns = ['총합', '남성', '여성']

l701['총합'] = l701['총합'].str.replace(',', '').astype(int)
l701['남성'] = l701['남성'].str.replace(',', '').astype(int)
l701['여성'] = l701['여성'].str.replace(',', '').astype(int)

l701.astype(int)

l701 = l701.rename(index = {'환자수.0':'2016_1', '환자수.1':'2016_2', '환자수.2':'2016_3',  '환자수.3':'2016_4', '환자수.4':'2016_5',
                             '환자수.5':'2016_6', '환자수.6':'2016_7', '환자수.7':'2016_8',
                              '환자수.8':'2016_9', '환자수.9':'2016_10', '환자수.10':'2016_11', '환자수.11':'2016_12',
                               '환자수.12':'2017_1', '환자수.13':'2017_2', '환자수.14':'2017_3', '환자수.15':'2017_4',
                                '환자수.16':'2017_5', '환자수.17':'2017_6', '환자수.18':'2017_7', '환자수.19':'2017_8',
                                 '환자수.20':'2017_9', '환자수.21':'2017_10', '환자수.22':'2017_11', '환자수.23':'2017_12',
                                  '환자수.24':'2018_1', '환자수.25':'2018_2', '환자수.26':'2018_3', '환자수.27':'2018_4',
                                   '환자수.28':'2018_5', '환자수.29':'2018_6', '환자수.30':'2018_7', '환자수.31':'2018_8',
                                    '환자수.32':'2018_9', '환자수.33':'2018_10', '환자수.34':'2018_11', '환자수.35':'2018_12',
                                    '환자수.36':'2019_1', '환자수.37':'2019_2', '환자수.38':'2019_3', '환자수.39':'2019_4',
                                    '환자수.40':'2019_5', '환자수.41':'2019_6', '환자수.42':'2019_7', '환자수.43':'2019_8',
                                    '환자수.44':'2019_9', '환자수.45':'2019_10', '환자수.46':'2019_11', '환자수.47':'2019_12',
                                    '환자수.48':'2020_1', '환자수.49':'2020_2', '환자수.50':'2020_3', '환자수.51':'2020_4',
                                    '환자수.52':'2020_5', '환자수.53':'2020_6', '환자수.54':'2020_7', '환자수.55':'2020_8',
                                    '환자수.56':'2020_9'})

l701

plt.plot(l701)


#======================================================================================================================================


l702 = pd.read_excel('c:/data/final/l702_외래.xls', encoding='cp949')

l702.rename(columns = {'환자수':'환자수.0'}, inplace=True)
l702

cnt = 0
l = []
for i in range(0, 36):
    l.append(l702['환자수.{}'.format(i)])
    cnt += 1

l702 = pd.DataFrame(l)
l702 = l702.drop([2,3, 5], axis=1)
l702.columns = ['총합', '남성', '여성']

l702 = l702.astype(int)
l702

l702 = l702.rename(index = {'환자수.0':'2016_1', '환자수.1':'2016_2', '환자수.2':'2016_3',  '환자수.3':'2016_4', '환자수.4':'2016_5',
                             '환자수.5':'2016_6', '환자수.6':'2016_7', '환자수.7':'2016_8',
                              '환자수.8':'2016_9', '환자수.9':'2016_10', '환자수.10':'2016_11', '환자수.11':'2016_12',
                               '환자수.12':'2017_1', '환자수.13':'2017_2', '환자수.14':'2017_3', '환자수.15':'2017_4',
                                '환자수.16':'2017_5', '환자수.17':'2017_6', '환자수.18':'2017_7', '환자수.19':'2017_8',
                                 '환자수.20':'2017_9', '환자수.21':'2017_10', '환자수.22':'2017_11', '환자수.23':'2017_12',
                                  '환자수.24':'2018_1', '환자수.25':'2018_2', '환자수.26':'2018_3', '환자수.27':'2018_4',
                                   '환자수.28':'2018_5', '환자수.29':'2018_6', '환자수.30':'2018_7', '환자수.31':'2018_8',
                                    '환자수.32':'2018_9', '환자수.33':'2018_10', '환자수.34':'2018_11', '환자수.35':'2018_12',
                                    '환자수.36':'2019_1', '환자수.37':'2019_2', '환자수.38':'2019_3', '환자수.39':'2019_4',
                                    '환자수.40':'2019_5', '환자수.41':'2019_6', '환자수.42':'2019_7', '환자수.43':'2019_8',
                                    '환자수.44':'2019_9', '환자수.45':'2019_10', '환자수.46':'2019_11', '환자수.47':'2019_12',
                                    '환자수.48':'2020_1', '환자수.49':'2020_2', '환자수.50':'2020_3', '환자수.51':'2020_4',
                                    '환자수.52':'2020_5', '환자수.53':'2020_6', '환자수.54':'2020_7', '환자수.55':'2020_8',
                                    '환자수.56':'2020_9'})
l702

plt.plot(l702['총합'])


#======================================================================================================================================


l703 = pd.read_excel('c:/data/final/l703_외래.xls', encoding='cp949')

l703.rename(columns = {'환자수':'환자수.0'}, inplace=True)
l703

cnt = 0
l = []
for i in range(0, 35):
    l.append(l703['환자수.{}'.format(i)])
    cnt += 1

l703 = pd.DataFrame(l)
l703 = l703.drop([2,3], axis=1)
l703.columns = ['총합', '남성', '여성']

l703.loc[l703['남성'] == '-', '남성'] = 0
l703.loc[l703['여성'] == '-', '여성'] = 0

l703 = l703.astype(int)
l703

l703 = l703.rename(index = {'환자수.0':'2016_1', '환자수.1':'2016_2', '환자수.2':'2016_3',  '환자수.3':'2016_4', '환자수.4':'2016_5',
                             '환자수.5':'2016_6', '환자수.6':'2016_7', '환자수.7':'2016_8',
                              '환자수.8':'2016_9', '환자수.9':'2016_10', '환자수.10':'2016_11', '환자수.11':'2016_12',
                               '환자수.12':'2017_1', '환자수.13':'2017_2', '환자수.14':'2017_3', '환자수.15':'2017_4',
                                '환자수.16':'2017_5', '환자수.17':'2017_6', '환자수.18':'2017_7', '환자수.19':'2017_8',
                                 '환자수.20':'2017_9', '환자수.21':'2017_10', '환자수.22':'2017_11', '환자수.23':'2017_12',
                                  '환자수.24':'2018_1', '환자수.25':'2018_2', '환자수.26':'2018_3', '환자수.27':'2018_4',
                                   '환자수.28':'2018_5', '환자수.29':'2018_6', '환자수.30':'2018_7', '환자수.31':'2018_8',
                                    '환자수.32':'2018_9', '환자수.33':'2018_10', '환자수.34':'2018_11', '환자수.35':'2018_12',
                                    '환자수.36':'2019_1', '환자수.37':'2019_2', '환자수.38':'2019_3', '환자수.39':'2019_4',
                                    '환자수.40':'2019_5', '환자수.41':'2019_6', '환자수.42':'2019_7', '환자수.43':'2019_8',
                                    '환자수.44':'2019_9', '환자수.45':'2019_10', '환자수.46':'2019_11', '환자수.47':'2019_12',
                                    '환자수.48':'2020_1', '환자수.49':'2020_2', '환자수.50':'2020_3', '환자수.51':'2020_4',
                                    '환자수.52':'2020_5', '환자수.53':'2020_6', '환자수.54':'2020_7', '환자수.55':'2020_8',
                                    '환자수.56':'2020_9'})

l703.loc['2018_12'] = [0, 0, 0]
l703
plt.plot(l703['총합'])



#======================================================================================================================================


l704 = pd.read_excel('c:/data/final/l704_외래.xls', encoding='cp949')

l704.rename(columns = {'환자수':'환자수.0'}, inplace=True)
l704

cnt = 0
l = []
for i in range(0, 36):
    l.append(l704['환자수.{}'.format(i)])
    cnt += 1

l704 = pd.DataFrame(l)
l704 = l704.drop([2,3, 5, 6], axis=1)
l704.columns = ['총합', '남성', '여성']

l704 = l704.astype(int)
l704

l704 = l704.rename(index = {'환자수.0':'2016_1', '환자수.1':'2016_2', '환자수.2':'2016_3',  '환자수.3':'2016_4', '환자수.4':'2016_5',
                             '환자수.5':'2016_6', '환자수.6':'2016_7', '환자수.7':'2016_8',
                              '환자수.8':'2016_9', '환자수.9':'2016_10', '환자수.10':'2016_11', '환자수.11':'2016_12',
                               '환자수.12':'2017_1', '환자수.13':'2017_2', '환자수.14':'2017_3', '환자수.15':'2017_4',
                                '환자수.16':'2017_5', '환자수.17':'2017_6', '환자수.18':'2017_7', '환자수.19':'2017_8',
                                 '환자수.20':'2017_9', '환자수.21':'2017_10', '환자수.22':'2017_11', '환자수.23':'2017_12',
                                  '환자수.24':'2018_1', '환자수.25':'2018_2', '환자수.26':'2018_3', '환자수.27':'2018_4',
                                   '환자수.28':'2018_5', '환자수.29':'2018_6', '환자수.30':'2018_7', '환자수.31':'2018_8',
                                    '환자수.32':'2018_9', '환자수.33':'2018_10', '환자수.34':'2018_11', '환자수.35':'2018_12',
                                    '환자수.36':'2019_1', '환자수.37':'2019_2', '환자수.38':'2019_3', '환자수.39':'2019_4',
                                    '환자수.40':'2019_5', '환자수.41':'2019_6', '환자수.42':'2019_7', '환자수.43':'2019_8',
                                    '환자수.44':'2019_9', '환자수.45':'2019_10', '환자수.46':'2019_11', '환자수.47':'2019_12',
                                    '환자수.48':'2020_1', '환자수.49':'2020_2', '환자수.50':'2020_3', '환자수.51':'2020_4',
                                    '환자수.52':'2020_5', '환자수.53':'2020_6', '환자수.54':'2020_7', '환자수.55':'2020_8',
                                    '환자수.56':'2020_9'})

l704

plt.plot(l704['총합'])

#======================================================================================================================================


l705 = pd.read_excel('c:/data/final/l705_외래.xls', encoding='cp949')

l705.rename(columns = {'환자수':'환자수.0'}, inplace=True)
l705

cnt = 0
l = []
for i in range(0, 36):
    l.append(l705['환자수.{}'.format(i)])
    cnt += 1

l705 = pd.DataFrame(l)
l705 = l705.drop([2,4], axis=1)
l705.columns = ['총합', '남성', '여성']
l705

l705.loc[l705['남성'] == '-', '남성'] = 0
l705.loc[l705['여성'] == '-', '여성'] = 0

l705 = l705.astype(int)
l705

l705 = l705.rename(index = {'환자수.0':'2016_1', '환자수.1':'2016_2', '환자수.2':'2016_3',  '환자수.3':'2016_4', '환자수.4':'2016_5',
                             '환자수.5':'2016_6', '환자수.6':'2016_7', '환자수.7':'2016_8',
                              '환자수.8':'2016_9', '환자수.9':'2016_10', '환자수.10':'2016_11', '환자수.11':'2016_12',
                               '환자수.12':'2017_1', '환자수.13':'2017_2', '환자수.14':'2017_3', '환자수.15':'2017_4',
                                '환자수.16':'2017_5', '환자수.17':'2017_6', '환자수.18':'2017_7', '환자수.19':'2017_8',
                                 '환자수.20':'2017_9', '환자수.21':'2017_10', '환자수.22':'2017_11', '환자수.23':'2017_12',
                                  '환자수.24':'2018_1', '환자수.25':'2018_2', '환자수.26':'2018_3', '환자수.27':'2018_4',
                                   '환자수.28':'2018_5', '환자수.29':'2018_6', '환자수.30':'2018_7', '환자수.31':'2018_8',
                                    '환자수.32':'2018_9', '환자수.33':'2018_10', '환자수.34':'2018_11', '환자수.35':'2018_12',
                                    '환자수.36':'2019_1', '환자수.37':'2019_2', '환자수.38':'2019_3', '환자수.39':'2019_4',
                                    '환자수.40':'2019_5', '환자수.41':'2019_6', '환자수.42':'2019_7', '환자수.43':'2019_8',
                                    '환자수.44':'2019_9', '환자수.45':'2019_10', '환자수.46':'2019_11', '환자수.47':'2019_12',
                                    '환자수.48':'2020_1', '환자수.49':'2020_2', '환자수.50':'2020_3', '환자수.51':'2020_4',
                                    '환자수.52':'2020_5', '환자수.53':'2020_6', '환자수.54':'2020_7', '환자수.55':'2020_8',
                                    '환자수.56':'2020_9'})

l705

plt.plot(l705['총합'])

#======================================================================================================================================


l708 = pd.read_excel('c:/data/final/l708_외래.xls', encoding='cp949')

l708.rename(columns = {'환자수':'환자수.0'}, inplace=True)
l708

cnt = 0
l = []
for i in range(0, 36):
    l.append(l708['환자수.{}'.format(i)])
    cnt += 1

l708 = pd.DataFrame(l)
l708 = l708.drop([2,3, 5, 6], axis=1)
l708.columns = ['총합', '남성', '여성']
l708

l708 = l708.astype(int)
l708

l708 = l708.rename(index = {'환자수.0':'2016_1', '환자수.1':'2016_2', '환자수.2':'2016_3',  '환자수.3':'2016_4', '환자수.4':'2016_5',
                             '환자수.5':'2016_6', '환자수.6':'2016_7', '환자수.7':'2016_8',
                              '환자수.8':'2016_9', '환자수.9':'2016_10', '환자수.10':'2016_11', '환자수.11':'2016_12',
                               '환자수.12':'2017_1', '환자수.13':'2017_2', '환자수.14':'2017_3', '환자수.15':'2017_4',
                                '환자수.16':'2017_5', '환자수.17':'2017_6', '환자수.18':'2017_7', '환자수.19':'2017_8',
                                 '환자수.20':'2017_9', '환자수.21':'2017_10', '환자수.22':'2017_11', '환자수.23':'2017_12',
                                  '환자수.24':'2018_1', '환자수.25':'2018_2', '환자수.26':'2018_3', '환자수.27':'2018_4',
                                   '환자수.28':'2018_5', '환자수.29':'2018_6', '환자수.30':'2018_7', '환자수.31':'2018_8',
                                    '환자수.32':'2018_9', '환자수.33':'2018_10', '환자수.34':'2018_11', '환자수.35':'2018_12',
                                    '환자수.36':'2019_1', '환자수.37':'2019_2', '환자수.38':'2019_3', '환자수.39':'2019_4',
                                    '환자수.40':'2019_5', '환자수.41':'2019_6', '환자수.42':'2019_7', '환자수.43':'2019_8',
                                    '환자수.44':'2019_9', '환자수.45':'2019_10', '환자수.46':'2019_11', '환자수.47':'2019_12',
                                    '환자수.48':'2020_1', '환자수.49':'2020_2', '환자수.50':'2020_3', '환자수.51':'2020_4',
                                    '환자수.52':'2020_5', '환자수.53':'2020_6', '환자수.54':'2020_7', '환자수.55':'2020_8',
                                    '환자수.56':'2020_9'})

l708

plt.plot(l708['총합'])

#======================================================================================================================================


l709 = pd.read_excel('c:/data/final/l709_외래.xls', encoding='cp949')

l709.rename(columns = {'환자수':'환자수.0'}, inplace=True)
l709

cnt = 0
l = []
for i in range(0, 36):
    l.append(l709['환자수.{}'.format(i)])
    cnt += 1

l709 = pd.DataFrame(l)
l709 = l709.drop([2,3, 5], axis=1)
l709.columns = ['총합', '남성', '여성']
l709

l709['총합'] = l709['총합'].str.replace(',', '').astype(int)

l709 = l709.astype(int)
l709

l709 = l709.rename(index = {'환자수.0':'2016_1', '환자수.1':'2016_2', '환자수.2':'2016_3',  '환자수.3':'2016_4', '환자수.4':'2016_5',
                             '환자수.5':'2016_6', '환자수.6':'2016_7', '환자수.7':'2016_8',
                              '환자수.8':'2016_9', '환자수.9':'2016_10', '환자수.10':'2016_11', '환자수.11':'2016_12',
                               '환자수.12':'2017_1', '환자수.13':'2017_2', '환자수.14':'2017_3', '환자수.15':'2017_4',
                                '환자수.16':'2017_5', '환자수.17':'2017_6', '환자수.18':'2017_7', '환자수.19':'2017_8',
                                 '환자수.20':'2017_9', '환자수.21':'2017_10', '환자수.22':'2017_11', '환자수.23':'2017_12',
                                  '환자수.24':'2018_1', '환자수.25':'2018_2', '환자수.26':'2018_3', '환자수.27':'2018_4',
                                   '환자수.28':'2018_5', '환자수.29':'2018_6', '환자수.30':'2018_7', '환자수.31':'2018_8',
                                    '환자수.32':'2018_9', '환자수.33':'2018_10', '환자수.34':'2018_11', '환자수.35':'2018_12',
                                    '환자수.36':'2019_1', '환자수.37':'2019_2', '환자수.38':'2019_3', '환자수.39':'2019_4',
                                    '환자수.40':'2019_5', '환자수.41':'2019_6', '환자수.42':'2019_7', '환자수.43':'2019_8',
                                    '환자수.44':'2019_9', '환자수.45':'2019_10', '환자수.46':'2019_11', '환자수.47':'2019_12',
                                    '환자수.48':'2020_1', '환자수.49':'2020_2', '환자수.50':'2020_3', '환자수.51':'2020_4',
                                    '환자수.52':'2020_5', '환자수.53':'2020_6', '환자수.54':'2020_7', '환자수.55':'2020_8',
                                    '환자수.56':'2020_9'})

l709

plt.plot(l709['총합'])

#======================================================================================================================================


l730 = pd.read_excel('c:/data/final/l730_외래.xls', encoding='cp949')

l730.rename(columns = {'환자수':'환자수.0'}, inplace=True)
l730

cnt = 0
l = []
for i in range(0, 36):
    l.append(l730['환자수.{}'.format(i)])
    cnt += 1

l730 = pd.DataFrame(l)
l730 = l730.drop([2,3, 5, 6], axis=1)
l730.columns = ['총합', '남성', '여성']
l730

l730 = l730.astype(int)
l730

l730 = l730.rename(index = {'환자수.0':'2016_1', '환자수.1':'2016_2', '환자수.2':'2016_3',  '환자수.3':'2016_4', '환자수.4':'2016_5',
                             '환자수.5':'2016_6', '환자수.6':'2016_7', '환자수.7':'2016_8',
                              '환자수.8':'2016_9', '환자수.9':'2016_10', '환자수.10':'2016_11', '환자수.11':'2016_12',
                               '환자수.12':'2017_1', '환자수.13':'2017_2', '환자수.14':'2017_3', '환자수.15':'2017_4',
                                '환자수.16':'2017_5', '환자수.17':'2017_6', '환자수.18':'2017_7', '환자수.19':'2017_8',
                                 '환자수.20':'2017_9', '환자수.21':'2017_10', '환자수.22':'2017_11', '환자수.23':'2017_12',
                                  '환자수.24':'2018_1', '환자수.25':'2018_2', '환자수.26':'2018_3', '환자수.27':'2018_4',
                                   '환자수.28':'2018_5', '환자수.29':'2018_6', '환자수.30':'2018_7', '환자수.31':'2018_8',
                                    '환자수.32':'2018_9', '환자수.33':'2018_10', '환자수.34':'2018_11', '환자수.35':'2018_12',
                                    '환자수.36':'2019_1', '환자수.37':'2019_2', '환자수.38':'2019_3', '환자수.39':'2019_4',
                                    '환자수.40':'2019_5', '환자수.41':'2019_6', '환자수.42':'2019_7', '환자수.43':'2019_8',
                                    '환자수.44':'2019_9', '환자수.45':'2019_10', '환자수.46':'2019_11', '환자수.47':'2019_12',
                                    '환자수.48':'2020_1', '환자수.49':'2020_2', '환자수.50':'2020_3', '환자수.51':'2020_4',
                                    '환자수.52':'2020_5', '환자수.53':'2020_6', '환자수.54':'2020_7', '환자수.55':'2020_8',
                                    '환자수.56':'2020_9', '환자수.57':'2020_10', '환자수.58':'2020_11', '환자수.59':'2020_12',})

l730


#=========================================================================================================================================
#=========================================================================================================================================


l70_1920 = pd.read_excel('c:/data/final/l70_1920.xls', encoding='cp949')
l70_1920

l70_1920.rename(columns = {'환자수':'환자수.0'}, inplace=True)

cnt = 0
l = []
for i in range(0, 14):
    l.append(l70_1920['환자수.{}'.format(i)])
    cnt += 1

l70_1920 = pd.DataFrame(l)
l70_1920 = l70_1920.drop([2,4], axis=1)
l70_1920.columns = ['총합', '남성', '여성']

l70_1920.loc[l70_1920['남성'] == '-', '남성'] = 0
l70_1920.loc[l70_1920['여성'] == '-', '여성'] = 0
l70_1920
l70_1920 = l70_1920.astype(int)

l70_1920 = l70_1920.rename(index = {'환자수.0':'2019_1', '환자수.1':'2019_2', '환자수.2':'2019_3',  '환자수.3':'2019_4', '환자수.4':'2019_5',
                             '환자수.5':'2019_6', '환자수.6':'2019_7', '환자수.7':'2019_8',
                              '환자수.8':'2019_9', '환자수.9':'2019_10', '환자수.10':'2019_11', '환자수.11':'2019_12',
                               '환자수.12':'2020_1', '환자수.13':'2020_2'})

l70_1920
plt.plot(l70_1920)

#======================================================================================================================================


l700_1920 = pd.read_excel('c:/data/final/l700_1920.xls', encoding='cp949')


l700_1920.rename(columns = {'환자수':'환자수.0'}, inplace=True)

cnt = 0
l = []
for i in range(0, 14):
    l.append(l700_1920['환자수.{}'.format(i)])
    cnt += 1

l700_1920 = pd.DataFrame(l)
l700_1920 = l700_1920.drop([2,3, 5], axis=1)
l700_1920.columns = ['총합', '남성', '여성']

l700_1920.loc[l700_1920['남성'] == '-', '남성'] = 0
l700_1920.loc[l700_1920['여성'] == '-', '여성'] = 0
l700_1920
l700_1920 = l700_1920.astype(int)

l700_1920 = l700_1920.rename(index = {'환자수.0':'2019_1', '환자수.1':'2019_2', '환자수.2':'2019_3',  '환자수.3':'2019_4', '환자수.4':'2019_5',
                             '환자수.5':'2019_6', '환자수.6':'2019_7', '환자수.7':'2019_8',
                              '환자수.8':'2019_9', '환자수.9':'2019_10', '환자수.10':'2019_11', '환자수.11':'2019_12',
                               '환자수.12':'2020_1', '환자수.13':'2020_2'})

l700_1920


plt.plot(l700_1920)

#======================================================================================================================================


l701_1920 = pd.read_excel('c:/data/final/l701_1920.xls', encoding='cp949')

l701_1920.rename(columns = {'환자수':'환자수.0'}, inplace=True)
l701_1920

cnt = 0
l = []
for i in range(0, 14):
    l.append(l701_1920['환자수.{}'.format(i)])
    cnt += 1

l701_1920 = pd.DataFrame(l)
l701_1920 = l701_1920.drop([2,3, 5, 6], axis=1)
l701_1920.columns = ['총합', '남성', '여성']

l701_1920['총합'] = l701_1920['총합'].str.replace(',', '').astype(int)
l701_1920['남성'] = l701_1920['남성'].str.replace(',', '').astype(int)
l701_1920['여성'] = l701_1920['여성'].str.replace(',', '').astype(int)

l701_1920 = l701_1920.astype(int)
l701_1920


l701_1920 = l701_1920.rename(index = {'환자수.0':'2019_1', '환자수.1':'2019_2', '환자수.2':'2019_3',  '환자수.3':'2019_4', '환자수.4':'2019_5',
                             '환자수.5':'2019_6', '환자수.6':'2019_7', '환자수.7':'2019_8',
                              '환자수.8':'2019_9', '환자수.9':'2019_10', '환자수.10':'2019_11', '환자수.11':'2019_12',
                               '환자수.12':'2020_1', '환자수.13':'2020_2'})

l701_1920

plt.plot(l701_1920)


#======================================================================================================================================


l702_1920 = pd.read_excel('c:/data/final/l702_1920.xls', encoding='cp949')

l702_1920.rename(columns = {'환자수':'환자수.0'}, inplace=True)
l702_1920

cnt = 0
l = []
for i in range(0, 14):
    l.append(l702_1920['환자수.{}'.format(i)])
    cnt += 1

l702_1920 = pd.DataFrame(l)
l702_1920 = l702_1920.drop([2,3, 5], axis=1)
l702_1920.columns = ['총합', '남성', '여성']

l702_1920 = l702_1920.astype(int)
l702_1920

l702_1920 = l702_1920.rename(index = {'환자수.0':'2019_1', '환자수.1':'2019_2', '환자수.2':'2019_3',  '환자수.3':'2019_4', '환자수.4':'2019_5',
                             '환자수.5':'2019_6', '환자수.6':'2019_7', '환자수.7':'2019_8',
                              '환자수.8':'2019_9', '환자수.9':'2019_10', '환자수.10':'2019_11', '환자수.11':'2019_12',
                               '환자수.12':'2020_1', '환자수.13':'2020_2'})
l702_1920

plt.plot(l702_1920)


#======================================================================================================================================


l703_1920 = pd.read_excel('c:/data/final/l703_1920.xls', encoding='cp949')

l703_1920.rename(columns = {'환자수':'환자수.0'}, inplace=True)
l703_1920

cnt = 0
l = []
for i in range(0, 13):
    l.append(l703_1920['환자수.{}'.format(i)])
    cnt += 1

l703_1920 = pd.DataFrame(l)
l703_1920 = l703_1920.drop([2,3], axis=1)
l703_1920.columns = ['총합', '남성', '여성']

l703_1920.loc[l703_1920['남성'] == '-', '남성'] = 0
l703_1920.loc[l703_1920['여성'] == '-', '여성'] = 0

l703_1920 = l703_1920.astype(int)
l703_1920

l703_1920 = l703_1920.rename(index = {'환자수.0':'2019_1', '환자수.1':'2019_2', '환자수.2':'2019_3',  '환자수.3':'2019_4', '환자수.4':'2019_5',
                             '환자수.5':'2019_6', '환자수.6':'2019_7', '환자수.7':'2019_8',
                              '환자수.8':'2019_9', '환자수.9':'2019_10', '환자수.10':'2019_11', '환자수.11':'2019_12',
                               '환자수.12':'2020_1', '환자수.13':'2020_2'})

l703_1920.loc['2020_2'] = [0, 0, 0]
l703_1920
plt.plot(l703_1920)



#======================================================================================================================================


l704_1920 = pd.read_excel('c:/data/final/l704_1920.xls', encoding='cp949')

l704_1920.rename(columns = {'환자수':'환자수.0'}, inplace=True)
l704_1920

cnt = 0
l = []
for i in range(0, 14):
    l.append(l704_1920['환자수.{}'.format(i)])
    cnt += 1

l704_1920 = pd.DataFrame(l)
l704_1920 = l704_1920.drop([2,3, 5, 6], axis=1)
l704_1920.columns = ['총합', '남성', '여성']

l704_1920 = l704_1920.astype(int)
l704_1920

l704_1920 = l704_1920.rename(index = {'환자수.0':'2019_1', '환자수.1':'2019_2', '환자수.2':'2019_3',  '환자수.3':'2019_4', '환자수.4':'2019_5',
                             '환자수.5':'2019_6', '환자수.6':'2019_7', '환자수.7':'2019_8',
                              '환자수.8':'2019_9', '환자수.9':'2019_10', '환자수.10':'2019_11', '환자수.11':'2019_12',
                               '환자수.12':'2020_1', '환자수.13':'2020_2'})

l704_1920

plt.plot(l704_1920)

#======================================================================================================================================


l705_1920 = pd.read_excel('c:/data/final/l705_1920.xls', encoding='cp949')

l705_1920.rename(columns = {'환자수':'환자수.0'}, inplace=True)
l705_1920

cnt = 0
l = []
for i in range(0, 14):
    l.append(l705_1920['환자수.{}'.format(i)])
    cnt += 1

l705_1920 = pd.DataFrame(l)
l705_1920 = l705_1920.drop([2,4], axis=1)
l705_1920.columns = ['총합', '남성', '여성']
l705_1920

l705_1920.loc[l705_1920['남성'] == '-', '남성'] = 0
l705_1920.loc[l705_1920['여성'] == '-', '여성'] = 0

l705_1920 = l705_1920.astype(int)
l705_1920

l705_1920 = l705_1920.rename(index = {'환자수.0':'2019_1', '환자수.1':'2019_2', '환자수.2':'2019_3',  '환자수.3':'2019_4', '환자수.4':'2019_5',
                             '환자수.5':'2019_6', '환자수.6':'2019_7', '환자수.7':'2019_8',
                              '환자수.8':'2019_9', '환자수.9':'2019_10', '환자수.10':'2019_11', '환자수.11':'2019_12',
                               '환자수.12':'2020_1', '환자수.13':'2020_2'})

l705_1920

plt.plot(l705_1920)

#======================================================================================================================================


l708_1920 = pd.read_excel('c:/data/final/l708_1920.xls', encoding='cp949')

l708_1920.rename(columns = {'환자수':'환자수.0'}, inplace=True)
l708_1920

cnt = 0
l = []
for i in range(0, 14):
    l.append(l708_1920['환자수.{}'.format(i)])
    cnt += 1

l708_1920 = pd.DataFrame(l)
l708_1920 = l708_1920.drop([2,3, 5, 6], axis=1)
l708_1920.columns = ['총합', '남성', '여성']
l708_1920

l708_1920 = l708_1920.astype(int)
l708_1920

l708_1920 = l708_1920.rename(index = {'환자수.0':'2019_1', '환자수.1':'2019_2', '환자수.2':'2019_3',  '환자수.3':'2019_4', '환자수.4':'2019_5',
                             '환자수.5':'2019_6', '환자수.6':'2019_7', '환자수.7':'2019_8',
                              '환자수.8':'2019_9', '환자수.9':'2019_10', '환자수.10':'2019_11', '환자수.11':'2019_12',
                               '환자수.12':'2020_1', '환자수.13':'2020_2'})

l708_1920

plt.plot(l708_1920)

#======================================================================================================================================


l709_1920 = pd.read_excel('c:/data/final/l709_1920.xls', encoding='cp949')

l709_1920.rename(columns = {'환자수':'환자수.0'}, inplace=True)
l709_1920

cnt = 0
l = []
for i in range(0, 14):
    l.append(l709_1920['환자수.{}'.format(i)])
    cnt += 1

l709_1920 = pd.DataFrame(l)
l709_1920 = l709_1920.drop([2,3, 5], axis=1)
l709_1920.columns = ['총합', '남성', '여성']
l709_1920

l709_1920['총합'] = l709_1920['총합'].str.replace(',', '').astype(int)

l709_1920 = l709_1920.astype(int)
l709_1920

l709_1920 = l709_1920.rename(index = {'환자수.0':'2019_1', '환자수.1':'2019_2', '환자수.2':'2019_3',  '환자수.3':'2019_4', '환자수.4':'2019_5',
                             '환자수.5':'2019_6', '환자수.6':'2019_7', '환자수.7':'2019_8',
                              '환자수.8':'2019_9', '환자수.9':'2019_10', '환자수.10':'2019_11', '환자수.11':'2019_12',
                               '환자수.12':'2020_1', '환자수.13':'2020_2'})

l709_1920

plt.plot(l709_1920)

#======================================================================================================================================


l730_1920 = pd.read_excel('c:/data/final/l730_1920.xls', encoding='cp949')

l730_1920.rename(columns = {'환자수':'환자수.0'}, inplace=True)
l730_1920

cnt = 0
l = []
for i in range(0, 14):
    l.append(l730_1920['환자수.{}'.format(i)])
    cnt += 1

l730_1920 = pd.DataFrame(l)
l730_1920 = l730_1920.drop([2,3, 5], axis=1)
l730_1920.columns = ['총합', '남성', '여성']
l730_1920

l730_1920 = l730_1920.astype(int)
l730_1920

l730_1920 = l730_1920.rename(index = {'환자수.0':'2019_1', '환자수.1':'2019_2', '환자수.2':'2019_3',  '환자수.3':'2019_4', '환자수.4':'2019_5',
                             '환자수.5':'2019_6', '환자수.6':'2019_7', '환자수.7':'2019_8',
                              '환자수.8':'2019_9', '환자수.9':'2019_10', '환자수.10':'2019_11', '환자수.11':'2019_12',
                               '환자수.12':'2020_1', '환자수.13':'2020_2'})

l730_1920





#==============================================================================================================================================




acne_l = pd.DataFrame(columns = ['총합', '남성', '여성'])

acne_l['총합'] = l70['총합'] + l700['총합'] + l701['총합'] + l702['총합'] + l703['총합'] + l704['총합'] + l705['총합'] + l708['총합'] + l709['총합'] + l730['총합']
acne_l['남성'] = l70['남성'] + l700['남성'] + l701['남성'] + l702['남성'] + l703['남성'] + l704['남성'] + l705['남성'] + l708['남성'] + l709['남성'] + l730['남성']
acne_l['여성'] = l70['여성'] + l700['여성'] + l701['여성'] + l702['여성'] + l703['여성'] + l704['여성'] + l705['여성'] + l708['여성'] + l709['여성'] + l730['여성']


acne_l.reset_index(inplace=True)
acne_l.columns = [['year', '총합', '남성', '여성']]
acne_l.info()


acne_l1920 = pd.DataFrame(columns = ['총합', '남성', '여성'])

acne_l1920['총합'] = l70_1920['총합'] + l700_1920['총합'] + l701_1920['총합'] + l702_1920['총합'] + l703_1920['총합'] + l704_1920['총합'] + l705_1920['총합'] + l708_1920['총합'] + l709_1920['총합'] + l730_1920['총합']
acne_l1920['남성'] = l70_1920['남성'] + l700_1920['남성'] + l701_1920['남성'] + l702_1920['남성'] + l703_1920['남성'] + l704_1920['남성'] + l705_1920['남성'] + l708_1920['남성'] + l709_1920['남성'] + l730_1920['남성']
acne_l1920['여성'] = l70_1920['여성'] + l700_1920['여성'] + l701_1920['여성'] + l702_1920['여성'] + l703_1920['여성'] + l704_1920['여성'] + l705_1920['여성'] + l708_1920['여성'] + l709_1920['여성'] + l730_1920['여성']



acne_l1920.reset_index(inplace=True)
acne_l1920.columns = [['year', '총합', '남성', '여성']]
acne_l1920


acne_l7_ = pd.concat([acne_l, acne_l1920])
acne_l7_.reset_index(drop=True, inplace=True)
acne_l7_.to_csv('c:/data/final/acne_l7_.csv', encoding='cp949')
acne_l7_


acne_con = pd.concat([acne_naver, acne_naver1, acne_naver2, acne_naver3, acne_naver4])

acne_con.reset_index(inplace=True, drop=True)
acne_con

acne_df = pd.concat([acne_l7_, acne_con], axis=1)


acne_df.drop(['period'], axis=1, inplace=True)

acne_df.columns = ['year', 'man/woman', 'man', 'woman', 'search']
acne_df

tta = pd.read_csv('c:/data/final/tta.csv', encoding='cp949')

tta.drop([50, 51, 52, 53, 54, 55, 56, 57], inplace=True)

tta.drop(['년월', '지점', '최저기온(℃)', '최고기온(℃)'], axis=1, inplace=True)

acne_df = pd.concat([acne_df, tta], axis=1)


acne_df.columns = ['year', 'man/woman', 'man', 'woman', 'search', 'temp(mean)']
acne_df.to_csv('c:/data/final/acne_df.csv', encoding='cp949', index=False)
acne_df = pd.read_csv('c:/data/final/acne_df.csv', encoding='cp949')
acne_df = acne_df.loc[:, ~acne_df.columns.str.contains('^Unnamed')]

acne_df2 = acne_df.drop(['man', 'woman'], axis=1)



acne_df2 = pd.read_csv('c:/data/final/acne_df2.csv', encoding='cp949')
acne_df2 = acne_df2.loc[:, ~acne_df2.columns.str.contains('^Unnamed')]

acne_df2['man/woman'] = acne_df2['man/woman'].astype('int')
acne_df2['search'] = acne_df2['search'].astype('int')
acne_df2['temp(mean)'] = acne_df2['temp(mean)'].astype('int')

acne_df2.to_csv('c:/data/final/acne_df2.csv', encoding='cp949', index=False)

acne_df2 = pd.read_csv('c:/data/final/acne_df2.csv', encoding='cp949')

acne_df2

#===================================================================================================================

#여드름 화장품 검색 트렌드


client_id = "a7sewAJZVT2hdTz17pJQ"
client_secret = "1dstmcRYya"

url = "https://openapi.naver.com/v1/datalab/search";
body = {
    'startDate' : '2016-01-01',
    'endDate' : '2016-12-31',
    'timeUnit' : 'month',        # input : [date, week, month]
    'keywordGroups' : [         #
        {'groupName': '화장품','keywords': ['여드름 화장품']},
        ],
}
body = json.dumps(body)
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
request.add_header("Content-Type","application/json")
response = urllib.request.urlopen(request, data=body.encode("utf-8"))
data = json.loads(response.read().decode('utf-8'))

tmp = pd.DataFrame(data['results'])
print(tmp)

res = data['results'][0]['data']
acne_cos = pd.DataFrame(res)


client_id = "a7sewAJZVT2hdTz17pJQ"
client_secret = "1dstmcRYya"

url = "https://openapi.naver.com/v1/datalab/search";
body = {
    'startDate' : '2017-01-01',
    'endDate' : '2017-12-31',
    'timeUnit' : 'month',        # input : [date, week, month]
    'keywordGroups' : [         #
        {'groupName': '화장품','keywords': ['여드름 화장품']},
        ],
}
body = json.dumps(body)
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
request.add_header("Content-Type","application/json")
response = urllib.request.urlopen(request, data=body.encode("utf-8"))
data = json.loads(response.read().decode('utf-8'))

tmp = pd.DataFrame(data['results'])
print(tmp)
res1 = data['results'][0]['data']
acne_cos1 = pd.DataFrame(res1)


client_id = "a7sewAJZVT2hdTz17pJQ"
client_secret = "1dstmcRYya"

url = "https://openapi.naver.com/v1/datalab/search";
body = {
    'startDate' : '2018-01-01',
    'endDate' : '2018-12-31',
    'timeUnit' : 'month',        # input : [date, week, month]
    'keywordGroups' : [         #
        {'groupName': '화장품','keywords': ['여드름 화장품']},
        ],
}
body = json.dumps(body)
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
request.add_header("Content-Type","application/json")
response = urllib.request.urlopen(request, data=body.encode("utf-8"))
data = json.loads(response.read().decode('utf-8'))

tmp = pd.DataFrame(data['results'])
print(tmp)
res2 = data['results'][0]['data']
acne_cos2 = pd.DataFrame(res2)


client_id = "a7sewAJZVT2hdTz17pJQ"
client_secret = "1dstmcRYya"

url = "https://openapi.naver.com/v1/datalab/search";
body = {
    'startDate' : '2019-01-01',
    'endDate' : '2019-12-31',
    'timeUnit' : 'month',        # input : [date, week, month]
    'keywordGroups' : [         #
        {'groupName': '화장품','keywords': ['여드름 화장품']},
        ],
}
body = json.dumps(body)
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
request.add_header("Content-Type","application/json")
response = urllib.request.urlopen(request, data=body.encode("utf-8"))
data = json.loads(response.read().decode('utf-8'))

tmp = pd.DataFrame(data['results'])
print(tmp)
res3 = data['results'][0]['data']
acne_cos3 = pd.DataFrame(res3)


client_id = "a7sewAJZVT2hdTz17pJQ"
client_secret = "1dstmcRYya"

url = "https://openapi.naver.com/v1/datalab/search";
body = {
    'startDate' : '2020-01-01',
    'endDate' : '2020-02-28',
    'timeUnit' : 'month',        # input : [date, week, month]
    'keywordGroups' : [         #
        {'groupName': '화장품','keywords': ['여드름 화장품']},
        ],
}
body = json.dumps(body)
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
request.add_header("Content-Type","application/json")
response = urllib.request.urlopen(request, data=body.encode("utf-8"))
data = json.loads(response.read().decode('utf-8'))

tmp = pd.DataFrame(data['results'])
print(tmp)
res4 = data['results'][0]['data']
acne_cos4 = pd.DataFrame(res4)

ac = pd.concat([acne_cos, acne_cos1, acne_cos2, acne_cos3, acne_cos4])

plt.bar(height = ac['ratio'], x = ac['period'])

#=============================================================================

pm_2016 = pd.read_csv('c:/data/final/pol_2016.csv', encoding='cp949')
pm_2016 = pm_2016.fillna(0)
pm_2016 = pm_2016.drop(pm_2016.index[66:101])
pm_2016 = pm_2016.drop(pm_2016.columns[[14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44]],axis=1)

cols = ['1월', '2월', '3월','4월', '5월', '6월', '7월', '8월', '9월', '10월', '11월', '12월', '연평균']
for col in cols:
       pm_2016[col] = pm_2016[col].map(lambda x: str(x).lstrip('*').rstrip('*')).astype(int)

pm_2016.to_csv('c:/data/final/pol_2016.csv', encoding='cp949', index=False)
pm_2016

pm_2017 = pd.read_csv('c:/data/final/pol_2017.csv', encoding='cp949')
pm_2017 = pm_2017.fillna(0)
pm_2017 = pm_2017.drop(pm_2017.index[91:126])
pm_2017 = pm_2017.drop(pm_2017.columns[[14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44]],axis=1)

pm_2017['1월'] = pm_2017['1월'].astype('int')
pm_2017['3월'] = pm_2017['3월'].astype('int')
pm_2017['4월'] = pm_2017['4월'].astype('int')

cols = ['1월', '2월', '3월','4월', '5월', '6월', '7월', '8월', '9월', '10월', '11월', '12월', '연평균']
for col in cols:
       pm_2017[col] = pm_2017[col].map(lambda x: str(x).lstrip('*').rstrip('*')).astype(int)

pm_2017.to_csv('c:/data/final/pol_2017.csv', encoding='cp949', index=False)
pm_2017

pm_2018 = pd.read_csv('c:/data/final/pol_2018.csv', encoding='cp949')
pm_2018 = pm_2018.fillna(0)

cols = ['1월', '2월', '3월','4월', '5월', '6월', '7월', '8월', '9월', '10월', '11월', '12월', '연평균']
for col in cols:
       pm_2018[col] = pm_2018[col].map(lambda x: str(x).lstrip('*').rstrip('*')).astype(int)

pm_2018.to_csv('c:/data/final/pol_2018.csv', encoding='cp949', index=False)
pm_2018

pm_2019_1 = pd.read_csv('c:/data/final/pol_2019_1.csv', encoding='cp949')
pm_2019_1 = pm_2019_1.drop(pm_2019_1.index[0])
pm_2019_1 = pm_2019_1.fillna(0)

cols = ['PM2.5']
for col in cols:
       pm_2019_1[col] = pm_2019_1[col].map(lambda x: str(x).lstrip('*').rstrip('*')).astype(int)

pm_2019_1['연평균'] = pm_2019_1['PM2.5'].astype('int')
pm_2019_1 = pm_2019_1.drop('PM2.5', axis=1)
pm_2019_1.to_csv('c:/data/final/pol_2019_1.csv', encoding='cp949', index=False)
pm_2019_1


pm_2019_2 = pd.read_csv('c:/data/final/pol_2019_2.csv', encoding='cp949')
pm_2019_2.info()
pm_2019_2 = pm_2019_2.drop(pm_2019_2.columns[[2, 3, 4, 5, 6, 7, 8, 9]], axis=1)
pm_2019_2 = pm_2019_2.drop(pm_2019_2.index[147:])

cols = ['월평균']
for col in cols:
       pm_2019_2[col] = pm_2019_2[col].map(lambda x: str(x).lstrip('*').rstrip('*')).astype(int)

pm_2019_2
pm_2019_2 = pm_2019_2[pm_2019_2.도시 != '도평균']
pm_2019_2.to_csv('c:/data/final/pol_2019_2.csv', encoding='cp949', index=False)
pm_2019_2

pm_2019_3 = pd.read_csv('c:/data/final/pol_2019_3.csv', encoding='cp949')
pm_2019_3.info()
pm_2019_3 = pm_2019_3.drop(pm_2019_3.columns[[2, 3, 4, 5, 6, 7, 8, 9]], axis=1)
pm_2019_3 = pm_2019_3[pm_2019_3.도시 != '도평균']
pm_2019_3 = pm_2019_3.dropna()
pm_2019_3
pm_2019_3['월평균'] = pm_2019_3['월평균'].astype('int')
pm_2019_3.to_csv('c:/data/final/pol_2019_3.csv', encoding='cp949', index=False)
pm_2019_3

pm_2019_4 = pd.read_csv('c:/data/final/pol_2019_4.csv', encoding='cp949')
pm_2019_4.info()
pm_2019_4 = pm_2019_4.drop(pm_2019_4.columns[[2, 3, 4, 5, 6, 7, 8, 9]], axis=1)
pm_2019_4 = pm_2019_4[pm_2019_4.도시 != '도평균']
pm_2019_4 = pm_2019_4.dropna()
pm_2019_4
pm_2019_4.to_csv('c:/data/final/pol_2019_4.csv', encoding='cp949', index=False)
pm_2019_4

pm_2019_5 = pd.read_csv('c:/data/final/pol_2019_5.csv', encoding='cp949')
pm_2019_5.info()
pm_2019_5 = pm_2019_5.drop(pm_2019_5.columns[[2, 3, 4, 5, 6, 7, 8, 9]], axis=1)
pm_2019_5 = pm_2019_5[pm_2019_5.도시 != '도평균']
pm_2019_5 = pm_2019_5.dropna()
pm_2019_5
pm_2019_5.to_csv('c:/data/final/pol_2019_5.csv', encoding='cp949', index=False)
pm_2019_5

pm_2019_6 = pd.read_csv('c:/data/final/pol_2019_6.csv', encoding='cp949')
pm_2019_6.info()
pm_2019_6 = pm_2019_6.drop(pm_2019_6.columns[[2, 3, 4, 5, 6, 7, 8, 9]], axis=1)
pm_2019_6 = pm_2019_6[pm_2019_6.도시 != '도평균']
pm_2019_6 = pm_2019_6.dropna()
pm_2019_6
cols = ['월평균']
for col in cols:
       pm_2019_6[col] = pm_2019_6[col].map(lambda x: str(x).lstrip('*').rstrip('*')).astype(int)
pm_2019_6.to_csv('c:/data/final/pol_2019_6.csv', encoding='cp949', index=False)
pm_2019_6

pm_2019_7 = pd.read_csv('c:/data/final/pol_2019_7.csv', encoding='cp949')
pm_2019_7.info()
pm_2019_7 = pm_2019_7.drop(pm_2019_7.columns[[2, 3, 4, 5, 6, 7, 8, 9]], axis=1)
pm_2019_7 = pm_2019_7[pm_2019_7.도시 != '도평균']
pm_2019_7 = pm_2019_7.dropna()
pm_2019_7
cols = ['월평균']
for col in cols:
       pm_2019_7[col] = pm_2019_7[col].map(lambda x: str(x).lstrip('*').rstrip('*')).astype(int)
pm_2019_7.to_csv('c:/data/final/pol_2019_7.csv', encoding='cp949', index=False)
pm_2019_7

pm_2019_8 = pd.read_csv('c:/data/final/pol_2019_8.csv', encoding='cp949')
pm_2019_8.info()
pm_2019_8 = pm_2019_8.drop(pm_2019_8.columns[[2, 3, 4, 5, 6, 7, 8, 9]], axis=1)
pm_2019_8 = pm_2019_8[pm_2019_8.도시 != '도평균']
pm_2019_8 = pm_2019_8.dropna()
pm_2019_8
cols = ['월평균']
for col in cols:
       pm_2019_8[col] = pm_2019_8[col].map(lambda x: str(x).lstrip('*').rstrip('*')).astype(int)
pm_2019_8.to_csv('c:/data/final/pol_2019_8.csv', encoding='cp949', index=False)
pm_2019_8

pm_2019_9 = pd.read_csv('c:/data/final/pol_2019_9.csv', encoding='cp949')
pm_2019_9.info()
pm_2019_9 = pm_2019_9.drop(pm_2019_9.columns[[2, 3, 4, 5, 6, 7, 8, 9]], axis=1)
pm_2019_9 = pm_2019_9[pm_2019_9.도시 != '도평균']
pm_2019_9 = pm_2019_9.dropna()
pm_2019_9
cols = ['월평균']
for col in cols:
       pm_2019_9[col] = pm_2019_9[col].map(lambda x: str(x).lstrip('*').rstrip('*')).astype(int)
cols = ['월평균']
for col in cols:
       pm_2019_9[col] = pm_2019_9[col].map(lambda x: str(x).lstrip('#').rstrip('#')).astype(int)
pm_2019_9.to_csv('c:/data/final/pol_2019_9.csv', encoding='cp949', index=False)
pm_2019_9

pm_2019_10 = pd.read_csv('c:/data/final/pol_2019_10.csv', encoding='cp949')
pm_2019_10.info()
pm_2019_10 = pm_2019_10.drop(pm_2019_10.columns[[2, 3, 4, 5, 6, 7, 8, 9]], axis=1)
pm_2019_10 = pm_2019_10[pm_2019_10.도시 != '도평균']
pm_2019_10 = pm_2019_10.dropna()
pm_2019_10
cols = ['월평균']
for col in cols:
       pm_2019_10[col] = pm_2019_10[col].map(lambda x: str(x).lstrip('*').rstrip('*')).astype(int)
pm_2019_10.to_csv('c:/data/final/pol_2019_10.csv', encoding='cp949', index=False)
pm_2019_10

pm_2019_11 = pd.read_csv('c:/data/final/pol_2019_11.csv', encoding='cp949')
pm_2019_11.info()
pm_2019_11 = pm_2019_11.drop(pm_2019_11.columns[[2, 3, 4, 5, 6, 7, 8, 9]], axis=1)
pm_2019_11 = pm_2019_11[pm_2019_11.도시 != '도평균']
pm_2019_11 = pm_2019_11.dropna()
pm_2019_11
cols = ['월평균']
for col in cols:
       pm_2019_11[col] = pm_2019_11[col].map(lambda x: str(x).lstrip('*').rstrip('*')).astype(int)
pm_2019_11.to_csv('c:/data/final/pol_2019_11.csv', encoding='cp949', index=False)
pm_2019_11

pm_2019_12 = pd.read_csv('c:/data/final/pol_2019_12.csv', encoding='cp949')
pm_2019_12.info()
pm_2019_12 = pm_2019_12.drop(pm_2019_12.columns[[2, 3, 4, 5, 6, 7, 8, 9]], axis=1)
pm_2019_12 = pm_2019_12[pm_2019_12.도시 != '도평균']
pm_2019_12 = pm_2019_12.dropna()
pm_2019_12
cols = ['월평균']
for col in cols:
       pm_2019_12[col] = pm_2019_12[col].map(lambda x: str(x).lstrip('*').rstrip('*')).astype(int)
pm_2019_12.to_csv('c:/data/final/pol_2019_12.csv', encoding='cp949', index=False)
pm_2019_12

pm_2019 = pd.concat([pm_2019, pm_2019_3], axis=1)
pm_2019 = pd.concat([pm_2019, pm_2019_4], axis=1)
pm_2019 = pd.concat([pm_2019, pm_2019_5], axis=1)
pm_2019 = pd.concat([pm_2019, pm_2019_6], axis=1)
pm_2019 = pd.concat([pm_2019, pm_2019_7], axis=1)
pm_2019 = pd.concat([pm_2019, pm_2019_8], axis=1)
pm_2019 = pd.concat([pm_2019, pm_2019_9], axis=1)
pm_2019 = pd.concat([pm_2019, pm_2019_10], axis=1)
pm_2019 = pd.concat([pm_2019, pm_2019_11], axis=1)
pm_2019 = pd.concat([pm_2019, pm_2019_12], axis=1)



pm_2019.to_csv('c:/data/final/pm_2019.csv', encoding='cp949', index=False)
pm_2019 = pd.read_csv('c:/data/final/pm_2019.csv', encoding='cp949')
pm_2019.info()

pm_2019 = pm_2019.drop(pm_2019.columns[[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22]], axis=1)

pm_2019['연평균'] = pm_2019.mean(axis=1)
pm_2019['연평균'] = pm_2019['연평균'].astype('int')
pm_2019_2.reset_index(drop=True, inplace=True)

pm_2019.columns = [['도시', '1월', '2월', '3월', '4월', '5월', '6월', '7월', '8월', '9월', '10월', '11월', '12월', '연평균']]

pm_2016.info()



pm_2020_1 = pd.read_csv('c:/data/final/pol_2020_1.csv', encoding='cp949')
pm_2020_1.info()
pm_2020_1 = pm_2020_1.drop(pm_2020_1.columns[[2, 3, 4, 5, 6, 7, 8, 9]], axis=1)
pm_2020_1 = pm_2020_1[pm_2020_1.도시 != '도평균']
pm_2020_1 = pm_2020_1.dropna()
pm_2020_1
cols = ['월평균']
for col in cols:
       pm_2020_1[col] = pm_2020_1[col].map(lambda x: str(x).lstrip('*').rstrip('*')).astype(int)
pm_2020_1.to_csv('c:/data/final/pol_2020_1.csv', encoding='cp949', index=False)
pm_2020_1


pm_2020_2 = pd.read_csv('c:/data/final/pol_2020_2.csv', encoding='cp949')
pm_2020_2.info()
pm_2020_2 = pm_2020_2.drop(pm_2020_2.columns[[2, 3, 4, 5, 6, 7, 8, 9]], axis=1)
pm_2020_2 = pm_2020_2[pm_2020_2.도시 != '도평균']
pm_2020_2 = pm_2020_2.dropna()
pm_2020_2
cols = ['월평균']
for col in cols:
       pm_2020_2[col] = pm_2020_2[col].map(lambda x: str(x).lstrip('*').rstrip('*')).astype(int)
pm_2020_2.to_csv('c:/data/final/pol_2020_2.csv', encoding='cp949', index=False)
pm_2020_2


pm_2020 = pd.concat([pm_2020_1, pm_2020_2], axis=1)
pm_2020
pm_2020 = pm_2020.drop('도시', axis=1)
pm_2020.columns = ['도시', '1월', '도시1', '2월']
pm_2020 = pm_2020.drop('도시1', axis=1)
pm_2020.to_csv('c:/data/final/pol_2020.csv', encoding='cp949', index=False)
pm_2020


pm2_5 = []
for i in range(1, 13, 1):
    pm2_5.append(pm_2016['{}월'.format(i)].mean())
x = pd.DataFrame(pm2_5)

pm3_5 = []
for i in range(1, 13, 1):
    pm3_5.append(pm_2017['{}월'.format(i)].mean())
y = pd.DataFrame(pm3_5)

pm4_5 = []
for i in range(1, 13, 1):
    pm4_5.append(pm_2018['{}월'.format(i)].mean())
z = pd.DataFrame(pm4_5)

pm5_5 = []
for i in range(1, 13, 1):
    pm5_5.append(pm_2019['{}월'.format(i)].mean())
w = pd.DataFrame(pm5_5)

pm6_5 = []
for i in range(1, 3, 1):
    pm6_5.append(pm_2020['{}월'.format(i)].mean())
s = pd.DataFrame(pm6_5)


acne_df2['pm2.5'] = xz

xz = pd.concat([x, y, z, w, s], axis=0)
xz.reset_index(drop=True, inplace=True)
xz = xz.astype('int')

acne_df2 = acne_df2[['year', 'man/woman', 'search', 'temp(mean)', 'pm2.5', 'target1']]

acne_df2.columns = ['month', 'patient', 'trand', 'temp', 'pm2.5', 'target']
acne_df2.to_csv('c:/data/final/acne_df2.csv', encoding='cp949', index=False)


# month : 년 월, patient : 환자 수 , trand : 트렌드 검색 비율, temp : 평균기온, pm2.5 : 평균 미세먼지 지수
# target : 0 : 2016, 1 : 2017, 2 : 2018, 3 : 2019, 4 : 2020
acne_df2 = pd.read_csv('c:/data/final/acne_df2.csv', encoding='cp949')
acne_df2

#====================================================================================================

age = pd.read_csv('c:/data/final/age2016.csv', encoding='utf-8')
age

age.dropna(how='all', axis=1, inplace=True)
age.drop(age.index[[0, 7, 14]], axis=0, inplace=True)
age.replace('-', 0, inplace=True)
age.iloc[:,2:] = age.iloc[:,2:].astype('int')
age['total'] = age.iloc[:,2:].sum(axis=1).astype('int')
age
age

age2016 = pd.DataFrame(columns=('10대이전', '10대', '20대', '30대', '40대', '50대'))
age2016['10대이전']= age.loc[[1, 8]].sum(axis=0)
age2016['10대']= age.loc[[2, 9]].sum(axis=0)
age2016['20대']= age.loc[[3, 10]].sum(axis=0)
age2016['30대']= age.loc[[4, 11]].sum(axis=0)
age2016['40대']= age.loc[[5, 12]].sum(axis=0)
age2016['50대']= age.loc[[6, 13]].sum(axis=0)
age2016.drop(age2016.index[[0, 1]], axis=0, inplace=True)
age2016.fillna(0, inplace=True)
age2016.info()

agel70_2020 = pd.read_csv('c:/data/final/agel70_2020.csv', encoding='utf-8')
agel70_2020.dropna(how='all', axis=1, inplace=True)
agel70_2020.drop(agel70_2020.index[[0, 1, 7]], axis=0, inplace=True)
agel70_2020.replace('-', 0, inplace=True)
agel70_2020.iloc[:,2:] = agel70_2020.iloc[:,2:].astype('int')
agel70_2020['total'] = agel70_2020.iloc[:,2:].sum(axis=1).astype('int')
agel70_2020

agel70_2020.reset_index(drop=True, inplace=True)
agel70_2020

age2020_l70 = pd.DataFrame(columns=('10대이전', '10대', '20대', '30대', '40대', '50대'))
age2020_l70['10대']= agel70_2020.loc[[0, 5]].sum(axis=0)
age2020_l70['20대']= agel70_2020.loc[[1, 6]].sum(axis=0)
age2020_l70['30대']= agel70_2020.loc[[2, 7]].sum(axis=0)
age2020_l70['40대']= agel70_2020.loc[[3, 8]].sum(axis=0)
age2020_l70['50대']= agel70_2020.loc[[4, 9]].sum(axis=0)
age2020_l70.drop(age2020_l70.index[[0, 1]], axis=0, inplace=True)
age2020_l70.fillna(0, inplace=True)
type(age2020_l70)

agel70 = pd.concat([age2016, age2020_l70], axis=0)
agel70.drop(['total'], inplace=True)
agel70.reset_index(drop=True, inplace=True)
agel70

#==============================================================================================================

agel700_2016 = pd.read_csv('c:/data/final/agel700_2016.csv', encoding='utf-8')
agel700_2016.dropna(how='all', axis=1, inplace=True)
agel700_2016.drop(agel700_2016.index[[0, 1, 8, 9, 10, 11, 18, 19, 20]], axis=0, inplace=True)
agel700_2016.replace('-', 0, inplace=True)
agel700_2016.iloc[:,2:] = agel700_2016.iloc[:,2:].astype('int')
agel700_2016['total'] = agel700_2016.iloc[:,2:].sum(axis=1).astype('int')

agel700_2016.reset_index(drop=True, inplace=True)
agel700_2016

age2016_l700 = pd.DataFrame(columns=('10대이전', '10대', '20대', '30대', '40대', '50대'))
age2016_l700['10대이전']= agel700_2016.loc[[0, 6]].sum(axis=0)
age2016_l700['10대']= agel700_2016.loc[[1, 7]].sum(axis=0)
age2016_l700['20대']= agel700_2016.loc[[2, 8]].sum(axis=0)
age2016_l700['30대']= agel700_2016.loc[[3, 9]].sum(axis=0)
age2016_l700['40대']= agel700_2016.loc[[4, 10]].sum(axis=0)
age2016_l700['50대']= agel700_2016.loc[[5, 11]].sum(axis=0)
age2016_l700.drop(age2016_l700.index[[0, 1]], axis=0, inplace=True)
age2016_l700

agel700_2020 = pd.read_csv('c:/data/final/age2020_l700.csv', encoding='utf-8')
agel700_2020
agel700_2020.dropna(how='all', axis=1, inplace=True)
agel700_2020.drop(agel700_2020.index[[0, 1, 8, 9, 10, 11, 18, 19, 20]], axis=0, inplace=True)
agel700_2020.replace('-', 0, inplace=True)
agel700_2020.iloc[:,2:] = agel700_2020.iloc[:,2:].astype('int')
agel700_2020.reset_index(drop=True, inplace=True)
agel700_2020

age2020_l700 = pd.DataFrame(columns=('10대이전', '10대', '20대', '30대', '40대', '50대'))
age2020_l700['10대이전']= agel700_2020.loc[[0, 6]].sum(axis=0)
age2020_l700['10대']= agel700_2020.loc[[1, 7]].sum(axis=0)
age2020_l700['20대']= agel700_2020.loc[[2, 8]].sum(axis=0)
age2020_l700['30대']= agel700_2020.loc[[3, 9]].sum(axis=0)
age2020_l700['40대']= agel700_2020.loc[[4, 10]].sum(axis=0)
age2020_l700['50대']= agel700_2020.loc[[5, 11]].sum(axis=0)
age2020_l700.drop(age2020_l700.index[[0, 1]], axis=0, inplace=True)
age2020_l700

agel700 = pd.concat([age2016_l700, age2020_l700], axis=0)
agel700.drop(['total'], inplace=True)
agel700.reset_index(drop=True, inplace=True)

#============================================================================================================

agel701_2016 = pd.read_csv('c:/data/final/agel701_2016.csv', encoding='utf-8')
agel701_2016
agel701_2016.drop(agel701_2016.index[[0, 1, 8, 9, 10, 11, 18, 19, 20]], axis=0, inplace=True)
agel701_2016.replace('-', 0, inplace=True)
agel701_2016['환자수'] = agel701_2016['환자수'].str.replace(pat=r'[^0-9]', repl= r'', regex=True)
agel701_2016['환자수.1'] = agel701_2016['환자수.1'].str.replace(pat=r'[^0-9]', repl= r'', regex=True)
agel701_2016['환자수.2'] = agel701_2016['환자수.2'].str.replace(pat=r'[^0-9]', repl= r'', regex=True)
agel701_2016['환자수.3'] = agel701_2016['환자수.3'].str.replace(pat=r'[^0-9]', repl= r'', regex=True)
agel701_2016['환자수.4'] = agel701_2016['환자수.4'].str.replace(pat=r'[^0-9]', repl= r'', regex=True)
agel701_2016['환자수.5'] = agel701_2016['환자수.5'].str.replace(pat=r'[^0-9]', repl= r'', regex=True)
agel701_2016['환자수.6'] = agel701_2016['환자수.6'].str.replace(pat=r'[^0-9]', repl= r'', regex=True)
agel701_2016['환자수.7'] = agel701_2016['환자수.7'].str.replace(pat=r'[^0-9]', repl= r'', regex=True)
agel701_2016['환자수.8'] = agel701_2016['환자수.8'].str.replace(pat=r'[^0-9]', repl= r'', regex=True)
agel701_2016['환자수.9'] = agel701_2016['환자수.9'].str.replace(pat=r'[^0-9]', repl= r'', regex=True)
agel701_2016['환자수.10'] = agel701_2016['환자수.10'].str.replace(pat=r'[^0-9]', repl= r'', regex=True)
agel701_2016['환자수.11'] = agel701_2016['환자수.11'].str.replace(pat=r'[^0-9]', repl= r'', regex=True)
agel701_2016['환자수.12'] = agel701_2016['환자수.12'].str.replace(pat=r'[^0-9]', repl= r'', regex=True)
agel701_2016['환자수.13'] = agel701_2016['환자수.13'].str.replace(pat=r'[^0-9]', repl= r'', regex=True)
agel701_2016['환자수.14'] = agel701_2016['환자수.14'].str.replace(pat=r'[^0-9]', repl= r'', regex=True)
agel701_2016['환자수.15'] = agel701_2016['환자수.15'].str.replace(pat=r'[^0-9]', repl= r'', regex=True)
agel701_2016['환자수.16'] = agel701_2016['환자수.16'].str.replace(pat=r'[^0-9]', repl= r'', regex=True)
agel701_2016['환자수.17'] = agel701_2016['환자수.17'].str.replace(pat=r'[^0-9]', repl= r'', regex=True)
agel701_2016['환자수.18'] = agel701_2016['환자수.18'].str.replace(pat=r'[^0-9]', repl= r'', regex=True)
agel701_2016['환자수.19'] = agel701_2016['환자수.19'].str.replace(pat=r'[^0-9]', repl= r'', regex=True)
agel701_2016['환자수.20'] = agel701_2016['환자수.20'].str.replace(pat=r'[^0-9]', repl= r'', regex=True)
agel701_2016['환자수.21'] = agel701_2016['환자수.21'].str.replace(pat=r'[^0-9]', repl= r'', regex=True)
agel701_2016['환자수.22'] = agel701_2016['환자수.22'].str.replace(pat=r'[^0-9]', repl= r'', regex=True)
agel701_2016['환자수.23'] = agel701_2016['환자수.23'].str.replace(pat=r'[^0-9]', repl= r'', regex=True)
agel701_2016['환자수.24'] = agel701_2016['환자수.24'].str.replace(pat=r'[^0-9]', repl= r'', regex=True)
agel701_2016['환자수.25'] = agel701_2016['환자수.25'].str.replace(pat=r'[^0-9]', repl= r'', regex=True)
agel701_2016['환자수.26'] = agel701_2016['환자수.26'].str.replace(pat=r'[^0-9]', repl= r'', regex=True)
agel701_2016['환자수.27'] = agel701_2016['환자수.27'].str.replace(pat=r'[^0-9]', repl= r'', regex=True)
agel701_2016['환자수.28'] = agel701_2016['환자수.28'].str.replace(pat=r'[^0-9]', repl= r'', regex=True)
agel701_2016['환자수.29'] = agel701_2016['환자수.29'].str.replace(pat=r'[^0-9]', repl= r'', regex=True)
agel701_2016['환자수.30'] = agel701_2016['환자수.30'].str.replace(pat=r'[^0-9]', repl= r'', regex=True)
agel701_2016['환자수.31'] = agel701_2016['환자수.31'].str.replace(pat=r'[^0-9]', repl= r'', regex=True)
agel701_2016['환자수.32'] = agel701_2016['환자수.32'].str.replace(pat=r'[^0-9]', repl= r'', regex=True)
agel701_2016['환자수.33'] = agel701_2016['환자수.33'].str.replace(pat=r'[^0-9]', repl= r'', regex=True)
agel701_2016['환자수.34'] = agel701_2016['환자수.34'].str.replace(pat=r'[^0-9]', repl= r'', regex=True)
agel701_2016['환자수.35'] = agel701_2016['환자수.35'].str.replace(pat=r'[^0-9]', repl= r'', regex=True)

agel701_2016

agel701_2016.iloc[:,2:] = agel701_2016.iloc[:,2:].astype('int')
agel701_2016
agel701_2016.reset_index(drop=True, inplace=True)
agel701_2016.fillna(0, inplace=True)

age2016_l701 = pd.DataFrame(columns=('10대이전', '10대', '20대', '30대', '40대', '50대'))
age2016_l701['10대이전']= agel701_2016.loc[[0, 6]].sum(axis=0)
age2016_l701['10대']= agel701_2016.loc[[1, 7]].sum(axis=0)
age2016_l701['20대']= agel701_2016.loc[[2, 8]].sum(axis=0)
age2016_l701['30대']= agel701_2016.loc[[3, 9]].sum(axis=0)
age2016_l701['40대']= agel701_2016.loc[[4, 10]].sum(axis=0)
age2016_l701['50대']= agel701_2016.loc[[5, 11]].sum(axis=0)
age2016_l701.drop(age2016_l701.index[[0, 1]], axis=0, inplace=True)

age2016_l701


age2020_l701 = pd.read_csv('c:/data/final/age2020_l701.csv', encoding='utf-8')
age2020_l701
age2020_l701.drop(age2020_l701.index[[0, 1, 8, 9, 10, 11, 18, 19, 20]], axis=0, inplace=True)
age2020_l701.replace('-', 0, inplace=True)
age2020_l701['환자수'] = age2020_l701['환자수'].str.replace(pat=r'[^0-9]', repl= r'', regex=True)
age2020_l701['환자수.1'] = age2020_l701['환자수.1'].str.replace(pat=r'[^0-9]', repl= r'', regex=True)
age2020_l701['환자수.2'] = age2020_l701['환자수.2'].str.replace(pat=r'[^0-9]', repl= r'', regex=True)
age2020_l701['환자수.3'] = age2020_l701['환자수.3'].str.replace(pat=r'[^0-9]', repl= r'', regex=True)
age2020_l701['환자수.4'] = age2020_l701['환자수.4'].str.replace(pat=r'[^0-9]', repl= r'', regex=True)
age2020_l701['환자수.5'] = age2020_l701['환자수.5'].str.replace(pat=r'[^0-9]', repl= r'', regex=True)
age2020_l701['환자수.6'] = age2020_l701['환자수.6'].str.replace(pat=r'[^0-9]', repl= r'', regex=True)
age2020_l701['환자수.7'] = age2020_l701['환자수.7'].str.replace(pat=r'[^0-9]', repl= r'', regex=True)
age2020_l701['환자수.8'] = age2020_l701['환자수.8'].str.replace(pat=r'[^0-9]', repl= r'', regex=True)
age2020_l701['환자수.9'] = age2020_l701['환자수.9'].str.replace(pat=r'[^0-9]', repl= r'', regex=True)
age2020_l701['환자수.10'] = age2020_l701['환자수.10'].str.replace(pat=r'[^0-9]', repl= r'', regex=True)
age2020_l701['환자수.11'] = age2020_l701['환자수.11'].str.replace(pat=r'[^0-9]', repl= r'', regex=True)
age2020_l701['환자수.12'] = age2020_l701['환자수.12'].str.replace(pat=r'[^0-9]', repl= r'', regex=True)
age2020_l701['환자수.13'] = age2020_l701['환자수.13'].str.replace(pat=r'[^0-9]', repl= r'', regex=True)

age2020_l701.iloc[:,2:] = age2020_l701.iloc[:,2:].astype('int')
age2020_l701
age2020_l701.reset_index(drop=True, inplace=True)
age2020_l701.fillna(0, inplace=True)

agel701_2020 = pd.DataFrame(columns=('10대이전', '10대', '20대', '30대', '40대', '50대'))
agel701_2020['10대이전']= age2020_l701.loc[[0, 6]].sum(axis=0)
agel701_2020['10대']= age2020_l701.loc[[1, 7]].sum(axis=0)
agel701_2020['20대']= age2020_l701.loc[[2, 8]].sum(axis=0)
agel701_2020['30대']= age2020_l701.loc[[3, 9]].sum(axis=0)
agel701_2020['40대']= age2020_l701.loc[[4, 10]].sum(axis=0)
agel701_2020['50대']= age2020_l701.loc[[5, 11]].sum(axis=0)
agel701_2020.drop(agel701_2020.index[[0, 1]], axis=0, inplace=True)

agel701_2020

agel701 = pd.concat([age2016_l701, agel701_2020], axis=0)
agel701
agel701.drop(['total'], inplace=True)
agel701.reset_index(drop=True, inplace=True)


#===================================================================================================================
agel702_2016 = pd.read_csv('c:/data/final/agel702_2016.csv', encoding='utf-8')
agel702_2016
agel702_2016.dropna(how='all', axis=1, inplace=True)
agel702_2016.drop(agel702_2016.index[[0, 1, 8, 9, 10, 11, 18, 19, 20]], axis=0, inplace=True)
agel702_2016.replace('-', 0, inplace=True)
agel702_2016.iloc[:,2:] = agel702_2016.iloc[:,2:].astype('int')
agel702_2016
agel702_2016['total'] = agel702_2016.iloc[:,2:].sum(axis=1).astype('int')
agel702_2016.reset_index(drop=True, inplace=True)
agel702_2016

age2016_l702 = pd.DataFrame(columns=('10대이전', '10대', '20대', '30대', '40대', '50대'))
age2016_l702['10대이전']= agel702_2016.loc[[0, 6]].sum(axis=0)
age2016_l702['10대']= agel702_2016.loc[[1, 7]].sum(axis=0)
age2016_l702['20대']= agel702_2016.loc[[2, 8]].sum(axis=0)
age2016_l702['30대']= agel702_2016.loc[[3, 9]].sum(axis=0)
age2016_l702['40대']= agel702_2016.loc[[4, 10]].sum(axis=0)
age2016_l702['50대']= agel702_2016.loc[[5, 11]].sum(axis=0)
age2016_l702.drop(age2016_l702.index[[0, 1]], axis=0, inplace=True)
age2016_l702


age2020_l702 = pd.read_csv('c:/data/final/age2020_l702.csv', encoding='utf-8')
age2020_l702.dropna(how='all', axis=1, inplace=True)
age2020_l702.drop(age2020_l702.index[[0, 1, 8, 9, 10, 11, 18, 19, 20]], axis=0, inplace=True)
age2020_l702.replace('-', 0, inplace=True)
age2020_l702.iloc[:,2:] = age2020_l702.iloc[:,2:].astype('int')
age2020_l702.reset_index(drop=True, inplace=True)
age2020_l702

age_l702_2020 = pd.DataFrame(columns=('10대이전', '10대', '20대', '30대', '40대', '50대'))
age_l702_2020['10대이전']= age2020_l702.loc[[0, 6]].sum(axis=0)
age_l702_2020['10대']= age2020_l702.loc[[1, 7]].sum(axis=0)
age_l702_2020['20대']= age2020_l702.loc[[2, 8]].sum(axis=0)
age_l702_2020['30대']= age2020_l702.loc[[3, 9]].sum(axis=0)
age_l702_2020['40대']= age2020_l702.loc[[4, 10]].sum(axis=0)
age_l702_2020['50대']= age2020_l702.loc[[5, 11]].sum(axis=0)
age_l702_2020.drop(age_l702_2020.index[[0, 1]], axis=0, inplace=True)
age_l702_2020

agel702 = pd.concat([age2016_l702, age_l702_2020], axis=0)
agel702.drop(['total'], inplace=True)
agel702.reset_index(drop=True, inplace=True)

#=======================================================================================================================

agel703_2016 = pd.read_csv('c:/data/final/agel703_2016.csv', encoding='utf-8')
agel703_2016
agel703_2016.dropna(how='all', axis=1, inplace=True)
agel703_2016.drop(agel703_2016.index[[0, 1, 8, 15, 16]], axis=0, inplace=True)
agel703_2016.replace('-', 0, inplace=True)
agel703_2016.iloc[:,2:] = agel703_2016.iloc[:,2:].astype('int')
agel703_2016
agel703_2016.reset_index(drop=True, inplace=True)
agel703_2016

age2016_l703 = pd.DataFrame(columns=('10대이전', '10대', '20대', '30대', '40대', '50대'))
age2016_l703['10대이전']= agel703_2016.loc[[0, 6]].sum(axis=0)
age2016_l703['10대']= agel703_2016.loc[[1, 7]].sum(axis=0)
age2016_l703['20대']= agel703_2016.loc[[2, 8]].sum(axis=0)
age2016_l703['30대']= agel703_2016.loc[[3, 9]].sum(axis=0)
age2016_l703['40대']= agel703_2016.loc[[4, 10]].sum(axis=0)
age2016_l703['50대']= agel703_2016.loc[[5, 11]].sum(axis=0)
age2016_l703.drop(age2016_l703.index[[0, 1]], axis=0, inplace=True)
age2016_l703


age2020_l703 = pd.read_csv('c:/data/final/age2020_l703.csv', encoding='utf-8')
age2020_l703.dropna(how='all', axis=1, inplace=True)
age2020_l703.replace('-', 0, inplace=True)
age2020_l703.iloc[:,2:] = age2020_l703.iloc[:,2:].astype('int')
age2020_l703.reset_index(drop=True, inplace=True)
age2020_l703
agel703_2020 = pd.DataFrame(columns=('10대이전', '10대', '20대', '30대', '40대', '50대'))
agel703_2020['10대이전']= age2020_l703.loc[[2, 6]].sum(axis=0)
agel703_2020['10대']= age2020_l703.loc[[3, 7]].sum(axis=0)
agel703_2020['20대']= age2020_l703.loc[[4, 8]].sum(axis=0)
agel703_2020['30대']= age2020_l703.loc[[5, 9]].sum(axis=0)
agel703_2020['40대']= age2020_l703.loc[[1, 10]].sum(axis=0)
agel703_2020['50대']= age2020_l703.loc[0]
agel703_2020.drop(agel703_2020.index[[0, 1]], axis=0, inplace=True)
agel703_2020


agel703 = pd.concat([age2016_l703, agel703_2020], axis=0)
agel703
agel703.reset_index(drop=True, inplace=True)

#=============================================================================================================

agel704_2016 = pd.read_csv('c:/data/final/agel704_2016.csv', encoding='utf-8')
agel704_2016
agel704_2016.dropna(how='all', axis=1, inplace=True)
agel704_2016.drop(agel704_2016.index[[0, 1, 7]], axis=0, inplace=True)
agel704_2016.replace('-', 0, inplace=True)
agel704_2016.iloc[:,2:] = agel704_2016.iloc[:,2:].astype('int')
agel704_2016
agel704_2016['total'] = agel704_2016.iloc[:,2:].sum(axis=1).astype('int')
agel704_2016.reset_index(drop=True, inplace=True)
agel704_2016

age2016_l704 = pd.DataFrame(columns=('10대이전', '10대', '20대', '30대', '40대', '50대'))
age2016_l704['10대이전']= agel704_2016.loc[[0, 5]].sum(axis=0)
age2016_l704['10대']= agel704_2016.loc[[1, 6]].sum(axis=0)
age2016_l704['20대']= agel704_2016.loc[[2, 7]].sum(axis=0)
age2016_l704['30대']= agel704_2016.loc[[3, 8]].sum(axis=0)
age2016_l704['40대']= agel704_2016.loc[[4, 9]].sum(axis=0)
age2016_l704['50대']= agel704_2016.loc[[5, 10]].sum(axis=0)
age2016_l704.drop(age2016_l704.index[[0, 1]], axis=0, inplace=True)
age2016_l704

age2020_l704 = pd.read_csv('c:/data/final/age2020_l704.csv', encoding='utf-8')
age2020_l704.dropna(how='all', axis=1, inplace=True)
age2020_l704
age2020_l704.replace('-', 0, inplace=True)
age2020_l704.iloc[:,2:] = age2020_l704.iloc[:,2:].astype('int')
age2020_l704.reset_index(drop=True, inplace=True)
age2020_l704

agel704_2020 = pd.DataFrame(columns=('10대이전', '10대', '20대', '30대', '40대', '50대'))
agel704_2020['10대이전']= age2020_l704.loc[[2, 5]].sum(axis=0)
agel704_2020['10대']= age2020_l704.loc[6]
agel704_2020['20대']= age2020_l704.loc[7]
agel704_2020['30대']= age2020_l704.loc[8]
agel704_2020.drop(agel704_2020.index[[0, 1]], axis=0, inplace=True)
agel704_2020.fillna(0, inplace=True)
agel704_2020

agel704 = pd.concat([age2016_l704, agel704_2020], axis=0)
agel704
agel704.drop(['total'], inplace=True)
agel704.reset_index(drop=True, inplace=True)

#=================================================================================================================


agel705_2016 = pd.read_csv('c:/data/final/agel705_2016.csv', encoding='utf-8')
agel705_2016
agel705_2016.dropna(how='all', axis=1, inplace=True)
agel705_2016.drop(agel705_2016.index[[0, 1, 8, 9, 16]], axis=0, inplace=True)
agel705_2016.replace('-', 0, inplace=True)
agel705_2016.iloc[:,2:] = agel705_2016.iloc[:,2:].astype('int')
agel705_2016
agel705_2016['total'] = agel705_2016.iloc[:,2:].sum(axis=1).astype('int')
agel705_2016.reset_index(drop=True, inplace=True)
agel705_2016

age2016_l705 = pd.DataFrame(columns=('10대이전', '10대', '20대', '30대', '40대', '50대'))
age2016_l705['10대이전']= agel705_2016.loc[[0, 6]].sum(axis=0)
age2016_l705['10대']= agel705_2016.loc[[1, 7]].sum(axis=0)
age2016_l705['20대']= agel705_2016.loc[[2, 8]].sum(axis=0)
age2016_l705['30대']= agel705_2016.loc[[3, 9]].sum(axis=0)
age2016_l705['40대']= agel705_2016.loc[[4, 10]].sum(axis=0)
age2016_l705['50대']= agel705_2016.loc[[5, 11]].sum(axis=0)
age2016_l705.drop(age2016_l705.index[[0, 1]], axis=0, inplace=True)
age2016_l705


age2020_l705 =  pd.read_csv('c:/data/final/age2020_l705.csv', encoding='utf-8')
age2020_l705.dropna(how='all', axis=1, inplace=True)
age2020_l705.drop(age2020_l705.index[[0, 1, 7, 8, 14]], axis=0, inplace=True)
age2020_l705.replace('-', 0, inplace=True)
age2020_l705.iloc[:,2:] = age2020_l705.iloc[:,2:].astype('int')
age2020_l705.reset_index(drop=True, inplace=True)
age2020_l705

agel705_2020 = pd.DataFrame(columns=('10대이전', '10대', '20대', '30대', '40대', '50대'))
agel705_2020['10대']= age2020_l705.loc[[0, 5]].sum(axis=0)
agel705_2020['20대']= age2020_l705.loc[[1, 6]].sum(axis=0)
agel705_2020['30대']= age2020_l705.loc[[2, 7]].sum(axis=0)
agel705_2020['40대']= age2020_l705.loc[[3, 8]].sum(axis=0)
agel705_2020['50대']= age2020_l705.loc[[4, 9]].sum(axis=0)
agel705_2020.drop(agel705_2020.index[[0, 1]], axis=0, inplace=True)
agel705_2020.fillna(0, inplace=True)
agel705_2020

agel705 = pd.concat([age2016_l705, agel705_2020], axis=0)
agel705
agel705.drop(['total'], inplace=True)
agel705.reset_index(drop=True, inplace=True)


#==============================================================================================================


agel708_2016 = pd.read_csv('c:/data/final/agel708_2016.csv', encoding='utf-8')
agel708_2016
agel708_2016.dropna(how='all', axis=1, inplace=True)
agel708_2016.drop(agel708_2016.index[[0, 1, 8, 9, 10, 11, 18, 19, 20]], axis=0, inplace=True)
agel708_2016.replace('-', 0, inplace=True)
agel708_2016.iloc[:,2:] = agel708_2016.iloc[:,2:].astype('int')
agel708_2016
agel708_2016['total'] = agel708_2016.iloc[:,2:].sum(axis=1).astype('int')
agel708_2016.reset_index(drop=True, inplace=True)
agel708_2016

age2016_l708 = pd.DataFrame(columns=('10대이전', '10대', '20대', '30대', '40대', '50대'))
age2016_l708['10대이전']= agel708_2016.loc[[0, 6]].sum(axis=0)
age2016_l708['10대']= agel708_2016.loc[[1, 7]].sum(axis=0)
age2016_l708['20대']= agel708_2016.loc[[2, 8]].sum(axis=0)
age2016_l708['30대']= agel708_2016.loc[[3, 9]].sum(axis=0)
age2016_l708['40대']= agel708_2016.loc[[4, 10]].sum(axis=0)
age2016_l708['50대']= agel708_2016.loc[[5, 11]].sum(axis=0)
age2016_l708.drop(age2016_l708.index[[0, 1]], axis=0, inplace=True)
age2016_l708


age2020_l708 = pd.read_csv('c:/data/final/age2020_l708.csv', encoding='utf-8')
age2020_l708.dropna(how='all', axis=1, inplace=True)
age2020_l708.drop(age2020_l708.index[[0, 1, 8, 9, 10, 11, 18, 19, 20]], axis=0, inplace=True)
age2020_l708.replace('-', 0, inplace=True)
age2020_l708.iloc[:,2:] = age2020_l708.iloc[:,2:].astype('int')
age2020_l708
age2020_l708.reset_index(drop=True, inplace=True)
age2020_l708

agel708_2020 = pd.DataFrame(columns=('10대이전', '10대', '20대', '30대', '40대', '50대'))
agel708_2020['10대이전']= age2020_l708.loc[[0, 6]].sum(axis=0)
agel708_2020['10대']= age2020_l708.loc[[1, 7]].sum(axis=0)
agel708_2020['20대']= age2020_l708.loc[[2, 8]].sum(axis=0)
agel708_2020['30대']= age2020_l708.loc[[3, 9]].sum(axis=0)
agel708_2020['40대']= age2020_l708.loc[[4, 10]].sum(axis=0)
agel708_2020['50대']= age2020_l708.loc[[5, 11]].sum(axis=0)
agel708_2020.drop(agel708_2020.index[[0, 1]], axis=0, inplace=True)
agel708_2020


agel708 = pd.concat([age2016_l708, agel708_2020], axis=0)
agel708.drop(['total'], inplace=True)
agel708.reset_index(drop=True, inplace=True)




#========================================================================================================

agel709_2016 = pd.read_csv('c:/data/final/agel709_2016.csv', encoding='utf-8')
agel709_2016
agel709_2016.dropna(how='all', axis=1, inplace=True)
agel709_2016.drop(agel709_2016.index[[0, 1, 8, 9, 10, 11, 18, 19, 20]], axis=0, inplace=True)
agel709_2016.replace('-', 0, inplace=True)
agel709_2016.iloc[:,2:] = agel709_2016.iloc[:,2:].astype('int')
agel709_2016
agel709_2016['total'] = agel709_2016.iloc[:,2:].sum(axis=1).astype('int')
agel709_2016.reset_index(drop=True, inplace=True)
agel709_2016

age2016_l709 = pd.DataFrame(columns=('10대이전', '10대', '20대', '30대', '40대', '50대'))
age2016_l709['10대이전']= agel709_2016.loc[[0, 6]].sum(axis=0)
age2016_l709['10대']= agel709_2016.loc[[1, 7]].sum(axis=0)
age2016_l709['20대']= agel709_2016.loc[[2, 8]].sum(axis=0)
age2016_l709['30대']= agel709_2016.loc[[3, 9]].sum(axis=0)
age2016_l709['40대']= agel709_2016.loc[[4, 10]].sum(axis=0)
age2016_l709['50대']= agel709_2016.loc[[5, 11]].sum(axis=0)
age2016_l709.drop(age2016_l709.index[[0, 1]], axis=0, inplace=True)
age2016_l709

age2020_l709 =  pd.read_csv('c:/data/final/age2020_l709.csv', encoding='utf-8')
age2020_l709
age2020_l709.dropna(how='all', axis=1, inplace=True)
age2020_l709.drop(age2020_l709.index[[0, 1, 8, 9, 10, 11, 18, 19, 20]], axis=0, inplace=True)
age2020_l709.replace('-', 0, inplace=True)
age2020_l709.iloc[:,2:] = age2020_l709.iloc[:,2:].astype('int')
age2020_l709
age2020_l709.reset_index(drop=True, inplace=True)
age2020_l709

agel709_2020 = pd.DataFrame(columns=('10대이전', '10대', '20대', '30대', '40대', '50대'))
agel709_2020['10대이전']= age2020_l709.loc[[0, 6]].sum(axis=0)
agel709_2020['10대']= age2020_l709.loc[[1, 7]].sum(axis=0)
agel709_2020['20대']= age2020_l709.loc[[2, 8]].sum(axis=0)
agel709_2020['30대']= age2020_l709.loc[[3, 9]].sum(axis=0)
agel709_2020['40대']= age2020_l709.loc[[4, 10]].sum(axis=0)
agel709_2020['50대']= age2020_l709.loc[[5, 11]].sum(axis=0)
agel709_2020.drop(agel709_2020.index[[0, 1]], axis=0, inplace=True)
agel709_2020

agel709 = pd.concat([age2016_l709, agel709_2020], axis=0)
agel709.drop(['total'], inplace=True)
agel709.reset_index(drop=True, inplace=True)


#========================================================================================================

agel730_2016 = pd.read_csv('c:/data/final/agel730_2016.csv', encoding='utf-8')
agel730_2016
agel730_2016.dropna(how='all', axis=1, inplace=True)
agel730_2016.drop(agel730_2016.index[[0, 1, 8, 9, 10, 11, 18, 19, 20]], axis=0, inplace=True)
agel730_2016.replace('-', 0, inplace=True)
agel730_2016.iloc[:,2:] = agel730_2016.iloc[:,2:].astype('int')
agel730_2016
agel730_2016['total'] = agel730_2016.iloc[:,2:].sum(axis=1).astype('int')
agel730_2016.reset_index(drop=True, inplace=True)
agel730_2016

age2016_l730 = pd.DataFrame(columns=('10대이전', '10대', '20대', '30대', '40대', '50대'))
age2016_l730['10대이전']= agel730_2016.loc[[0, 6]].sum(axis=0)
age2016_l730['10대']= agel730_2016.loc[[1, 7]].sum(axis=0)
age2016_l730['20대']= agel730_2016.loc[[2, 8]].sum(axis=0)
age2016_l730['30대']= agel730_2016.loc[[3, 9]].sum(axis=0)
age2016_l730['40대']= agel730_2016.loc[[4, 10]].sum(axis=0)
age2016_l730['50대']= agel730_2016.loc[[5, 11]].sum(axis=0)
age2016_l730.drop(age2016_l730.index[[0, 1]], axis=0, inplace=True)
age2016_l730


age2020_l730 = pd.read_csv('c:/data/final/age2020_l730.csv', encoding='utf-8')
age2020_l730
age2020_l730.dropna(how='all', axis=1, inplace=True)
age2020_l730.drop(age2020_l730.index[[0, 1, 8, 9, 10, 11, 18, 19, 20]], axis=0, inplace=True)
age2020_l730.replace('-', 0, inplace=True)
age2020_l730.iloc[:,2:] = age2020_l730.iloc[:,2:].astype('int')
age2020_l730
age2020_l730.reset_index(drop=True, inplace=True)
age2020_l730

agel730_2020 = pd.DataFrame(columns=('10대이전', '10대', '20대', '30대', '40대', '50대'))
agel730_2020['10대이전']= age2020_l730.loc[[0, 6]].sum(axis=0)
agel730_2020['10대']= age2020_l730.loc[[1, 7]].sum(axis=0)
agel730_2020['20대']= age2020_l730.loc[[2, 8]].sum(axis=0)
agel730_2020['30대']= age2020_l730.loc[[3, 9]].sum(axis=0)
agel730_2020['40대']= age2020_l730.loc[[4, 10]].sum(axis=0)
agel730_2020['50대']= age2020_l730.loc[[5, 11]].sum(axis=0)
agel730_2020.drop(agel730_2020.index[[0, 1]], axis=0, inplace=True)
agel730_2020


agel730 = pd.concat([age2016_l730, agel730_2020], axis=0)
agel730.drop(['total'], inplace=True)
agel730.reset_index(drop=True, inplace=True)









client_id = "C2QUU8idCr59BHXMN1qx"
client_secret = "s62CxCE2rP"

q = urllib.parse.quote('여드름')
idx = 0
display = 100
start = 1
end = 1000
sort = 'sim'

in_df = pd.DataFrame(columns=('title', 'description'))

for i in range(start, end, display):
    url = "https://openapi.naver.com/v1/search/kin?query=" + q \
        + '&display=' + str(display) \
        + '&start=' + str(i) \
        + '&sort=' + sort

request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200): # 정상적으로 코드를 받으면 200 표시
    response_body = response.read()
    response_dict = json.loads(response_body.decode('utf-8'))
    items = response_dict['items']
    for i_index in range(0, len(items)):
        remove_tag = re.compile('[^가-힣 ]')
        title = re.sub(remove_tag, '', items[i_index]['title'])
        description = re.sub(remove_tag, '', items[i_index]['description'])
        in_df.loc[idx] = [title, description]
        idx += 1
else:
    print("Error Code:" + rescode)

jisik = pd.DataFrame(columns = ['description'])
jisik['description'] = in_df['description']

jisik.to_csv('c:/data/final/jisik.csv', encoding='cp949', index=False)
jisik = pd.read_csv('c:/data/final/jisik.csv', encoding='cp949', header=0, names=['description'])
jisik


stop_word = []
with open('c:/data/stop_words.txt', 'r', encoding='utf-8') as s:
    for word in s:
        stop_word.append(word.strip())
stop_word
from konlpy.tag import Okt
pos = Okt()
def text_tokenizing(doc):
    return [word for word in pos.nouns(doc) if word not in stop_word and len(word) > 1]
contents_token = [text_tokenizing(i) for i in jisik['description']]
contents_token
contents = contents_token

embedding_model = Word2Vec(contents, size=100, window = 2, min_count=3, workers=4, iter=100, sg=1)
contents1 = pd.DataFrame(embedding_model.most_similar("여드름", topn=100))
contents1.columns = ['word', '2vec']
contents1
#=======================================================================================

client_id = "C2QUU8idCr59BHXMN1qx"
client_secret = "s62CxCE2rP"

q = urllib.parse.quote('여드름')
idx = 0
display = 100
start = 1
end = 1000
sort = 'sim'

in_df = pd.DataFrame(columns=('title', 'description'))

for i in range(start, end, display):
  url = "https://openapi.naver.com/v1/search/news?query=" + q \
        + '&display=' + str(display) \
        + '&start=' + str(i) \
        + '&sort=' + sort

  request = urllib.request.Request(url)
  request.add_header("X-Naver-Client-Id",client_id)
  request.add_header("X-Naver-Client-Secret",client_secret)
  response = urllib.request.urlopen(request)
  rescode = response.getcode()
  if(rescode==200): # 정상적으로 코드를 받으면 200 표시
      response_body = response.read()
      response_dict = json.loads(response_body.decode('utf-8'))
      items = response_dict['items']
      for i_index in range(0, len(items)):
        remove_tag = re.compile('[^가-힣 ]')
        title = re.sub(remove_tag, '', items[i_index]['title'])
        description = re.sub(remove_tag, '', items[i_index]['description'])
        in_df.loc[idx] = [title, description]
        idx += 1
  else:
      print("Error Code:" + rescode)

news = pd.DataFrame(columns = ['description'])
news['description'] = in_df['description']



stop_word = []
with open('c:/data/stop_words.txt', 'r', encoding='utf-8') as s:
    for word in s:
        stop_word.append(word.strip())
stop_word
from konlpy.tag import Okt
pos = Okt()
def text_tokenizing(doc):
    return [word for word in pos.nouns(doc) if word not in stop_word and len(word) > 1]
contents_token = [text_tokenizing(i) for i in news['description']]
contents2 = contents_token

embedding_model1 = Word2Vec(contents2, size=100, window = 2, min_count=3, workers=4, iter=100, sg=1)
contents2 = pd.DataFrame(embedding_model1.most_similar("여드름", topn=100))
contents2.columns = ['word', '2vec']
contents2