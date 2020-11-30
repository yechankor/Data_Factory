# 1-2-3) 문화취미 스크래핑과 토큰화 

import urllib.request as req
from urllib.request import urlopen
import collections
from bs4 import BeautifulSoup
import re
import pandas as pd
import numpy as np
from numpy import nan as na
from pandas import Series, DataFrame
from urllib.parse import quote # 아스키 문자로 변환해주는 함수
import json
from fake_useragent import UserAgent
import requests

quote('문화취미')
Kkma = Kkma()
Komoran = Komoran()
Hannanum = Hannanum()
Okt = Okt()

# 201902 문화취미 ================================================================================ 
url = 'https://news.joins.com/Search/News?StartSearchDate=2019.02.01&EndSearchDate=2019.02.29&Keyword=%EB%AC%B8%ED%99%94%EC%B7%A8%EB%AF%B8&SortType=New&SearchCategoryType=News&PeriodType=DirectInput&ScopeType=All&ServiceCode=&SourceGroupType=&ReporterCode=&ImageType=All&JplusType=All&BlogType=All&ImageSearchType=Image&MatchKeyword=&IncludeKeyword=&ExcluedeKeyword='
html = urlopen(url)
soup = BeautifulSoup(html, 'html.parser')

# 문화취미 url
urls = []
for i in soup.select('h2.headline > a'):
    urls.append(i['href'])

texts = []
for i in urls:
    url = i
    html = urlopen(url)
    soup = BeautifulSoup(html, "html.parser")
    try:
        while True:
            soup.select_one('div#article_body > div').replace_with("").text
            if len(soup.select_one('div#article_body > div').replace_with("").text) == 0:
                break
    except Exception as err:
        print(err)
        pass
    data = soup.select_one('div.article_body').text.strip()
    texts.append(data)

cul201902_cul = []
for i in range(len(texts)) :
    article = texts[i]
    sentences = article.split(". ")
    for setence_idx in range(len(sentences) -1) :
        line = sentences[setence_idx].strip().replace(u'\xa0', u' ')
        cul201902_cul.append(line)
        

# 201903 문화취미 ================================================================================ 
url = 'https://news.joins.com/Search/News?StartSearchDate=2019.03.01&EndSearchDate=2019.03.31&Keyword=%EB%AC%B8%ED%99%94%EC%B7%A8%EB%AF%B8&SortType=New&SearchCategoryType=News&PeriodType=DirectInput&ScopeType=All&ServiceCode=&SourceGroupType=&ReporterCode=&ImageType=All&JplusType=All&BlogType=All&ImageSearchType=Image&MatchKeyword=&IncludeKeyword=&ExcluedeKeyword='
html = urlopen(url)
soup = BeautifulSoup(html, 'html.parser')

# 문화취미 url
urls = []
for i in soup.select('h2.headline > a'):
    urls.append(i['href'])

texts = []
for i in urls:
    url = i
    html = urlopen(url)
    soup = BeautifulSoup(html, "html.parser")
    try:
        while True:
            soup.select_one('div#article_body > div').replace_with("").text
            if len(soup.select_one('div#article_body > div').replace_with("").text) == 0:
                break
    except Exception as err:
        print(err)
        pass
    data = soup.select_one('div.article_body').text.strip()
    texts.append(data)

cul201903_cul = []
for i in range(len(texts)) :
    article = texts[i]
    sentences = article.split(". ")
    for setence_idx in range(len(sentences) -1) :
        line = sentences[setence_idx].strip().replace(u'\xa0', u' ')
        cul201903_cul.append(line)
        
        
# 201904 문화취미 ================================================================================      
url = 'https://news.joins.com/Search/News?StartSearchDate=2019.04.01&EndSearchDate=2019.04.30&Keyword=%EB%AC%B8%ED%99%94%EC%B7%A8%EB%AF%B8&SortType=New&SearchCategoryType=News&PeriodType=DirectInput&ScopeType=All&ServiceCode=&SourceGroupType=&ReporterCode=&ImageType=All&JplusType=All&BlogType=All&ImageSearchType=Image&MatchKeyword=&IncludeKeyword=&ExcluedeKeyword='
html = urlopen(url)
soup = BeautifulSoup(html, 'html.parser')

# 문화취미 url
urls = []
for i in soup.select('h2.headline > a'):
    urls.append(i['href'])

texts = []
for i in urls:
    url = i
    html = urlopen(url)
    soup = BeautifulSoup(html, "html.parser")
    try:
        while True:
            soup.select_one('div#article_body > div').replace_with("").text
            if len(soup.select_one('div#article_body > div').replace_with("").text) == 0:
                break
    except Exception as err:
        print(err)
        pass
    data = soup.select_one('div.article_body').text.strip()
    texts.append(data)

cul201904_cul = []
for i in range(len(texts)) :
    article = texts[i]
    sentences = article.split(". ")
    for setence_idx in range(len(sentences) -1) :
        line = sentences[setence_idx].strip().replace(u'\xa0', u' ')
        cul201904_cul.append(line)

        
# 201905 문화취미 ================================================================================ 
url = 'https://news.joins.com/Search/News?StartSearchDate=2019.05.01&EndSearchDate=2019.05.31&Keyword=%EB%AC%B8%ED%99%94%EC%B7%A8%EB%AF%B8&SortType=New&SearchCategoryType=News&PeriodType=DirectInput&ScopeType=All&ServiceCode=&SourceGroupType=&ReporterCode=&ImageType=All&JplusType=All&BlogType=All&ImageSearchType=Image&MatchKeyword=&IncludeKeyword=&ExcluedeKeyword='
html = urlopen(url)
soup = BeautifulSoup(html, 'html.parser')

# 문화취미 url
urls = []
for i in soup.select('h2.headline > a'):
    urls.append(i['href'])

texts = []
for i in urls:
    url = i
    html = urlopen(url)
    soup = BeautifulSoup(html, "html.parser")
    try:
        while True:
            soup.select_one('div.article_body > div').replace_with("").text
            if len(soup.select_one('div.article_body > div').replace_with("").text) == 0:
                break
    except Exception as err:
        print(err)
        pass
    data = soup.select_one('div.article_body').text.strip()
    texts.append(data)

cul201905_cul = []
for i in range(len(texts)) :
    article = texts[i]
    sentences = article.split(". ")
    for setence_idx in range(len(sentences) -1) :
        line = sentences[setence_idx].strip().replace(u'\xa0', u' ')
        cul201905_cul.append(line)
        
        
# 202002 문화취미 ================================================================================ 
url = 'https://news.joins.com/Search/News?StartSearchDate=2020.02.01&EndSearchDate=2020.02.29&Keyword=%EB%AC%B8%ED%99%94%EC%B7%A8%EB%AF%B8&SortType=New&SearchCategoryType=News&PeriodType=DirectInput&ScopeType=All&ServiceCode=&SourceGroupType=&ReporterCode=&ImageType=All&JplusType=All&BlogType=All&ImageSearchType=Image&MatchKeyword=&IncludeKeyword=&ExcluedeKeyword='
html = urlopen(url)
soup = BeautifulSoup(html, 'html.parser')

# 문화취미 url
urls = []
for i in soup.select('h2.headline > a'):
    urls.append(i['href'])

texts = []
for i in urls:
    url = i
    html = urlopen(url)
    soup = BeautifulSoup(html, "html.parser")
    try:
        while True:
            soup.select_one('div#article_body > div').replace_with("").text
            if len(soup.select_one('div#article_body > div').replace_with("").text) == 0:
                break
    except Exception as err:
        print(err)
        pass
    data = soup.select_one('div.article_body').text.strip()
    texts.append(data)

cul202002_cul = []
for i in range(len(texts)) :
    article = texts[i]
    sentences = article.split(". ")
    for setence_idx in range(len(sentences) -1) :
        line = sentences[setence_idx].strip().replace(u'\xa0', u' ')
        cul202002_cul.append(line)


# 202003 문화취미 ================================================================================ 
url = 'https://news.joins.com/Search/News?StartSearchDate=2020.03.01&EndSearchDate=2020.03.31&Keyword=%EB%AC%B8%ED%99%94%EC%B7%A8%EB%AF%B8&SortType=New&SearchCategoryType=News&PeriodType=DirectInput&ScopeType=All&ServiceCode=&SourceGroupType=&ReporterCode=&ImageType=All&JplusType=All&BlogType=All&ImageSearchType=Image&MatchKeyword=&IncludeKeyword=&ExcluedeKeyword='
html = urlopen(url)
soup = BeautifulSoup(html, 'html.parser')
 
# 문화취미 url
urls = []
for i in soup.select('h2.headline > a'):
    urls.append(i['href'])

texts = []
for i in urls:
    url = i
    html = urlopen(url)
    soup = BeautifulSoup(html, "html.parser")
    try:
        while True:
            soup.select_one('div#article_body > div').replace_with("").text
            if len(soup.select_one('div#article_body > div').replace_with("").text) == 0:
                break
    except Exception as err:
        print(err)
        pass
    data = soup.select_one('div.article_body').text.strip()
    texts.append(data)

cul202003_cul = []
for i in range(len(texts)) :
    article = texts[i]
    sentences = article.split(". ")
    for setence_idx in range(len(sentences) -1) :
        line = sentences[setence_idx].strip().replace(u'\xa0', u' ')
        cul202003_cul.append(line)

        
# 202004 문화취미 ================================================================================ 
url = 'https://news.joins.com/Search/News?StartSearchDate=2020.04.01&EndSearchDate=2020.04.30&Keyword=%EB%AC%B8%ED%99%94%EC%B7%A8%EB%AF%B8&SortType=New&SearchCategoryType=News&PeriodType=DirectInput&ScopeType=All&ServiceCode=&SourceGroupType=&ReporterCode=&ImageType=All&JplusType=All&BlogType=All&ImageSearchType=Image&MatchKeyword=&IncludeKeyword=&ExcluedeKeyword='
html = urlopen(url)
soup = BeautifulSoup(html, 'html.parser')

# 문화취미 url
urls = []
for i in soup.select('h2.headline > a'):
    urls.append(i['href'])

texts = []
for i in urls:
    url = i
    html = urlopen(url)
    soup = BeautifulSoup(html, "html.parser")
    try:
        while True:
            soup.select_one('div#article_body > div').replace_with("").text
            if len(soup.select_one('div#article_body > div').replace_with("").text) == 0:
                break
    except Exception as err:
        print(err)
        pass
    data = soup.select_one('div.article_body').text.strip()
    texts.append(data)

cul202004_cul = []
for i in range(len(texts)) :
    article = texts[i]
    sentences = article.split(". ")
    for setence_idx in range(len(sentences) -1) :
        line = sentences[setence_idx].strip().replace(u'\xa0', u' ')
        cul202004_cul.append(line)
        
        
# 202005 문화취미 ================================================================================ 
url = 'https://news.joins.com/Search/News?StartSearchDate=2020.05.01&EndSearchDate=2020.05.30&Keyword=%EB%AC%B8%ED%99%94%EC%B7%A8%EB%AF%B8&SortType=New&SearchCategoryType=News&PeriodType=DirectInput&ScopeType=All&ServiceCode=&SourceGroupType=&ReporterCode=&ImageType=All&JplusType=All&BlogType=All&ImageSearchType=Image&MatchKeyword=&IncludeKeyword=&ExcluedeKeyword='
html = urlopen(url)
soup = BeautifulSoup(html, 'html.parser')

# 문화취미 url
urls = []
for i in soup.select('h2.headline > a'):
    urls.append(i['href'])

texts = []
for i in urls:
    url = i
    html = urlopen(url)
    soup = BeautifulSoup(html, "html.parser")
    try:
        while True:
            soup.select_one('div#article_body > div').replace_with("").text
            if len(soup.select_one('div#article_body > div').replace_with("").text) == 0:
                break
    except Exception as err:
        print(err)
        pass
    data = soup.select_one('div.article_body').text.strip()
    texts.append(data)

cul202005_cul = []
for i in range(len(texts)) :
    article = texts[i]
    sentences = article.split(". ")
    for setence_idx in range(len(sentences) -1) :
        line = sentences[setence_idx].strip().replace(u'\xa0', u' ')
        cul202005_cul.append(line)
        

# 토큰화 =========================================================================================

# 2019년 2월 문화취미
cul201902=[]
for i in cul201902_cul:
    x = i.replace(',', ' ')
    x = x.replace('(', ' ')
    x = x.replace(')', ' ')
    x = x.replace('”', ' ')
    x = x.replace('“', ' ')
    x = x.replace('.', ' ')
    x = x.replace('\'', ' ')
    x = x.replace('▶', ' ')
    x = x.replace('·', ' ')
    x = x.replace('·', ' ')
    x = x.replace('‘', ' ')
    x = x.replace('’', ' ')
    x = x.replace('"', ' ')
    x = x.replace('?', ' ')
    cul201902.append(Okt.morphs(x))
print(cul201902) 

# 2019년 3월 문화취미
cul201903=[]
for i in cul201903_cul:
    x = i.replace(',', ' ')
    x = x.replace('(', ' ')
    x = x.replace(')', ' ')
    x = x.replace('”', ' ')
    x = x.replace('“', ' ')
    x = x.replace('.', ' ')
    x = x.replace('\'', ' ')
    x = x.replace('▶', ' ')
    x = x.replace('·', ' ')
    x = x.replace('·', ' ')
    x = x.replace('‘', ' ')
    x = x.replace('’', ' ')
    x = x.replace('"', ' ')
    x = x.replace('?', ' ')
    cul201903.append(Okt.morphs(x))
print(cul201903) 

# 2019년 4월 문화취미
cul201904=[]
for i in cul201904_cul:
    x = i.replace(',', ' ')
    x = x.replace('(', ' ')
    x = x.replace(')', ' ')
    x = x.replace('”', ' ')
    x = x.replace('“', ' ')
    x = x.replace('.', ' ')
    x = x.replace('\'', ' ')
    x = x.replace('▶', ' ')
    x = x.replace('·', ' ')
    x = x.replace('·', ' ')
    x = x.replace('‘', ' ')
    x = x.replace('’', ' ')
    x = x.replace('"', ' ')
    x = x.replace('?', ' ')
    cul201904.append(Okt.morphs(x))
print(cul201904) 

# 2019년 5월 문화취미
cul201905=[]
for i in cul201905_cul:
    x = i.replace(',', ' ')
    x = x.replace('(', ' ')
    x = x.replace(')', ' ')
    x = x.replace('”', ' ')
    x = x.replace('“', ' ')
    x = x.replace('.', ' ')
    x = x.replace('\'', ' ')
    x = x.replace('▶', ' ')
    x = x.replace('·', ' ')
    x = x.replace('·', ' ')
    x = x.replace('‘', ' ')
    x = x.replace('’', ' ')
    x = x.replace('"', ' ')
    x = x.replace('?', ' ')
    cul201905.append(Okt.morphs(x))
print(cul201905) 

# 2020년 2월 문화취미
cul202002=[]
for i in cul202002_cul:
    x = i.replace(',', ' ')
    x = x.replace('(', ' ')
    x = x.replace(')', ' ')
    x = x.replace('”', ' ')
    x = x.replace('“', ' ')
    x = x.replace('.', ' ')
    x = x.replace('\'', ' ')
    x = x.replace('▶', ' ')
    x = x.replace('·', ' ')
    x = x.replace('·', ' ')
    x = x.replace('‘', ' ')
    x = x.replace('’', ' ')
    x = x.replace('"', ' ')
    x = x.replace('?', ' ')
    cul202002.append(Okt.morphs(x))
print(cul202002) 

# 2020년 3월 문화취미
cul202003=[]
for i in cul202003_cul:
    x = i.replace(',', ' ')
    x = x.replace('(', ' ')
    x = x.replace(')', ' ')
    x = x.replace('”', ' ')
    x = x.replace('“', ' ')
    x = x.replace('.', ' ')
    x = x.replace('\'', ' ')
    x = x.replace('▶', ' ')
    x = x.replace('·', ' ')
    x = x.replace('·', ' ')
    x = x.replace('‘', ' ')
    x = x.replace('’', ' ')
    x = x.replace('"', ' ')
    x = x.replace('?', ' ')
    cul202003.append(Okt.morphs(x))
print(cul202003)

# 2020년 4월 문화취미
cul202004=[]
for i in cul202004_cul:
    x = i.replace(',', ' ')
    x = x.replace('(', ' ')
    x = x.replace(')', ' ')
    x = x.replace('”', ' ')
    x = x.replace('“', ' ')
    x = x.replace('.', ' ')
    x = x.replace('\'', ' ')
    x = x.replace('▶', ' ')
    x = x.replace('·', ' ')
    x = x.replace('·', ' ')
    x = x.replace('‘', ' ')
    x = x.replace('’', ' ')
    x = x.replace('"', ' ')
    x = x.replace('?', ' ')
    cul202004.append(Okt.morphs(x))
print(cul202004) # 2020년 4월 문화취미 수집

# 2020년 5월 문화취미
cul202005=[]
for i in cul202005_cul:
    x = i.replace(',', ' ')
    x = x.replace('(', ' ')
    x = x.replace(')', ' ')
    x = x.replace('”', ' ')
    x = x.replace('“', ' ')
    x = x.replace('.', ' ')
    x = x.replace('\'', ' ')
    x = x.replace('▶', ' ')
    x = x.replace('·', ' ')
    x = x.replace('·', ' ')
    x = x.replace('‘', ' ')
    x = x.replace('’', ' ')
    x = x.replace('"', ' ')
    x = x.replace('?', ' ')
    cul202005.append(Okt.morphs(x))
print(cul202005) # 2020년 5월 문화취미 수집