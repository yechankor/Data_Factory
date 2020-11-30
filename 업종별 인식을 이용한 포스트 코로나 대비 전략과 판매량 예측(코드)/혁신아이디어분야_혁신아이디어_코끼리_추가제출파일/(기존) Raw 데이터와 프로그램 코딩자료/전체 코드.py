# 1. 업종별 긍정부정 인식 확인

# 1-1) SNS 데이터 확인 ================================================================================

import csv
import pandas as pd

data = pd.read_csv("C:/data/2020 bigcontest data_wisenut.csv", delimiter='')
display(data)
type(data)

# 구+행정동에 대한 화제어
# 서울 중구
s_j = data[['UP_TOPIC_201902','UP_TOPIC_201903','UP_TOPIC_201904','UP_TOPIC_201905',
            'UP_TOPIC_202002','UP_TOPIC_202003','UP_TOPIC_202004','UP_TOPIC_202005']][0:13]
# 서울 노원구
s_n = data[['UP_TOPIC_201902','UP_TOPIC_201903','UP_TOPIC_201904','UP_TOPIC_201905',
            'UP_TOPIC_202002','UP_TOPIC_202003','UP_TOPIC_202004','UP_TOPIC_202005']][13:18]
# 대구 수성구
d_s = data[['UP_TOPIC_201902','UP_TOPIC_201903','UP_TOPIC_201904','UP_TOPIC_201905',
            'UP_TOPIC_202002','UP_TOPIC_202003','UP_TOPIC_202004','UP_TOPIC_202005']][18:29]
# 대구 중구
d_j = data[['UP_TOPIC_201902','UP_TOPIC_201903','UP_TOPIC_201904','UP_TOPIC_201905',
            'UP_TOPIC_202002','UP_TOPIC_202003','UP_TOPIC_202004','UP_TOPIC_202005']][29:35]


# 2019년 월별 업종1에 대한 긍정게시량
for i in range(2,6):
  x='UP1_POSITIVE_20190{}'.format(i)
print('{}월'.format(i),'\n',data[x])

# 2019년 월별 업종2에 대한 긍정게시량
for i in range(2,6):
  x='UP2_POSITIVE_20190{}'.format(i)
print('{}월'.format(i),'\n',data[x])

# 2019년 월별 업종3에 대한 긍정게시량
for i in range(2,6):
  x='UP3_POSITIVE_20190{}'.format(i)
print('{}월'.format(i),'\n',data[x])

# 2019년 월별 업종4에 대한 긍정게시량
for i in range(2,6):
  x='UP4_POSITIVE_20190{}'.format(i)
print('{}월'.format(i),'\n',data[x])

# 2019년 월별 업종5에 대한 긍정게시량
for i in range(2,6):
  x='UP5_POSITIVE_20190{}'.format(i)
print('{}월'.format(i),'\n',data[x])

# 2019년 월별 업종6에 대한 긍정게시량
for i in range(2,6):
  x='UP6_POSITIVE_20190{}'.format(i)
print('{}월'.format(i),'\n',data[x])

# 2020년 월별 업종1에 대한 긍정게시량
for i in range(2,6):
  x='UP1_POSITIVE_20200{}'.format(i)
print('{}월'.format(i),'\n',data[x])

# 2020년 월별 업종2에 대한 긍정게시량
for i in range(2,6):
  x='UP2_POSITIVE_20200{}'.format(i)
print('{}월'.format(i),'\n',data[x])

# 2020년 월별 업종3에 대한 긍정게시량
for i in range(2,6):
  x='UP3_POSITIVE_20200{}'.format(i)
print('{}월'.format(i),'\n',data[x])

# 2020년 월별 업종4에 대한 긍정게시량
for i in range(2,6):
  x='UP4_POSITIVE_20200{}'.format(i)
print('{}월'.format(i),'\n',data[x])

# 2020년 월별 업종5에 대한 긍정게시량
for i in range(2,6):
  x='UP5_POSITIVE_20200{}'.format(i)
print('{}월'.format(i),'\n',data[x])

# 2020년 월별 업종6에 대한 긍정게시량
for i in range(2,6):
  x='UP6_POSITIVE_20200{}'.format(i)
print('{}월'.format(i),'\n',data[x])


# 2019년 월별 업종1에 대한 부정게시량
for i in range(2,6):
  x='UP1_NEGATIVE_20190{}'.format(i)
print('{}월'.format(i),'\n',data[x])

# 2019년 월별 업종2에 대한 부정게시량
for i in range(2,6):
  x='UP2_NEGATIVE_20190{}'.format(i)
print('{}월'.format(i),'\n',data[x])

# 2019년 월별 업종3에 대한 부정게시량
for i in range(2,6):
  x='UP3_NEGATIVE_20190{}'.format(i)
print('{}월'.format(i),'\n',data[x])

# 2019년 월별 업종4에 대한 부정게시량
for i in range(2,6):
  x='UP4_NEGATIVE_20190{}'.format(i)
print('{}월'.format(i),'\n',data[x])

# 2019년 월별 업종5에 대한 부정게시량
for i in range(2,6):
  x='UP5_NEGATIVE_20190{}'.format(i)
print('{}월'.format(i),'\n',data[x])

# 2019년 월별 업종6에 대한 부정게시량
for i in range(2,6):
  x='UP6_NEGATIVE_20190{}'.format(i)
print('{}월'.format(i),'\n',data[x])

# 2020년 월별 업종1에 대한 부정게시량
for i in range(2,6):
  x='UP1_NEGATIVE_20200{}'.format(i)
print('{}월'.format(i),'\n',data[x])

# 2020년 월별 업종2에 대한 부정게시량
for i in range(2,6):
  x='UP2_NEGATIVE_20200{}'.format(i)
print('{}월'.format(i),'\n',data[x])

# 2020년 월별 업종3에 대한 부정게시량
for i in range(2,6):
  x='UP3_NEGATIVE_20200{}'.format(i)
print('{}월'.format(i),'\n',data[x])

# 2020년 월별 업종4에 대한 부정게시량
for i in range(2,6):
  x='UP4_NEGATIVE_20200{}'.format(i)
print('{}월'.format(i),'\n',data[x])

# 2020년 월별 업종5에 대한 부정게시량
for i in range(2,6):
  x='UP5_NEGATIVE_20200{}'.format(i)
print('{}월'.format(i),'\n',data[x])

# 2020년 월별 업종6에 대한 부정게시량
for i in range(2,6):
  x='UP6_NEGATIVE_20200{}'.format(i)
print('{}월'.format(i),'\n',data[x])


# 1-2-1) 숙박 스크래핑과 토큰화 

# 201902 숙박 =========================================================================================
url = 'https://news.joins.com/Search/JoongangNews?StartSearchDate=2019.02.01&EndSearchDate=2019.02.28&Keyword=%EC%88%99%EB%B0%95&SortType=New&SearchCategoryType=JoongangNews&PeriodType=DirectInput&ScopeType=All&ServiceCode=&SourceGroupType=&ReporterCode=&ImageType=All&JplusType=All&BlogType=All&ImageSearchType=Image&MatchKeyword=&IncludeKeyword=&ExcluedeKeyword='
html = urlopen(url)
soup = BeautifulSoup(html, 'html.parser')

# 숙박 url
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

lines201902_s = []
for i in range(len(texts)) :
    article = texts[i]
    sentences = article.split(". ")
    for setence_idx in range(len(sentences) -1) :
        line = sentences[setence_idx].strip().replace(u'\xa0', u' ')
        lines201902_s.append(line)

        
# 201903 숙박 =========================================================================================
url = 'https://news.joins.com/Search/JoongangNews?StartSearchDate=2019.03.01&EndSearchDate=2019.03.30&Keyword=%EC%88%99%EB%B0%95&SortType=New&SearchCategoryType=JoongangNews&PeriodType=DirectInput&ScopeType=All&ServiceCode=&SourceGroupType=&ReporterCode=&ImageType=All&JplusType=All&BlogType=All&ImageSearchType=Image&MatchKeyword=&IncludeKeyword=&ExcluedeKeyword='
html = urlopen(url)
soup = BeautifulSoup(html, 'html.parser')
    
# 숙박 url
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

lines201903_s = []
for i in range(len(texts)) :
    article = texts[i]
    sentences = article.split(". ")
    for setence_idx in range(len(sentences) -1) :
        line = sentences[setence_idx].strip().replace(u'\xa0', u' ')
        lines201903_s.append(line)
        

# 201904 숙박 =========================================================================================
url = 'https://news.joins.com/Search/JoongangNews?StartSearchDate=2019.04.01&EndSearchDate=2019.04.30&Keyword=%EC%88%99%EB%B0%95&SortType=New&SearchCategoryType=JoongangNews&PeriodType=DirectInput&ScopeType=All&ServiceCode=&SourceGroupType=&ReporterCode=&ImageType=All&JplusType=All&BlogType=All&ImageSearchType=Image&MatchKeyword=&IncludeKeyword=&ExcluedeKeyword='
html = urlopen(url)
soup = BeautifulSoup(html, 'html.parser')

# 숙박 url
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

lines201904_s = []
for i in range(len(texts)) :
    article = texts[i]
    sentences = article.split(". ")
    for setence_idx in range(len(sentences) -1) :
        line = sentences[setence_idx].strip().replace(u'\xa0', u' ')
        lines201904_s.append(line)

        
# 201905 숙박 =========================================================================================
url = 'https://news.joins.com/Search/JoongangNews?StartSearchDate=2019.05.01&EndSearchDate=2019.05.31&Keyword=%EC%88%99%EB%B0%95&SortType=New&SearchCategoryType=JoongangNews&PeriodType=DirectInput&ScopeType=All&ServiceCode=&SourceGroupType=&ReporterCode=&ImageType=All&JplusType=All&BlogType=All&ImageSearchType=Image&MatchKeyword=&IncludeKeyword=&ExcluedeKeyword='
html = urlopen(url)
soup = BeautifulSoup(html, 'html.parser')
  
# 숙박 url
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

lines201905_s = []
for i in range(len(texts)) :
    article = texts[i]
    
    sentences = article.split(". ")
    
    for setence_idx in range(len(sentences) -1) :
        line = sentences[setence_idx].strip().replace(u'\xa0', u' ')
        lines201905_s.append(line)

        
# 202002 숙박 =========================================================================================
url = 'https://news.joins.com/Search/JoongangNews?StartSearchDate=2020.02.01&EndSearchDate=2020.02.29&Keyword=%EC%88%99%EB%B0%95&SortType=New&SearchCategoryType=JoongangNews&PeriodType=DirectInput&ScopeType=All&ServiceCode=&SourceGroupType=&ReporterCode=&ImageType=All&JplusType=All&BlogType=All&ImageSearchType=Image&MatchKeyword=&IncludeKeyword=&ExcluedeKeyword='
html = urlopen(url)
soup = BeautifulSoup(html, 'html.parser')

# 숙박 url
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

lines202002_s = []
for i in range(len(texts)) :
    article = texts[i]
    sentences = article.split(". ")
    for setence_idx in range(len(sentences) -1) :
        line = sentences[setence_idx].strip().replace(u'\xa0', u' ')
        lines202002_s.append(line)

        
# 202003 숙박 =========================================================================================
url = 'https://news.joins.com/Search/JoongangNews?StartSearchDate=2020.03.01&EndSearchDate=2020.03.23&Keyword=%EC%88%99%EB%B0%95&SortType=New&SearchCategoryType=JoongangNews&PeriodType=DirectInput&ScopeType=All&ServiceCode=&SourceGroupType=&ReporterCode=&ImageType=All&JplusType=All&BlogType=All&ImageSearchType=Image&MatchKeyword=&IncludeKeyword=&ExcluedeKeyword='
html = urlopen(url)
soup = BeautifulSoup(html, 'html.parser')
 
# 숙박 url
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

lines202003_s = []
for i in range(len(texts)) :
    article = texts[i]
    sentences = article.split(". ")
    for setence_idx in range(len(sentences) -1) :
        line = sentences[setence_idx].strip().replace(u'\xa0', u' ')
        lines202003_s.append(line)

        
# 202003 숙박 =========================================================================================
url = 'https://news.joins.com/Search/JoongangNews?StartSearchDate=2020.04.01&EndSearchDate=2020.04.30&Keyword=%EC%88%99%EB%B0%95&SortType=New&SearchCategoryType=JoongangNews&PeriodType=DirectInput&ScopeType=All&ServiceCode=&SourceGroupType=&ReporterCode=&ImageType=All&JplusType=All&BlogType=All&ImageSearchType=Image&MatchKeyword=&IncludeKeyword=&ExcluedeKeyword='
html = urlopen(url)
soup = BeautifulSoup(html, 'html.parser')

# 숙박 url
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

lines202004_s = []
for i in range(len(texts)) :
    article = texts[i]
    sentences = article.split(". ")
    for setence_idx in range(len(sentences) -1) :
        line = sentences[setence_idx].strip().replace(u'\xa0', u' ')
        lines202004_s.append(line)


# 202005 숙박 =========================================================================================
url = 'https://news.joins.com/Search/JoongangNews?StartSearchDate=2020.05.01&EndSearchDate=2020.05.31&Keyword=%EC%88%99%EB%B0%95&SortType=New&SearchCategoryType=JoongangNews&PeriodType=DirectInput&ScopeType=All&ServiceCode=&SourceGroupType=&ReporterCode=&ImageType=All&JplusType=All&BlogType=All&ImageSearchType=Image&MatchKeyword=&IncludeKeyword=&ExcluedeKeyword='
html = urlopen(url)
soup = BeautifulSoup(html, 'html.parser')

# 숙박 url
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

lines202005_s = []
for i in range(len(texts)) :
    article = texts[i]
    sentences = article.split(". ")
    for setence_idx in range(len(sentences) -1) :
        line = sentences[setence_idx].strip().replace(u'\xa0', u' ')
        lines202005_s.append(line)



# 토큰화 =========================================================================================
from konlpy.tag import Kkma
from konlpy.tag import Komoran
from konlpy.tag import Hannanum
from konlpy.tag import Okt

kkma=Kkma()
komoran=Komoran()
hannanum=Hannanum()
okt=Okt()

kkma.pos(text)
komoran.pos(text)
hannanum.pos(text)
okt.pos(lines202005_leisure)

# 2019년 2월 숙박
stay201902=[]
for i in lines201902_s:
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
    stay201902.append(okt.morphs(x))
print(stay201902)

# 2019년 3월 숙박
stay201903=[]
for i in lines201903_s:
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
    stay201903.append(okt.morphs(x))
print(stay201903)

# 2019년 4월 숙박
stay201904=[]
for i in lines201904_s:
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
    stay201904.append(okt.morphs(x))
print(stay201904)

# 2019년 5월 숙박
stay201905=[]
for i in lines201905_s:
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
    stay201905.append(okt.morphs(x))
print(stay201905)

# 2020년 2월 숙박
stay202002=[]
for i in lines202002_s:
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
    stay202002.append(okt.morphs(x))
print(stay202002)

# 2020년 3월 숙박
stay202003=[]
for i in lines202003_s:
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
    stay202003.append(okt.morphs(x))
print(stay202003)

# 2020년 4월 숙박
stay202004=[]
for i in lines202004_s:
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
    stay202004.append(okt.morphs(x))
print(stay202004)

# 2020년 5월 숙박
stay202005=[]
for i in lines202005_s:
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
    stay202005.append(okt.morphs(x))
print(stay202005)

# 1-2-2) 레저 스크래핑과 토큰화 

# 201902 레저 =========================================================================================
url = 'https://news.joins.com/Search/JoongangNews?StartSearchDate=2019.02.01&EndSearchDate=2019.02.28&Keyword=%EB%A0%88%EC%A0%80&SortType=New&SearchCategoryType=JoongangNews&PeriodType=DirectInput&ScopeType=All&ServiceCode=&SourceGroupType=&ReporterCode=&ImageType=All&JplusType=All&BlogType=All&ImageSearchType=Image&MatchKeyword=&IncludeKeyword=&ExcluedeKeyword='
html = urlopen(url)
soup = BeautifulSoup(html, 'html.parser')

# 레저 url
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

lines201902_leisure = []
for i in range(len(texts)) :
    article = texts[i]
    
    sentences = article.split(". ")
    
    for setence_idx in range(len(sentences) -1) :
        line = sentences[setence_idx].strip().replace(u'\xa0', u' ')
        lines201902_leisure.append(line)

        
# 201903 레저 =========================================================================================
url = 'https://news.joins.com/Search/JoongangNews?StartSearchDate=2019.03.01&EndSearchDate=2019.03.31&Keyword=%EB%A0%88%EC%A0%80&SortType=New&SearchCategoryType=JoongangNews&PeriodType=DirectInput&ScopeType=All&ServiceCode=&SourceGroupType=&ReporterCode=&ImageType=All&JplusType=All&BlogType=All&ImageSearchType=Image&MatchKeyword=&IncludeKeyword=&ExcluedeKeyword='
html = urlopen(url)
soup = BeautifulSoup(html, 'html.parser')

# 레저 url
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

lines201903_leisure = []
for i in range(len(texts)) :
    article = texts[i]
    sentences = article.split(". ")
    for setence_idx in range(len(sentences) -1) :
        line = sentences[setence_idx].strip().replace(u'\xa0', u' ')
        lines201903_leisure.append(line)

     
# 201904 레저 =========================================================================================
url = 'https://news.joins.com/Search/JoongangNews?StartSearchDate=2019.04.01&EndSearchDate=2019.04.30&Keyword=%EB%A0%88%EC%A0%80&SortType=New&SearchCategoryType=JoongangNews&PeriodType=DirectInput&ScopeType=All&ServiceCode=&SourceGroupType=&ReporterCode=&ImageType=All&JplusType=All&BlogType=All&ImageSearchType=Image&MatchKeyword=&IncludeKeyword=&ExcluedeKeyword='
html = urlopen(url)
soup = BeautifulSoup(html, 'html.parser')

# 레저 url
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

lines201904_leisure = []
for i in range(len(texts)) :
    article = texts[i]
    sentences = article.split(". ")
    for setence_idx in range(len(sentences) -1) :
        line = sentences[setence_idx].strip().replace(u'\xa0', u' ')
        lines201904_leisure.append(line)

    
# 201905 레저 =========================================================================================
url = 'https://news.joins.com/Search/JoongangNews?StartSearchDate=2019.05.01&EndSearchDate=2019.05.31&Keyword=%EB%A0%88%EC%A0%80&SortType=New&SearchCategoryType=JoongangNews&PeriodType=DirectInput&ScopeType=All&ServiceCode=&SourceGroupType=&ReporterCode=&ImageType=All&JplusType=All&BlogType=All&ImageSearchType=Image&MatchKeyword=&IncludeKeyword=&ExcluedeKeyword='
html = urlopen(url)
soup = BeautifulSoup(html, 'html.parser')

# 레저 url
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

lines201905_leisure = []
for i in range(len(texts)) :
    article = texts[i]
    sentences = article.split(". ")
    for setence_idx in range(len(sentences) -1) :
        line = sentences[setence_idx].strip().replace(u'\xa0', u' ')
        lines201905_leisure.append(line)

        
# 202002 레저 =========================================================================================
url = 'https://news.joins.com/Search/JoongangNews?StartSearchDate=2020.02.01&EndSearchDate=2020.02.28&Keyword=%EB%A0%88%EC%A0%80&SortType=New&SearchCategoryType=JoongangNews&PeriodType=DirectInput&ScopeType=All&ServiceCode=&SourceGroupType=&ReporterCode=&ImageType=All&JplusType=All&BlogType=All&ImageSearchType=Image&MatchKeyword=&IncludeKeyword=&ExcluedeKeyword='
html = urlopen(url)
soup = BeautifulSoup(html, 'html.parser')

# 레저 url
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

lines202002_leisure = []
for i in range(len(texts)) :
    article = texts[i]
    sentences = article.split(". ")
    for setence_idx in range(len(sentences) -1) :
        line = sentences[setence_idx].strip().replace(u'\xa0', u' ')
        lines202002_leisure.append(line)

        
# 202003 레저 =========================================================================================
url = 'https://news.joins.com/Search/JoongangNews?StartSearchDate=2020.03.01&EndSearchDate=2020.03.31&Keyword=%EB%A0%88%EC%A0%80&SortType=New&SearchCategoryType=JoongangNews&PeriodType=DirectInput&ScopeType=All&ServiceCode=&SourceGroupType=&ReporterCode=&ImageType=All&JplusType=All&BlogType=All&ImageSearchType=Image&MatchKeyword=&IncludeKeyword=&ExcluedeKeyword='
html = urlopen(url)
soup = BeautifulSoup(html, 'html.parser')

# 레저 url
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

lines202003_leisure = []
for i in range(len(texts)) :
    article = texts[i]
    sentences = article.split(". ")
    for setence_idx in range(len(sentences) -1) :
        line = sentences[setence_idx].strip().replace(u'\xa0', u' ')
        lines202003_leisure.append(line)

        
# 202004 레저 =========================================================================================
url = 'https://news.joins.com/Search/JoongangNews?StartSearchDate=2020.04.01&EndSearchDate=2020.04.30&Keyword=%EB%A0%88%EC%A0%80&SortType=New&SearchCategoryType=JoongangNews&PeriodType=DirectInput&ScopeType=All&ServiceCode=&SourceGroupType=&ReporterCode=&ImageType=All&JplusType=All&BlogType=All&ImageSearchType=Image&MatchKeyword=&IncludeKeyword=&ExcluedeKeyword='
html = urlopen(url)
soup = BeautifulSoup(html, 'html.parser')

# 레저 url
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

lines202004_leisure = []
for i in range(len(texts)) :
    article = texts[i]
    sentences = article.split(". ")
    for setence_idx in range(len(sentences) -1) :
        line = sentences[setence_idx].strip().replace(u'\xa0', u' ')
        lines202004_leisure.append(line)

        
# 202005 레저 =========================================================================================
url = 'https://news.joins.com/Search/JoongangNews?StartSearchDate=2020.05.01&EndSearchDate=2020.05.31&Keyword=%EB%A0%88%EC%A0%80&SortType=New&SearchCategoryType=JoongangNews&PeriodType=DirectInput&ScopeType=All&ServiceCode=&SourceGroupType=&ReporterCode=&ImageType=All&JplusType=All&BlogType=All&ImageSearchType=Image&MatchKeyword=&IncludeKeyword=&ExcluedeKeyword='
html = urlopen(url)
soup = BeautifulSoup(html, 'html.parser')

# 레저 url
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

lines202005_leisure = []
for i in range(len(texts)) :
    article = texts[i]
    sentences = article.split(". ")
    for setence_idx in range(len(sentences) -1) :
        line = sentences[setence_idx].strip().replace(u'\xa0', u' ')
        lines202005_leisure.append(line)


 
# 토큰화 =========================================================================================

# 2019년 2월 레저
leisure201902=[]
for i in lines201902_leisure:
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
    leisure201902.append(okt.morphs(x))
print(leisure201902)

# 2019년 3월 레저
leisure201903=[]
for i in lines201903_leisure:
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
    leisure201903.append(okt.morphs(x))
print(leisure201903)

# 2019년 4월 레저
leisure201904=[]
for i in lines201904_leisure:
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
    leisure201904.append(okt.morphs(x))
print(leisure201904)

# 2019년 5월 레저
leisure201905=[]
for i in lines201905_leisure:
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
    leisure201905.append(okt.morphs(x))
print(leisure201905)

# 2020년 2월 레저
leisure202002=[]
for i in lines202002_leisure:
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
    leisure202002.append(okt.morphs(x))
print(leisure202002)

# 2020년 3월 레저
leisure202003=[]
for i in lines202003_leisure:
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
    leisure202003.append(okt.morphs(x))
print(leisure202003)

# 2020년 4월 레저
leisure202004=[]
for i in lines202004_leisure:
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
    leisure202004.append(okt.morphs(x))
print(leisure202004)

# 2020년 5월 레저
leisure202005=[]
for i in lines202005_leisure:
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
    leisure202005.append(okt.morphs(x))
print(leisure202005)

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

# 1-2-4) 의료기관 스크래핑과 토큰화       

quote('의료기관')

# 201902 의료기관 ================================================================================ 
url = 'https://news.joins.com/Search/News?StartSearchDate=2019.02.01&EndSearchDate=2019.02.27&Keyword=%EC%9D%98%EB%A3%8C%EA%B8%B0%EA%B4%80&SortType=New&SearchCategoryType=News&PeriodType=DirectInput&ScopeType=All&ServiceCode=&SourceGroupType=&ReporterCode=&ImageType=All&JplusType=All&BlogType=All&ImageSearchType=Image&MatchKeyword=&IncludeKeyword=&ExcluedeKeyword='
html = urlopen(url)
soup = BeautifulSoup(html, 'html.parser')

# 의료기관 url
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

medi201902_medi = []
for i in range(len(texts)) :
    article = texts[i]
    sentences = article.split(". ")
    for setence_idx in range(len(sentences) -1) :
        line = sentences[setence_idx].strip().replace(u'\xa0', u' ')
        medi201902_medi.append(line)
        
        
# 201903 의료기관 ================================================================================ 
url = 'https://news.joins.com/Search/News?StartSearchDate=2019.03.01&EndSearchDate=2019.03.29&Keyword=%EC%9D%98%EB%A3%8C%EA%B8%B0%EA%B4%80&SortType=New&SearchCategoryType=News&PeriodType=DirectInput&ScopeType=All&ServiceCode=&SourceGroupType=&ReporterCode=&ImageType=All&JplusType=All&BlogType=All&ImageSearchType=Image&MatchKeyword=&IncludeKeyword=&ExcluedeKeyword='
html = urlopen(url)
soup = BeautifulSoup(html, 'html.parser')
 
# 의료기관 url
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

medi201903_medi = []
for i in range(len(texts)) :
    article = texts[i] 
    sentences = article.split(". ")
    for setence_idx in range(len(sentences) -1) :
        line = sentences[setence_idx].strip().replace(u'\xa0', u' ')
        medi201903_medi.append(line)
        
        
# 201904 의료기관 ================================================================================ 
url = 'https://news.joins.com/Search/News?StartSearchDate=2019.04.01&EndSearchDate=2019.04.29&Keyword=%EC%9D%98%EB%A3%8C%EA%B8%B0%EA%B4%80&SortType=New&SearchCategoryType=News&PeriodType=DirectInput&ScopeType=All&ServiceCode=&SourceGroupType=&ReporterCode=&ImageType=All&JplusType=All&BlogType=All&ImageSearchType=Image&MatchKeyword=&IncludeKeyword=&ExcluedeKeyword='
html = urlopen(url)
soup = BeautifulSoup(html, 'html.parser')

# 의료기관 url
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

medi201904_medi = []
for i in range(len(texts)) :
    article = texts[i]
    sentences = article.split(". ")
    for setence_idx in range(len(sentences) -1) :
        line = sentences[setence_idx].strip().replace(u'\xa0', u' ')
        medi201904_medi.append(line)
        
        
# 201905 의료기관 ================================================================================ 
url = 'https://news.joins.com/Search/News?StartSearchDate=2019.05.01&EndSearchDate=2019.05.31&Keyword=%EC%9D%98%EB%A3%8C%EA%B8%B0%EA%B4%80&SortType=New&SearchCategoryType=News&PeriodType=DirectInput&ScopeType=All&ServiceCode=&SourceGroupType=&ReporterCode=&ImageType=All&JplusType=All&BlogType=All&ImageSearchType=Image&MatchKeyword=&IncludeKeyword=&ExcluedeKeyword='
html = urlopen(url)
soup = BeautifulSoup(html, 'html.parser')

# 의료기관 url
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

medi201905_medi = []
for i in range(len(texts)) :
    article = texts[i]
    sentences = article.split(". ")
    for setence_idx in range(len(sentences) -1) :
        line = sentences[setence_idx].strip().replace(u'\xa0', u' ')
        medi201905_medi.append(line)
        
        
# 202002 의료기관 ================================================================================ 
url = 'https://news.joins.com/Search/News?StartSearchDate=2020.02.01&EndSearchDate=2020.02.27&Keyword=%EC%9D%98%EB%A3%8C%EA%B8%B0%EA%B4%80&SortType=New&SearchCategoryType=News&PeriodType=DirectInput&ScopeType=All&ServiceCode=&SourceGroupType=&ReporterCode=&ImageType=All&JplusType=All&BlogType=All&ImageSearchType=Image&MatchKeyword=&IncludeKeyword=&ExcluedeKeyword='
html = urlopen(url)
soup = BeautifulSoup(html, 'html.parser')

# 의료기관 url
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

medi202002_medi = []
for i in range(len(texts)) :
    article = texts[i]
    sentences = article.split(". ")
    for setence_idx in range(len(sentences) -1) :
        line = sentences[setence_idx].strip().replace(u'\xa0', u' ')
        medi202002_medi.append(line)
        
        
# 202003 의료기관 ================================================================================ 
url = 'https://news.joins.com/Search/News?StartSearchDate=2020.03.01&EndSearchDate=2020.03.29&Keyword=%EC%9D%98%EB%A3%8C%EA%B8%B0%EA%B4%80&SortType=New&SearchCategoryType=News&PeriodType=DirectInput&ScopeType=All&ServiceCode=&SourceGroupType=&ReporterCode=&ImageType=All&JplusType=All&BlogType=All&ImageSearchType=Image&MatchKeyword=&IncludeKeyword=&ExcluedeKeyword='
html = urlopen(url)
soup = BeautifulSoup(html, 'html.parser')

# 의료기관 url
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

medi202003_medi = []
for i in range(len(texts)) :
    article = texts[i]
    sentences = article.split(". ")
    for setence_idx in range(len(sentences) -1) :
        line = sentences[setence_idx].strip().replace(u'\xa0', u' ')
        medi202003_medi.append(line)
        
        
# 202004 의료기관 ================================================================================ 
url = 'https://news.joins.com/Search/News?StartSearchDate=2020.04.01&EndSearchDate=2020.04.29&Keyword=%EC%9D%98%EB%A3%8C%EA%B8%B0%EA%B4%80&SortType=New&SearchCategoryType=News&PeriodType=DirectInput&ScopeType=All&ServiceCode=&SourceGroupType=&ReporterCode=&ImageType=All&JplusType=All&BlogType=All&ImageSearchType=Image&MatchKeyword=&IncludeKeyword=&ExcluedeKeyword='
html = urlopen(url)
soup = BeautifulSoup(html, 'html.parser')

# 의료기관 url
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

medi202004_medi = []
for i in range(len(texts)) :
    article = texts[i]
    sentences = article.split(". ")
    for setence_idx in range(len(sentences) -1) :
        line = sentences[setence_idx].strip().replace(u'\xa0', u' ')
        medi202004_medi.append(line)
        
        
# 202005 의료기관 ================================================================================ 
url = 'https://news.joins.com/Search/News?StartSearchDate=2020.05.01&EndSearchDate=2020.05.31&Keyword=%EC%9D%98%EB%A3%8C%EA%B8%B0%EA%B4%80&SortType=New&SearchCategoryType=News&PeriodType=DirectInput&ScopeType=All&ServiceCode=&SourceGroupType=&ReporterCode=&ImageType=All&JplusType=All&BlogType=All&ImageSearchType=Image&MatchKeyword=&IncludeKeyword=&ExcluedeKeyword='
html = urlopen(url)
soup = BeautifulSoup(html, 'html.parser')
 
# 의료기관 url
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

medi202005_medi = []
for i in range(len(texts)) :
    article = texts[i]
    sentences = article.split(". ")
    for setence_idx in range(len(sentences) -1) :
        line = sentences[setence_idx].strip().replace(u'\xa0', u' ')
        medi202005_medi.append(line)
        
        

# 토큰화 =========================================================================================

# 2019년 2월 의료기관
medi201902=[]
for i in medi201902_medi:
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
    medi201902.append(Okt.morphs(x))
print(medi201902) 

# 2019년 3월 의료기관
medi201903=[]
for i in medi201903_medi:
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
    medi201903.append(Okt.morphs(x))
print(medi201903)

# 2019년 4월 의료기관
medi201904=[]
for i in medi201904_medi:
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
    medi201904.append(Okt.morphs(x))
print(medi201904)

# 2019년 5월 의료기관
medi201905=[]
for i in medi201905_medi:
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
    medi201905.append(Okt.morphs(x))
print(medi201905)

# 2020년 2월 의료기관
medi202002=[]
for i in medi202002_medi:
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
    medi202002.append(Okt.morphs(x))
print(medi202002)

# 2020년 3월 의료기관
medi202003=[]
for i in medi202003_medi:
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
    medi202003.append(Okt.morphs(x))
print(medi202003)

# 2020년 4월 의료기관
medi202004=[]
for i in medi202004_medi:
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
    medi202004.append(Okt.morphs(x))
print(medi202004)

# 2020년 5월 의료기관
medi202005=[]
for i in medi202005_medi:
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
    medi202005.append(Okt.morphs(x))
print(medi202005)


# 1-2-5) 식품 스크래핑과 토큰화        

quote('요식업')
quote('커피전문점')
quote('주점')

# RSTUDIO에서 Rselenium 자동화로 기사 스크래핑하고 파일로 저장  =========================================

'''
install.packages("XML", type="binary")
install.packages("RSelenium")
library(rvest)
library(RSelenium)
library(tm)

#cmd 창에서
# cd c:\data
# java -Dwebdriver.gecko.driver="geckodriver.exe" -jar selenium-server-standalone-4.0.0-alpha-1.jar -port 4445

## 요식업소 201902 
## 키워드 : 요식업
remdr<- remoteDriver(remoteServerAddr="localhost", port=4445L,browserName="chrome")
remdr$open()
remdr$navigate("https://news.joins.com/Search/JoongangNews?StartSearchDate=2019.02.01&EndSearchDate=2019.02.28&Keyword=%EC%9A%94%EC%8B%9D%EC%97%85&SortType=Accuracy&SearchCategoryType=JoongangNews&PeriodType=DirectInput&ScopeType=All&ServiceCode=&SourceGroupType=&ReporterCode=&ImageType=All&JplusType=All&BlogType=All&ImageSearchType=Image&MatchKeyword=&IncludeKeyword=&ExcluedeKeyword=")
source<-remdr$getPageSource()[[1]]
html<-read_html(source)
url<-c()
for (i in 1:5){
  url<-c(url, 
         html_nodes(html, ".headline ")%>%
           html_nodes('a') %>%
           html_attr('href'))
}
article_body<-NULL
for (i in 1:length(url)){
  html<-read_html(url[i])
  body<-html_node(html,'#article_body')%>%
    html_text()
  article_body<-c(article_body,body)
}

## 키워드 : 커피전문점
remdr$navigate("https://news.joins.com/Search/JoongangNews?StartSearchDate=2019.02.01&EndSearchDate=2019.02.28&Keyword=%EC%BB%A4%ED%94%BC%EC%A0%84%EB%AC%B8%EC%A0%90&SortType=Accuracy&SearchCategoryType=JoongangNews&PeriodType=DirectInput&ScopeType=All&ServiceCode=&SourceGroupType=&ReporterCode=&ImageType=All&JplusType=All&BlogType=All&ImageSearchType=Image&MatchKeyword=&IncludeKeyword=&ExcluedeKeyword=")
source<-remdr$getPageSource()[[1]]
html<-read_html(source)
url<-c()
for (i in 1:5){
  url<-c(url, 
         html_nodes(html, ".headline ")%>%
           html_nodes('a') %>%
           html_attr('href'))
}
for (i in 1:length(url)){
  html<-read_html(url[i])
  body<-html_node(html,'#article_body')%>%
    html_text()
  article_body<-c(article_body,body)
}

## 키워드 : 주점
remdr$navigate("https://news.joins.com/Search/JoongangNews?StartSearchDate=2019.02.01&EndSearchDate=2019.02.28&Keyword=%EC%A3%BC%EC%A0%90&SortType=Accuracy&SearchCategoryType=JoongangNews&PeriodType=DirectInput&ScopeType=All&ServiceCode=&SourceGroupType=&ReporterCode=&ImageType=All&JplusType=All&BlogType=All&ImageSearchType=Image&MatchKeyword=&IncludeKeyword=&ExcluedeKeyword=")
source<-remdr$getPageSource()[[1]]
html<-read_html(source)
url<-c()
for (i in 1:5){
  url<-c(url, 
         html_nodes(html, ".headline ")%>%
           html_nodes('a') %>%
           html_attr('href'))
}
for (i in 1:length(url)){
  html<-read_html(url[i])
  body<-html_node(html,'#article_body')%>%
    html_text()
  article_body<-c(article_body,body)
}
write(article_body, "C:/data/food201902.txt")


## 요식업소 201903 
## 키워드 : 요식업
remdr<- remoteDriver(remoteServerAddr="localhost", port=4445L,browserName="chrome")
remdr$open()
remdr$navigate("https://news.joins.com/Search/JoongangNews?StartSearchDate=2019.03.01&EndSearchDate=2019.03.31&Keyword=%EC%9A%94%EC%8B%9D%EC%97%85&SortType=Accuracy&SearchCategoryType=JoongangNews&PeriodType=DirectInput&ScopeType=All&ServiceCode=&SourceGroupType=&ReporterCode=&ImageType=All&JplusType=All&BlogType=All&ImageSearchType=Image&MatchKeyword=&IncludeKeyword=&ExcluedeKeyword=")
source<-remdr$getPageSource()[[1]]
html<-read_html(source)
url<-c()
for (i in 1:5){
  url<-c(url, 
         html_nodes(html, ".headline ")%>%
           html_nodes('a') %>%
           html_attr('href'))
}
article_body<-NULL
for (i in 1:length(url)){
  html<-read_html(url[i])
  body<-html_node(html,'#article_body')%>%
    html_text()
  article_body<-c(article_body,body)
}

## 키워드 : 커피전문점
remdr$navigate("https://news.joins.com/Search/JoongangNews?StartSearchDate=2019.03.01&EndSearchDate=2019.03.31&Keyword=%EC%BB%A4%ED%94%BC%EC%A0%84%EB%AC%B8%EC%A0%90&SortType=Accuracy&SearchCategoryType=JoongangNews&PeriodType=DirectInput&ScopeType=All&ServiceCode=&SourceGroupType=&ReporterCode=&ImageType=All&JplusType=All&BlogType=All&ImageSearchType=Image&MatchKeyword=&IncludeKeyword=&ExcluedeKeyword=")
source<-remdr$getPageSource()[[1]]
html<-read_html(source)
url<-c()
for (i in 1:5){
  url<-c(url, 
         html_nodes(html, ".headline ")%>%
           html_nodes('a') %>%
           html_attr('href'))
}
for (i in 1:length(url)){
  html<-read_html(url[i])
  body<-html_node(html,'#article_body')%>%
    html_text()
  article_body<-c(article_body,body)
}


## 키워드 : 주점
remdr$navigate("https://news.joins.com/Search/JoongangNews?StartSearchDate=2019.03.01&EndSearchDate=2019.03.31&Keyword=%EC%A3%BC%EC%A0%90&SortType=Accuracy&SearchCategoryType=JoongangNews&PeriodType=DirectInput&ScopeType=All&ServiceCode=&SourceGroupType=&ReporterCode=&ImageType=All&JplusType=All&BlogType=All&ImageSearchType=Image&MatchKeyword=&IncludeKeyword=&ExcluedeKeyword=")
source<-remdr$getPageSource()[[1]]
html<-read_html(source)
url<-c()
for (i in 1:5){
  url<-c(url, 
         html_nodes(html, ".headline ")%>%
           html_nodes('a') %>%
           html_attr('href'))
}
for (i in 1:length(url)){
  html<-read_html(url[i])
  body<-html_node(html,'#article_body')%>%
    html_text()
  article_body<-c(article_body,body)
}
write(article_body, "C:/data/food201903.txt")


## 요식업소 201904
## 키워드 : 요식업
remdr<- remoteDriver(remoteServerAddr="localhost", port=4445L,browserName="chrome")
remdr$open()
remdr$navigate("https://news.joins.com/Search/JoongangNews?StartSearchDate=2019.04.01&EndSearchDate=2019.04.30&Keyword=%EC%9A%94%EC%8B%9D%EC%97%85&SortType=Accuracy&SearchCategoryType=JoongangNews&PeriodType=DirectInput&ScopeType=All&ServiceCode=&SourceGroupType=&ReporterCode=&ImageType=All&JplusType=All&BlogType=All&ImageSearchType=Image&MatchKeyword=&IncludeKeyword=&ExcluedeKeyword=")
source<-remdr$getPageSource()[[1]]
html<-read_html(source)
url<-c()
for (i in 1:5){
  url<-c(url, 
         html_nodes(html, ".headline ")%>%
           html_nodes('a') %>%
           html_attr('href'))
}
article_body<-NULL
for (i in 1:length(url)){
  html<-read_html(url[i])
  body<-html_node(html,'#article_body')%>%
    html_text()
  article_body<-c(article_body,body)
}

## 키워드 : 커피전문점
remdr$navigate("https://news.joins.com/Search/JoongangNews?StartSearchDate=2019.04.01&EndSearchDate=2019.04.30&Keyword=%EC%BB%A4%ED%94%BC%EC%A0%84%EB%AC%B8%EC%A0%90&SortType=Accuracy&SearchCategoryType=JoongangNews&PeriodType=DirectInput&ScopeType=All&ServiceCode=&SourceGroupType=&ReporterCode=&ImageType=All&JplusType=All&BlogType=All&ImageSearchType=Image&MatchKeyword=&IncludeKeyword=&ExcluedeKeyword=")
source<-remdr$getPageSource()[[1]]
html<-read_html(source)
url<-c()
for (i in 1:5){
  url<-c(url, 
         html_nodes(html, ".headline ")%>%
           html_nodes('a') %>%
           html_attr('href'))
}
for (i in 1:length(url)){
  html<-read_html(url[i])
  body<-html_node(html,'#article_body')%>%
    html_text()
  article_body<-c(article_body,body)
}


## 키워드 : 주점
remdr$navigate("https://news.joins.com/Search/JoongangNews?StartSearchDate=2019.04.01&EndSearchDate=2019.04.30&Keyword=%EC%A3%BC%EC%A0%90&SortType=Accuracy&SearchCategoryType=JoongangNews&PeriodType=DirectInput&ScopeType=All&ServiceCode=&SourceGroupType=&ReporterCode=&ImageType=All&JplusType=All&BlogType=All&ImageSearchType=Image&MatchKeyword=&IncludeKeyword=&ExcluedeKeyword=")
source<-remdr$getPageSource()[[1]]
html<-read_html(source)
url<-c()
for (i in 1:5){
  url<-c(url, 
         html_nodes(html, ".headline ")%>%
           html_nodes('a') %>%
           html_attr('href'))
}
for (i in 1:length(url)){
  html<-read_html(url[i])
  body<-html_node(html,'#article_body')%>%
    html_text()
  article_body<-c(article_body,body)
}
write(article_body, "C:/data/food201904.txt")


## 요식업소 201905 
## 키워드 : 요식업
remdr<- remoteDriver(remoteServerAddr="localhost", port=4445L,browserName="chrome")
remdr$open()
remdr$navigate("https://news.joins.com/Search/JoongangNews?StartSearchDate=2019.05.01&EndSearchDate=2019.05.31&Keyword=%EC%9A%94%EC%8B%9D%EC%97%85&SortType=Accuracy&SearchCategoryType=JoongangNews&PeriodType=DirectInput&ScopeType=All&ServiceCode=&SourceGroupType=&ReporterCode=&ImageType=All&JplusType=All&BlogType=All&ImageSearchType=Image&MatchKeyword=&IncludeKeyword=&ExcluedeKeyword=")
source<-remdr$getPageSource()[[1]]
html<-read_html(source)
url<-c()
for (i in 1:5){
  url<-c(url, 
         html_nodes(html, ".headline ")%>%
           html_nodes('a') %>%
           html_attr('href'))
}
article_body<-NULL
for (i in 1:length(url)){
  html<-read_html(url[i])
  body<-html_node(html,'#article_body')%>%
    html_text()
  article_body<-c(article_body,body)
}

## 키워드 : 커피전문점
remdr$navigate("https://news.joins.com/Search/JoongangNews?StartSearchDate=2019.05.01&EndSearchDate=2019.05.31&Keyword=%EC%BB%A4%ED%94%BC%EC%A0%84%EB%AC%B8%EC%A0%90&SortType=Accuracy&SearchCategoryType=JoongangNews&PeriodType=DirectInput&ScopeType=All&ServiceCode=&SourceGroupType=&ReporterCode=&ImageType=All&JplusType=All&BlogType=All&ImageSearchType=Image&MatchKeyword=&IncludeKeyword=&ExcluedeKeyword=")
source<-remdr$getPageSource()[[1]]
html<-read_html(source)
url<-c()
for (i in 1:5){
  url<-c(url, 
         html_nodes(html, ".headline ")%>%
           html_nodes('a') %>%
           html_attr('href'))
}
for (i in 1:length(url)){
  html<-read_html(url[i])
  body<-html_node(html,'#article_body')%>%
    html_text()
  article_body<-c(article_body,body)
}

## 키워드 : 주점
remdr$navigate("https://news.joins.com/Search/JoongangNews?StartSearchDate=2019.05.01&EndSearchDate=2019.05.31&Keyword=%EC%A3%BC%EC%A0%90&SortType=Accuracy&SearchCategoryType=JoongangNews&PeriodType=DirectInput&ScopeType=All&ServiceCode=&SourceGroupType=&ReporterCode=&ImageType=All&JplusType=All&BlogType=All&ImageSearchType=Image&MatchKeyword=&IncludeKeyword=&ExcluedeKeyword=")
source<-remdr$getPageSource()[[1]]
html<-read_html(source)
url<-c()
for (i in 1:5){
  url<-c(url, 
         html_nodes(html, ".headline ")%>%
           html_nodes('a') %>%
           html_attr('href'))
}
for (i in 1:length(url)){
  html<-read_html(url[i])
  body<-html_node(html,'#article_body')%>%
    html_text()
  article_body<-c(article_body,body)
}
write(article_body, "C:/data/food201905.txt")


## 요식업소 202002
## 키워드 : 요식업소
remdr<- remoteDriver(remoteServerAddr="localhost", port=4445L,browserName="chrome")
remdr$open()
remdr$navigate("https://news.joins.com/Search/JoongangNews?StartSearchDate=2020.02.01&EndSearchDate=2020.02.28&Keyword=%EC%9A%94%EC%8B%9D%EC%97%85&SortType=Accuracy&SearchCategoryType=JoongangNews&PeriodType=DirectInput&ScopeType=All&ServiceCode=&SourceGroupType=&ReporterCode=&ImageType=All&JplusType=All&BlogType=All&ImageSearchType=Image&MatchKeyword=&IncludeKeyword=&ExcluedeKeyword=")
source<-remdr$getPageSource()[[1]]
html<-read_html(source)
url<-c()
for (i in 1:5){
  url<-c(url, 
         html_nodes(html, ".headline ")%>%
           html_nodes('a') %>%
           html_attr('href'))
}
article_body<-NULL
for (i in 1:length(url)){
  html<-read_html(url[i])
  body<-html_node(html,'#article_body')%>%
    html_text()
  article_body<-c(article_body,body)
}

## 키워드 : 커피전문점
remdr$navigate("https://news.joins.com/Search/JoongangNews?StartSearchDate=2020.02.01&EndSearchDate=2020.02.28&Keyword=%EC%BB%A4%ED%94%BC%EC%A0%84%EB%AC%B8%EC%A0%90&SortType=Accuracy&SearchCategoryType=JoongangNews&PeriodType=DirectInput&ScopeType=All&ServiceCode=&SourceGroupType=&ReporterCode=&ImageType=All&JplusType=All&BlogType=All&ImageSearchType=Image&MatchKeyword=&IncludeKeyword=&ExcluedeKeyword=")
source<-remdr$getPageSource()[[1]]
html<-read_html(source)
url<-c()
for (i in 1:5){
  url<-c(url, 
         html_nodes(html, ".headline ")%>%
           html_nodes('a') %>%
           html_attr('href'))
}
for (i in 1:length(url)){
  html<-read_html(url[i])
  body<-html_node(html,'#article_body')%>%
    html_text()
  article_body<-c(article_body,body)
}

## 키워드 : 주점
remdr$navigate("https://news.joins.com/Search/JoongangNews?StartSearchDate=2020.02.01&EndSearchDate=2020.02.28&Keyword=%EC%A3%BC%EC%A0%90&SortType=Accuracy&SearchCategoryType=JoongangNews&PeriodType=DirectInput&ScopeType=All&ServiceCode=&SourceGroupType=&ReporterCode=&ImageType=All&JplusType=All&BlogType=All&ImageSearchType=Image&MatchKeyword=&IncludeKeyword=&ExcluedeKeyword=")
source<-remdr$getPageSource()[[1]]
html<-read_html(source)
url<-c()
for (i in 1:5){
  url<-c(url, 
         html_nodes(html, ".headline ")%>%
           html_nodes('a') %>%
           html_attr('href'))
}
for (i in 1:length(url)){
  html<-read_html(url[i])
  body<-html_node(html,'#article_body')%>%
    html_text()
  article_body<-c(article_body,body)
}
write(article_body, "C:/data/food202002.txt")


## 요식업소 202003 
## 키워드 : 요식업소
remdr<- remoteDriver(remoteServerAddr="localhost", port=4445L,browserName="chrome")
remdr$open()
remdr$navigate("https://news.joins.com/Search/JoongangNews?StartSearchDate=2020.03.01&EndSearchDate=2020.03.31&Keyword=%EC%9A%94%EC%8B%9D%EC%97%85&SortType=Accuracy&SearchCategoryType=JoongangNews&PeriodType=DirectInput&ScopeType=All&ServiceCode=&SourceGroupType=&ReporterCode=&ImageType=All&JplusType=All&BlogType=All&ImageSearchType=Image&MatchKeyword=&IncludeKeyword=&ExcluedeKeyword=")
source<-remdr$getPageSource()[[1]]
html<-read_html(source)
url<-c()
for (i in 1:5){
  url<-c(url, 
         html_nodes(html, ".headline ")%>%
           html_nodes('a') %>%
           html_attr('href'))
}
article_body<-NULL
for (i in 1:length(url)){
  html<-read_html(url[i])
  body<-html_node(html,'#article_body')%>%
    html_text()
  article_body<-c(article_body,body)
}

## 키워드 : 커피전문점
remdr$navigate("https://news.joins.com/Search/JoongangNews?StartSearchDate=2020.03.01&EndSearchDate=2020.03.31&Keyword=%EC%BB%A4%ED%94%BC%EC%A0%84%EB%AC%B8%EC%A0%90&SortType=Accuracy&SearchCategoryType=JoongangNews&PeriodType=DirectInput&ScopeType=All&ServiceCode=&SourceGroupType=&ReporterCode=&ImageType=All&JplusType=All&BlogType=All&ImageSearchType=Image&MatchKeyword=&IncludeKeyword=&ExcluedeKeyword=")
source<-remdr$getPageSource()[[1]]
html<-read_html(source)
url<-c()
for (i in 1:5){
  url<-c(url, 
         html_nodes(html, ".headline ")%>%
           html_nodes('a') %>%
           html_attr('href'))
}
for (i in 1:length(url)){
  html<-read_html(url[i])
  body<-html_node(html,'#article_body')%>%
    html_text()
  article_body<-c(article_body,body)
}

## 키워드 : 주점
remdr$navigate("https://news.joins.com/Search/JoongangNews?StartSearchDate=2020.03.01&EndSearchDate=2020.03.31&Keyword=%EC%A3%BC%EC%A0%90&SortType=Accuracy&SearchCategoryType=JoongangNews&PeriodType=DirectInput&ScopeType=All&ServiceCode=&SourceGroupType=&ReporterCode=&ImageType=All&JplusType=All&BlogType=All&ImageSearchType=Image&MatchKeyword=&IncludeKeyword=&ExcluedeKeyword=")
source<-remdr$getPageSource()[[1]]
html<-read_html(source)
url<-c()
for (i in 1:5){
  url<-c(url, 
         html_nodes(html, ".headline ")%>%
           html_nodes('a') %>%
           html_attr('href'))
}
for (i in 1:length(url)){
  html<-read_html(url[i])
  body<-html_node(html,'#article_body')%>%
    html_text()
  article_body<-c(article_body,body)
}
write(article_body, "C:/data/food202003.txt")


## 요식업소 202004
## 키워드 : 요식업소
remdr<- remoteDriver(remoteServerAddr="localhost", port=4445L,browserName="chrome")
remdr$open()
remdr$navigate("https://news.joins.com/Search/JoongangNews?StartSearchDate=2020.04.01&EndSearchDate=2020.04.30&Keyword=%EC%9A%94%EC%8B%9D%EC%97%85&SortType=Accuracy&SearchCategoryType=JoongangNews&PeriodType=DirectInput&ScopeType=All&ServiceCode=&SourceGroupType=&ReporterCode=&ImageType=All&JplusType=All&BlogType=All&ImageSearchType=Image&MatchKeyword=&IncludeKeyword=&ExcluedeKeyword=")
source<-remdr$getPageSource()[[1]]
html<-read_html(source)
url<-c()
for (i in 1:5){
  url<-c(url, 
         html_nodes(html, ".headline ")%>%
           html_nodes('a') %>%
           html_attr('href'))
}
article_body<-NULL
for (i in 1:length(url)){
  html<-read_html(url[i])
  body<-html_node(html,'#article_body')%>%
    html_text()
  article_body<-c(article_body,body)
}

## 키워드 : 커피전문점
remdr$navigate("https://news.joins.com/Search/JoongangNews?StartSearchDate=2020.04.01&EndSearchDate=2020.04.30&Keyword=%EC%BB%A4%ED%94%BC%EC%A0%84%EB%AC%B8%EC%A0%90&SortType=Accuracy&SearchCategoryType=JoongangNews&PeriodType=DirectInput&ScopeType=All&ServiceCode=&SourceGroupType=&ReporterCode=&ImageType=All&JplusType=All&BlogType=All&ImageSearchType=Image&MatchKeyword=&IncludeKeyword=&ExcluedeKeyword=")
source<-remdr$getPageSource()[[1]]
html<-read_html(source)
url<-c()
for (i in 1:5){
  url<-c(url, 
         html_nodes(html, ".headline ")%>%
           html_nodes('a') %>%
           html_attr('href'))
}
for (i in 1:length(url)){
  html<-read_html(url[i])
  body<-html_node(html,'#article_body')%>%
    html_text()
  article_body<-c(article_body,body)
}


## 키워드 : 주점
remdr$navigate("https://news.joins.com/Search/JoongangNews?StartSearchDate=2020.04.01&EndSearchDate=2020.04.30&Keyword=%EC%A3%BC%EC%A0%90&SortType=Accuracy&SearchCategoryType=JoongangNews&PeriodType=DirectInput&ScopeType=All&ServiceCode=&SourceGroupType=&ReporterCode=&ImageType=All&JplusType=All&BlogType=All&ImageSearchType=Image&MatchKeyword=&IncludeKeyword=&ExcluedeKeyword=")
source<-remdr$getPageSource()[[1]]
html<-read_html(source)
url<-c()
for (i in 1:5){
  url<-c(url, 
         html_nodes(html, ".headline ")%>%
           html_nodes('a') %>%
           html_attr('href'))
}
for (i in 1:length(url)){
  html<-read_html(url[i])
  body<-html_node(html,'#article_body')%>%
    html_text()
  article_body<-c(article_body,body)
}
write(article_body, "C:/data/food202004.txt")


## 요식업소 202005
## 키워드 : 요식업소
remdr<- remoteDriver(remoteServerAddr="localhost", port=4445L,browserName="chrome")
remdr$open()
remdr$navigate("https://news.joins.com/Search/JoongangNews?StartSearchDate=2020.05.01&EndSearchDate=2020.05.31&Keyword=%EC%9A%94%EC%8B%9D%EC%97%85&SortType=Accuracy&SearchCategoryType=JoongangNews&PeriodType=DirectInput&ScopeType=All&ServiceCode=&SourceGroupType=&ReporterCode=&ImageType=All&JplusType=All&BlogType=All&ImageSearchType=Image&MatchKeyword=&IncludeKeyword=&ExcluedeKeyword=")
source<-remdr$getPageSource()[[1]]
html<-read_html(source)
url<-c()
for (i in 1:5){
  url<-c(url, 
         html_nodes(html, ".headline ")%>%
           html_nodes('a') %>%
           html_attr('href'))
}
article_body<-NULL
for (i in 1:length(url)){
  html<-read_html(url[i])
  body<-html_node(html,'#article_body')%>%
    html_text()
  article_body<-c(article_body,body)
}

## 키워드 : 커피전문점
remdr$navigate("https://news.joins.com/Search/JoongangNews?StartSearchDate=2020.05.01&EndSearchDate=2020.05.31&Keyword=%EC%BB%A4%ED%94%BC%EC%A0%84%EB%AC%B8%EC%A0%90&SortType=Accuracy&SearchCategoryType=JoongangNews&PeriodType=DirectInput&ScopeType=All&ServiceCode=&SourceGroupType=&ReporterCode=&ImageType=All&JplusType=All&BlogType=All&ImageSearchType=Image&MatchKeyword=&IncludeKeyword=&ExcluedeKeyword=")
source<-remdr$getPageSource()[[1]]
html<-read_html(source)
url<-c()
for (i in 1:5){
  url<-c(url, 
         html_nodes(html, ".headline ")%>%
           html_nodes('a') %>%
           html_attr('href'))
}
for (i in 1:length(url)){
  html<-read_html(url[i])
  body<-html_node(html,'#article_body')%>%
    html_text()
  article_body<-c(article_body,body)
}

## 키워드 : 주점
remdr$navigate("https://news.joins.com/Search/JoongangNews?StartSearchDate=2020.05.01&EndSearchDate=2020.05.31&Keyword=%EC%A3%BC%EC%A0%90&SortType=Accuracy&SearchCategoryType=JoongangNews&PeriodType=DirectInput&ScopeType=All&ServiceCode=&SourceGroupType=&ReporterCode=&ImageType=All&JplusType=All&BlogType=All&ImageSearchType=Image&MatchKeyword=&IncludeKeyword=&ExcluedeKeyword=")
source<-remdr$getPageSource()[[1]]
html<-read_html(source)
url<-c()
for (i in 1:5){
  url<-c(url, 
         html_nodes(html, ".headline ")%>%
           html_nodes('a') %>%
           html_attr('href'))
}
for (i in 1:length(url)){
  html<-read_html(url[i])
  body<-html_node(html,'#article_body')%>%
    html_text()
  article_body<-c(article_body,body)
}
write(article_body, "C:/data/food202005.txt")
'''

# 파이썬에서 R에서 만든 기사 모음 파일 읽고 토큰화 ======================================================

from selenium import webdriver
from urllib.parse import quote
import csv
from urllib.request import urlopen
from konlpy.tag import Okt 
okt=Okt()    

# 201902 식품 
file=open("C:/data/food201902.txt","r")
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

# 201903 식품 
file=open("C:/data/food201903.txt","r")
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

# 201904 식품 
file=open("C:/data/food201904.txt","r")
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

# 201905 식품 
file=open("C:/data/food201905.txt","r")
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

# 202002 식품 
file=open("C:/data/food202002.txt","r")
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

# 202003 식품
file=open("C:/data/food202003.txt","r")
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

# 202004 식품 
file=open("C:/data/food202004.txt","r")
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

# 202005 식품 
file=open("C:/data/food202005.txt","r")
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

# 1-2-6) 보건위생 스크래핑과 토큰화             

quote('보건위생')
quote('마스크')

# RSTUDIO에서 Rselenium 자동화로 기사 스크래핑하고 파일로 저장  =========================================

'''
## 보건위생 201901
## 키워드 : 보건위생
remdr<- remoteDriver(remoteServerAddr="localhost", port=4445L,browserName="chrome")
remdr$open()
remdr$navigate("https://news.joins.com/Search/JoongangNews?StartSearchDate=2019.01.01&EndSearchDate=2019.01.31&Keyword=%EB%B3%B4%EA%B1%B4%EC%9C%84%EC%83%9D&SortType=Accuracy&SearchCategoryType=JoongangNews&PeriodType=DirectInput&ScopeType=All&ServiceCode=&SourceGroupType=&ReporterCode=&ImageType=All&JplusType=All&BlogType=All&ImageSearchType=Image&MatchKeyword=&IncludeKeyword=&ExcluedeKeyword=")
source<-remdr$getPageSource()[[1]]
html<-read_html(source)
url<-c()
for (i in 1:5){
  url<-c(url, 
         html_nodes(html, ".headline ")%>%
           html_nodes('a') %>%
           html_attr('href'))
}
article_body<-NULL
for (i in 1:length(url)){
  html<-read_html(url[i])
  body<-html_node(html,'#article_body')%>%
    html_text()
  article_body<-c(article_body,body)
}

## 키워드 : 마스크
remdr$navigate("https://news.joins.com/Search/JoongangNews?StartSearchDate=2019.01.01&EndSearchDate=2019.01.31&Keyword=%EB%A7%88%EC%8A%A4%ED%81%AC&SortType=Accuracy&SearchCategoryType=JoongangNews&PeriodType=DirectInput&ScopeType=All&ServiceCode=&SourceGroupType=&ReporterCode=&ImageType=All&JplusType=All&BlogType=All&ImageSearchType=Image&MatchKeyword=&IncludeKeyword=&ExcluedeKeyword=")
source<-remdr$getPageSource()[[1]]
html<-read_html(source)
url<-c()
for (i in 1:5){
  url<-c(url, 
         html_nodes(html, ".headline ")%>%
           html_nodes('a') %>%
           html_attr('href'))
}
for (i in 1:length(url)){
  html<-read_html(url[i])
  body<-html_node(html,'#article_body')%>%
    html_text()
  article_body<-c(article_body,body)
}
write(article_body, "C:/data/health201901.txt")


## 보건위생 201902
## 키워드 : 보건위생
remdr<- remoteDriver(remoteServerAddr="localhost", port=4445L,browserName="chrome")
remdr$open()
remdr$navigate("https://news.joins.com/Search/JoongangNews?Keyword=%EB%B3%B4%EA%B1%B4%EC%9C%84%EC%83%9D&StartSearchDate=02%2F01%2F2019%2000%3A00%3A00&EndSearchDate=02%2F28%2F2019%2000%3A00%3A00&SortType=Accuracy&SearchCategoryType=JoongangNews&PeriodType=DirectInput&ScopeType=All&ImageType=All&JplusType=All&BlogType=All&ImageSearchType=Image&TotalCount=0&StartCount=0&IsChosung=False&IssueCategoryType=All&IsDuplicate=True&Page=1&PageSize=10&IsNeedTotalCount=True")
source<-remdr$getPageSource()[[1]]
html<-read_html(source)
url<-c()
for (i in 1:5){
  url<-c(url, 
         html_nodes(html, ".headline ")%>%
           html_nodes('a') %>%
           html_attr('href'))
}
article_body<-NULL
for (i in 1:length(url)){
  html<-read_html(url[i])
  body<-html_node(html,'#article_body')%>%
    html_text()
  article_body<-c(article_body,body)
}

## 키워드 : 마스크
remdr$navigate("https://news.joins.com/Search/JoongangNews?StartSearchDate=2019.02.01&EndSearchDate=2019.02.28&Keyword=%EB%A7%88%EC%8A%A4%ED%81%AC&SortType=Accuracy&SearchCategoryType=JoongangNews&PeriodType=DirectInput&ScopeType=All&ServiceCode=&SourceGroupType=&ReporterCode=&ImageType=All&JplusType=All&BlogType=All&ImageSearchType=Image&MatchKeyword=&IncludeKeyword=&ExcluedeKeyword=")
source<-remdr$getPageSource()[[1]]
html<-read_html(source)
url<-c()
for (i in 1:5){
  url<-c(url, 
         html_nodes(html, ".headline ")%>%
           html_nodes('a') %>%
           html_attr('href'))
}
for (i in 1:length(url)){
  html<-read_html(url[i])
  body<-html_node(html,'#article_body')%>%
    html_text()
  article_body<-c(article_body,body)
}
write(article_body, "C:/data/health201902.txt")


## 보건위생 201903 
## 키워드 : 보건위생
remdr<- remoteDriver(remoteServerAddr="localhost", port=4445L,browserName="chrome")
remdr$open()
remdr$navigate("https://news.joins.com/Search/JoongangNews?Keyword=%EB%B3%B4%EA%B1%B4%EC%9C%84%EC%83%9D&StartSearchDate=03%2F01%2F2019%2000%3A00%3A00&EndSearchDate=03%2F31%2F2019%2000%3A00%3A00&SortType=Accuracy&SearchCategoryType=JoongangNews&PeriodType=DirectInput&ScopeType=All&ImageType=All&JplusType=All&BlogType=All&ImageSearchType=Image&TotalCount=0&StartCount=0&IsChosung=False&IssueCategoryType=All&IsDuplicate=True&Page=1&PageSize=10&IsNeedTotalCount=True")
source<-remdr$getPageSource()[[1]]
html<-read_html(source)
url<-c()
for (i in 1:5){
  url<-c(url, 
         html_nodes(html, ".headline ")%>%
           html_nodes('a') %>%
           html_attr('href'))
}
article_body<-NULL
for (i in 1:length(url)){
  html<-read_html(url[i])
  body<-html_node(html,'#article_body')%>%
    html_text()
  article_body<-c(article_body,body)
}

## 키워드 : 마스크
remdr$navigate("https://news.joins.com/Search/JoongangNews?StartSearchDate=2019.03.01&EndSearchDate=2019.03.31&Keyword=%EB%A7%88%EC%8A%A4%ED%81%AC&SortType=Accuracy&SearchCategoryType=JoongangNews&PeriodType=DirectInput&ScopeType=All&ServiceCode=&SourceGroupType=&ReporterCode=&ImageType=All&JplusType=All&BlogType=All&ImageSearchType=Image&MatchKeyword=&IncludeKeyword=&ExcluedeKeyword=")
source<-remdr$getPageSource()[[1]]
html<-read_html(source)
url<-c()
for (i in 1:5){
  url<-c(url, 
         html_nodes(html, ".headline ")%>%
           html_nodes('a') %>%
           html_attr('href'))
}
for (i in 1:length(url)){
  html<-read_html(url[i])
  body<-html_node(html,'#article_body')%>%
    html_text()
  article_body<-c(article_body,body)
}
write(article_body, "C:/data/health201903.txt")


## 보건위생 201904
## 키워드 : 보건위생
remdr<- remoteDriver(remoteServerAddr="localhost", port=4445L,browserName="chrome")
remdr$open()
remdr$navigate("https://news.joins.com/Search/JoongangNews?StartSearchDate=2019.04.01&EndSearchDate=2019.04.31&Keyword=%EB%B3%B4%EA%B1%B4%EC%9C%84%EC%83%9D&SortType=Accuracy&SearchCategoryType=JoongangNews&PeriodType=DirectInput&ScopeType=All&ServiceCode=&SourceGroupType=&ReporterCode=&ImageType=All&JplusType=All&BlogType=All&ImageSearchType=Image&MatchKeyword=&IncludeKeyword=&ExcluedeKeyword=")
source<-remdr$getPageSource()[[1]]
html<-read_html(source)
url<-c()
for (i in 1:5){
  url<-c(url, 
         html_nodes(html, ".headline ")%>%
           html_nodes('a') %>%
           html_attr('href'))
}
article_body<-NULL
for (i in 1:length(url)){
  html<-read_html(url[i])
  body<-html_node(html,'#article_body')%>%
    html_text()
  article_body<-c(article_body,body)
}

## 키워드 : 마스크
remdr$navigate("https://news.joins.com/Search/JoongangNews?StartSearchDate=2019.04.01&EndSearchDate=2019.04.30&Keyword=%EB%A7%88%EC%8A%A4%ED%81%AC&SortType=Accuracy&SearchCategoryType=JoongangNews&PeriodType=DirectInput&ScopeType=All&ServiceCode=&SourceGroupType=&ReporterCode=&ImageType=All&JplusType=All&BlogType=All&ImageSearchType=Image&MatchKeyword=&IncludeKeyword=&ExcluedeKeyword=")
source<-remdr$getPageSource()[[1]]
html<-read_html(source)
url<-c()
for (i in 1:5){
  url<-c(url, 
         html_nodes(html, ".headline ")%>%
           html_nodes('a') %>%
           html_attr('href'))
}
for (i in 1:length(url)){
  html<-read_html(url[i])
  body<-html_node(html,'#article_body')%>%
    html_text()
  article_body<-c(article_body,body)
}
write(article_body, "C:/data/health201904.txt")


## 보건위생 201905 
## 키워드 : 보건위생
remdr<- remoteDriver(remoteServerAddr="localhost", port=4445L,browserName="chrome")
remdr$open()
remdr$navigate("https://news.joins.com/Search/JoongangNews?StartSearchDate=2019.05.01&EndSearchDate=2019.05.31&Keyword=%EB%B3%B4%EA%B1%B4%EC%9C%84%EC%83%9D&SortType=Accuracy&SearchCategoryType=JoongangNews&PeriodType=DirectInput&ScopeType=All&ServiceCode=&SourceGroupType=&ReporterCode=&ImageType=All&JplusType=All&BlogType=All&ImageSearchType=Image&MatchKeyword=&IncludeKeyword=&ExcluedeKeyword=")
source<-remdr$getPageSource()[[1]]
html<-read_html(source)
url<-c()
for (i in 1:5){
  url<-c(url, 
         html_nodes(html, ".headline ")%>%
           html_nodes('a') %>%
           html_attr('href'))
}
article_body<-NULL
for (i in 1:length(url)){
  html<-read_html(url[i])
  body<-html_node(html,'#article_body')%>%
    html_text()
  article_body<-c(article_body,body)
}

## 키워드 : 마스크
remdr$navigate("https://news.joins.com/Search/JoongangNews?StartSearchDate=2019.05.01&EndSearchDate=2019.05.31&Keyword=%EB%A7%88%EC%8A%A4%ED%81%AC&SortType=Accuracy&SearchCategoryType=JoongangNews&PeriodType=DirectInput&ScopeType=All&ServiceCode=&SourceGroupType=&ReporterCode=&ImageType=All&JplusType=All&BlogType=All&ImageSearchType=Image&MatchKeyword=&IncludeKeyword=&ExcluedeKeyword=")
source<-remdr$getPageSource()[[1]]
html<-read_html(source)
url<-c()
for (i in 1:5){
  url<-c(url, 
         html_nodes(html, ".headline ")%>%
           html_nodes('a') %>%
           html_attr('href'))
}
for (i in 1:length(url)){
  html<-read_html(url[i])
  body<-html_node(html,'#article_body')%>%
    html_text()
  article_body<-c(article_body,body)
}
write(article_body, "C:/data/health201905.txt")


## 보건위생 202001
## 키워드 : 보건위생
remdr<- remoteDriver(remoteServerAddr="localhost", port=4445L,browserName="chrome")
remdr$open()
remdr$navigate("https://news.joins.com/Search/JoongangNews?StartSearchDate=2020.01.01&EndSearchDate=2020.01.31&Keyword=%EB%B3%B4%EA%B1%B4%EC%9C%84%EC%83%9D&SortType=Accuracy&SearchCategoryType=JoongangNews&PeriodType=DirectInput&ScopeType=All&ServiceCode=&SourceGroupType=&ReporterCode=&ImageType=All&JplusType=All&BlogType=All&ImageSearchType=Image&MatchKeyword=&IncludeKeyword=&ExcluedeKeyword=")
source<-remdr$getPageSource()[[1]]
html<-read_html(source)
url<-c()
for (i in 1:5){
  url<-c(url, 
         html_nodes(html, ".headline ")%>%
           html_nodes('a') %>%
           html_attr('href'))
}
article_body<-NULL
for (i in 1:length(url)){
  html<-read_html(url[i])
  body<-html_node(html,'#article_body')%>%
    html_text()
  article_body<-c(article_body,body)
}

## 키워드 : 마스크
remdr$navigate("https://news.joins.com/Search/JoongangNews?StartSearchDate=2020.01.01&EndSearchDate=2020.01.31&Keyword=%EB%A7%88%EC%8A%A4%ED%81%AC&SortType=Accuracy&SearchCategoryType=JoongangNews&PeriodType=DirectInput&ScopeType=All&ServiceCode=&SourceGroupType=&ReporterCode=&ImageType=All&JplusType=All&BlogType=All&ImageSearchType=Image&MatchKeyword=&IncludeKeyword=&ExcluedeKeyword=")
source<-remdr$getPageSource()[[1]]
html<-read_html(source)
url<-c()
for (i in 1:5){
  url<-c(url, 
         html_nodes(html, ".headline ")%>%
           html_nodes('a') %>%
           html_attr('href'))
}
for (i in 1:length(url)){
  html<-read_html(url[i])
  body<-html_node(html,'#article_body')%>%
    html_text()
  article_body<-c(article_body,body)
}
write(article_body, "C:/data/health202001.txt")


## 보건위생 202002 
## 키워드 : 보건위생
remdr<- remoteDriver(remoteServerAddr="localhost", port=4445L,browserName="chrome")
remdr$open()
remdr$navigate("https://news.joins.com/Search/JoongangNews?StartSearchDate=2020.02.01&EndSearchDate=2020.02.28&Keyword=%EB%B3%B4%EA%B1%B4%EC%9C%84%EC%83%9D&SortType=Accuracy&SearchCategoryType=JoongangNews&PeriodType=DirectInput&ScopeType=All&ServiceCode=&SourceGroupType=&ReporterCode=&ImageType=All&JplusType=All&BlogType=All&ImageSearchType=Image&MatchKeyword=&IncludeKeyword=&ExcluedeKeyword=")
source<-remdr$getPageSource()[[1]]
html<-read_html(source)
url<-c()
for (i in 1:5){
  url<-c(url, 
         html_nodes(html, ".headline ")%>%
           html_nodes('a') %>%
           html_attr('href'))
}
article_body<-NULL
for (i in 1:length(url)){
  html<-read_html(url[i])
  body<-html_node(html,'#article_body')%>%
    html_text()
  article_body<-c(article_body,body)
}

## 키워드 : 마스크
remdr$navigate("https://news.joins.com/Search/JoongangNews?StartSearchDate=2020.02.01&EndSearchDate=2020.02.28&Keyword=%EB%A7%88%EC%8A%A4%ED%81%AC&SortType=Accuracy&SearchCategoryType=JoongangNews&PeriodType=DirectInput&ScopeType=All&ServiceCode=&SourceGroupType=&ReporterCode=&ImageType=All&JplusType=All&BlogType=All&ImageSearchType=Image&MatchKeyword=&IncludeKeyword=&ExcluedeKeyword=")
source<-remdr$getPageSource()[[1]]
html<-read_html(source)
url<-c()
for (i in 1:5){
  url<-c(url, 
         html_nodes(html, ".headline ")%>%
           html_nodes('a') %>%
           html_attr('href'))
}
for (i in 1:length(url)){
  html<-read_html(url[i])
  body<-html_node(html,'#article_body')%>%
    html_text()
  article_body<-c(article_body,body)
}
write(article_body, "C:/data/health202002.txt")


## 보건위생 202003
## 키워드 : 보건위생
remdr<- remoteDriver(remoteServerAddr="localhost", port=4445L,browserName="chrome")
remdr$open()
remdr$navigate("https://news.joins.com/Search/JoongangNews?StartSearchDate=2020.03.01&EndSearchDate=2020.03.30&Keyword=%EB%B3%B4%EA%B1%B4%EC%9C%84%EC%83%9D&SortType=Accuracy&SearchCategoryType=JoongangNews&PeriodType=DirectInput&ScopeType=All&ServiceCode=&SourceGroupType=&ReporterCode=&ImageType=All&JplusType=All&BlogType=All&ImageSearchType=Image&MatchKeyword=&IncludeKeyword=&ExcluedeKeyword=")
source<-remdr$getPageSource()[[1]]
html<-read_html(source)
url<-c()
for (i in 1:5){
  url<-c(url, 
         html_nodes(html, ".headline ")%>%
           html_nodes('a') %>%
           html_attr('href'))
}
article_body<-NULL
for (i in 1:length(url)){
  html<-read_html(url[i])
  body<-html_node(html,'#article_body')%>%
    html_text()
  article_body<-c(article_body,body)
}

## 키워드 : 마스크
remdr$navigate("https://news.joins.com/Search/JoongangNews?StartSearchDate=2020.03.01&EndSearchDate=2020.03.31&Keyword=%EB%A7%88%EC%8A%A4%ED%81%AC&SortType=Accuracy&SearchCategoryType=JoongangNews&PeriodType=DirectInput&ScopeType=All&ServiceCode=&SourceGroupType=&ReporterCode=&ImageType=All&JplusType=All&BlogType=All&ImageSearchType=Image&MatchKeyword=&IncludeKeyword=&ExcluedeKeyword=")
source<-remdr$getPageSource()[[1]]
html<-read_html(source)
url<-c()
for (i in 1:5){
  url<-c(url, 
         html_nodes(html, ".headline ")%>%
           html_nodes('a') %>%
           html_attr('href'))
}
for (i in 1:length(url)){
  html<-read_html(url[i])
  body<-html_node(html,'#article_body')%>%
    html_text()
  article_body<-c(article_body,body)
}
write(article_body, "C:/data/health202003.txt")


## 보건위생 202004 
## 키워드 : 보건위생
remdr<- remoteDriver(remoteServerAddr="localhost", port=4445L,browserName="chrome")
remdr$open()
remdr$navigate("https://news.joins.com/Search/JoongangNews?StartSearchDate=2020.04.01&EndSearchDate=2020.04.31&Keyword=%EB%B3%B4%EA%B1%B4%EC%9C%84%EC%83%9D&SortType=Accuracy&SearchCategoryType=JoongangNews&PeriodType=DirectInput&ScopeType=All&ServiceCode=&SourceGroupType=&ReporterCode=&ImageType=All&JplusType=All&BlogType=All&ImageSearchType=Image&MatchKeyword=&IncludeKeyword=&ExcluedeKeyword=")
source<-remdr$getPageSource()[[1]]
html<-read_html(source)
url<-c()
for (i in 1:5){
  url<-c(url, 
         html_nodes(html, ".headline ")%>%
           html_nodes('a') %>%
           html_attr('href'))
}
article_body<-NULL
for (i in 1:length(url)){
  html<-read_html(url[i])
  body<-html_node(html,'#article_body')%>%
    html_text()
  article_body<-c(article_body,body)
}

## 키워드 : 마스크
remdr$navigate("https://news.joins.com/Search/JoongangNews?StartSearchDate=2020.04.01&EndSearchDate=2020.04.30&Keyword=%EB%A7%88%EC%8A%A4%ED%81%AC&SortType=Accuracy&SearchCategoryType=JoongangNews&PeriodType=DirectInput&ScopeType=All&ServiceCode=&SourceGroupType=&ReporterCode=&ImageType=All&JplusType=All&BlogType=All&ImageSearchType=Image&MatchKeyword=&IncludeKeyword=&ExcluedeKeyword=")
source<-remdr$getPageSource()[[1]]
html<-read_html(source)
url<-c()
for (i in 1:5){
  url<-c(url, 
         html_nodes(html, ".headline ")%>%
           html_nodes('a') %>%
           html_attr('href'))
}
for (i in 1:length(url)){
  html<-read_html(url[i])
  body<-html_node(html,'#article_body')%>%
    html_text()
  article_body<-c(article_body,body)
}
write(article_body, "C:/data/health202004.txt")


## 보건위생 202005 
## 키워드 : 보건위생
remdr<- remoteDriver(remoteServerAddr="localhost", port=4445L,browserName="chrome")
remdr$open()
remdr$navigate("https://news.joins.com/Search/JoongangNews?StartSearchDate=2020.05.01&EndSearchDate=2020.05.31&Keyword=%EB%B3%B4%EA%B1%B4%EC%9C%84%EC%83%9D&SortType=Accuracy&SearchCategoryType=JoongangNews&PeriodType=DirectInput&ScopeType=All&ServiceCode=&SourceGroupType=&ReporterCode=&ImageType=All&JplusType=All&BlogType=All&ImageSearchType=Image&MatchKeyword=&IncludeKeyword=&ExcluedeKeyword=")
source<-remdr$getPageSource()[[1]]
html<-read_html(source)
url<-c()
for (i in 1:5){
  url<-c(url, 
         html_nodes(html, ".headline ")%>%
           html_nodes('a') %>%
           html_attr('href'))
}
article_body<-NULL
for (i in 1:length(url)){
  html<-read_html(url[i])
  body<-html_node(html,'#article_body')%>%
    html_text()
  article_body<-c(article_body,body)
}

## 키워드 : 마스크
remdr$navigate("https://news.joins.com/Search/JoongangNews?StartSearchDate=2020.05.01&EndSearchDate=2020.05.31&Keyword=%EB%A7%88%EC%8A%A4%ED%81%AC&SortType=Accuracy&SearchCategoryType=JoongangNews&PeriodType=DirectInput&ScopeType=All&ServiceCode=&SourceGroupType=&ReporterCode=&ImageType=All&JplusType=All&BlogType=All&ImageSearchType=Image&MatchKeyword=&IncludeKeyword=&ExcluedeKeyword=")
source<-remdr$getPageSource()[[1]]
html<-read_html(source)
url<-c()
for (i in 1:5){
  url<-c(url, 
         html_nodes(html, ".headline ")%>%
           html_nodes('a') %>%
           html_attr('href'))
}
for (i in 1:length(url)){
  html<-read_html(url[i])
  body<-html_node(html,'#article_body')%>%
    html_text()
  article_body<-c(article_body,body)
}
write(article_body, "C:/data/health202005.txt")
'''

# 201902 보건위생
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

# 201903 보건위생 
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

# 201904 보건위생 
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

# 201905 보건위생 
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

# 202002 보건위생 
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

# 202003 보건위생 
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

# 202004 보건위생 
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

# 202005 보건위생 
file=open("C:/data/health202005.csv","r")
data=file.read()
print(data)
data=data.replace('\n',' ')
data=data.replace('\t',' ')
data=data.replace('<U+00A0>',' ')
data=data.split('.')
file.close()
# 토큰화
health202005=[]
for i in data:
    health202005.append(okt.morphs(i))
print(health202005)


# 2. 감성사전 구축 적용

# library
from gensim.models import Word2Vec
from sklearn.decomposition import PCA
import pandas as pd
from pandas import *
import numpy as np

'''
# variable 
health_2020_02 ~ health_2020_05
health_2019_02 ~ health_2019_05
food_2020_02 ~ food_2020_05
food_2019_02 ~ food_2019_05
cul_2020_02 ~ cul_2020_05
cul_2019_02 ~ cul_2019_05
medi_2020_02 ~ medi_2020_05
medi_2019_02 ~ medi_2019_05
leisure_2020_02 ~ leisure_2020_05
leisure_2019_02 ~ leisure_2019_05
stay_2020_02 ~ stay_2020_05
stay_2019_02 ~ stay_2019_05
'''


# class word
class word():
    def __init__(self):
        self.word = []

    def input_word(self, arg):
        self.arg = arg
        self.word.append(self.arg)
        return self.word


if __name__ == "__main__":
    test = word()
    test1 = test.input_word("가")
    test1 = test.input_word("나")
    test1 = test.input_word("다")
    print(test1)
'''
#health 2020
result: health_2020_02  ~  health_2020_05
'''
# from health202002
embedding_mode = Word2Vec(health202002, size=100, window=2,
                          min_count=1, workers=4, iter=100,
                          sg=1)
# 유사도
print(embedding_mode.wv.most_similar(positive=['건강'], topn=100))
# 건강 : 위협(-) /중대한(-)/ 헛걸음(-)/ 당혹스럽긴(-) / 범죄 (-) / 성급히(-) / 지키기 (+)

health = word()
health_20_02 = health.input_word("위협")
health_20_02 = health.input_word("중대한")
health_20_02 = health.input_word("헛걸음")
health_20_02 = health.input_word("당혹스럽긴")
health_20_02 = health.input_word("범죄")
health_20_02 = health.input_word("성급히")
health_20_02 = health.input_word("지키기")

health_2020_02 = pd.DataFrame({'keyword': ['건강' for i in range(0, len(health_20_02))], 'target': health_20_02,
                               'vector': [float(embedding_mode.wv.similarity(w1='건강', w2=i)) for i in health_20_02]})

health_2020_02['postivie'] = ['-', '-', '-', '-', '-', '-', '+']
print(health_2020_02)

# from health202003
embedding_mode = Word2Vec(health202003, size=100, window=2,
                          min_count=1, workers=4, iter=50,
                          sg=1)
# 유사도
print(embedding_mode.wv.most_similar(positive=['건강'], topn=100))
# 염려(-)/ 회복(+)/ 위생(중립)/공중(중립)/ 밀봉(중립) /공중보건(중립) /분쟁(-)
# (주석참고) 염려(-)/ 회복(+)/ 위생(-)/공중(-)/ 밀봉(-) /공중보건(-) /분쟁(-)
health = word()
health_20_03 = health.input_word("염려")
health_20_03 = health.input_word("회복")
health_20_03 = health.input_word("위생")
health_20_03 = health.input_word("공중")
health_20_03 = health.input_word("밀봉")
health_20_03 = health.input_word("공중보건")
health_20_03 = health.input_word("분쟁")
health_2020_03 = pd.DataFrame({'keyword': ['건강' for i in range(0, len(health_20_03))], 'target': health_20_03,
                               'vector': [float(embedding_mode.wv.similarity(w1='건강', w2=i)) for i in health_20_03]})
health_2020_03['postivie'] = ['-', '+', '-', '-', '-', '-', '-']
print(health_2020_03)
'''
# 중립단어 : 위생, 공중, 밀봉, 공중보건
print(embedding_mode.wv.most_similar(positive=['위생'],topn=100)) # 책임지는(-), 염려(-), 회복(+)
print(embedding_mode.wv.most_similar(positive=['공중'],topn=100)) # 책임지는(-), 위생(중립)
print(embedding_mode.wv.most_similar(positive=['밀봉'],topn=100)) # 속였다(-), 구속(-), KF(-), 염려(-)
print(embedding_mode.wv.most_similar(positive=['공중보건'],topn=100)) #책임지는 (-), 통제(-)
#result : 중립단어 모두 -
'''

# from health202004
embedding_mode = Word2Vec(health202004, size=100, window=2,
                          min_count=1, workers=4, iter=100,
                          sg=1)
print(embedding_mode.wv.most_similar(positive=['건강'], topn=100))
# 생명(+)/ 걱정(-)/ 스테이(-) / 과로(-) / 불편(-) / 힘들(-) / 줄일(-) / 대가(-) / 호소(-)
health = word()
health_20_04 = health.input_word("생명")
health_20_04 = health.input_word("걱정")
health_20_04 = health.input_word("스테이")
health_20_04 = health.input_word("과로")
health_20_04 = health.input_word("불편")
health_20_04 = health.input_word("힘들")
health_20_04 = health.input_word("줄일")
health_20_04 = health.input_word("대가")
health_20_04 = health.input_word("호소")
health_2020_04 = pd.DataFrame({'keyword': ['건강' for i in range(0, len(health_20_04))], 'target': health_20_04,
                               'vector': [float(embedding_mode.wv.similarity(w1='건강', w2=i)) for i in health_20_04]})

health_2020_04['postivie'] = ['+', '-', '-', '-', '-', '-', '-', '-', '-']
print(health_2020_04)

# from health202005
embedding_mode = Word2Vec(health202005, size=100, window=2,
                          min_count=1, workers=4, iter=100,
                          sg=1)
print(embedding_mode.wv.most_similar(positive=['건강'], topn=100))
# 생명(+)/ 신선(+)/ 염려(-)/ 과로(-) /무리한(-)
health = word()
health_20_05 = health.input_word("생명")
health_20_05 = health.input_word("신선")
health_20_05 = health.input_word("염려")
health_20_05 = health.input_word("과로")
health_20_05 = health.input_word("무리한")
health_2020_05 = pd.DataFrame({'keyword': ['건강' for i in range(0, len(health_20_05))], 'target': health_20_05,
                               'vector': [float(embedding_mode.wv.similarity(w1='건강', w2=i)) for i in health_20_05]})
health_2020_05['postivie'] = ['+', '+', '-', '-', '-']
print(health_2020_05)

'''
#health 2019
result: health_2019_02  ~  health_2019_05
'''

# from health201902
embedding_mode = Word2Vec(health201902, size=100, window=2,
                          min_count=1, workers=4, iter=100,
                          sg=1)
print(embedding_mode.wv.most_similar(positive=['건강'], topn=100))
# 조심해야(-)/위협(-)/즐기는(+)/주의(-)/해외여행(+)/다행히(+)/성실하게(+)
health = word()
health_19_02 = health.input_word("조심해야")
health_19_02 = health.input_word("위협")
health_19_02 = health.input_word("즐기는")
health_19_02 = health.input_word("주의")
health_19_02 = health.input_word("해외여행")
health_19_02 = health.input_word("다행히")
health_19_02 = health.input_word("성실하게")

health_2019_02 = pd.DataFrame({'keyword': ['건강' for i in range(0, len(health_19_02))], 'target': health_19_02,
                               'vector': [float(embedding_mode.wv.similarity(w1='건강', w2=i)) for i in health_19_02]})
health_2019_02['postivie'] = ['-', '-', '+', '-', '+', '+', '+']
print(health_2019_02)

# from health201903
embedding_mode = Word2Vec(health201903, size=100, window=2,
                          min_count=1, workers=4, iter=100,
                          sg=1)
print(embedding_mode.wv.most_similar(positive=['건강'], topn=100))
# 안전한지(-)/비싸지만(-)/힘들어져(-)/격차(-)/해롭다(-)/지킬(+)/Healthiest(+)
health = word()
health_19_03 = health.input_word("안전한지")
health_19_03 = health.input_word("비싸지만")
health_19_03 = health.input_word("힘들어져")
health_19_03 = health.input_word("격차")
health_19_03 = health.input_word("해롭다")
health_19_03 = health.input_word("지킬")
health_19_03 = health.input_word("Healthiest")

health_2019_03 = pd.DataFrame({'keyword': ['건강' for i in range(0, len(health_19_03))], 'target': health_19_03,
                               'vector': [float(embedding_mode.wv.similarity(w1='건강', w2=i)) for i in health_19_03]})
health_2019_03['postivie'] = ['-', '-', '-', '-', '-', '+', '+']
print(health_2019_03)

# from health201904
embedding_mode = Word2Vec(health201904, size=100, window=2,
                          min_count=1, workers=4, iter=100,
                          sg=1)
print(embedding_mode.wv.most_similar(positive=['건강'], topn=100))
# 호흡기(-)/위협(-)/생명(+)/과로(-)/침투(-)/좋다(+)
health = word()
health_19_04 = health.input_word("호흡기")
health_19_04 = health.input_word("위협")
health_19_04 = health.input_word("생명")
health_19_04 = health.input_word("과로")
health_19_04 = health.input_word("침투")
health_19_04 = health.input_word("좋다")
health_2019_04 = pd.DataFrame({'keyword': ['건강' for i in range(0, len(health_19_04))], 'target': health_19_04,
                               'vector': [float(embedding_mode.wv.similarity(w1='건강', w2=i)) for i in health_19_04]})
health_2019_04['postivie'] = ['-', '-', '+', '-', '-', '+']
print(health_2019_04)

# from health201905
embedding_mode = Word2Vec(health201905, size=100, window=2,
                          min_count=1, workers=4, iter=100,
                          sg=1)
print(embedding_mode.wv.most_similar(positive=['건강'], topn=100))
# 지켜(+)/복지(+)/웰빙(+)/위협(-)/좋지(+)/진흥(+)/따뜻한(+)/깨끗한(+)
health = word()
health_19_05 = health.input_word("지켜")
health_19_05 = health.input_word("복지")
health_19_05 = health.input_word("웰빙")
health_19_05 = health.input_word("위협")
health_19_05 = health.input_word("좋지")
health_19_05 = health.input_word("진흥")
health_19_05 = health.input_word("따뜻한")
health_19_05 = health.input_word("깨끗한")

health_2019_05 = pd.DataFrame({'keyword': ['건강' for i in range(0, len(health_19_05))], 'target': health_19_05,
                               'vector': [float(embedding_mode.wv.similarity(w1='건강', w2=i)) for i in health_19_05]})
health_2019_05['postivie'] = ['+', '+', '+', '-', '+', '+', '+', '+']
print(health_2019_05)

'''
#food 2020
result: food_2020_02  ~  food_2020_05
'''

# from food202002
embedding_mode = Word2Vec(food202002, size=100, window=2,
                          min_count=1, workers=4, iter=100,
                          sg=1)
print(embedding_mode.wv.most_similar(positive=['음식'], topn=100))
# 까다로운(-)/좋다(+)/소형(-)/궁합(+)/정해진(-)/외부(-)/살아남은(+)/배달(-)/지킨(+)/성공한(+)
food = word()
food_20_02 = food.input_word("까다로운")
food_20_02 = food.input_word("좋다")
food_20_02 = food.input_word("소형")
food_20_02 = food.input_word("궁합")
food_20_02 = food.input_word("정해진")
food_20_02 = food.input_word("외부")
food_20_02 = food.input_word("살아남은")
food_20_02 = food.input_word("배달")
food_20_02 = food.input_word("지킨")
food_20_02 = food.input_word("성공한")
food_2020_02 = pd.DataFrame({'keyword': ['음식' for i in range(0, len(food_20_02))], 'target': food_20_02,
                             'vector': [float(embedding_mode.wv.similarity(w1='음식', w2=i)) for i in food_20_02]})
food_2020_02['positive'] = ['-', '+', '-', '+', '-', '-', '+', '-', '+', '+']
print(food_2020_02)

# from food202003
embedding_mode = Word2Vec(food202003, size=100, window=2,
                          min_count=1, workers=4, iter=100,
                          sg=1)
print(embedding_mode.wv.most_similar(positive=['음식'], topn=100))
# 빠른(+)/잃었고(-)/닫은(-)/배달(-)/관광(중립)/대유행(중립)/불확실하다(-)
# 빠른(+)/잃었고(-)/닫은(-)/배달(-)/관광(-)/대유행(-)/불확실하다(-)
'''
#중립단어 : 관광, 대유행
print(embedding_mode.wv.most_similar(positive=['관광'],topn=100)) #마비(-)/떠나(-)/열악한(-)
print(embedding_mode.wv.most_similar(positive=['대유행'],topn=100)) #잃었고(-)/억제(-)/압도(-)
'''
food = word()
food_20_03 = food.input_word("빠른")
food_20_03 = food.input_word("잃었고")
food_20_03 = food.input_word("닫은")
food_20_03 = food.input_word("배달")
food_20_03 = food.input_word("관광")
food_20_03 = food.input_word("대유행")
food_20_03 = food.input_word("불확실하다")
food_2020_03 = pd.DataFrame({'keyword': ['음식' for i in range(0, len(food_20_03))], 'target': food_20_03,
                             'vector': [float(embedding_mode.wv.similarity(w1='음식', w2=i)) for i in food_20_03]})
food_2020_03['positive'] = ['+', '-', '-', '-', '-', '-', '-']

print(food_2020_03)

# from food202004
embedding_mode = Word2Vec(food202004, size=100, window=2,
                          min_count=1, workers=4, iter=100,
                          sg=1)
print(embedding_mode.wv.most_similar(positive=['음식'], topn=100))
# 기름진(-)/피하(-)/맛있어야(+)/맛집(+)
print(embedding_mode.wv.most_similar(positive=['배달'], topn=100))
# 급증(+)/많습니다(+)/않습니다(-)/폴리프로필렌(-)/포장(-)

food = word()
food_20_04 = food.input_word("기름진")
food_20_04 = food.input_word("피하")
food_20_04 = food.input_word("맛있어야")
food_20_04 = food.input_word("맛집")
food_2020_04 = pd.DataFrame({'keyword': ['음식' for i in range(0, len(food_20_04))], 'target': food_20_04,
                             'vector': [float(embedding_mode.wv.similarity(w1='음식', w2=i)) for i in food_20_04]})
food = word()
food_20_04_1 = food.input_word("급증")
food_20_04_1 = food.input_word("많습니다")
food_20_04_1 = food.input_word("않습니다")
food_20_04_1 = food.input_word("폴리프로필렌")
food_20_04_1 = food.input_word("포장")

food_2020_04 = food_2020_04.append(
    pd.DataFrame({'keyword': ['배달' for i in range(0, len(food_20_04_1))], 'target': food_20_04_1,
                  'vector': [float(embedding_mode.wv.similarity(w1='음식', w2=i)) for i in food_20_04_1]}))
food_2020_04 = food_2020_04.reset_index(drop=True)
food_2020_04['positive'] = ['-', '-', '+', '+', '+', '+', '-', '-', '-']
print(food_2020_04)

# from food202005
embedding_mode = Word2Vec(food202005, size=100, window=2,
                          min_count=1, workers=4, iter=100,
                          sg=1)
print(embedding_mode.wv.most_similar(positive=['음식'], topn=100))
# 비해(-)/신선한(+)/Personal(-)/장벽(-)/즐기기(+)/일상생활(+)
food = word()
food_20_05 = food.input_word("비해")
food_20_05 = food.input_word("신선한")
food_20_05 = food.input_word("Personal")
food_20_05 = food.input_word("장벽")
food_20_05 = food.input_word("즐기기")
food_20_05 = food.input_word("일상생활")
food_2020_05 = pd.DataFrame({'keyword': ['음식' for i in range(0, len(food_20_05))], 'target': food_20_05,
                             'vector': [float(embedding_mode.wv.similarity(w1='음식', w2=i)) for i in food_20_05]})
food_2020_05['positive'] = ['-', '+', '-', '-', '+', '+']

'''
#food 2019
result: food_2019_02  ~  food_2019_05
'''

# from food201902
embedding_mode = Word2Vec(food201902, size=100, window=2,
                          min_count=1, workers=4, iter=100,
                          sg=1)
print(embedding_mode.wv.most_similar(positive=['음식'], topn=100))
# 기회(+)/배려하되(+)/전세계(+)/편하게(+)/깔끔한(+)/좋고(+)
food = word()
food_19_02 = food.input_word("기회")
food_19_02 = food.input_word("배려하되")
food_19_02 = food.input_word("전세계")
food_19_02 = food.input_word("편하게")
food_19_02 = food.input_word("깔끔한")
food_19_02 = food.input_word("좋고")
food_2019_02 = pd.DataFrame({'keyword': ['음식' for i in range(0, len(food_19_02))], 'target': food_19_02,
                             'vector': [float(embedding_mode.wv.similarity(w1='음식', w2=i)) for i in food_19_02]})
food_2019_02['positive'] = ['+', '+', '+', '+', '+', '+']
print(food_2019_02)

# from food201903
embedding_mode = Word2Vec(food201903, size=100, window=2,
                          min_count=1, workers=4, iter=100,
                          sg=1)
print(embedding_mode.wv.most_similar(positive=['음식'], topn=100))
# 재미있고(+)/흥(+)/가볍게(+)/좋아한다면(+)/춤(+)/힐링(+)
food = word()
food_19_03 = food.input_word("재미있고")
food_19_03 = food.input_word("흥")
food_19_03 = food.input_word("가볍게")
food_19_03 = food.input_word("좋아한다면")
food_19_03 = food.input_word("흥")
food_19_03 = food.input_word("힐링")
food_2019_03 = pd.DataFrame({'keyword': ['음식' for i in range(0, len(food_19_03))], 'target': food_19_03,
                             'vector': [float(embedding_mode.wv.similarity(w1='음식', w2=i)) for i in food_19_03]})
food_2019_03['positive'] = ['+', '+', '+', '+', '+', '+']
print(food_2019_03)

# from food201904
embedding_mode = Word2Vec(food201904, size=100, window=2,
                          min_count=1, workers=4, iter=100,
                          sg=1)
print(embedding_mode.wv.most_similar(positive=['음식'], topn=100))
# 세련되게(+)/나눠주고(+)/업그레이드(+)/맛있는(+)/특별하게(+)/야무진(+)/밝은(+)
food = word()
food_19_04 = food.input_word("세련되게")
food_19_04 = food.input_word("나눠주고")
food_19_04 = food.input_word("업그레이드")
food_19_04 = food.input_word("맛있는")
food_19_04 = food.input_word("특별하게")
food_19_04 = food.input_word("야무진")
food_19_04 = food.input_word("밝은")

food_2019_04 = pd.DataFrame({'keyword': ['음식' for i in range(0, len(food_19_04))], 'target': food_19_04,
                             'vector': [float(embedding_mode.wv.similarity(w1='음식', w2=i)) for i in food_19_04]})
food_2019_04['positive'] = ['+' for i in range(0, 7)]

# from food201905
embedding_mode = Word2Vec(food201905, size=100, window=2,
                          min_count=1, workers=4, iter=100,
                          sg=1)
print(embedding_mode.wv.most_similar(positive=['음식'], topn=100))
# 아니라(-)/레저(+)/않으려(-)/버텨(-)/휴식(+)/가능해지게(+)/거친(-)/제재(-)/맛있을(+)
food = word()
food_19_05 = food.input_word("아니라")
food_19_05 = food.input_word("레저")
food_19_05 = food.input_word("않으려")
food_19_05 = food.input_word("버텨")
food_19_05 = food.input_word("휴식")
food_19_05 = food.input_word("가능해지게")
food_19_05 = food.input_word("거친")
food_19_05 = food.input_word("제재")
food_19_05 = food.input_word("맛있을")
food_2019_05 = pd.DataFrame({'keyword': ['음식' for i in range(0, len(food_19_05))], 'target': food_19_05,
                             'vector': [float(embedding_mode.wv.similarity(w1='음식', w2=i)) for i in food_19_05]})
food_2019_05['positive'] = ['-', '+', '-', '-', '+', '+', '-', '-', '+']
print(food_2019_05)

'''
#culture 2020
result: cul_2020_02  ~  cul_2020_05
'''
# from cul202002
embedding_mode = Word2Vec(cul202002, size=100, window=2,
                          min_count=1, workers=4, iter=100,
                          sg=1)
print(embedding_mode.wv.most_similar(positive=['문화'], topn=100))
# 줄어들고(-)/불가능(-)/돌이켜(-)/즐기기(+)/없다고(-)/장점(+)/즐기자(+)
cul = word()
cul_20_02 = cul.input_word("줄어들고")
cul_20_02 = cul.input_word("불가능")
cul_20_02 = cul.input_word("돌이켜")
cul_20_02 = cul.input_word("즐기기")
cul_20_02 = cul.input_word("없다고")
cul_20_02 = cul.input_word("장점")
cul_20_02 = cul.input_word("즐기자")

cul_2020_02 = pd.DataFrame({'keyword': ['문화' for i in range(0, len(cul_20_02))], 'target': cul_20_02,
                            'vector': [float(embedding_mode.wv.similarity(w1='문화', w2=i)) for i in cul_20_02]})
cul_2020_02['positive'] = ['-', '-', '-', '+', '-', '+', '+']
print(cul_2020_02)

# from cul202003
embedding_mode = Word2Vec(cul202003, size=100, window=2,
                          min_count=1, workers=4, iter=100,
                          sg=1)
print(embedding_mode.wv.most_similar(positive=['문화'], topn=100))
# 가능해진(+)/웃는(+)/미비한(-)/활성화(+)/힘들죠(-)
cul = word()
cul_20_03 = cul.input_word("가능해진")
cul_20_03 = cul.input_word("웃는")
cul_20_03 = cul.input_word("미비한")
cul_20_03 = cul.input_word("활성화")
cul_20_03 = cul.input_word("힘들죠")
cul_2020_03 = pd.DataFrame({'keyword': ['문화' for i in range(0, len(cul_20_03))], 'target': cul_20_03,
                            'vector': [float(embedding_mode.wv.similarity(w1='문화', w2=i)) for i in cul_20_03]})
print(embedding_mode.wv.most_similar(positive=['취미'], topn=100))

# 그립습니다(-)/편의(+)/소중한(+)/힘든(-)/좋습니다(+)/좋다(+)
cul = word()
cul_20_03_1 = cul.input_word("그립습니다")
cul_20_03_1 = cul.input_word("편의")
cul_20_03_1 = cul.input_word("소중한")
cul_20_03_1 = cul.input_word("힘든")
cul_20_03_1 = cul.input_word("좋습니다")
cul_20_03_1 = cul.input_word("좋다")
cul_2020_03 = cul_2020_03.append(
    pd.DataFrame({'keyword': ['취미' for i in range(0, len(cul_20_03_1))], 'target': cul_20_03_1,
                  'vector': [float(embedding_mode.wv.similarity(w1='취미', w2=i)) for i in cul_20_03_1]}))
cul_2020_03['positive'] = ['+', '+', '-', '+', '-', '-', '+', '+', '-', '+', '+']
cul_2020_03 = cul_2020_03.reset_index(drop=True)
print(cul_2020_03)

# from cul202004
embedding_mode = Word2Vec(cul202004, size=100, window=2,
                          min_count=1, workers=4, iter=100,
                          sg=1)
print(embedding_mode.wv.most_similar(positive=['문화'], topn=100))
# 편의(+)/풍부하다(+)/건전한(+)/다양한(+)/좋다며(+)/우수하다(+)/훈훈함을(+)/편리하게(+)/어렵고(-)
cul = word()
cul_20_04 = cul.input_word("편의")
cul_20_04 = cul.input_word("풍부하다")
cul_20_04 = cul.input_word("건전한")
cul_20_04 = cul.input_word("다양한")
cul_20_04 = cul.input_word("좋다며")
cul_20_04 = cul.input_word("우수하다")
cul_20_04 = cul.input_word("훈훈함을")
cul_20_04 = cul.input_word("편리하게")
cul_20_04 = cul.input_word("어렵고")
cul_2020_04 = pd.DataFrame({'keyword': ['문화' for i in range(0, len(cul_20_04))], 'target': cul_20_04,
                            'vector': [float(embedding_mode.wv.similarity(w1='문화', w2=i)) for i in cul_20_04]})

print(embedding_mode.wv.most_similar(positive=['취미'], topn=100))
# 극복(+)/슬기로운(+)/씁쓸한(-)/즐기고(+)/즐거움(+)/재치(+)
cul = word()
cul_20_04_1 = cul.input_word("극복")
cul_20_04_1 = cul.input_word("슬기로운")
cul_20_04_1 = cul.input_word("씁쓸한")
cul_20_04_1 = cul.input_word("즐기고")
cul_20_04_1 = cul.input_word("즐거움")
cul_20_04_1 = cul.input_word("재치")
cul_2020_04 = cul_2020_04.append(
    pd.DataFrame({'keyword': ['취미' for i in range(0, len(cul_20_04_1))], 'target': cul_20_04_1,
                  'vector': [float(embedding_mode.wv.similarity(w1='취미', w2=i)) for i in cul_20_04_1]}))
cul_2020_04['positive'] = ['+', '+', '+', '+', '+', '+', '+', '+', '-', '+', '+', '-', '+', '+', '+']
cul_2020_04 = cul_2020_04.reset_index(drop=True)
print(cul_2020_04)

# from cul202005
embedding_mode = Word2Vec(cul202005, size=100, window=2,
                          min_count=1, workers=4, iter=100,
                          sg=1)
print(embedding_mode.wv.most_similar(positive=['문화'], topn=100))
# 확산(-)/다양한(+)/배낭여행(+)/좋아했다(+)/유치했다(-)
cul = word()
cul_20_05 = cul.input_word("확산")
cul_20_05 = cul.input_word("다양한")
cul_20_05 = cul.input_word("배낭여행")
cul_20_05 = cul.input_word("좋아했다")
cul_20_05 = cul.input_word("유치했다")
cul_2020_05 = pd.DataFrame({'keyword': ['문화' for i in range(0, len(cul_20_05))], 'target': cul_20_05,
                            'vector': [float(embedding_mode.wv.similarity(w1='문화', w2=i)) for i in cul_20_05]})
cul_2020_05['positive'] = ['-', '+', '+', '+', '-']
print(cul_2020_05)

'''
#culture 2019
result: cul_2019_02  ~  cul_2019_05
'''
# from cul201902
embedding_mode= Word2Vec(cul201902, size=100,window=2,
                         min_count=1, workers=4, iter=100,
                         sg=1)
print(embedding_mode.wv.most_similar(positive=['문화'],topn=100))
#성숙한(+)/안전하답니다(+)/열린(+)/역량(+)/활성화(+)
cul=word()
cul_19_02=cul.input_word("성숙한")
cul_19_02=cul.input_word("안전하답니다")
cul_19_02=cul.input_word("열린")
cul_19_02=cul.input_word("역량")
cul_19_02=cul.input_word("활성화")
cul_2019_02=pd.DataFrame({'keyword':['문화' for i in range(0,len(cul_19_02))],'target':cul_19_02,
              'vector':[float(embedding_mode.wv.similarity(w1='문화',w2=i)) for i in cul_19_02]})

print(embedding_mode.wv.most_similar(positive=['취미'],topn=100))
#좋아하는(+)/중요한(+)/기대할(+)/성숙한(+)
cul=word()
cul_19_02_1=cul.input_word("좋아하는")
cul_19_02_1=cul.input_word("중요한")
cul_19_02_1=cul.input_word("기대할")
cul_19_02_1=cul.input_word("성숙한")
cul_2019_02=cul_2019_02.append(pd.DataFrame({'keyword':['취미' for i in range(0,len(cul_19_02_1))],'target':cul_19_02_1,
              'vector':[float(embedding_mode.wv.similarity(w1='취미',w2=i)) for i in cul_19_02_1]}))
cul_2019_02['positive']=['+','+','+','+','+','+','+','+','+']
cul_2019_02=cul_2019_02.reset_index(drop=True)
print(cul_2019_02)

# from cul201903
embedding_mode = Word2Vec(cul201903, size=100, window=2,
                          min_count=1, workers=4, iter=100,
                          sg=1)
print(embedding_mode.wv.most_similar(positive=['문화'], topn=100))
# 줄면서(-)/다지는(+)/없는(-)/뜨거웠다(+)/짜릿함과(+)/강했지만(+)
cul = word()
cul_19_03 = cul.input_word("줄면서")
cul_19_03 = cul.input_word("다지는")
cul_19_03 = cul.input_word("없는")
cul_19_03 = cul.input_word("뜨거웠다")
cul_19_03 = cul.input_word("짜릿함과")
cul_19_03 = cul.input_word("강했지만")
cul_2019_03 = pd.DataFrame({'keyword': ['문화' for i in range(0, len(cul_19_03))], 'target': cul_19_03,
                            'vector': [float(embedding_mode.wv.similarity(w1='문화', w2=i)) for i in cul_19_03]})
cul_2019_03['positive'] = ['-', '+', '-', '+', '+', '+']
print(cul_2019_03)

# from cul201904
embedding_mode = Word2Vec(cul201904, size=100, window=2,
                          min_count=1, workers=4, iter=100,
                          sg=1)
print(embedding_mode.wv.most_similar(positive=['문화'], topn=100))
# 불과했다(-)/기대해(+)/않아(-)/적합하다는(+)/당황(-)/신선했다(+)
cul = word()
cul_19_04 = cul.input_word("불과했다")
cul_19_04 = cul.input_word("기대해")
cul_19_04 = cul.input_word("않아")
cul_19_04 = cul.input_word("적합하다는")
cul_19_04 = cul.input_word("당황")
cul_19_04 = cul.input_word("신선했다")
cul_2019_04 = pd.DataFrame({'keyword': ['문화' for i in range(0, len(cul_19_04))], 'target': cul_19_04,
                            'vector': [float(embedding_mode.wv.similarity(w1='문화', w2=i)) for i in cul_19_04]})
cul_2019_04['positive'] = ['-', '+', '-', '+', '-', '+']
print(cul_2019_04)

# from cul201905
embedding_mode = Word2Vec(cul201905, size=100, window=2,
                          min_count=1, workers=4, iter=100,
                          sg=1)
print(embedding_mode.wv.most_similar(positive=['문화'], topn=100))
# 놀이(+)/선물(+)/유행(+)/교류(+)/힐링(+)/광범위하게(+)/않는다(-)/생명력(+)/효행(+)/맑은(+)
cul = word()
cul_19_05 = cul.input_word("놀이")
cul_19_05 = cul.input_word("선물")
cul_19_05 = cul.input_word("유행")
cul_19_05 = cul.input_word("교류")
cul_19_05 = cul.input_word("힐링")
cul_19_05 = cul.input_word("광범위하게")
cul_19_05 = cul.input_word("않는다")
cul_19_05 = cul.input_word("생명력")
cul_19_05 = cul.input_word("효행")
cul_19_05 = cul.input_word("맑은")
cul_2019_05 = pd.DataFrame({'keyword': ['문화' for i in range(0, len(cul_19_05))], 'target': cul_19_05,
                            'vector': [float(embedding_mode.wv.similarity(w1='문화', w2=i)) for i in cul_19_05]})
cul_2019_05['positive'] = ['+', '+', '+', '+', '+', '+', '-', '+', '+', '+']
print(cul_2019_05)

'''
#medi 2020
result: medi_2020_02  ~  medi_2020_05
'''

# from medi202002
embedding_mode = Word2Vec(medi202002, size=100, window=2,
                          min_count=1, workers=4, iter=100,
                          sg=1)
print(embedding_mode.wv.most_similar(positive=['의료'], topn=100))
# 떨어진다(-)/ 싸우는(-)/ 피로(-)/폐쇄입니(-)/열악하다(-)/마비(-)/폐쇄(-)/회복(+)
medi = word()
medi_20_02 = medi.input_word("떨어진다")
medi_20_02 = medi.input_word("싸우는")
medi_20_02 = medi.input_word("피로")
medi_20_02 = medi.input_word("폐쇄입니")
medi_20_02 = medi.input_word("열악하다")
medi_20_02 = medi.input_word("마비")
medi_20_02 = medi.input_word("폐쇄")
medi_20_02 = medi.input_word("회복")
medi_2020_02 = pd.DataFrame({'keyword': ['의료' for i in range(0, len(medi_20_02))], 'target': medi_20_02,
                             'vector': [float(embedding_mode.wv.similarity(w1='의료', w2=i)) for i in medi_20_02]})
medi_2020_02['positive'] = ['-', '-', '-', '-', '-', '-', '-', '+']
medi_2020_02.at[3, 'target'] = '폐쇄'
print(medi_2020_02)

# from medi202003
embedding_mode = Word2Vec(medi202003, size=100, window=2,
                          min_count=1, workers=4, iter=100,
                          sg=1)
print(embedding_mode.wv.most_similar(positive=['의료'], topn=100))
# 협업(+)/감염증(-)/확진(-)/찔려(-)/노력(+)/다양한(+)/이뤄졌다(+)/불안감(-)/책임(-)
medi = word()
medi_20_03 = medi.input_word("협업")
medi_20_03 = medi.input_word("감염증")
medi_20_03 = medi.input_word("확진")
medi_20_03 = medi.input_word("찔려")
medi_20_03 = medi.input_word("노력")
medi_20_03 = medi.input_word("다양한")
medi_20_03 = medi.input_word("이뤄졌다")
medi_20_03 = medi.input_word("불안감")
medi_20_03 = medi.input_word("책임")
medi_2020_03 = pd.DataFrame({'keyword': ['의료' for i in range(0, len(medi_20_03))], 'target': medi_20_03,
                             'vector': [float(embedding_mode.wv.similarity(w1='의료', w2=i)) for i in medi_20_03]})
medi_2020_03['positive'] = ['+', '-', '-', '-', '+', '+', '+', '-', '-']
print(medi_2020_03)

# from medi202004
embedding_mode = Word2Vec(medi202004, size=100, window=2,
                          min_count=1, workers=4, iter=100,
                          sg=1)
print(embedding_mode.wv.most_similar(positive=['의료'], topn=100))
# 위반(-)/압박(-)/연장(-)/악화(-)/윤리(+)/않기로(-)/화해(+)/면역(+)/협업(+)/비판(-)/죄송하다(-)
medi = word()
medi_20_04 = medi.input_word("위반")
medi_20_04 = medi.input_word("압박")
medi_20_04 = medi.input_word("연장")
medi_20_04 = medi.input_word("악화")
medi_20_04 = medi.input_word("윤리")
medi_20_04 = medi.input_word("않기로")
medi_20_04 = medi.input_word("화해")
medi_20_04 = medi.input_word("면역")
medi_20_04 = medi.input_word("협업")
medi_20_04 = medi.input_word("비판")
medi_20_04 = medi.input_word("죄송하다")
medi_2020_04 = pd.DataFrame({'keyword': ['의료' for i in range(0, len(medi_20_04))], 'target': medi_20_04,
                             'vector': [float(embedding_mode.wv.similarity(w1='의료', w2=i)) for i in medi_20_04]})

medi_2020_04['positive'] = ['-', '-', '-', '-', '+', '-', '+', '+', '+', '-', '-']
print(medi_2020_04)

# from medi202005
embedding_mode = Word2Vec(medi202005, size=100, window=2,
                          min_count=1, workers=4, iter=100,
                          sg=1)
print(embedding_mode.wv.most_similar(positive=['의료'], topn=100))
# 대란(-)/active(+)/일어날지도(암시,-)/방호복(-)/종교시설(-)/모른다(-)/집착(-)/참여(+)/Care(+)/않습니다(-)/
medi = word()
medi_20_05 = medi.input_word("대란")
medi_20_05 = medi.input_word("active")
medi_20_05 = medi.input_word("일어날지도")
medi_20_05 = medi.input_word("방호복")
medi_20_05 = medi.input_word("종교시설")
medi_20_05 = medi.input_word("모른다")
medi_20_05 = medi.input_word("집착")
medi_20_05 = medi.input_word("참여")
medi_20_05 = medi.input_word("Care")
medi_20_05 = medi.input_word("않습니다")
medi_2020_05 = pd.DataFrame({'keyword': ['의료' for i in range(0, len(medi_20_05))], 'target': medi_20_05,
                             'vector': [float(embedding_mode.wv.similarity(w1='의료', w2=i)) for i in medi_20_05]})
medi_2020_05['positive'] = ['-', '+', '-', '-', '-', '-', '-', '+', '+', '-']
print(medi_2020_05)

'''
#medi 2019
result: medi_2019_02  ~  medi_2019_05
'''
# from medi201902
embedding_mode = Word2Vec(medi201902, size=100, window=2,
                          min_count=1, workers=4, iter=100,
                          sg=1)
print(embedding_mode.wv.most_similar(positive=['의료'], topn=100))
# care(+)/잘(+)/못(-)/하지만(-)/Healthiest(+)/새로운(+)/않겠다는(-)/사망자(-)
medi = word()
medi_19_02 = medi.input_word("care")
medi_19_02 = medi.input_word("잘")
medi_19_02 = medi.input_word("못")
medi_19_02 = medi.input_word("하지만")
medi_19_02 = medi.input_word("Healthiest")
medi_19_02 = medi.input_word("새로운")
medi_19_02 = medi.input_word("않겠다는")
medi_19_02 = medi.input_word("사망자")

medi_2019_02 = pd.DataFrame({'keyword': ['의료' for i in range(0, len(medi_19_02))], 'target': medi_19_02,
                             'vector': [float(embedding_mode.wv.similarity(w1='의료', w2=i)) for i in medi_19_02]})
medi_2019_02['positive'] = ['+', '+', '-', '-', '+', '+', '-', '-']
print(medi_2019_02)

# from medi201903
embedding_mode = Word2Vec(medi201903, size=100, window=2,
                          min_count=1, workers=4, iter=100,
                          sg=1)
print(embedding_mode.wv.most_similar(positive=['의료'], topn=100))
# 중단(-)/늘리고(+)/말기(-)/폭력(-)/객관성(+)/안전(+)/예방(+)/않는다(-)
medi = word()
medi_19_03 = medi.input_word("중단")
medi_19_03 = medi.input_word("늘리고")
medi_19_03 = medi.input_word("말기")
medi_19_03 = medi.input_word("폭력")
medi_19_03 = medi.input_word("객관성")
medi_19_03 = medi.input_word("안전")
medi_19_03 = medi.input_word("예방")
medi_19_03 = medi.input_word("않는다")
medi_2019_03 = pd.DataFrame({'keyword': ['의료' for i in range(0, len(medi_19_03))], 'target': medi_19_03,
                             'vector': [float(embedding_mode.wv.similarity(w1='의료', w2=i)) for i in medi_19_03]})
medi_2019_03['positive'] = ['-', '+', '-', '-', '+', '+', '+', '-']
print(medi_2019_03)

# from medi201904
embedding_mode = Word2Vec(medi201904, size=100, window=2,
                          min_count=1, workers=4, iter=100,
                          sg=1)
print(embedding_mode.wv.most_similar(positive=['의료'], topn=100))
# 지식(+)/필요한(+)/부담(-)/좋다(+)/유예(-)
medi = word()
medi_19_04 = medi.input_word("지식")
medi_19_04 = medi.input_word("필요한")
medi_19_04 = medi.input_word("부담")
medi_19_04 = medi.input_word("좋다")
medi_19_04 = medi.input_word("유예")
medi_2019_04 = pd.DataFrame({'keyword': ['의료' for i in range(0, len(medi_19_04))], 'target': medi_19_04,
                             'vector': [float(embedding_mode.wv.similarity(w1='의료', w2=i)) for i in medi_19_04]})
medi_2019_04['positive'] = ['+', '+', '-', '+', '-']
print(medi_2019_04)

# from medi201905
embedding_mode = Word2Vec(medi201905, size=100, window=2,
                          min_count=1, workers=4, iter=100,
                          sg=1)
print(embedding_mode.wv.most_similar(positive=['의료'], topn=100))
# 피부관리(+)/방해(-)/완전히(+)/다양한(+)/않는다(-)/
medi = word()
medi_19_05 = medi.input_word("피부관리")
medi_19_05 = medi.input_word("방해")
medi_19_05 = medi.input_word("완전히")
medi_19_05 = medi.input_word("다양한")
medi_19_05 = medi.input_word("않는다")
medi_2019_05 = pd.DataFrame({'keyword': ['의료' for i in range(0, len(medi_19_05))], 'target': medi_19_05,
                             'vector': [float(embedding_mode.wv.similarity(w1='의료', w2=i)) for i in medi_19_05]})
medi_2019_05['positive'] = ['+', '-', '+', '+', '-']
print(medi_2019_05)

'''
#leisure 2020
result: leisure_2020_02  ~  leisure_2020_05
'''
# from leisure202002
embedding_mode = Word2Vec(leisure202002, size=100, window=2,
                          min_count=1, workers=4, iter=100,
                          sg=1)
print(embedding_mode.wv.most_similar(positive=['레저'], topn=100))
# 찾는(+)/보트(+)/함께(+)/해변(+)/새롭게(+)/명소(+)/색다른(+)
leisure = word()
leisure_20_02 = leisure.input_word("찾는")
leisure_20_02 = leisure.input_word("보트")
leisure_20_02 = leisure.input_word("함께")
leisure_20_02 = leisure.input_word("해변")
leisure_20_02 = leisure.input_word("새롭게")
leisure_20_02 = leisure.input_word("명소")
leisure_20_02 = leisure.input_word("색다른")
leisure_2020_02 = pd.DataFrame({'keyword': ['레저' for i in range(0, len(leisure_20_02))], 'target': leisure_20_02,
                                'vector': [float(embedding_mode.wv.similarity(w1='레저', w2=i)) for i in leisure_20_02]})
leisure_2020_02['positive'] = ['+', '+', '+', '+', '+', '+', '+']
print(leisure_2020_02)

# from leisure202003
embedding_mode = Word2Vec(leisure202003, size=100, window=2,
                          min_count=1, workers=4, iter=100,
                          sg=1)
print(embedding_mode.wv.most_similar(positive=['레저'], topn=100))
# 축제(+)/휴양(+)/기대하고(+)/친근한(+)/대단한(+)/편안한(+)
leisure = word()
leisure_20_03 = leisure.input_word("축제")
leisure_20_03 = leisure.input_word("휴양")
leisure_20_03 = leisure.input_word("기대하고")
leisure_20_03 = leisure.input_word("친근한")
leisure_20_03 = leisure.input_word("대단한")
leisure_20_03 = leisure.input_word("편안한")
leisure_2020_03 = pd.DataFrame({'keyword': ['레저' for i in range(0, len(leisure_20_03))], 'target': leisure_20_03,
                                'vector': [float(embedding_mode.wv.similarity(w1='레저', w2=i)) for i in leisure_20_03]})
leisure_2020_03['positive'] = ['+', '+', '+', '+', '+', '+']
print(leisure_2020_03)

# from leisure202004
embedding_mode = Word2Vec(leisure202004, size=100, window=2,
                          min_count=1, workers=4, iter=100,
                          sg=1)
print(embedding_mode.wv.most_similar(positive=['레저'], topn=100))
# 휴식(+)/즐기려는(+)/건강한(+)/즐길(+)/다양한(+)/불안해진다(-)/불가능하다(-)
leisure = word()
leisure_20_04 = leisure.input_word("휴식")
leisure_20_04 = leisure.input_word("즐기려는")
leisure_20_04 = leisure.input_word("건강한")
leisure_20_04 = leisure.input_word("즐길")
leisure_20_04 = leisure.input_word("다양한")
leisure_20_04 = leisure.input_word("불안해진다")
leisure_20_04 = leisure.input_word("불가능하다")
leisure_2020_04 = pd.DataFrame({'keyword': ['레저' for i in range(0, len(leisure_20_04))], 'target': leisure_20_04,
                                'vector': [float(embedding_mode.wv.similarity(w1='레저', w2=i)) for i in leisure_20_04]})
leisure_2020_04['positive'] = ['+', '+', '+', '+', '+', '-', '-']
print(leisure_2020_04)

# from leisure202005
embedding_mode = Word2Vec(leisure202005, size=100, window=2,
                          min_count=1, workers=4, iter=100,
                          sg=1)
print(embedding_mode.wv.most_similar(positive=['레저'], topn=100))
# 없고(-)/해양(+)/쏘다니는(+)/담긴(+)
# print(embedding_mode.wv.most_similar(positive=['관광'],topn=100)) : 다를게 없음
leisure = word()
leisure_20_05 = leisure.input_word("없고")
leisure_20_05 = leisure.input_word("해양")
leisure_20_05 = leisure.input_word("쏘다니는")
leisure_20_05 = leisure.input_word("담긴")
leisure_2020_05 = pd.DataFrame({'keyword': ['레저' for i in range(0, len(leisure_20_05))], 'target': leisure_20_05,
                                'vector': [float(embedding_mode.wv.similarity(w1='레저', w2=i)) for i in leisure_20_05]})
leisure_2020_05['positive'] = ['-', '+', '+', '+']
print(leisure_2020_05)

'''
#leisure 2019
result: leisure_2019_02  ~  leisure_2019_05
'''
# from leisure201902
embedding_mode = Word2Vec(leisure201902, size=100, window=2,
                          min_count=1, workers=4, iter=100,
                          sg=1)
print(embedding_mode.wv.most_similar(positive=['레저'], topn=100))
# 않아(-)/결합(+)/가까워(+)/함께(+)/밤하늘(+)/앓았던(-)/단순한(+)
leisure = word()
leisure_19_02 = leisure.input_word("않아")
leisure_19_02 = leisure.input_word("결합")
leisure_19_02 = leisure.input_word("가까워")
leisure_19_02 = leisure.input_word("함께")
leisure_19_02 = leisure.input_word("밤하늘")
leisure_19_02 = leisure.input_word("앓았던")
leisure_19_02 = leisure.input_word("단순한")
leisure_2019_02 = pd.DataFrame({'keyword': ['레저' for i in range(0, len(leisure_19_02))], 'target': leisure_19_02,
                                'vector': [float(embedding_mode.wv.similarity(w1='레저', w2=i)) for i in leisure_19_02]})
leisure_2019_02['positive'] = ['-', '+', '+', '+', '+', '-', '+']
print(leisure_2019_02)

# from leisure201903
embedding_mode = Word2Vec(leisure201903, size=100, window=2,
                          min_count=1, workers=4, iter=100,
                          sg=1)
print(embedding_mode.wv.most_similar(positive=['레저'], topn=100))
# 허세(-)/통증(-)/프리미엄(+)/필수(+)/좋다며(+)/해롭습니다(-)
leisure = word()
leisure_19_03 = leisure.input_word("허세")
leisure_19_03 = leisure.input_word("통증")
leisure_19_03 = leisure.input_word("프리미엄")
leisure_19_03 = leisure.input_word("필수")
leisure_19_03 = leisure.input_word("좋다며")
leisure_19_03 = leisure.input_word("해롭습니다")
leisure_2019_03 = pd.DataFrame({'keyword': ['레저' for i in range(0, len(leisure_19_03))], 'target': leisure_19_03,
                                'vector': [float(embedding_mode.wv.similarity(w1='레저', w2=i)) for i in leisure_19_03]})
leisure_2019_03['positive'] = ['-', '-', '+', '+', '+', '-']
print(leisure_2019_03)

# from leisure201904
embedding_mode = Word2Vec(leisure201904, size=100, window=2,
                          min_count=1, workers=4, iter=100,
                          sg=1)
print(embedding_mode.wv.most_similar(positive=['레저'], topn=100))
# 해양(+)/받는(+)/참여(+)/재난(-)/색다른(+)/늘었다(+)/불황(-)
leisure = word()
leisure_19_04 = leisure.input_word("해양")
leisure_19_04 = leisure.input_word("받는")
leisure_19_04 = leisure.input_word("참여")
leisure_19_04 = leisure.input_word("재난")
leisure_19_04 = leisure.input_word("색다른")
leisure_19_04 = leisure.input_word("늘었다")
leisure_19_04 = leisure.input_word("불황")
leisure_2019_04 = pd.DataFrame({'keyword': ['레저' for i in range(0, len(leisure_19_04))], 'target': leisure_19_04,
                                'vector': [float(embedding_mode.wv.similarity(w1='레저', w2=i)) for i in leisure_19_04]})
leisure_2019_04['positive'] = ['+', '+', '+', '-', '+', '+', '-']
print(leisure_2019_04)

# from leisure201905
embedding_mode = Word2Vec(leisure201905, size=100, window=2,
                          min_count=1, workers=4, iter=100,
                          sg=1)
print(embedding_mode.wv.most_similar(positive=['레저'], topn=100))
# 캠핑장(+)/휴식(+)/수상(+)/외식(+)/꿀맛(+)/꿀잠(+)/꿀잼(+)
leisure = word()
leisure_19_05 = leisure.input_word("캠핑장")
leisure_19_05 = leisure.input_word("휴식")
leisure_19_05 = leisure.input_word("수상")
leisure_19_05 = leisure.input_word("외식")
leisure_19_05 = leisure.input_word("꿀맛")
leisure_19_05 = leisure.input_word("꿀잠")
leisure_19_05 = leisure.input_word("꿀잼")
leisure_2019_05 = pd.DataFrame({'keyword': ['레저' for i in range(0, len(leisure_19_05))], 'target': leisure_19_05,
                                'vector': [float(embedding_mode.wv.similarity(w1='레저', w2=i)) for i in leisure_19_05]})
leisure_2019_05['positive'] = ['+', '+', '+', '+', '+', '+', '+']
print(leisure_2019_05)

'''
#stay 2020
result: stay_2020_02  ~  stay_2020_05
'''
# from stay202002
embedding_mode = Word2Vec(stay202002, size=100, window=2,
                          min_count=1, workers=4, iter=100,
                          sg=1)
print(embedding_mode.wv.most_similar(positive=['숙박'], topn=100))
# 함께(+)/한산한(-)/않을(-)/새로운(+)/썰렁한(-)
stay = word()
stay_20_02 = stay.input_word("함께")
stay_20_02 = stay.input_word("한산한")
stay_20_02 = stay.input_word("않을")
stay_20_02 = stay.input_word("새로운")
stay_20_02 = stay.input_word("썰렁한")
stay_2020_02 = pd.DataFrame({'keyword': ['숙박' for i in range(0, len(stay_20_02))], 'target': stay_20_02,
                             'vector': [float(embedding_mode.wv.similarity(w1='숙박', w2=i)) for i in stay_20_02]})
stay_2020_02['positive'] = ['+', '-', '-', '+', '-']
print(stay_2020_02)

# from stay202003
embedding_mode = Word2Vec(stay202003, size=100, window=2,
                          min_count=1, workers=4, iter=100,
                          sg=1)
print(embedding_mode.wv.most_similar(positive=['숙박'], topn=100))
# 원하는(+)/협력(+)/다양한(+)/좋다(+)/가까운(+)/최신(+)
stay = word()
stay_20_03 = stay.input_word("원하는")
stay_20_03 = stay.input_word("협력")
stay_20_03 = stay.input_word("다양한")
stay_20_03 = stay.input_word("좋다")
stay_20_03 = stay.input_word("가까운")
stay_20_03 = stay.input_word("최신")
stay_2020_03 = pd.DataFrame({'keyword': ['숙박' for i in range(0, len(stay_20_03))], 'target': stay_20_03,
                             'vector': [float(embedding_mode.wv.similarity(w1='숙박', w2=i)) for i in stay_20_03]})
stay_2020_03['positive'] = ['+', '+', '+', '+', '+', '+']
print(stay_2020_03)

# from stay202004
embedding_mode = Word2Vec(stay202004, size=100, window=2,
                          min_count=1, workers=4, iter=100,
                          sg=1)
print(embedding_mode.wv.most_similar(positive=['숙박'], topn=100))
# 용이(+)/여파(-)/떨어지면서(-)/직격탄(-)/아니었다(-)/없었는데(-)/헐값(-)/많던(-)/긴장감(-)/곤란하다고(-)
stay = word()
stay_20_04 = stay.input_word("용이")
stay_20_04 = stay.input_word("여파")
stay_20_04 = stay.input_word("떨어지면서")
stay_20_04 = stay.input_word("직격탄")
stay_20_04 = stay.input_word("아니었다")
stay_20_04 = stay.input_word("없었는데")
stay_20_04 = stay.input_word("헐값")
stay_20_04 = stay.input_word("많던")
stay_20_04 = stay.input_word("긴장감")
stay_20_04 = stay.input_word("곤란하다고")
stay_2020_04 = pd.DataFrame({'keyword': ['숙박' for i in range(0, len(stay_20_04))], 'target': stay_20_04,
                             'vector': [float(embedding_mode.wv.similarity(w1='숙박', w2=i)) for i in stay_20_04]})
stay_2020_04['positive'] = ['+', '-', '-', '-', '-', '-', '-', '-', '-', '-']
print(stay_2020_04)

# from stay202005
embedding_mode = Word2Vec(stay202005, size=100, window=2,
                          min_count=1, workers=4, iter=100,
                          sg=1)
print(embedding_mode.wv.most_similar(positive=['숙박'], topn=100))
# 완성(+)/외식(+)/맛집(+)/고문(-)/손실(-)/했지만(-)/적발(-)/불법(-)/사기(-)
stay = word()
stay_20_05 = stay.input_word("완성")
stay_20_05 = stay.input_word("외식")
stay_20_05 = stay.input_word("맛집")
stay_20_05 = stay.input_word("고문")
stay_20_05 = stay.input_word("손실")
stay_20_05 = stay.input_word("했지만")
stay_20_05 = stay.input_word("적발")
stay_20_05 = stay.input_word("불법")
stay_20_05 = stay.input_word("사기")
stay_2020_05 = pd.DataFrame({'keyword': ['숙박' for i in range(0, len(stay_20_05))], 'target': stay_20_05,
                             'vector': [float(embedding_mode.wv.similarity(w1='숙박', w2=i)) for i in stay_20_05]})
stay_2020_05['positive'] = ['+', '+', '+', '-', '-', '-', '-', '-', '-']
print(stay_2020_05)

'''
#stay 2019
result: stay_2019_02  ~  stay_2019_05
'''
# from stay201902
embedding_mode = Word2Vec(stay201902, size=100, window=2,
                          min_count=1, workers=4, iter=100,
                          sg=1)
print(embedding_mode.wv.most_similar(positive=['숙박'], topn=100))
# 편의(+)/복합(+)/최대(+)/부당(-)/어려움(-)/편리하게(+)/자유(+)
stay = word()
stay_19_02 = stay.input_word("편의")
stay_19_02 = stay.input_word("복합")
stay_19_02 = stay.input_word("최대")
stay_19_02 = stay.input_word("부당")
stay_19_02 = stay.input_word("어려움")
stay_19_02 = stay.input_word("편리하게")
stay_19_02 = stay.input_word("자유")
stay_2019_02 = pd.DataFrame({'keyword': ['숙박' for i in range(0, len(stay_19_02))], 'target': stay_19_02,
                             'vector': [float(embedding_mode.wv.similarity(w1='숙박', w2=i)) for i in stay_19_02]})
stay_2019_02['positive'] = ['-', '-', '-', '+', '-', '+', '+']
print(stay_2019_02)

# from stay201903
embedding_mode = Word2Vec(stay201903, size=100, window=2,
                          min_count=1, workers=4, iter=100,
                          sg=1)
print(embedding_mode.wv.most_similar(positive=['숙박'], topn=100))
# 징계(-)/슬픔(-)/모든(+)/함께(+)/사고(-)/절반(-)/어렵게(-)/
stay = word()
stay_19_03 = stay.input_word("징계")
stay_19_03 = stay.input_word("슬픔")
stay_19_03 = stay.input_word("모든")
stay_19_03 = stay.input_word("함께")
stay_19_03 = stay.input_word("사고")
stay_19_03 = stay.input_word("절반")
stay_19_03 = stay.input_word("어렵게")
stay_2019_03 = pd.DataFrame({'keyword': ['숙박' for i in range(0, len(stay_19_03))], 'target': stay_19_03,
                             'vector': [float(embedding_mode.wv.similarity(w1='숙박', w2=i)) for i in stay_19_03]})
stay_2019_03['positive'] = ['-', '-', '+', '+', '-', '-', '-']
print(stay_2019_03)

# from stay201904
embedding_mode = Word2Vec(stay201904, size=100, window=2,
                          min_count=1, workers=4, iter=100,
                          sg=1)
print(embedding_mode.wv.most_similar(positive=['숙박'], topn=100))
# 했지만(-)/그런데(-)/부담(-)/거절(-)/쟁점(-)/다양한(+)/최저(-)
stay = word()
stay_19_04 = stay.input_word("했지만")
stay_19_04 = stay.input_word("그런데")
stay_19_04 = stay.input_word("부담")
stay_19_04 = stay.input_word("거절")
stay_19_04 = stay.input_word("쟁점")
stay_19_04 = stay.input_word("다양한")
stay_19_04 = stay.input_word("최저")
stay_2019_04 = pd.DataFrame({'keyword': ['숙박' for i in range(0, len(stay_19_04))], 'target': stay_19_04,
                             'vector': [float(embedding_mode.wv.similarity(w1='숙박', w2=i)) for i in stay_19_04]})
stay_2019_04['positive'] = ['-', '-', '-', '-', '-', '+', '-']
print(stay_2019_04)

# from stay201905
embedding_mode = Word2Vec(stay201905, size=100, window=2,
                          min_count=1, workers=4, iter=100,
                          sg=1)
print(embedding_mode.wv.most_similar(positive=['숙박'], topn=100))
# 편의(+)/비용(-)/하기에는(-)/건너갔다(-)/부적절하다는(-)/폭언(-)/실종(-)/욕설(-)
stay = word()
stay_19_05 = stay.input_word("편의")
stay_19_05 = stay.input_word("비용")
stay_19_05 = stay.input_word("하기에는")
stay_19_05 = stay.input_word("건너갔다")
stay_19_05 = stay.input_word("부적절하다는")
stay_19_05 = stay.input_word("폭언")
stay_19_05 = stay.input_word("실종")
stay_19_05 = stay.input_word("욕설")
stay_2019_05 = pd.DataFrame({'keyword': ['숙박' for i in range(0, len(stay_19_05))], 'target': stay_19_05,
                             'vector': [float(embedding_mode.wv.similarity(w1='숙박', w2=i)) for i in stay_19_05]})
stay_2019_05['positive'] = ['+', '-', '-', '-', '-', '-', '-', '-']
print(stay_2019_05)


# 3. PN 변수

# 3-1) PN 변수 계산

# 19년 2월 숙박관련 정보
PN = stay_2019_02['vector'] 

vec = []
for i in PN:
    if i == PN[0]:
        vec.append('-{}'.format(PN[0]))
    elif i == PN[1]:
        vec.append('-{}'.format(PN[1]))
    elif i == PN[2]:
        vec.append('-{}'.format(PN[2]))
    elif i == PN[3]:
        vec.append('{}'.format(PN[3]))
    elif i == PN[4]:
        vec.append('-{}'.format(PN[4]))
    elif i == PN[5]:
        vec.append('{}'.format(PN[5]))
    elif i == PN[6]:
        vec.append('{}'.format(PN[6]))
    
sum = 0
for i in range(len(vec)):
    sum = sum + float(vec[i])
average = sum / len(vec)
average

# 19년 3월 숙박 PN 계산 ===============================================================================
PN = stay_2019_03['vector'] 
vec = []
for i in PN:
    if i == PN[0]:
        vec.append('-{}'.format(PN[0]))
    elif i == PN[1]:
        vec.append('-{}'.format(PN[1]))
    elif i == PN[2]:
        vec.append('+{}'.format(PN[2]))
    elif i == PN[3]:
        vec.append('+{}'.format(PN[3]))
    elif i == PN[4]:
        vec.append('-{}'.format(PN[4]))
    elif i == PN[5]:
        vec.append('-{}'.format(PN[5]))
    elif i == PN[6]:
        vec.append('-{}'.format(PN[6]))


sum = 0
for i in range(len(vec)):
    sum = sum + float(vec[i])
average = sum / len(vec)
average


# 19년 4월 숙박 PN 계산 ===============================================================================
PN = stay_2019_04['vector'] 

vec = []
for i in PN:
    if i == PN[0]:
        vec.append('-{}'.format(PN[0]))
    elif i == PN[1]:
        vec.append('-{}'.format(PN[1]))
    elif i == PN[2]:
        vec.append('-{}'.format(PN[2]))
    elif i == PN[3]:
        vec.append('-{}'.format(PN[3]))
    elif i == PN[4]:
        vec.append('-{}'.format(PN[4]))
    elif i == PN[5]:
        vec.append('+{}'.format(PN[5]))
    elif i == PN[6]:
        vec.append('-{}'.format(PN[6]))

sum = 0
for i in range(len(vec)):
    sum = sum + float(vec[i])
average = sum / len(vec)
average


# 19년 5월 숙박 PN 계산 ===============================================================================
PN = stay_2019_05['vector']

vec = []
for i in PN:
    if i == PN[0]:
        vec.append('+{}'.format(PN[0]))
    elif i == PN[1]:
        vec.append('-{}'.format(PN[1]))
    elif i == PN[2]:
        vec.append('-{}'.format(PN[2]))
    elif i == PN[3]:
        vec.append('-{}'.format(PN[3]))
    elif i == PN[4]:
        vec.append('-{}'.format(PN[4]))
    elif i == PN[5]:
        vec.append('-{}'.format(PN[5]))
    elif i == PN[6]:
        vec.append('-{}'.format(PN[6]))
    elif i == PN[7]:
        vec.append('-{}'.format(PN[7]))

sum = 0
for i in range(len(vec)):
    sum = sum + float(vec[i])
average = sum / len(vec)
average


# 20년 2월 숙박 PN 계산 ===============================================================================
PN = stay_2020_02['vector']

vec = []
for i in PN:
    if i == PN[0]:
        vec.append('+{}'.format(PN[0]))
    elif i == PN[1]:
        vec.append('-{}'.format(PN[1]))
    elif i == PN[2]:
        vec.append('-{}'.format(PN[2]))
    elif i == PN[3]:
        vec.append('+{}'.format(PN[3]))
    elif i == PN[4]:
        vec.append('-{}'.format(PN[4]))

sum = 0
for i in range(len(vec)):
    sum = sum + float(vec[i])
average = sum / len(vec)
average


# 20년 3월 숙박 PN 계산 ===============================================================================

PN = stay_2020_03['vector'] 

vec = []
for i in PN:
    if i == PN[0]:
        vec.append('+{}'.format(PN[0]))
    elif i == PN[1]:
        vec.append('+{}'.format(PN[1]))
    elif i == PN[2]:
        vec.append('+{}'.format(PN[2]))
    elif i == PN[3]:
        vec.append('+{}'.format(PN[3]))
    elif i == PN[4]:
        vec.append('+{}'.format(PN[4]))
    elif i == PN[5]:
        vec.append('+{}'.format(PN[5]))

sum = 0
for i in range(len(vec)):
    sum = sum + float(vec[i])
average = sum / len(vec)
average


# 20년 4월 숙박 PN 계산 ===============================================================================

PN = stay_2020_04['vector'] 

vec = []
for i in PN:
    if i == PN[0]:
        vec.append('+{}'.format(PN[0]))
    elif i == PN[1]:
        vec.append('-{}'.format(PN[1]))
    elif i == PN[2]:
        vec.append('-{}'.format(PN[2]))
    elif i == PN[3]:
        vec.append('-{}'.format(PN[3]))
    elif i == PN[4]:
        vec.append('-{}'.format(PN[4]))
    elif i == PN[5]:
        vec.append('-{}'.format(PN[5]))
    elif i == PN[6]:
        vec.append('-{}'.format(PN[6]))
    elif i == PN[7]:
        vec.append('-{}'.format(PN[7]))
    elif i == PN[8]:
        vec.append('-{}'.format(PN[8]))
    elif i == PN[9]:
        vec.append('-{}'.format(PN[9]))

sum = 0
for i in range(len(vec)):
    sum = sum + float(vec[i])
average = sum / len(vec)
average


# 20년 5월 숙박 PN 계산 ===============================================================================
PN = stay_2020_05['vector'] 


vec = []
for i in PN:
    if i == PN[0]:
        vec.append('+{}'.format(PN[0]))
    elif i == PN[1]:
        vec.append('-{}'.format(PN[1]))
    elif i == PN[2]:
        vec.append('-{}'.format(PN[2]))
    elif i == PN[3]:
        vec.append('-{}'.format(PN[3]))
    elif i == PN[4]:
        vec.append('-{}'.format(PN[4]))
    elif i == PN[5]:
        vec.append('-{}'.format(PN[5]))
    elif i == PN[6]:
        vec.append('-{}'.format(PN[6]))
    elif i == PN[7]:
        vec.append('-{}'.format(PN[7]))
    elif i == PN[8]:
        vec.append('-{}'.format(PN[8]))


sum = 0
for i in range(len(vec)):
    sum = sum + float(vec[i])
average = sum / len(vec)
average


# 19년 2월 문화취미 PN 계산 ==========================================================================
PN = cul_2019_02['vector'] 


vec = []
for i in PN:
    if i == PN[0]:
        vec.append('+{}'.format(PN[0]))
    elif i == PN[1]:
        vec.append('-{}'.format(PN[1]))
    elif i == PN[2]:
        vec.append('-{}'.format(PN[2]))
    elif i == PN[3]:
        vec.append('-{}'.format(PN[3]))
    elif i == PN[4]:
        vec.append('-{}'.format(PN[4]))
    elif i == PN[5]:
        vec.append('-{}'.format(PN[5]))
    elif i == PN[6]:
        vec.append('-{}'.format(PN[6]))
    elif i == PN[7]:
        vec.append('-{}'.format(PN[7]))
    elif i == PN[8]:
        vec.append('-{}'.format(PN[8]))


sum = 0
for i in range(len(vec)):
    sum = sum + float(vec[i])
average = sum / len(vec)
average


# 19년 3월 문화취미 PN 계산 ==========================================================================

PN = cul_2019_03['vector'] 

vec = []
for i in PN:
    if i == PN[0]:
        vec.append('-{}'.format(PN[0]))
    elif i == PN[1]:
        vec.append('+{}'.format(PN[1]))
    elif i == PN[2]:
        vec.append('-{}'.format(PN[2]))
    elif i == PN[3]:
        vec.append('+{}'.format(PN[3]))
    elif i == PN[4]:
        vec.append('+{}'.format(PN[4]))
    elif i == PN[5]:
        vec.append('+{}'.format(PN[5]))


sum = 0
for i in range(len(vec)):
    sum = sum + float(vec[i])
average = sum / len(vec)
average


# 19년 4월 문화취미 PN 계산 ==========================================================================

PN = cul_2019_04['vector'] 


vec = []
for i in PN:
    if i == PN[0]:
        vec.append('-{}'.format(PN[0]))
    elif i == PN[1]:
        vec.append('+{}'.format(PN[1]))
    elif i == PN[2]:
        vec.append('-{}'.format(PN[2]))
    elif i == PN[3]:
        vec.append('+{}'.format(PN[3]))
    elif i == PN[4]:
        vec.append('-{}'.format(PN[4]))
    elif i == PN[5]:
        vec.append('+{}'.format(PN[5]))


sum = 0
for i in range(len(vec)):
    sum = sum + float(vec[i])
average = sum / len(vec)
average


# 19년 5월 문화취미 PN 계산 ==========================================================================

PN = cul_2019_05['vector'] 


vec = []
for i in PN:
    if i == PN[0]:
        vec.append('+{}'.format(PN[0]))
    elif i == PN[1]:
        vec.append('-{}'.format(PN[1]))
    elif i == PN[2]:
        vec.append('-{}'.format(PN[2]))
    elif i == PN[3]:
        vec.append('-{}'.format(PN[3]))
    elif i == PN[4]:
        vec.append('-{}'.format(PN[4]))
    elif i == PN[5]:
        vec.append('-{}'.format(PN[5]))
    elif i == PN[6]:
        vec.append('-{}'.format(PN[6]))
    elif i == PN[7]:
        vec.append('-{}'.format(PN[7]))
    elif i == PN[8]:
        vec.append('-{}'.format(PN[8]))
    elif i == PN[9]:
        vec.append('-{}'.format(PN[9]))

sum = 0
for i in range(len(vec)):
    sum = sum + float(vec[i])
average = sum / len(vec)
average


# 20년 2월 문화취미 PN 계산 ==========================================================================
PN = cul_2020_02['vector'] 


vec = []
for i in PN:
    if i == PN[0]:
        vec.append('-{}'.format(PN[0]))
    elif i == PN[1]:
        vec.append('-{}'.format(PN[1]))
    elif i == PN[2]:
        vec.append('-{}'.format(PN[2]))
    elif i == PN[3]:
        vec.append('+{}'.format(PN[3]))
    elif i == PN[4]:
        vec.append('-{}'.format(PN[4]))
    elif i == PN[5]:
        vec.append('+{}'.format(PN[5]))
    elif i == PN[6]:
        vec.append('+{}'.format(PN[6]))

sum = 0
for i in range(len(vec)):
    sum = sum + float(vec[i])
average = sum / len(vec)
average


# 20년 3월 문화취미 PN 계산 ==========================================================================
PN = cul_2020_03['vector'] 


vec = []
for i in PN:
    if i == PN[0]:
        vec.append('+{}'.format(PN[0]))
    elif i == PN[1]:
        vec.append('+{}'.format(PN[1]))
    elif i == PN[2]:
        vec.append('-{}'.format(PN[2]))
    elif i == PN[3]:
        vec.append('+{}'.format(PN[3]))
    elif i == PN[4]:
        vec.append('-{}'.format(PN[4]))
    elif i == PN[5]:
        vec.append('-{}'.format(PN[5]))
    elif i == PN[6]:
        vec.append('+{}'.format(PN[6]))
    elif i == PN[7]:
        vec.append('+{}'.format(PN[7]))
    elif i == PN[8]:
        vec.append('-{}'.format(PN[8]))
    elif i == PN[9]:
        vec.append('+{}'.format(PN[9]))
    elif i == PN[10]:
        vec.append('+{}'.format(PN[10]))

sum = 0
for i in range(len(vec)):
    sum = sum + float(vec[i])
average = sum / len(vec)
average


# 20년 4월 문화취미 PN 계산 ==========================================================================
PN = cul_2020_04['vector']


vec = []
for i in PN:
    if i == PN[0]:
        vec.append('+{}'.format(PN[0]))
    elif i == PN[1]:
        vec.append('+{}'.format(PN[1]))
    elif i == PN[2]:
        vec.append('+{}'.format(PN[2]))
    elif i == PN[3]:
        vec.append('+{}'.format(PN[3]))
    elif i == PN[4]:
        vec.append('+{}'.format(PN[4]))
    elif i == PN[5]:
        vec.append('+{}'.format(PN[5]))
    elif i == PN[6]:
        vec.append('+{}'.format(PN[6]))
    elif i == PN[7]:
        vec.append('+{}'.format(PN[7]))
    elif i == PN[8]:
        vec.append('-{}'.format(PN[8]))
    elif i == PN[9]:
        vec.append('+{}'.format(PN[9]))
    elif i == PN[10]:
        vec.append('+{}'.format(PN[10]))
    elif i == PN[11]:
        vec.append('-{}'.format(PN[11]))
    elif i == PN[12]:
        vec.append('+{}'.format(PN[12]))
    elif i == PN[13]:
        vec.append('+{}'.format(PN[13]))
    elif i == PN[14]:
        vec.append('+{}'.format(PN[14]))

sum = 0
for i in range(len(vec)):
    sum = sum + float(vec[i])
average = sum / len(vec)
average


# 20년 5월 문화취미 PN 계산 ==========================================================================
PN = cul_2020_05['vector']


vec = []
for i in PN:
    if i == PN[0]:
        vec.append('-{}'.format(PN[0]))
    elif i == PN[1]:
        vec.append('+{}'.format(PN[1]))
    elif i == PN[2]:
        vec.append('+{}'.format(PN[2]))
    elif i == PN[3]:
        vec.append('+{}'.format(PN[3]))
    elif i == PN[4]:
        vec.append('-{}'.format(PN[4]))


sum = 0
for i in range(len(vec)):
    sum = sum + float(vec[i])
average = sum / len(vec)
average


# 19년 2월 푸드 PN 계산 ==========================================================================

PN = food_2019_02['vector'] 


vec = []
for i in PN:
    if i == PN[0]:
        vec.append('+{}'.format(PN[0]))
    elif i == PN[1]:
        vec.append('+{}'.format(PN[1]))
    elif i == PN[2]:
        vec.append('+{}'.format(PN[2]))
    elif i == PN[3]:
        vec.append('+{}'.format(PN[3]))
    elif i == PN[4]:
        vec.append('+{}'.format(PN[4]))
    elif i == PN[5]:
        vec.append('+{}'.format(PN[5]))


sum = 0
for i in range(len(vec)):
    sum = sum + float(vec[i])
average = sum / len(vec)
average


# 19년 3월 푸드 PN 계산 ==========================================================================
PN = food_2019_03['vector']


vec = []
for i in PN:
    if i == PN[0]:
        vec.append('+{}'.format(PN[0]))
    elif i == PN[1]:
        vec.append('+{}'.format(PN[1]))
    elif i == PN[2]:
        vec.append('+{}'.format(PN[2]))
    elif i == PN[3]:
        vec.append('+{}'.format(PN[3]))
    elif i == PN[4]:
        vec.append('+{}'.format(PN[4]))
    elif i == PN[5]:
        vec.append('+{}'.format(PN[5]))

sum = 0
for i in range(len(vec)):
    sum = sum + float(vec[i])
average = sum / len(vec)
average


# 19년 4월 푸드 PN 계산 ==========================================================================
PN = food_2019_04['vector'] 


vec = []
for i in PN:
    if i == PN[0]:
        vec.append('+{}'.format(PN[0]))
    elif i == PN[1]:
        vec.append('+{}'.format(PN[1]))
    elif i == PN[2]:
        vec.append('+{}'.format(PN[2]))
    elif i == PN[3]:
        vec.append('+{}'.format(PN[3]))
    elif i == PN[4]:
        vec.append('+{}'.format(PN[4]))
    elif i == PN[5]:
        vec.append('+{}'.format(PN[5]))
    elif i == PN[6]:
        vec.append('+{}'.format(PN[6]))

sum = 0
for i in range(len(vec)):
    sum = sum + float(vec[i])
average = sum / len(vec)
average


# 19년 5월 푸드 PN 계산 ==========================================================================
PN = food_2019_05['vector'] 


vec = []
for i in PN:
    if i == PN[0]:
        vec.append('-{}'.format(PN[0]))
    elif i == PN[1]:
        vec.append('+{}'.format(PN[1]))
    elif i == PN[2]:
        vec.append('-{}'.format(PN[2]))
    elif i == PN[3]:
        vec.append('-{}'.format(PN[3]))
    elif i == PN[4]:
        vec.append('+{}'.format(PN[4]))
    elif i == PN[5]:
        vec.append('+{}'.format(PN[5]))
    elif i == PN[6]:
        vec.append('-{}'.format(PN[6]))
    elif i == PN[7]:
        vec.append('-{}'.format(PN[7]))
    elif i == PN[8]:
        vec.append('+{}'.format(PN[8]))

sum = 0
for i in range(len(vec)):
    sum = sum + float(vec[i])
average = sum / len(vec)
average

#==========================================================================================
# 20년 2월 푸드관련 정보
PN = food_2020_02['vector'] 


vec = []
for i in PN:
    if i == PN[0]:
        vec.append('-{}'.format(PN[0]))
    elif i == PN[1]:
        vec.append('+{}'.format(PN[1]))
    elif i == PN[2]:
        vec.append('-{}'.format(PN[2]))
    elif i == PN[3]:
        vec.append('+{}'.format(PN[3]))
    elif i == PN[4]:
        vec.append('-{}'.format(PN[4]))
    elif i == PN[5]:
        vec.append('-{}'.format(PN[5]))
    elif i == PN[6]:
        vec.append('+{}'.format(PN[6]))
    elif i == PN[7]:
        vec.append('-{}'.format(PN[7]))
    elif i == PN[8]:
        vec.append('+{}'.format(PN[8]))
    elif i == PN[9]:
        vec.append('+{}'.format(PN[9]))

sum = 0
for i in range(len(vec)):
    sum = sum + float(vec[i])
average = sum / len(vec)
average


# 20년 3월 푸드 PN 계산 ==========================================================================
PN = food_2020_03['vector'] 


vec = []
for i in PN:
    if i == PN[0]:
        vec.append('+{}'.format(PN[0]))
    elif i == PN[1]:
        vec.append('-{}'.format(PN[1]))
    elif i == PN[2]:
        vec.append('-{}'.format(PN[2]))
    elif i == PN[3]:
        vec.append('-{}'.format(PN[3]))
    elif i == PN[4]:
        vec.append('-{}'.format(PN[4]))
    elif i == PN[5]:
        vec.append('-{}'.format(PN[5]))
    elif i == PN[6]:
        vec.append('-{}'.format(PN[6]))

sum = 0
for i in range(len(vec)):
    sum = sum + float(vec[i])
average = sum / len(vec)
average


# 20년 4월 푸드 PN 계산 ==========================================================================

PN = food_2020_04['vector'] 


vec = []
for i in PN:
    if i == PN[0]:
        vec.append('-{}'.format(PN[0]))
    elif i == PN[1]:
        vec.append('-{}'.format(PN[1]))
    elif i == PN[2]:
        vec.append('+{}'.format(PN[2]))
    elif i == PN[3]:
        vec.append('+{}'.format(PN[3]))
    elif i == PN[4]:
        vec.append('+{}'.format(PN[4]))
    elif i == PN[5]:
        vec.append('+{}'.format(PN[5]))
    elif i == PN[6]:
        vec.append('-{}'.format(PN[6]))
    elif i == PN[7]:
        vec.append('-{}'.format(PN[7]))
    elif i == PN[8]:
        vec.append('-{}'.format(PN[8]))

sum = 0
for i in range(len(vec)):
    sum = sum + float(vec[i])
average = sum / len(vec)
average


# 20년 5월 푸드 PN 계산 ==========================================================================


PN = food_2020_05['vector'] 


vec = []
for i in PN:
    if i == PN[0]:
        vec.append('-{}'.format(PN[0]))
    elif i == PN[1]:
        vec.append('+{}'.format(PN[1]))
    elif i == PN[2]:
        vec.append('-{}'.format(PN[2]))
    elif i == PN[3]:
        vec.append('-{}'.format(PN[3]))
    elif i == PN[4]:
        vec.append('+{}'.format(PN[4]))
    elif i == PN[5]:
        vec.append('+{}'.format(PN[5]))

sum = 0
for i in range(len(vec)):
    sum = sum + float(vec[i])
average = sum / len(vec)
average


# 19년 2월 의료기관 PN 계산 ==========================================================================
PN = medi_2019_02['vector'] 


vec = []
for i in PN:
    if i == PN[0]:
        vec.append('+{}'.format(PN[0]))
    elif i == PN[1]:
        vec.append('+{}'.format(PN[1]))
    elif i == PN[2]:
        vec.append('-{}'.format(PN[2]))
    elif i == PN[3]:
        vec.append('-{}'.format(PN[3]))
    elif i == PN[4]:
        vec.append('+{}'.format(PN[4]))
    elif i == PN[5]:
        vec.append('+{}'.format(PN[5]))
    elif i == PN[6]:
        vec.append('-{}'.format(PN[6]))
    elif i == PN[7]:
        vec.append('-{}'.format(PN[7]))

sum = 0
for i in range(len(vec)):
    sum = sum + float(vec[i])
average = sum / len(vec)
average


# 19년 3월 의료기관 PN 계산 ==========================================================================

PN = medi_2019_03['vector'] 


vec = []
for i in PN:
    if i == PN[0]:
        vec.append('-{}'.format(PN[0]))
    elif i == PN[1]:
        vec.append('+{}'.format(PN[1]))
    elif i == PN[2]:
        vec.append('-{}'.format(PN[2]))
    elif i == PN[3]:
        vec.append('-{}'.format(PN[3]))
    elif i == PN[4]:
        vec.append('+{}'.format(PN[4]))
    elif i == PN[5]:
        vec.append('+{}'.format(PN[5]))
    elif i == PN[6]:
        vec.append('+{}'.format(PN[6]))
    elif i == PN[7]:
        vec.append('-{}'.format(PN[7]))

sum = 0
for i in range(len(vec)):
    sum = sum + float(vec[i])
average = sum / len(vec)
average


# 19년 4월 의료기관 PN 계산 ==========================================================================
PN = medi_2019_04['vector']


vec = []
for i in PN:
    if i == PN[0]:
        vec.append('+{}'.format(PN[0]))
    elif i == PN[1]:
        vec.append('+{}'.format(PN[1]))
    elif i == PN[2]:
        vec.append('-{}'.format(PN[2]))
    elif i == PN[3]:
        vec.append('+{}'.format(PN[3]))
    elif i == PN[4]:
        vec.append('-{}'.format(PN[4]))

sum = 0
for i in range(len(vec)):
    sum = sum + float(vec[i])
average = sum / len(vec)
average


# 19년 5월 의료기관 PN 계산 ==========================================================================

PN = medi_2019_05['vector']


vec = []
for i in PN:
    if i == PN[0]:
        vec.append('+{}'.format(PN[0]))
    elif i == PN[1]:
        vec.append('-{}'.format(PN[1]))
    elif i == PN[2]:
        vec.append('+{}'.format(PN[2]))
    elif i == PN[3]:
        vec.append('+{}'.format(PN[3]))
    elif i == PN[4]:
        vec.append('-{}'.format(PN[4]))

sum = 0
for i in range(len(vec)):
    sum = sum + float(vec[i])
average = sum / len(vec)
average


# 20년 2월 의료기관 PN 계산 ==========================================================================

PN = medi_2020_02['vector'] 

vec = []
for i in PN:
    if i == PN[0]:
        vec.append('-{}'.format(PN[0]))
    elif i == PN[1]:
        vec.append('-{}'.format(PN[1]))
    elif i == PN[2]:
        vec.append('-{}'.format(PN[2]))
    elif i == PN[3]:
        vec.append('-{}'.format(PN[3]))
    elif i == PN[4]:
        vec.append('-{}'.format(PN[4]))
    elif i == PN[5]:
        vec.append('-{}'.format(PN[5]))
    elif i == PN[6]:
        vec.append('-{}'.format(PN[6]))
    elif i == PN[7]:
        vec.append('+{}'.format(PN[7]))

sum = 0
for i in range(len(vec)):
    sum = sum + float(vec[i])
average = sum / len(vec)
average


# 20년 3월 의료기관 PN 계산 ==========================================================================

PN = medi_2020_03['vector'] 


vec = []
for i in PN:
    if i == PN[0]:
        vec.append('+{}'.format(PN[0]))
    elif i == PN[1]:
        vec.append('-{}'.format(PN[1]))
    elif i == PN[2]:
        vec.append('-{}'.format(PN[2]))
    elif i == PN[3]:
        vec.append('-{}'.format(PN[3]))
    elif i == PN[4]:
        vec.append('+{}'.format(PN[4]))
    elif i == PN[5]:
        vec.append('+{}'.format(PN[5]))
    elif i == PN[6]:
        vec.append('+{}'.format(PN[6]))
    elif i == PN[7]:
        vec.append('-{}'.format(PN[7]))
    elif i == PN[8]:
        vec.append('-{}'.format(PN[8]))

sum = 0
for i in range(len(vec)):
    sum = sum + float(vec[i])
average = sum / len(vec)
average


# 20년 4월 의료기관 PN 계산 ==========================================================================

PN = medi_2020_04['vector'] 


vec = []
for i in PN:
    if i == PN[0]:
        vec.append('-{}'.format(PN[0]))
    elif i == PN[1]:
        vec.append('-{}'.format(PN[1]))
    elif i == PN[2]:
        vec.append('-{}'.format(PN[2]))
    elif i == PN[3]:
        vec.append('-{}'.format(PN[3]))
    elif i == PN[4]:
        vec.append('+{}'.format(PN[4]))
    elif i == PN[5]:
        vec.append('-{}'.format(PN[5]))
    elif i == PN[6]:
        vec.append('+{}'.format(PN[6]))
    elif i == PN[7]:
        vec.append('+{}'.format(PN[7]))
    elif i == PN[8]:
        vec.append('+{}'.format(PN[8]))
    elif i == PN[9]:
        vec.append('-{}'.format(PN[9]))
    elif i == PN[10]:
        vec.append('-{}'.format(PN[10]))

sum = 0
for i in range(len(vec)):
    sum = sum + float(vec[i])
average = sum / len(vec)
average


# 20년 5월 의료기관 PN 계산 ==========================================================================

PN = medi_2020_05['vector'] 


vec = []
for i in PN:
    if i == PN[0]:
        vec.append('-{}'.format(PN[0]))
    elif i == PN[1]:
        vec.append('+{}'.format(PN[1]))
    elif i == PN[2]:
        vec.append('-{}'.format(PN[2]))
    elif i == PN[3]:
        vec.append('-{}'.format(PN[3]))
    elif i == PN[4]:
        vec.append('-{}'.format(PN[4]))
    elif i == PN[5]:
        vec.append('-{}'.format(PN[5]))
    elif i == PN[6]:
        vec.append('-{}'.format(PN[6]))
    elif i == PN[7]:
        vec.append('+{}'.format(PN[7]))
    elif i == PN[8]:
        vec.append('+{}'.format(PN[8]))
    elif i == PN[9]:
        vec.append('-{}'.format(PN[9]))

sum = 0
for i in range(len(vec)):
    sum = sum + float(vec[i])
average = sum / len(vec)
average


# 19년 2월 보건위생 PN 계산 ==========================================================================

PN = health_2019_02['vector'] 


vec = []
for i in PN:
    if i == PN[0]:
        vec.append('-{}'.format(PN[0]))
    elif i == PN[1]:
        vec.append('-{}'.format(PN[1]))
    elif i == PN[2]:
        vec.append('+{}'.format(PN[2]))
    elif i == PN[3]:
        vec.append('-{}'.format(PN[3]))
    elif i == PN[4]:
        vec.append('+{}'.format(PN[4]))
    elif i == PN[5]:
        vec.append('+{}'.format(PN[5]))
    elif i == PN[6]:
        vec.append('+{}'.format(PN[6]))

sum = 0
for i in range(len(vec)):
    sum = sum + float(vec[i])
average = sum / len(vec)
average


# 19년 3월 보건위생 PN 계산 ==========================================================================
PN = health_2019_03['vector'] 


vec = []
for i in PN:
    if i == PN[0]:
        vec.append('-{}'.format(PN[0]))
    elif i == PN[1]:
        vec.append('-{}'.format(PN[1]))
    elif i == PN[2]:
        vec.append('-{}'.format(PN[2]))
    elif i == PN[3]:
        vec.append('-{}'.format(PN[3]))
    elif i == PN[4]:
        vec.append('-{}'.format(PN[4]))
    elif i == PN[5]:
        vec.append('+{}'.format(PN[5]))
    elif i == PN[6]:
        vec.append('+{}'.format(PN[6]))

sum = 0
for i in range(len(vec)):
    sum = sum + float(vec[i])
average = sum / len(vec)
average


# 19년 4월 보건위생 PN 계산 ==========================================================================
PN = health_2019_04['vector']


vec = []
for i in PN:
    if i == PN[0]:
        vec.append('-{}'.format(PN[0]))
    elif i == PN[1]:
        vec.append('-{}'.format(PN[1]))
    elif i == PN[2]:
        vec.append('+{}'.format(PN[2]))
    elif i == PN[3]:
        vec.append('-{}'.format(PN[3]))
    elif i == PN[4]:
        vec.append('-{}'.format(PN[4]))
    elif i == PN[5]:
        vec.append('+{}'.format(PN[5]))

sum = 0
for i in range(len(vec)):
    sum = sum + float(vec[i])
average = sum / len(vec)
average


# 19년 5월 보건위생 PN 계산 ==========================================================================
PN = health_2019_05['vector'] 


vec = []
for i in PN:
    if i == PN[0]:
        vec.append('+{}'.format(PN[0]))
    elif i == PN[1]:
        vec.append('+{}'.format(PN[1]))
    elif i == PN[2]:
        vec.append('+{}'.format(PN[2]))
    elif i == PN[3]:
        vec.append('-{}'.format(PN[3]))
    elif i == PN[4]:
        vec.append('+{}'.format(PN[4]))
    elif i == PN[5]:
        vec.append('+{}'.format(PN[5]))
    elif i == PN[6]:
        vec.append('+{}'.format(PN[6]))
    elif i == PN[7]:
        vec.append('+{}'.format(PN[7]))

sum = 0
for i in range(len(vec)):
    sum = sum + float(vec[i])
average = sum / len(vec)
average


# 20년 2월 보건위생 PN 계산 ==========================================================================
PN = health_2020_02['vector']


vec = []
for i in PN:
    if i == PN[0]:
        vec.append('-{}'.format(PN[0]))
    elif i == PN[1]:
        vec.append('-{}'.format(PN[1]))
    elif i == PN[2]:
        vec.append('-{}'.format(PN[2]))
    elif i == PN[3]:
        vec.append('-{}'.format(PN[3]))
    elif i == PN[4]:
        vec.append('-{}'.format(PN[4]))
    elif i == PN[5]:
        vec.append('-{}'.format(PN[5]))
    elif i == PN[6]:
        vec.append('+{}'.format(PN[6]))

sum = 0
for i in range(len(vec)):
    sum = sum + float(vec[i])
average = sum / len(vec)
average


# 20년 3월 보건위생 PN 계산 ==========================================================================
PN = health_2020_03['vector'] 


vec = []
for i in PN:
    if i == PN[0]:
        vec.append('-{}'.format(PN[0]))
    elif i == PN[1]:
        vec.append('+{}'.format(PN[1]))
    elif i == PN[2]:
        vec.append('-{}'.format(PN[2]))
    elif i == PN[3]:
        vec.append('-{}'.format(PN[3]))
    elif i == PN[4]:
        vec.append('-{}'.format(PN[4]))
    elif i == PN[5]:
        vec.append('-{}'.format(PN[5]))
    elif i == PN[6]:
        vec.append('-{}'.format(PN[6]))

sum = 0
for i in range(len(vec)):
    sum = sum + float(vec[i])
average = sum / len(vec)
average


# 20년 4월 보건위생 PN 계산 ==========================================================================
PN = health_2020_04['vector'] 

vec = []
for i in PN:
    if i == PN[0]:
        vec.append('+{}'.format(PN[0]))
    elif i == PN[1]:
        vec.append('-{}'.format(PN[1]))
    elif i == PN[2]:
        vec.append('-{}'.format(PN[2]))
    elif i == PN[3]:
        vec.append('-{}'.format(PN[3]))
    elif i == PN[4]:
        vec.append('-{}'.format(PN[4]))
    elif i == PN[5]:
        vec.append('-{}'.format(PN[5]))
    elif i == PN[6]:
        vec.append('-{}'.format(PN[6]))
    elif i == PN[7]:
        vec.append('-{}'.format(PN[7]))
    elif i == PN[8]:
        vec.append('-{}'.format(PN[8]))

sum = 0
for i in range(len(vec)):
    sum = sum + float(vec[i])
average = sum / len(vec)
average


# 20년 5월 보건위생 PN 계산 ==========================================================================

PN = health_2020_05['vector'] 


vec = []
for i in PN:
    if i == PN[0]:
        vec.append('+{}'.format(PN[0]))
    elif i == PN[1]:
        vec.append('+{}'.format(PN[1]))
    elif i == PN[2]:
        vec.append('-{}'.format(PN[2]))
    elif i == PN[3]:
        vec.append('-{}'.format(PN[3]))
    elif i == PN[4]:
        vec.append('-{}'.format(PN[4]))

sum = 0
for i in range(len(vec)):
    sum = sum + float(vec[i])
average = sum / len(vec)
average


# 19년 2월 레저 PN 계산 ==========================================================================

PN = leisure_2019_02['vector'] 


vec = []
for i in PN:
    if i == PN[0]:
        vec.append('-{}'.format(PN[0]))
    elif i == PN[1]:
        vec.append('+{}'.format(PN[1]))
    elif i == PN[2]:
        vec.append('+{}'.format(PN[2]))
    elif i == PN[3]:
        vec.append('+{}'.format(PN[3]))
    elif i == PN[4]:
        vec.append('+{}'.format(PN[4]))
    elif i == PN[5]:
        vec.append('-{}'.format(PN[5]))
    elif i == PN[6]:
        vec.append('+{}'.format(PN[6]))

sum = 0
for i in range(len(vec)):
    sum = sum + float(vec[i])
average = sum / len(vec)
average


# 19년 3월 레저 PN 계산 ==========================================================================

PN = leisure_2019_03['vector'] 


vec = []
for i in PN:
    if i == PN[0]:
        vec.append('-{}'.format(PN[0]))
    elif i == PN[1]:
        vec.append('-{}'.format(PN[1]))
    elif i == PN[2]:
        vec.append('+{}'.format(PN[2]))
    elif i == PN[3]:
        vec.append('+{}'.format(PN[3]))
    elif i == PN[4]:
        vec.append('+{}'.format(PN[4]))
    elif i == PN[5]:
        vec.append('-{}'.format(PN[5]))

sum = 0
for i in range(len(vec)):
    sum = sum + float(vec[i])
average = sum / len(vec)
average


# 19년 4월 레저 PN 계산 ==========================================================================

PN = leisure_2019_04['vector'] 


vec = []
for i in PN:
    if i == PN[0]:
        vec.append('+{}'.format(PN[0]))
    elif i == PN[1]:
        vec.append('+{}'.format(PN[1]))
    elif i == PN[2]:
        vec.append('+{}'.format(PN[2]))
    elif i == PN[3]:
        vec.append('-{}'.format(PN[3]))
    elif i == PN[4]:
        vec.append('+{}'.format(PN[4]))
    elif i == PN[5]:
        vec.append('+{}'.format(PN[5]))
    elif i == PN[6]:
        vec.append('-{}'.format(PN[6]))
        
sum = 0
for i in range(len(vec)):
    sum = sum + float(vec[i])
average = sum / len(vec)
average


# 19년 5월 레저 PN 계산 ==========================================================================

PN = leisure_2019_05['vector'] 


vec = []
for i in PN:
    if i == PN[0]:
        vec.append('+{}'.format(PN[0]))
    elif i == PN[1]:
        vec.append('+{}'.format(PN[1]))
    elif i == PN[2]:
        vec.append('+{}'.format(PN[2]))
    elif i == PN[3]:
        vec.append('+{}'.format(PN[3]))
    elif i == PN[4]:
        vec.append('+{}'.format(PN[4]))
    elif i == PN[5]:
        vec.append('+{}'.format(PN[5]))
    elif i == PN[6]:
        vec.append('+{}'.format(PN[6]))
        
sum = 0
for i in range(len(vec)):
    sum = sum + float(vec[i])
average = sum / len(vec)
average


# 20년 2월 레저 PN 계산 ==========================================================================

PN = leisure_2020_02['vector'] 


vec = []
for i in PN:
    if i == PN[0]:
        vec.append('+{}'.format(PN[0]))
    elif i == PN[1]:
        vec.append('+{}'.format(PN[1]))
    elif i == PN[2]:
        vec.append('+{}'.format(PN[2]))
    elif i == PN[3]:
        vec.append('+{}'.format(PN[3]))
    elif i == PN[4]:
        vec.append('+{}'.format(PN[4]))
    elif i == PN[5]:
        vec.append('+{}'.format(PN[5]))
    elif i == PN[6]:
        vec.append('+{}'.format(PN[6]))
        
sum = 0
for i in range(len(vec)):
    sum = sum + float(vec[i])
average = sum / len(vec)
average


# 20년 3월 레저 PN 계산 ==========================================================================

PN = leisure_2020_03['vector'] 


vec = []
for i in PN:
    if i == PN[0]:
        vec.append('+{}'.format(PN[0]))
    elif i == PN[1]:
        vec.append('+{}'.format(PN[1]))
    elif i == PN[2]:
        vec.append('+{}'.format(PN[2]))
    elif i == PN[3]:
        vec.append('+{}'.format(PN[3]))
    elif i == PN[4]:
        vec.append('+{}'.format(PN[4]))
    elif i == PN[5]:
        vec.append('+{}'.format(PN[5]))

        
sum = 0
for i in range(len(vec)):
    sum = sum + float(vec[i])
average = sum / len(vec)
average


# 20년 4월 레저 PN 계산 ==========================================================================

PN = leisure_2020_04['vector'] 


vec = []
for i in PN:
    if i == PN[0]:
        vec.append('+{}'.format(PN[0]))
    elif i == PN[1]:
        vec.append('+{}'.format(PN[1]))
    elif i == PN[2]:
        vec.append('+{}'.format(PN[2]))
    elif i == PN[3]:
        vec.append('+{}'.format(PN[3]))
    elif i == PN[4]:
        vec.append('+{}'.format(PN[4]))
    elif i == PN[5]:
        vec.append('-{}'.format(PN[5]))
    elif i == PN[6]:
        vec.append('-{}'.format(PN[6]))
        
sum = 0
for i in range(len(vec)):
    sum = sum + float(vec[i])
average = sum / len(vec)
average


# 20년 5월 레저 PN 계산 ==========================================================================

PN = leisure_2020_05['vector']


vec = []
for i in PN:
    if i == PN[0]:
        vec.append('-{}'.format(PN[0]))
    elif i == PN[1]:
        vec.append('+{}'.format(PN[1]))
    elif i == PN[2]:
        vec.append('+{}'.format(PN[2]))
    elif i == PN[3]:
        vec.append('+{}'.format(PN[3]))
        
sum = 0
for i in range(len(vec)):
    sum = sum + float(vec[i])
average = sum / len(vec)
average

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


# 4. COVID 변수

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

# 4-2) COVID 변수 추가

covid=pd.read_csv('c:/data/covid.csv')

#오프라인 숙박 COVID 컬럼 추가 =======================================================
off_acc = pd.read_csv('c:/data/off_acco.csv')
off_acc1 = off_acc[121:]
off_acco2020 = pd.merge(off_acc1, covid)
off_acc2 = off_acc[0:121]
off_acc1 = pd.concat([off_acc2, off_acco2020], join='outer').fillna(0)
off_acc1 = off_acc1.astype({'COVID' : 'int'})
off_acc1 = off_acc1[['DATE', 'PN', 'CN', 'COVID']]
off_acc1.to_csv('c:/data/off_acc1.csv')
off_acc1.reset_index(drop=True, inplace=True)
off_acc1.to_csv('c:/data/off_acc1.csv',index=False)
off_acc1

#오프라인 문화취미 COVID 컬럼 추가 =======================================================
off_cul = pd.read_csv('c:/data/off_cul.csv')
off_cul1 = off_cul.reset_index()
off_cul2 = off_cul1[121:]
off_cul2 = off_cul2.reset_index(drop=True)
off_cul3 = pd.merge(off_cul2, covid, left_index=True, right_index=True)
del off_cul3['DATE_x']
off_cul3 = off_cul3[['DATE_y', 'PN', 'CN', 'COVID']]
off_cul3 = off_cul3.rename(columns={'DATE_y':'DATE', 'PN':'PN', 'CN':'CN', 'COVID':'COVID'})
off_cul4 = off_cul1[:121]
off_cul5 = pd.concat([off_cul4, off_cul3], join='outer').fillna(0)
off_cul5 = off_cul5[['DATE', 'PN', 'CN', 'COVID']]
off_cul5 = off_cul5.astype({'COVID' : 'int'})
off_cul5.reset_index(drop=True, inplace=True)
off_cul5.to_csv("c:/data/off_cul1.csv")
off_cul5

#오프라인 식품 COVID 컬럼 추가 =======================================================
off_food = pd.read_csv('c:/data/off_food.csv')
off_food1 = off_food[121:]
off_food2020 = pd.merge(off_food1, covid)
off_food1 = off_food[:121]
off_food2 = pd.concat([off_food1, off_food2020], join='outer').fillna(0)
off_food2 = off_food2[['DATE', 'PN', 'CN', 'COVID']]
off_food2 = off_food2.astype({'COVID' : 'int'})
off_food2.reset_index(drop=True, inplace=True)
off_food2.to_csv("c:/data/off_food2.csv")
off_food2

#오프라인 레저 COVID 컬럼 추가 =======================================================
off_lei = pd.read_csv('c:/data/off_lei.csv')
off_lei1 = off_lei[121:]
off_lei2 = pd.merge(off_lei1, covid)
off_lei3 = off_lei[:121]
off_lei3 = pd.concat([off_lei3, off_lei2], join='outer').fillna(0)
off_lei3 = off_lei3[['DATE', 'PN', 'CN', 'COVID']]
off_lei3 = off_lei3.astype({'COVID' : 'int'})
off_lei3.reset_index(drop=True, inplace=True)
off_lei3.to_csv('c:/data/off_lei1.csv')
off_lei3

#오프라인 의료기관 COVID 컬럼 추가 =======================================================
off_medi = pd.read_csv('c:/data/off_medi.csv')
off_medi0 = off_medi[121:]
off_medi1 = pd.merge(off_medi, covid)
off_medi2 = off_medi[:121]
off_medi3 = pd.concat([off_medi2, off_medi1], join='outer').fillna(0)
off_medi3 = off_medi3[['DATE', 'PN', 'CN', 'COVID']]
off_medi3 = off_medi3.astype({'COVID' : 'int'})
off_medi3.reset_index(drop=True, inplace=True)
off_medi3.to_csv('c:/data/off_medi1.csv',index=False)
off_medi3

#오프라인 보건위생 COVID 컬럼 추가 =======================================================
off_sani = pd.read_csv('c:/data/off_sani.csv')
off_sani1 = off_sani[121:]
off_sani1 = off_sani1.reset_index(drop=True)
off_sani2 = pd.merge(off_sani1, covid)
off_sani3 = off_sani[:121]
off_sani3 = pd.concat([off_sani3, off_sani2], join='outer').fillna(0)
off_sani3 = off_sani3[['DATE', 'PN', 'CN', 'COVID']]
off_sani3 = off_sani3.astype({'COVID' : 'int'})
off_sani3.reset_index(drop=True, inplace=True)
off_sani3.to_csv("c:/data/off_sani1.csv",index=False)
off_sani3

#온라인 숙박 COVID 컬럼 추가 =======================================================
on_acc = pd.read_csv('c:/data/on_acco.csv')
on_acc1 = on_acc[121:]
on_acc1 = on_acc1.reset_index(drop=True)
on_acc2 = pd.merge(on_acc1, covid, left_index=True, right_index=True)
del on_acc2['DATE_y']
on_acc2 = on_acc2.rename(columns={'DATE_x':'DATE', 'PN':'PN', 'CN':'CN'})
on_acc2 = on_acc2[['DATE', 'PN', "CN", 'COVID']]
on_acc3 = on_acc[:121]
on_acc3 = pd.concat([on_acc3, on_acc2], join='outer').fillna(0)
on_acc3 = on_acc3[['DATE', 'PN', 'CN', 'COVID']]
on_acc3 = on_acc3.astype({'COVID' : 'int'})
on_acc3.reset_index(drop=True, inplace=True)
on_acc3.to_csv("c:/data/on_acc1.csv", index=False)
on_acc3

#온라인 문화취미 COVID 컬럼 추가 =======================================================
on_cul = pd.read_csv('c:/data/on_cul.csv')
on_cul1 = on_cul.reset_index()
on_cul2 = on_cul1[120:]
on_cul2 = on_cul2.reset_index(drop=True)
on_cul3 = pd.merge(on_cul2, covid, left_index=True, right_index=True)
del on_cul3['DATE_y']
on_cul3 = on_cul3.rename(columns = {'DATE_x':'DATE', 'CN':'CN', 'PN':'PN', 'COVID':'COVID'})
on_cul4 = on_cul1[:120]
on_cul4= on_cul4.reset_index(drop=True)
on_cul5 = pd.concat([on_cul4, on_cul3],).fillna(0)
on_cul5 = on_cul5[['DATE', 'PN', 'CN', 'COVID']]
on_cul5 = on_cul5.astype({'COVID' : 'int'})
on_cul5 = on_cul5.reset_index(drop=True)
on_cul5.to_csv("c:/data/on_cul1.csv",index=False)
on_cul5

#온라인 식품 COVID 컬럼 추가 =======================================================
on_food = pd.read_csv('c:/data/on_food.csv')
on_food1 = on_food[121:]
on_food1 = on_food1.reset_index(drop=True)
on_food2 = pd.merge(on_food1, covid, left_index=True, right_index=True)
del on_food2['DATE_y']
on_food2 = on_food2.rename(columns = {'DATE_x':'DATE', 'CN':'CN', 'PN':'PN', 'COVID':'COVID'})
on_food3 = on_food[:121]
on_food4 = pd.concat([on_food3, on_food2], join = 'outer').fillna(0)
on_food4 = on_food4[['DATE', 'PN', 'CN', 'COVID']]
on_food4 = on_food4.astype({'COVID' : 'int'})
on_food4 = on_food4.reset_index(drop=True)
on_food4.to_csv('c:/data/on_food1.csv',index=False)
on_food4

#온라인 레저 COVID 컬럼 추가 =======================================================
on_lei = pd.read_csv('c:/data/on_lei.csv')
on_lei1 = on_lei[119:]
on_lei1 = on_lei1.reset_index(drop=True)
on_lei2 = pd.merge(on_lei1, covid, left_index=True, right_index=True)
del on_lei2['DATE_y']
on_lei2 = on_lei2.rename(columns = {'DATE_x':'DATE', 'CN':'CN', 'PN':'PN', 'COVID':'COVID'})
on_lei3 = on_lei[:119]
on_lei4 = pd.concat([on_lei3, on_lei2], join = 'outer').fillna(0)
on_lei4 = on_lei4[['DATE', 'PN', 'CN', 'COVID']]
on_lei4 = on_lei4.astype({'COVID' : 'int'})
on_lei4.reset_index(drop=True, inplace=True)
on_lei4.to_csv('c:/data/on_lei1.csv', index=False)
on_lei4

#온라인 보건위생 COVID 컬럼 추가 =======================================================
on_sani0 = pd.read_csv('c:/data/on_sani.csv')
on_sani1 = on_sani0[121:]
on_sani1 = on_sani1.reset_index(drop=True)
on_sani2 = pd.merge(on_sani1, covid, left_index=True, right_index=True)
del on_sani2['DATE_y']
on_sani2 = on_sani2.rename(columns = {'DATE_x':'DATE', 'CN':'CN', 'PN':'PN', 'COVID':'COVID'})
on_sani3 = on_sani0[:121]
on_sani4 = pd.concat([on_sani3, on_sani2], join = 'outer').fillna(0)
on_sani4 = on_sani4[['DATE', 'PN', 'CN', 'COVID']]
on_sani4 = on_sani4.astype({'COVID' : 'int'})
on_sani4.reset_index(drop=True, inplace=True)
on_sani4.to_csv('c:/data/on_sani1.csv', index=False)
on_sani4

# 4-3) 데이터 분할

z = pd.read_csv("c:/big/corona/g/off_acc1.csv",)
s = pd.read_csv("c:/big/corona/g/off_cul1.csv")
d = pd.read_csv("c:/big/corona/g/off_food2.csv")
f = pd.read_csv("c:/big/corona/g/off_lei1.csv")
g = pd.read_csv("c:/big/corona/g/off_medi1.csv")
h = pd.read_csv("c:/big/corona/g/off_sani1.csv")
q = pd.read_csv("c:/big/corona/g/on_acc1.csv")
w = pd.read_csv("c:/big/corona/g/on_cul1.csv")
e = pd.read_csv("c:/big/corona/g/on_food1.csv")
r = pd.read_csv("c:/big/corona/g/on_lei1.csv")
t = pd.read_csv("c:/big/corona/g/on_sani1.csv")

# off_acc 데이터 분할
z[:int(len(z)*0.6)].to_csv("c:/big/corona/off_acci(train).csv", mode='w', index=False, encoding='utf-8')
train_data = pd.read_csv('c:/big/corona/off_acci(train).csv')
z[int(len(z)*0.6):].to_csv("C:/big/corona/off_acci(test).csv", mode='w', index=False, encoding='utf-8')   
test_data = pd.read_csv('c:/big/corona/off_acci(test).csv')

# off_cul 데이터 분할
s[:int(len(s)*0.6)].to_csv("c:/big/corona/off_cul(train).csv", mode='w', index=False, encoding='utf-8')
train_data = pd.read_csv('c:/big/corona/off_cul(train).csv')
s[int(len(s)*0.6):].to_csv("C:/big/corona/off_cul(test).csv", mode='w', index=False, encoding='utf-8')   
test_data = pd.read_csv('c:/big/corona/off_cul(test).csv')

# off_food 데이터 분할
d[:int(len(d)*0.6)].to_csv("c:/big/corona/off_food(train).csv", mode='w', index=False, encoding='utf-8')
train_data = pd.read_csv('c:/big/corona/off_food(train).csv')
d[int(len(d)*0.6):].to_csv("C:/big/corona/off_food(test).csv", mode='w', index=False, encoding='utf-8')   
test_data = pd.read_csv('c:/big/corona/off_food(test).csv')

# off_lei 데이터 분할
f[:int(len(f)*0.6)].to_csv("c:/big/corona/off_lei(train).csv", mode='w', index=False, encoding='utf-8')
train_data = pd.read_csv('c:/big/corona/off_lei(train).csv')
f[int(len(f)*0.6):].to_csv("C:/big/corona/off_lei(test).csv", mode='w', index=False, encoding='utf-8')   
test_data = pd.read_csv('c:/big/corona/off_lei(test).csv')

# off_medi 데이터 분할
g[:int(len(g)*0.6)].to_csv("c:/big/corona/off_medi(train).csv", mode='w', index=False, encoding='utf-8')
train_data = pd.read_csv('c:/big/corona/off_medi(train).csv')
g[int(len(g)*0.6):].to_csv("C:/big/corona/off_medi(test).csv", mode='w', index=False, encoding='utf-8')   
test_data = pd.read_csv('c:/big/corona/off_medi(test).csv')

# off_sani 데이터 분할
h[:int(len(h)*0.6)].to_csv("c:/big/corona/off_sani(train).csv", mode='w', index=False, encoding='utf-8')
train_data = pd.read_csv('c:/big/corona/off_sani(train).csv')
h[int(len(h)*0.6):].to_csv("C:/big/corona/off_sani(test).csv", mode='w', index=False, encoding='utf-8')   
test_data = pd.read_csv('c:/big/corona/off_sani(test).csv')

# on_acc 데이터 분할
q[:int(len(q)*0.6)].to_csv("c:/big/corona/on_acc(train).csv", mode='w', index=False, encoding='utf-8')
train_data = pd.read_csv('c:/big/corona/on_acc(train).csv')
q[int(len(q)*0.6):].to_csv("C:/big/corona/on_acc(test).csv", mode='w', index=False, encoding='utf-8')   
test_data = pd.read_csv('c:/big/corona/on_acc(test).csv')

# on_cul 데이터 분할
w[:int(len(w)*0.6)].to_csv("c:/big/corona/on_cul(train).csv", mode='w', index=False, encoding='utf-8')
train_data = pd.read_csv('c:/big/corona/on_cul(train).csv')
w[int(len(w)*0.6):].to_csv("C:/big/corona/on_cul(test).csv", mode='w', index=False, encoding='utf-8')   
test_data = pd.read_csv('c:/big/corona/on_cul(test).csv')

# on_food 데이터 분할
e[:int(len(e)*0.6)].to_csv("c:/big/corona/on_food(train).csv", mode='w', index=False, encoding='utf-8')
train_data = pd.read_csv('c:/big/corona/on_food(train).csv')
e[int(len(e)*0.6):].to_csv("C:/big/corona/on_food(test).csv", mode='w', index=False, encoding='utf-8')   
test_data = pd.read_csv('c:/big/corona/on_food(test).csv')

# on_lei 데이터 분할
r[:int(len(r)*0.6)].to_csv("c:/big/corona/on_lei(train).csv", mode='w', index=False, encoding='utf-8')
train_data = pd.read_csv('c:/big/corona/on_lei(train).csv')
r[int(len(r)*0.6):].to_csv("C:/big/corona/on_lei(test).csv", mode='w', index=False, encoding='utf-8')   
test_data = pd.read_csv('c:/big/corona/on_lei(test).csv')


# on_sani 데이터 분할
t[:int(len(t)*0.6)].to_csv("c:/big/corona/on_sani(train).csv", mode='w', index=False, encoding='utf-8')
train_data = pd.read_csv('c:/big/corona/on_sani(train).csv')
t[int(len(t)*0.6):].to_csv("C:/big/corona/on_sani(test).csv", mode='w', index=False, encoding='utf-8')   
test_data = pd.read_csv('c:/big/corona/on_sani(test).csv')


# 5) 회귀분석 상관분석

# Rstudio에서 회귀분석과 상관분석 진행
# 온라인 매출과 업종별 긍정부정정도와의 관계 확인하기

# CN: 오프라인/온라인 매출건수 
# DATE:시간
# PN: 업종에 대한 긍정부정정도 (업종에 대한 긍정부정 게시량과 신문기사에서의 긍정부정 키워드 벡터값)
# COVID: 코로나의 영향

'''
library(ggplot2)
off_acco<-read.csv("C:/data/off_acc1.csv",header=T,encoding = 'utf-8')
off_cul<-read.csv("C:/data/off_cul1.csv",header=T,encoding = 'utf-8')
off_food<-read.csv("C:/data/off_food2.csv",header=T,encoding = 'utf-8')
off_lei<-read.csv("C:/data/off_lei1.csv",header=T,encoding = 'utf-8')
off_medi<-read.csv("C:/data/off_medi1.csv",header=T,encoding = 'utf-8')
off_sani<-read.csv("C:/data/off_sani1.csv",header=T,encoding = 'utf-8')

## 오프라인 숙박 ====================================================================
## 회귀분석
fit = lm(CN ~ DATE + PN + COVID, data= off_acco)
summary(fit)
coef(fit)

par(mfrow = c(2, 2))
plot(CN ~ PN + COVID, data= off_acco)

## 상관분석
cor.test(off_acco$CN,off_acco$PN)
cor.test(off_acco$CN,off_acco$COVID)


## 오프라인 문화취미 ====================================================================
## 회귀분석
fit = lm(CN ~ DATE + PN + COVID, data= off_cul)
summary(fit)
coef(fit)

par(mfrow = c(2, 2))
plot(CN ~ PN + COVID, data= off_cul)

## 상관분석
cor.test(off_cul$CN,off_cul$PN)
cor.test(off_cul$CN,off_cul$COVID)


## 오프라인 식품 ====================================================================
## 회귀분석
fit = lm(CN ~ DATE + PN + COVID, data= off_food)
summary(fit)
coef(fit)

par(mfrow = c(2, 2))
plot(CN ~ PN+COVID, data= off_food)

## 상관분석
cor.test(off_food$CN,off_food$PN)
cor.test(off_food$CN,off_food$COVID)


## 오프라인 레저 ====================================================================
## 회귀분석
fit = lm(CN ~ DATE + PN + COVID, data= off_lei)
summary(fit)
coef(fit)

par(mfrow = c(2, 2))
plot(CN ~ PN+COVID, data= off_lei)

## 상관분석
cor.test(off_lei$CN,off_lei$PN)
cor.test(off_lei$CN,off_lei$COVID)

## 오프라인 의료기관 ====================================================================
## 회귀분석
fit = lm(CN ~ DATE + PN+COVID, data= off_medi)
summary(fit)
coef(fit)

par(mfrow = c(2, 2))
plot(CN ~ PN+COVID, data= off_medi)

## 상관분석
cor.test(off_medi$CN,off_medi$PN)
cor.test(off_medi$CN,off_medi$COVID)


## 오프라인 보건위생 ====================================================================
## 회귀분석
fit = lm(CN ~ DATE + PN+COVID, data= off_sani)
summary(fit)
coef(fit)

par(mfrow = c(2, 2))
plot(CN ~ PN+COVID, data= off_sani)

## 상관분석
cor.test(off_sani$CN,off_sani$PN)
cor.test(off_sani$CN,off_sani$COVID)


on_acco<-read.csv("C:/data/on_acc1.csv",header=T,encoding = 'utf-8')
on_cul<-read.csv("C:/data/on_cul1.csv",header=T,encoding = 'utf-8')
on_food<-read.csv("C:/data/on_food1.csv",header=T,encoding = 'utf-8')
on_lei<-read.csv("C:/data/on_lei1.csv",header=T,encoding = 'utf-8')
on_sani<-read.csv("C:/data/on_sani1.csv",header=T,encoding = 'utf-8')

## 온라인 숙박 ====================================================================
## 회귀분석
fit = lm(CN ~ DATE + PN+COVID, data= on_acco)
summary(fit)
coef(fit)

par(mfrow = c(2, 2))
plot(CN ~ PN+COVID, data= on_acco)


## 상관분석
cor.test(on_acco$CN,on_acco$PN)
cor.test(on_acco$CN,on_acco$COVID)


## 온라인 문화취미 ====================================================================
## 회귀분석
fit = lm(CN ~ DATE + PN+COVID, data= on_cul)
summary(fit)
coef(fit)

par(mfrow = c(2, 2))
plot(CN ~ PN+COVID, data= on_cul)


## 상관분석
cor.test(on_cul$CN,on_cul$PN)
cor.test(on_cul$CN,on_cul$COVID)


## 온라인 식품 ====================================================================
## 회귀분석
fit = lm(CN ~ DATE + PN +COVID, data= on_food)
summary(fit)
coef(fit)

par(mfrow = c(2, 2))
plot(CN ~ PN+COVID, data= on_food)


## 상관분석
cor.test(on_food$CN,on_food$PN)
cor.test(on_food$CN,on_food$COVID)


## 온라인 레저 ====================================================================
## 회귀분석
fit = lm(CN ~ DATE + PN+COVID, data= on_lei)
summary(fit)
coef(fit)

par(mfrow = c(2, 2))
plot(CN ~ PN+COVID, data= on_lei)


## 상관분석
cor.test(on_lei$CN,on_lei$PN)
cor.test(on_lei$CN,on_lei$COVID)


## 온라인 보건위생 ====================================================================
## 회귀분석
fit = lm(CN ~ DATE + PN+COVID, data= on_sani)
summary(fit)
coef(fit)

par(mfrow = c(2, 2))
plot(CN ~ PN+COVID, data= on_sani)


## 상관분석
cor.test(on_sani$CN,on_sani$PN)
cor.test(on_sani$CN,on_sani$COVID)

'''


# 6. 이산형 데이터 변환
# 연속형 데이터를 이산형 데이터로 변환

'''
off_data=pd.read_csv("C:/data/off_data.csv", encoding='utf-8')
on_data=pd.read_csv("C:/data/on_data.csv", encoding='utf-8')

## CN변수: 이전보다 50%이상 감소/증가한 경우 1, 그렇지 않은 경우 0
## PN변수: 음수인 경우 0, 양수인 경우 1로 분류
## COVID 변수: 0인 경우 0으로, 0이외의 값 중 50%분위값 10019를 기준으로 1,2로 분류
np.percentile(off_data['COVID'][off_data['COVID']!=0],50)
'''

## 오프라인 숙박==========================================================================
data=pd.read_csv("C:/data/off_acc1.csv", encoding='utf-8')

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
data=pd.read_csv("C:/data/off_cul1.csv", encoding='utf-8')

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
data=pd.read_csv("C:/data/off_food2.csv", encoding='utf-8')

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
data=pd.read_csv("C:/data/off_lei1.csv", encoding='utf-8')

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
data=pd.read_csv("C:/data/off_medi1.csv", encoding='utf-8')

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
data=pd.read_csv("C:/data/off_sani1.csv", encoding='utf-8')

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
data=pd.read_csv("C:/data/on_acc1.csv", encoding='utf-8')

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
data=pd.read_csv("C:/data/on_cul1.csv", encoding='utf-8')

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
data=pd.read_csv("C:/data/on_food1.csv", encoding='utf-8')

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
data=pd.read_csv("C:/data/on_lei1.csv", encoding='utf-8')

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
data=pd.read_csv("C:/data/on_sani1.csv", encoding='utf-8')

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


# 7. 모델적용

# 7-1) Ridge Lasso Regression

from sklearn.linear_model import Ridge, RidgeCV, Lasso, LassoCV, ElasticNet,ElasticNetCV
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# 오프라인 숙박================================================================
data=pd.read_csv("C:/data/off_acc1.csv", encoding='utf-8')
data=data.sample(frac=1).reset_index(drop=True)
train=data[:int(len(data)*0.6)]
test=data[int(len(data)*0.6):]

X_train = train[['PN','COVID']]
y_train = train['CN']
X_test = test[['PN','COVID']]
y_test = test['CN']

# Ridge
ridge = Ridge()
ridge.fit(X_train, y_train)

# Lasso
lasso = Lasso()
lasso.fit(X_train, y_train)

# Ridge 정확도
r_off_acc_train_score = ridge.score(X_train, y_train)
r_off_acc_test_score = ridge.score(X_test, y_test)
display('Ridge', r_off_acc_train_score, r_off_acc_test_score)

# Lasso 정확도
l_off_acc_train_score = lasso.score(X_train, y_train)
l_off_acc_test_score = lasso.score(X_test, y_test)
display('Lasso', l_off_acc_train_score, l_off_acc_test_score)

alphas = [10, 1, 0.1, 0.01, 0.001, 0.0001]
train_scores = []
test_scores = []
ws = []

for alpha in alphas:
    lasso = Lasso(alpha=alpha)
    lasso.fit(X_train, y_train)
    ws.append(lasso.coef_)
    
    s1 = lasso.score(X_train, y_train)
    s2 = lasso.score(X_test, y_test)
    train_scores.append(s1)
    test_scores.append(s2)
    
display(train_scores, test_scores, ws)


# lasso
# run Lasso cross validation test to find the best alpha based on training data
lasso_cv=LassoCV(alphas=alphas, cv=5)
model = lasso_cv.fit(X_train, y_train)
print(model.alpha_)

# calculate Lasso R2, MSE, RMSE from test data
lasso=Lasso(alpha=10).fit(X_train, y_train)
ypred_lasso = lasso.predict(X_test)
l_off_acc_score_lasso = lasso.score(X_test, y_test)
l_off_acc_mse_lasso = mean_squared_error(y_test, ypred_lasso)
print("Final Result: Lasso R2:{0:.3f}, MSE:{1:.2f}, RMSE:{2:.2f}".format(l_off_acc_score_lasso, l_off_acc_mse_lasso, np.sqrt(l_off_acc_mse_lasso)))

# ridge
# run Ridge cross validation test to find the best alpha based on training data
ridge_cv=RidgeCV(alphas=alphas, cv=5)
model = ridge_cv.fit(X_train, y_train)
print(model.alpha_)

# calculate Ridge R2, MSE, RMSE from test data
ridge=Ridge(alpha=0.0001).fit(X_train, y_train)
ypred_ridge = ridge.predict(X_test)
r_off_acc_score_ridge = ridge.score(X_test, y_test)
r_off_acc_mse_ridge = mean_squared_error(y_test, ypred_ridge)
print("Final Result: Ridge R2:{0:.3f}, MSE:{1:.2f}, RMSE:{2:.2f}".format(r_off_acc_score_ridge, r_off_acc_mse_ridge, np.sqrt(r_off_acc_mse_ridge)))


# 오프라인 문화================================================================
data=pd.read_csv("C:/data/off_cul1.csv", encoding='utf-8')
data=data.sample(frac=1).reset_index(drop=True)
train=data[:int(len(data)*0.6)]
test=data[int(len(data)*0.6):]

X_train = train[['PN','COVID']]
y_train = train['CN']
X_test = test[['PN','COVID']]
y_test = test['CN']

# Ridge
ridge = Ridge()
ridge.fit(X_train, y_train)

# Lasso
lasso = Lasso()
lasso.fit(X_train, y_train)

# Ridge 정확도
r_off_cul_train_score = ridge.score(X_train, y_train)
r_off_cul_test_score = ridge.score(X_test, y_test)
display('Ridge', r_off_cul_train_score, r_off_cul_test_score)

# Lasso 정확도
l_off_cul_train_score = lasso.score(X_train, y_train)
l_off_cul_test_score = lasso.score(X_test, y_test)
display('Lasso', l_off_cul_train_score, l_off_cul_test_score)

alphas = [10, 1, 0.1, 0.01, 0.001, 0.0001]
train_scores = []
test_scores = []
ws = []

for alpha in alphas:
    lasso = Lasso(alpha=alpha)
    lasso.fit(X_train, y_train)
    ws.append(lasso.coef_)
    
    s1 = lasso.score(X_train, y_train)
    s2 = lasso.score(X_test, y_test)
    train_scores.append(s1)
    test_scores.append(s2)
    
display(train_scores, test_scores, ws)

# lasso
# run Lasso cross validation test to find the best alpha based on training data
lasso_cv=LassoCV(alphas=alphas, cv=5)
model = lasso_cv.fit(X_train, y_train)
print(model.alpha_)

# calculate Lasso R2, MSE, RMSE from test data
lasso=Lasso(alpha=0.0001).fit(X_train, y_train)
ypred_lasso = lasso.predict(X_test)
l_off_cul_score_lasso = lasso.score(X_test, y_test)
l_off_cul_mse_lasso = mean_squared_error(y_test, ypred_lasso)
print("Final Result: Lasso R2:{0:.3f}, MSE:{1:.2f}, RMSE:{2:.2f}".format(l_off_cul_score_lasso, l_off_cul_mse_lasso, np.sqrt(l_off_cul_mse_lasso)))

# ridge
# run Ridge cross validation test to find the best alpha based on training data
ridge_cv=RidgeCV(alphas=alphas, cv=5)
model = ridge_cv.fit(X_train, y_train)
print(model.alpha_)

# calculate Ridge R2, MSE, RMSE from test data
ridge=Ridge(alpha=0.0001).fit(X_train, y_train)
ypred_ridge = ridge.predict(X_test)
r_off_cul_score_ridge = ridge.score(X_test, y_test)
r_off_cul_mse_ridge = mean_squared_error(y_test, ypred_ridge)
print("Final Result: Ridge R2:{0:.3f}, MSE:{1:.2f}, RMSE:{2:.2f}".format(r_off_cul_score_ridge, r_off_cul_mse_ridge, np.sqrt(r_off_cul_mse_ridge)))


# 오프라인 식품================================================================
data=pd.read_csv("C:/data/off_food2.csv", encoding='utf-8')
data=data.sample(frac=1).reset_index(drop=True)
train=data[:int(len(data)*0.6)]
test=data[int(len(data)*0.6):]

X_train = train[['PN','COVID']]
y_train = train['CN']
X_test = test[['PN','COVID']]
y_test = test['CN']

# Ridge
ridge = Ridge()
ridge.fit(X_train, y_train)

# Lasso
lasso = Lasso()
lasso.fit(X_train, y_train)

# Ridge 정확도
r_off_food_train_score = ridge.score(X_train, y_train)
r_off_food_test_score = ridge.score(X_test, y_test)
display('Ridge', r_off_food_train_score, r_off_food_test_score)

# Lasso 정확도
l_off_food_train_score = lasso.score(X_train, y_train)
l_off_food_test_score = lasso.score(X_test, y_test)
display('Lasso', l_off_food_train_score, l_off_food_test_score)

alphas = [10, 1, 0.1, 0.01, 0.001, 0.0001]
train_scores = []
test_scores = []
ws = []

for alpha in alphas:
    lasso = Lasso(alpha=alpha)
    lasso.fit(X_train, y_train)
    ws.append(lasso.coef_)
    
    s1 = lasso.score(X_train, y_train)
    s2 = lasso.score(X_test, y_test)
    train_scores.append(s1)
    test_scores.append(s2)
    
display(train_scores, test_scores, ws)


# lasso
# run Lasso cross validation test to find the best alpha based on training data
lasso_cv=LassoCV(alphas=alphas, cv=5)
model = lasso_cv.fit(X_train, y_train)
print(model.alpha_)

# calculate Lasso R2, MSE, RMSE from test data
lasso=Lasso(alpha=0.0001).fit(X_train, y_train)
ypred_lasso = lasso.predict(X_test)
l_off_food_score_lasso = lasso.score(X_test, y_test)
l_off_food_mse_lasso = mean_squared_error(y_test, ypred_lasso)
print("Final Result: Lasso R2:{0:.3f}, MSE:{1:.2f}, RMSE:{2:.2f}".format(l_off_food_score_lasso, l_off_food_mse_lasso, np.sqrt(l_off_food_mse_lasso)))

# ridge
# run Ridge cross validation test to find the best alpha based on training data
ridge_cv=RidgeCV(alphas=alphas, cv=5)
model = ridge_cv.fit(X_train, y_train)
print(model.alpha_)

# calculate Ridge R2, MSE, RMSE from test data
ridge=Ridge(alpha=0.1).fit(X_train, y_train)
ypred_ridge = ridge.predict(X_test)
r_off_food_score_ridge = ridge.score(X_test, y_test)
r_off_food_mse_ridge = mean_squared_error(y_test, ypred_ridge)
print("Final Result: Ridge R2:{0:.3f}, MSE:{1:.2f}, RMSE:{2:.2f}".format(r_off_food_score_ridge, r_off_food_mse_ridge, np.sqrt(r_off_food_mse_ridge)))


# 오프라인 레저================================================================
data=pd.read_csv("C:/data/off_lei1.csv", encoding='utf-8')
data=data.sample(frac=1).reset_index(drop=True)
train=data[:int(len(data)*0.6)]
test=data[int(len(data)*0.6):]

X_train = train[['PN','COVID']]
y_train = train['CN']
X_test = test[['PN','COVID']]
y_test = test['CN']

# Ridge
ridge = Ridge()
ridge.fit(X_train, y_train)

# Lasso
lasso = Lasso()
lasso.fit(X_train, y_train)

# Ridge 정확도
r_off_lei_train_score = ridge.score(X_train, y_train)
r_off_lei_test_score = ridge.score(X_test, y_test)
display('Ridge', r_off_lei_train_score, r_off_lei_test_score)

# Lasso 정확도
l_off_lei_train_score = lasso.score(X_train, y_train)
l_off_lei_test_score = lasso.score(X_test, y_test)
display('Lasso', l_off_lei_train_score, l_off_lei_test_score)

alphas = [10, 1, 0.1, 0.01, 0.001, 0.0001]
train_scores = []
test_scores = []
ws = []

for alpha in alphas:
    lasso = Lasso(alpha=alpha)
    lasso.fit(X_train, y_train)
    ws.append(lasso.coef_)
    
    s1 = lasso.score(X_train, y_train)
    s2 = lasso.score(X_test, y_test)
    train_scores.append(s1)
    test_scores.append(s2)
    
display(train_scores, test_scores, ws)

# lasso
# run Lasso cross validation test to find the best alpha based on training data
lasso_cv=LassoCV(alphas=alphas, cv=5)
model = lasso_cv.fit(X_train, y_train)
print(model.alpha_)

# calculate Lasso R2, MSE, RMSE from test data
lasso=Lasso(alpha=10).fit(X_train, y_train)
ypred_lasso = lasso.predict(X_test)
l_off_lei_score_lasso = lasso.score(X_test, y_test)
l_off_lei_mse_lasso = mean_squared_error(y_test, ypred_lasso)
print("Final Result: Lasso R2:{0:.3f}, MSE:{1:.2f}, RMSE:{2:.2f}".format(l_off_lei_score_lasso, l_off_lei_mse_lasso, np.sqrt(l_off_lei_mse_lasso)))

# ridge
# run Ridge cross validation test to find the best alpha based on training data
ridge_cv=RidgeCV(alphas=alphas, cv=5)
model = ridge_cv.fit(X_train, y_train)
print(model.alpha_)

# calculate Ridge R2, MSE, RMSE from test data
ridge=Ridge(alpha=10).fit(X_train, y_train)
ypred_ridge = ridge.predict(X_test)
r_off_lei_score_ridge = ridge.score(X_test, y_test)
r_off_lei_mse_ridge = mean_squared_error(y_test, ypred_ridge)
print("Final Result: Ridge R2:{0:.3f}, MSE:{1:.2f}, RMSE:{2:.2f}".format(r_off_lei_score_ridge, r_off_lei_mse_ridge, np.sqrt(r_off_lei_mse_ridge)))


# 오프라인 의료기관================================================================
data=pd.read_csv("C:/data/off_medi1.csv", encoding='utf-8')
data=data.sample(frac=1).reset_index(drop=True)
train=data[:int(len(data)*0.6)]
test=data[int(len(data)*0.6):]

X_train = train[['PN','COVID']]
y_train = train['CN']
X_test = test[['PN','COVID']]
y_test = test['CN']

# Ridge
ridge = Ridge()
ridge.fit(X_train, y_train)

# Lasso
lasso = Lasso()
lasso.fit(X_train, y_train)

# Ridge 정확도
r_off_medi_train_score = ridge.score(X_train, y_train)
r_off_medi_test_score = ridge.score(X_test, y_test)
display('Ridge', r_off_medi_train_score, r_off_medi_test_score)

# Lasso 정확도
l_off_medi_train_score = lasso.score(X_train, y_train)
l_off_medi_test_score = lasso.score(X_test, y_test)
display('Lasso', l_off_medi_train_score, l_off_medi_test_score)

alphas = [10, 1, 0.1, 0.01, 0.001, 0.0001]
train_scores = []
test_scores = []
ws = []

for alpha in alphas:
    lasso = Lasso(alpha=alpha)
    lasso.fit(X_train, y_train)
    ws.append(lasso.coef_)
    
    s1 = lasso.score(X_train, y_train)
    s2 = lasso.score(X_test, y_test)
    train_scores.append(s1)
    test_scores.append(s2)
    
display(train_scores, test_scores, ws)


# lasso
# run Lasso cross validation test to find the best alpha based on training data
lasso_cv=LassoCV(alphas=alphas, cv=5)
model = lasso_cv.fit(X_train, y_train)
print(model.alpha_)

# calculate Lasso R2, MSE, RMSE from test data
lasso=Lasso(alpha=10).fit(X_train, y_train)
ypred_lasso = lasso.predict(X_test)
l_off_medi_score_lasso = lasso.score(X_test, y_test)
l_off_medi_mse_lasso = mean_squared_error(y_test, ypred_lasso)
print("Final Result: Lasso R2:{0:.3f}, MSE:{1:.2f}, RMSE:{2:.2f}".format(l_off_medi_score_lasso, l_off_medi_mse_lasso, np.sqrt(l_off_medi_mse_lasso)))


# ridge
# run Ridge cross validation test to find the best alpha based on training data
ridge_cv=RidgeCV(alphas=alphas, cv=5)
model = ridge_cv.fit(X_train, y_train)
print(model.alpha_)

# calculate Ridge R2, MSE, RMSE from test data
ridge=Ridge(alpha=0.0001).fit(X_train, y_train)
ypred_ridge = ridge.predict(X_test)
r_off_medi_score_ridge = ridge.score(X_test, y_test)
r_off_medi_mse_ridge = mean_squared_error(y_test, ypred_ridge)
print("Final Result: Ridge R2:{0:.3f}, MSE:{1:.2f}, RMSE:{2:.2f}".format(r_off_medi_score_ridge, r_off_medi_mse_ridge, np.sqrt(r_off_medi_mse_ridge)))


# 오프라인 보건위생================================================================
data=pd.read_csv("C:/data/off_sani1.csv", encoding='utf-8')
data=data.sample(frac=1).reset_index(drop=True)
train=data[:int(len(data)*0.6)]
test=data[int(len(data)*0.6):]

X_train = train[['PN','COVID']]
y_train = train['CN']
X_test = test[['PN','COVID']]
y_test = test['CN']

# Ridge
ridge = Ridge()
ridge.fit(X_train, y_train)

# Lasso
lasso = Lasso()
lasso.fit(X_train, y_train)

# Ridge 정확도
r_off_sani_train_score = ridge.score(X_train, y_train)
r_off_sani_test_score = ridge.score(X_test, y_test)
display('Ridge', r_off_sani_train_score, r_off_sani_test_score)

# Lasso 정확도
l_off_sani_train_score = lasso.score(X_train, y_train)
l_off_sani_test_score = lasso.score(X_test, y_test)
display('Lasso', l_off_sani_train_score, l_off_sani_test_score)

alphas = [10, 1, 0.1, 0.01, 0.001, 0.0001]
train_scores = []
test_scores = []
ws = []

for alpha in alphas:
    lasso = Lasso(alpha=alpha)
    lasso.fit(X_train, y_train)
    ws.append(lasso.coef_)
    
    s1 = lasso.score(X_train, y_train)
    s2 = lasso.score(X_test, y_test)
    train_scores.append(s1)
    test_scores.append(s2)
    
display(train_scores, test_scores, ws)


# lasso
# run Lasso cross validation test to find the best alpha based on training data
lasso_cv=LassoCV(alphas=alphas, cv=5)
model = lasso_cv.fit(X_train, y_train)
print(model.alpha_)

# calculate Lasso R2, MSE, RMSE from test data
lasso=Lasso(alpha=0.0001).fit(X_train, y_train)
ypred_lasso = lasso.predict(X_test)
l_off_sani_score_lasso = lasso.score(X_test, y_test)
l_off_sani_mse_lasso = mean_squared_error(y_test, ypred_lasso)
print("Final Result: Lasso R2:{0:.3f}, MSE:{1:.2f}, RMSE:{2:.2f}".format(l_off_sani_score_lasso, l_off_sani_mse_lasso, np.sqrt(l_off_sani_mse_lasso)))


# ridge
# run Ridge cross validation test to find the best alpha based on training data
ridge_cv=RidgeCV(alphas=alphas, cv=5)
model = ridge_cv.fit(X_train, y_train)
print(model.alpha_)

# calculate Ridge R2, MSE, RMSE from test data
ridge=Ridge(alpha=0.0001).fit(X_train, y_train)
ypred_ridge = ridge.predict(X_test)
r_off_sani_score_ridge = ridge.score(X_test, y_test)
r_off_sani_mse_ridge = mean_squared_error(y_test, ypred_ridge)
print("Final Result: Ridge R2:{0:.3f}, MSE:{1:.2f}, RMSE:{2:.2f}".format(r_off_sani_score_ridge, r_off_sani_mse_ridge, np.sqrt(r_off_sani_mse_ridge)))


# 온라인 숙박================================================================
data=pd.read_csv("C:/data/on_acc1.csv", encoding='utf-8')
data=data.sample(frac=1).reset_index(drop=True)
train=data[:int(len(data)*0.6)]
test=data[int(len(data)*0.6):]

X_train = train[['PN','COVID']]
y_train = train['CN']
X_test = test[['PN','COVID']]
y_test = test['CN']

# Ridge
ridge = Ridge()
ridge.fit(X_train, y_train)

# Lasso
lasso = Lasso()
lasso.fit(X_train, y_train)

# Ridge 정확도
r_on_acc_train_score = ridge.score(X_train, y_train)
r_on_acc_test_score = ridge.score(X_test, y_test)
display('Ridge', r_on_acc_train_score, r_on_acc_test_score)

# Lasso 정확도
l_on_acc_train_score = lasso.score(X_train, y_train)
l_on_acc_test_score = lasso.score(X_test, y_test)
display('Lasso', l_on_acc_train_score, l_on_acc_test_score)

alphas = [10, 1, 0.1, 0.01, 0.001, 0.0001]
train_scores = []
test_scores = []
ws = []

for alpha in alphas:
    lasso = Lasso(alpha=alpha)
    lasso.fit(X_train, y_train)
    ws.append(lasso.coef_)
    
    s1 = lasso.score(X_train, y_train)
    s2 = lasso.score(X_test, y_test)
    train_scores.append(s1)
    test_scores.append(s2)
    
display(train_scores, test_scores, ws)


# lasso
# run Lasso cross validation test to find the best alpha based on training data
lasso_cv=LassoCV(alphas=alphas, cv=5)
model = lasso_cv.fit(X_train, y_train)
print(model.alpha_)

# calculate Lasso R2, MSE, RMSE from test data
lasso=Lasso(alpha=0.0001).fit(X_train, y_train)
ypred_lasso = lasso.predict(X_test)
l_on_acc_score_lasso = lasso.score(X_test, y_test)
l_on_acc_mse_lasso = mean_squared_error(y_test, ypred_lasso)
print("Final Result: Lasso R2:{0:.3f}, MSE:{1:.2f}, RMSE:{2:.2f}".format(l_on_acc_score_lasso, l_on_acc_mse_lasso, np.sqrt(l_on_acc_mse_lasso)))

# ridge
# run Ridge cross validation test to find the best alpha based on training data
ridge_cv=RidgeCV(alphas=alphas, cv=5)
model = ridge_cv.fit(X_train, y_train)
print(model.alpha_)

# calculate Ridge R2, MSE, RMSE from test data
ridge=Ridge(alpha=10).fit(X_train, y_train)
ypred_ridge = ridge.predict(X_test)
r_on_acc_score_ridge = ridge.score(X_test, y_test)
r_on_acc_mse_ridge = mean_squared_error(y_test, ypred_ridge)
print("Final Result: Ridge R2:{0:.3f}, MSE:{1:.2f}, RMSE:{2:.2f}".format(r_on_acc_score_ridge, r_on_acc_mse_ridge, np.sqrt(r_on_acc_mse_ridge)))


# 온라인 문화취미================================================================
data=pd.read_csv("C:/data/on_cul1.csv", encoding='utf-8')
data=data.sample(frac=1).reset_index(drop=True)
train=data[:int(len(data)*0.6)]
test=data[int(len(data)*0.6):]

X_train = train[['PN','COVID']]
y_train = train['CN']
X_test = test[['PN','COVID']]
y_test = test['CN']

# Ridge
ridge = Ridge()
ridge.fit(X_train, y_train)

# Lasso
lasso = Lasso()
lasso.fit(X_train, y_train)

# Ridge 정확도
r_on_cul_train_score = ridge.score(X_train, y_train)
r_on_cul_test_score = ridge.score(X_test, y_test)
display('Ridge', r_on_cul_train_score, r_on_cul_test_score)

# Lasso 정확도
l_on_cul_train_score = lasso.score(X_train, y_train)
l_on_cul_test_score = lasso.score(X_test, y_test)
display('Lasso', l_on_cul_train_score, l_on_cul_test_score)

alphas = [10, 1, 0.1, 0.01, 0.001, 0.0001]
train_scores = []
test_scores = []
ws = []

for alpha in alphas:
    lasso = Lasso(alpha=alpha)
    lasso.fit(X_train, y_train)
    ws.append(lasso.coef_)
    
    s1 = lasso.score(X_train, y_train)
    s2 = lasso.score(X_test, y_test)
    train_scores.append(s1)
    test_scores.append(s2)
    
display(train_scores, test_scores, ws)


# lasso
# run Lasso cross validation test to find the best alpha based on training data
lasso_cv=LassoCV(alphas=alphas, cv=5)
model = lasso_cv.fit(X_train, y_train)
print(model.alpha_)

# calculate Lasso R2, MSE, RMSE from test data
lasso=Lasso(alpha=0.0001).fit(X_train, y_train)
ypred_lasso = lasso.predict(X_test)
l_on_cul_score_lasso = lasso.score(X_test, y_test)
l_on_cul_mse_lasso = mean_squared_error(y_test, ypred_lasso)
print("Final Result: Lasso R2:{0:.3f}, MSE:{1:.2f}, RMSE:{2:.2f}".format(l_on_cul_score_lasso, l_on_cul_mse_lasso, np.sqrt(l_on_cul_mse_lasso)))


# ridge
# run Ridge cross validation test to find the best alpha based on training data
ridge_cv=RidgeCV(alphas=alphas, cv=5)
model = ridge_cv.fit(X_train, y_train)
print(model.alpha_)

# calculate Ridge R2, MSE, RMSE from test data
ridge=Ridge(alpha=10).fit(X_train, y_train)
ypred_ridge = ridge.predict(X_test)
r_on_cul_score_ridge = ridge.score(X_test, y_test)
r_on_cul_mse_ridge = mean_squared_error(y_test, ypred_ridge)
print("Final Result: Ridge R2:{0:.3f}, MSE:{1:.2f}, RMSE:{2:.2f}".format(r_on_cul_score_ridge, r_on_cul_mse_ridge, np.sqrt(r_on_cul_mse_ridge)))


# 온라인 요식업소================================================================
data=pd.read_csv("C:/data/on_food1.csv", encoding='utf-8')
data=data.sample(frac=1).reset_index(drop=True)
train=data[:int(len(data)*0.6)]
test=data[int(len(data)*0.6):]

X_train = train[['PN','COVID']]
y_train = train['CN']
X_test = test[['PN','COVID']]
y_test = test['CN']

# Ridge
ridge = Ridge()
ridge.fit(X_train, y_train)

# Lasso
lasso = Lasso()
lasso.fit(X_train, y_train)

# Ridge 정확도
r_on_food_train_score = ridge.score(X_train, y_train)
r_on_food_test_score = ridge.score(X_test, y_test)
display('Ridge', r_on_food_train_score, r_on_food_test_score)

# Lasso 정확도
l_on_food_train_score = lasso.score(X_train, y_train)
l_on_food_test_score = lasso.score(X_test, y_test)
display('Lasso', l_on_food_train_score, l_on_food_test_score)

alphas = [10, 1, 0.1, 0.01, 0.001, 0.0001]
train_scores = []
test_scores = []
ws = []

for alpha in alphas:
    lasso = Lasso(alpha=alpha)
    lasso.fit(X_train, y_train)
    ws.append(lasso.coef_)
    
    s1 = lasso.score(X_train, y_train)
    s2 = lasso.score(X_test, y_test)
    train_scores.append(s1)
    test_scores.append(s2)
    
display(train_scores, test_scores, ws)


# lasso
# run Lasso cross validation test to find the best alpha based on training data
lasso_cv=LassoCV(alphas=alphas, cv=5)
model = lasso_cv.fit(X_train, y_train)
print(model.alpha_)

# calculate Lasso R2, MSE, RMSE from test data
lasso=Lasso(alpha=0.0001).fit(X_train, y_train)
ypred_lasso = lasso.predict(X_test)
l_on_food_score_lasso = lasso.score(X_test, y_test)
l_on_food_mse_lasso = mean_squared_error(y_test, ypred_lasso)
print("Final Result: Lasso R2:{0:.3f}, MSE:{1:.2f}, RMSE:{2:.2f}".format(l_on_food_score_lasso, l_on_food_mse_lasso, np.sqrt(l_on_food_mse_lasso)))


# ridge
# run Ridge cross validation test to find the best alpha based on training data
ridge_cv=RidgeCV(alphas=alphas, cv=5)
model = ridge_cv.fit(X_train, y_train)
print(model.alpha_)

# calculate Ridge R2, MSE, RMSE from test data
ridge=Ridge(alpha=0.0001).fit(X_train, y_train)
ypred_ridge = ridge.predict(X_test)
r_on_food_score_ridge = ridge.score(X_test, y_test)
r_on_food_mse_ridge = mean_squared_error(y_test, ypred_ridge)
print("Final Result: Ridge R2:{0:.3f}, MSE:{1:.2f}, RMSE:{2:.2f}".format(r_on_food_score_ridge, r_on_food_mse_ridge, np.sqrt(r_on_food_mse_ridge)))


# 온라인 레저================================================================
data=pd.read_csv("C:/data/on_lei1.csv", encoding='utf-8')
data=data.sample(frac=1).reset_index(drop=True)
train=data[:int(len(data)*0.6)]
test=data[int(len(data)*0.6):]

X_train = train[['PN','COVID']]
y_train = train['CN']
X_test = test[['PN','COVID']]
y_test = test['CN']

# Ridge
ridge = Ridge()
ridge.fit(X_train, y_train)

# Lasso
lasso = Lasso()
lasso.fit(X_train, y_train)

# Ridge 정확도
r_on_lei_train_score = ridge.score(X_train, y_train)
r_on_lei_test_score = ridge.score(X_test, y_test)
display('Ridge', r_on_lei_train_score, r_on_lei_test_score)

# Lasso 정확도
l_on_lei_train_score = lasso.score(X_train, y_train)
l_on_lei_test_score = lasso.score(X_test, y_test)
display('Lasso', l_on_lei_train_score, l_on_lei_test_score)

alphas = [10, 1, 0.1, 0.01, 0.001, 0.0001]
train_scores = []
test_scores = []
ws = []

for alpha in alphas:
    lasso = Lasso(alpha=alpha)
    lasso.fit(X_train, y_train)
    ws.append(lasso.coef_)
    
    s1 = lasso.score(X_train, y_train)
    s2 = lasso.score(X_test, y_test)
    train_scores.append(s1)
    test_scores.append(s2)
    
display(train_scores, test_scores, ws)


# lasso
# run Lasso cross validation test to find the best alpha based on training data
lasso_cv=LassoCV(alphas=alphas, cv=5)
model = lasso_cv.fit(X_train, y_train)
print(model.alpha_)

# calculate Lasso R2, MSE, RMSE from test data
lasso=Lasso(alpha=10).fit(X_train, y_train)
ypred_lasso = lasso.predict(X_test)
l_on_lei_score_lasso = lasso.score(X_test, y_test)
l_on_lei_mse_lasso = mean_squared_error(y_test, ypred_lasso)
print("Final Result: Lasso R2:{0:.3f}, MSE:{1:.2f}, RMSE:{2:.2f}".format(l_on_lei_score_lasso, l_on_lei_mse_lasso, np.sqrt(l_on_lei_mse_lasso)))


# ridge
# run Ridge cross validation test to find the best alpha based on training data
ridge_cv=RidgeCV(alphas=alphas, cv=5)
model = ridge_cv.fit(X_train, y_train)
print(model.alpha_)

# calculate Ridge R2, MSE, RMSE from test data
ridge=Ridge(alpha=10).fit(X_train, y_train)
ypred_ridge = ridge.predict(X_test)
r_on_lei_score_ridge = ridge.score(X_test, y_test)
r_on_lei_mse_ridge = mean_squared_error(y_test, ypred_ridge)
print("Final Result: Ridge R2:{0:.3f}, MSE:{1:.2f}, RMSE:{2:.2f}".format(r_on_lei_score_ridge, r_on_lei_mse_ridge, np.sqrt(r_on_lei_mse_ridge)))


# 온라인 보건위생================================================================
data=pd.read_csv("C:/data/on_sani1.csv", encoding='utf-8')
data=data.sample(frac=1).reset_index(drop=True)
train=data[:int(len(data)*0.6)]
test=data[int(len(data)*0.6):]

X_train = train[['PN','COVID']]
y_train = train['CN']
X_test = test[['PN','COVID']]
y_test = test['CN']

# Ridge
ridge = Ridge()
ridge.fit(X_train, y_train)

# Lasso
lasso = Lasso()
lasso.fit(X_train, y_train)

# Ridge 정확도
r_on_sani_train_score = ridge.score(X_train, y_train)
r_on_sani_test_score = ridge.score(X_test, y_test)
display('Ridge', r_on_sani_train_score, r_on_sani_test_score)

# Lasso 정확도
l_on_sani_train_score = lasso.score(X_train, y_train)
l_on_sani_test_score = lasso.score(X_test, y_test)
display('Lasso', l_on_sani_train_score, l_on_sani_test_score)

alphas = [10, 1, 0.1, 0.01, 0.001, 0.0001]
train_scores = []
test_scores = []
ws = []

for alpha in alphas:
    lasso = Lasso(alpha=alpha)
    lasso.fit(X_train, y_train)
    ws.append(lasso.coef_)
    
    s1 = lasso.score(X_train, y_train)
    s2 = lasso.score(X_test, y_test)
    train_scores.append(s1)
    test_scores.append(s2)
    
display(train_scores, test_scores, ws)


# lasso
# run Lasso cross validation test to find the best alpha based on training data
lasso_cv=LassoCV(alphas=alphas, cv=5)
model = lasso_cv.fit(X_train, y_train)
print(model.alpha_)

# calculate Lasso R2, MSE, RMSE from test data
lasso=Lasso(alpha=0.0001).fit(X_train, y_train)
ypred_lasso = lasso.predict(X_test)
l_on_sani_score_lasso = lasso.score(X_test, y_test)
l_on_sani_mse_lasso = mean_squared_error(y_test, ypred_lasso)
print("Final Result: Lasso R2:{0:.3f}, MSE:{1:.2f}, RMSE:{2:.2f}".format(l_on_sani_score_lasso, l_on_sani_mse_lasso, np.sqrt(l_on_sani_mse_lasso)))




# ridge
# run Ridge cross validation test to find the best alpha based on training data
ridge_cv=RidgeCV(alphas=alphas, cv=5)
model = ridge_cv.fit(X_train, y_train)
print(model.alpha_)

# calculate Ridge R2, MSE, RMSE from test data
ridge=Ridge(alpha=0.0001).fit(X_train, y_train)
ypred_ridge = ridge.predict(X_test)
r_on_sani_score_ridge = ridge.score(X_test, y_test)
r_on_sani_mse_ridge = mean_squared_error(y_test, ypred_ridge)
print("Final Result: Ridge R2:{0:.3f}, MSE:{1:.2f}, RMSE:{2:.2f}".format(r_on_sani_score_ridge, r_on_sani_mse_ridge, np.sqrt(r_on_sani_mse_ridge)))

l_off_acc_train_score
l_off_acc_test_score
r_off_acc_train_score
r_off_acc_test_score

l_off_acc_score_lasso 
l_off_acc_mse_lasso 
np.sqrt(l_off_acc_mse_lasso)
r_off_acc_score_ridge
r_off_acc_mse_ridge 
np.sqrt(r_off_acc_mse_ridge)


df = pd.DataFrame(index=['off_acc','off_cul','off_food','off_lei','off_medi',
                         'off_sano','on_acc', 'on_cul', 'on_food', 'on_lei','on_sani'],
                  data = {'Lasso train모델점수' : [l_off_acc_train_score,l_off_cul_train_score,l_off_food_train_score,
                                          l_off_lei_train_score,l_off_medi_train_score,l_off_sani_train_score,
                                          l_on_acc_train_score,l_on_cul_train_score,l_on_food_train_score,
                                          l_on_lei_train_score,l_on_sani_train_score],
                          'Ridge train모델점수' : [r_off_acc_train_score,r_off_cul_train_score,r_off_food_train_score,
                                          r_off_lei_train_score,r_off_medi_train_score,r_off_sani_train_score,
                                          r_on_acc_train_score,r_on_cul_train_score,r_on_food_train_score,
                                          r_on_lei_train_score,r_on_sani_train_score],
                          'Lasso test모델점수' : [l_off_acc_test_score,l_off_cul_test_score,l_off_food_test_score,
                                          l_off_lei_test_score,l_off_medi_test_score,l_off_sani_test_score,
                                          l_on_acc_test_score,l_on_cul_test_score,l_on_food_test_score,
                                          l_on_lei_test_score,l_on_sani_test_score],
                          'Ridge test모델점수' : [r_off_acc_test_score,r_off_cul_test_score,r_off_food_test_score,
                                          r_off_lei_test_score,r_off_medi_test_score,r_off_sani_test_score,
                                          r_on_acc_test_score,r_on_cul_test_score,r_on_food_test_score,
                                          r_on_lei_test_score,r_on_sani_test_score],
                          'Lasso MSE' : [l_off_acc_mse_lasso,l_off_cul_mse_lasso,l_off_food_mse_lasso,
                                         l_off_lei_mse_lasso,l_off_medi_mse_lasso,l_off_sani_mse_lasso,
                                         l_on_acc_mse_lasso,l_on_cul_mse_lasso,l_on_food_mse_lasso,
                                         l_on_lei_mse_lasso,l_on_sani_mse_lasso],
                          'Ridge MSE' : [r_off_acc_mse_ridge,r_off_cul_mse_ridge,r_off_food_mse_ridge,
                                         r_off_lei_mse_ridge,r_off_medi_mse_ridge,r_off_sani_mse_ridge,
                                         r_on_acc_mse_ridge,r_on_cul_mse_ridge,r_on_food_mse_ridge,
                                         r_on_lei_mse_ridge,r_on_sani_mse_ridge],
                          'Lasso RMSE' : [np.sqrt(l_off_acc_mse_lasso),np.sqrt(l_off_cul_mse_lasso),np.sqrt(l_off_food_mse_lasso),
                                                                               np.sqrt(l_off_lei_mse_lasso),np.sqrt(l_off_medi_mse_lasso),np.sqrt(l_off_sani_mse_lasso),
                                                                               np.sqrt(l_on_acc_mse_lasso),np.sqrt(l_on_cul_mse_lasso),np.sqrt(l_on_food_mse_lasso),
                                                                               np.sqrt(l_on_lei_mse_lasso),np.sqrt(l_on_sani_mse_lasso)],
                          'Ridge RMSE' : [np.sqrt(r_off_acc_mse_ridge),np.sqrt(r_off_cul_mse_ridge),np.sqrt(r_off_food_mse_ridge),
                                                                               np.sqrt(r_off_lei_mse_ridge),np.sqrt(r_off_medi_mse_ridge),np.sqrt(r_off_sani_mse_ridge),
                                                                               np.sqrt(r_on_acc_mse_ridge),np.sqrt(r_on_cul_mse_ridge),np.sqrt(r_on_food_mse_ridge),
                                                                               np.sqrt(r_on_lei_mse_ridge),np.sqrt(r_on_sani_mse_ridge)]})


df

# 파일로 떨어트리기
df.to_csv('c:/data/Ridge_Lasso_MSE.csv',index=True)

# 7-2) Decision Tree

from sklearn.tree import DecisionTreeClassifier, export_graphviz
import pydot
import numpy as np
import pandas as pd
import sklearn.metrics as metrics
from pandas import Series, DataFrame

train_F1=[]
train_Accuracy=[]
test_F1=[]
test_Accuracy=[]

## 오프라인 숙박 ==========================================================
train=pd.read_csv("C:/data/off_acco(train).csv", sep=',', encoding='utf-8')
x_train=train[['PN','COVID']]
y_train=train['CN']

test=pd.read_csv("C:/data/off_acco(test).csv", sep=',', encoding='utf-8')
x_test=test[['PN','COVID']]
y_test=test['CN']

# 의사결정 트리 선언
dtree=DecisionTreeClassifier(random_state=0)

# 훈련 데이터를 입력해  모듈을 학습
dtree.fit(x_train, y_train)
y_train_pred=dtree.predict(x_train)

# Test data를 입력해 target data를 예측
y_pred=dtree.predict(x_test)

# 예측 결과 precision과 실제 test data의 target을 비교
print(y_pred)
print(list(y_test))

# 모델 성능 확인 : accuracy, F1 score
print("Train Score is: ", dtree.score(x_train,y_train))
print("Test Score is: ", dtree.score(x_test,y_test))
# train
print("Train F1 Score is: ", metrics.f1_score(y_train_pred, y_train))
print("Train Accuracy is: ", metrics.accuracy_score(y_train_pred, y_train))
train_F1.append(metrics.f1_score(y_train_pred, y_train))
train_Accuracy.append(metrics.accuracy_score(y_train_pred, y_train))
# test
print("Test F1 Score is: ", metrics.f1_score(y_test, y_pred))
print("Test Accuracy is: ", metrics.accuracy_score(y_test, y_pred))
test_F1.append(metrics.f1_score(y_test, y_pred))
test_Accuracy.append(metrics.accuracy_score(y_test, y_pred))

# 그래프
export_graphviz(dtree, out_file="dtree.dot", 
                class_names=['PN affected','COVID affected'],
                feature_names=['PN','COVID'], impurity=False, filled=True)

(graph,)=pydot.graph_from_dot_file('dtree.dot',encoding='utf8')
graph.write_png('C:/data/dtree.png')


## 오프라인 문화취미 ==========================================================
train=pd.read_csv("C:/data/off_cul(train).csv", sep=',', encoding='utf-8')
x_train=train[['PN','COVID']]
y_train=train['CN']

test=pd.read_csv("C:/data/off_cul(test).csv", sep=',', encoding='utf-8')
x_test=test[['PN','COVID']]
y_test=test['CN']

# 의사결정 트리 선언
dtree=DecisionTreeClassifier(random_state=0)

# 훈련 데이터를 입력해  모듈을 학습
dtree.fit(x_train, y_train)
y_train_pred=dtree.predict(x_train)

# Test data를 입력해 target data를 예측
y_pred=dtree.predict(x_test)

# 예측 결과 precision과 실제 test data의 target을 비교
print(y_pred)
print(list(y_test))

# 모델 성능 확인 : accuracy, F1 score
print("Train Score is: ", dtree.score(x_train,y_train))
print("Test Score is: ", dtree.score(x_test,y_test))
# train
print("Train F1 Score is: ", metrics.f1_score(y_train_pred, y_train))
print("Train Accuracy is: ", metrics.accuracy_score(y_train_pred, y_train))
train_F1.append(metrics.f1_score(y_train_pred, y_train))
train_Accuracy.append(metrics.accuracy_score(y_train_pred, y_train))
# test
print("Test F1 Score is: ", metrics.f1_score(y_test, y_pred))
print("Test Accuracy is: ", metrics.accuracy_score(y_test, y_pred))
test_F1.append(metrics.f1_score(y_test, y_pred))
test_Accuracy.append(metrics.accuracy_score(y_test, y_pred))

# 그래프
export_graphviz(dtree, out_file="dtree.dot", 
                class_names=['PN affected','COVID affected'],
                feature_names=['PN','COVID'], impurity=False, filled=True)

(graph,)=pydot.graph_from_dot_file('dtree.dot',encoding='utf8')
graph.write_png('C:/data/dtree.png')


## 오프라인 식품 ==========================================================
train=pd.read_csv("C:/data/off_food(train).csv", sep=',', encoding='utf-8')
x_train=train[['PN','COVID']]
y_train=train['CN']

test=pd.read_csv("C:/data/off_food(test).csv", sep=',', encoding='utf-8')
x_test=test[['PN','COVID']]
y_test=test['CN']

# 의사결정 트리 선언
dtree=DecisionTreeClassifier(random_state=0)

# 훈련 데이터를 입력해  모듈을 학습
dtree.fit(x_train, y_train)
y_train_pred=dtree.predict(x_train)

# Test data를 입력해 target data를 예측
y_pred=dtree.predict(x_test)

# 예측 결과 precision과 실제 test data의 target을 비교
print(y_pred)
print(list(y_test))

# 모델 성능 확인 : accuracy, F1 score
print("Train Score is: ", dtree.score(x_train,y_train))
print("Test Score is: ", dtree.score(x_test,y_test))
# train
print("Train F1 Score is: ", metrics.f1_score(y_train_pred, y_train))
print("Train Accuracy is: ", metrics.accuracy_score(y_train_pred, y_train))
train_F1.append(metrics.f1_score(y_train_pred, y_train))
train_Accuracy.append(metrics.accuracy_score(y_train_pred, y_train))
# test
print("Test F1 Score is: ", metrics.f1_score(y_test, y_pred))
print("Test Accuracy is: ", metrics.accuracy_score(y_test, y_pred))
test_F1.append(metrics.f1_score(y_test, y_pred))
test_Accuracy.append(metrics.accuracy_score(y_test, y_pred))

# 그래프
export_graphviz(dtree, out_file="dtree.dot", 
                class_names=['PN affected','COVID affected'],
                feature_names=['PN','COVID'], impurity=False, filled=True)

(graph,)=pydot.graph_from_dot_file('dtree.dot',encoding='utf8')
graph.write_png('C:/data/dtree.png')


## 오프라인 레저 ==========================================================
train=pd.read_csv("C:/data/off_lei(train).csv", sep=',', encoding='utf-8')
x_train=train[['PN','COVID']]
y_train=train['CN']

test=pd.read_csv("C:/data/off_lei(test).csv", sep=',', encoding='utf-8')
x_test=test[['PN','COVID']]
y_test=test['CN']

# 의사결정 트리 선언
dtree=DecisionTreeClassifier(random_state=0)

# 훈련 데이터를 입력해  모듈을 학습
dtree.fit(x_train, y_train)
y_train_pred=dtree.predict(x_train)

# Test data를 입력해 target data를 예측
y_pred=dtree.predict(x_test)

# 예측 결과 precision과 실제 test data의 target을 비교
print(y_pred)
print(list(y_test))

# 모델 성능 확인 : accuracy, F1 score
print("Train Score is: ", dtree.score(x_train,y_train))
print("Test Score is: ", dtree.score(x_test,y_test))
# train
print("Train F1 Score is: ", metrics.f1_score(y_train_pred, y_train))
print("Train Accuracy is: ", metrics.accuracy_score(y_train_pred, y_train))
train_F1.append(metrics.f1_score(y_train_pred, y_train))
train_Accuracy.append(metrics.accuracy_score(y_train_pred, y_train))
# test
print("Test F1 Score is: ", metrics.f1_score(y_test, y_pred))
print("Test Accuracy is: ", metrics.accuracy_score(y_test, y_pred))
test_F1.append(metrics.f1_score(y_test, y_pred))
test_Accuracy.append(metrics.accuracy_score(y_test, y_pred))

# 그래프
export_graphviz(dtree, out_file="dtree.dot", 
                class_names=['PN affected','COVID affected'],
                feature_names=['PN','COVID'], impurity=False, filled=True)

(graph,)=pydot.graph_from_dot_file('dtree.dot',encoding='utf8')
graph.write_png('C:/data/dtree.png')


## 오프라인 의료 ==========================================================
train=pd.read_csv("C:/data/off_medi(train).csv", sep=',', encoding='utf-8')
x_train=train[['PN','COVID']]
y_train=train['CN']

test=pd.read_csv("C:/data/off_medi(test).csv", sep=',', encoding='utf-8')
x_test=test[['PN','COVID']]
y_test=test['CN']

# 의사결정 트리 선언
dtree=DecisionTreeClassifier(random_state=0)

# 훈련 데이터를 입력해  모듈을 학습
dtree.fit(x_train, y_train)
y_train_pred=dtree.predict(x_train)

# Test data를 입력해 target data를 예측
y_pred=dtree.predict(x_test)

# 예측 결과 precision과 실제 test data의 target을 비교
print(y_pred)
print(list(y_test))

# 모델 성능 확인 : accuracy, F1 score
print("Train Score is: ", dtree.score(x_train,y_train))
print("Test Score is: ", dtree.score(x_test,y_test))
# train
print("Train F1 Score is: ", metrics.f1_score(y_train_pred, y_train))
print("Train Accuracy is: ", metrics.accuracy_score(y_train_pred, y_train))
train_F1.append(metrics.f1_score(y_train_pred, y_train))
train_Accuracy.append(metrics.accuracy_score(y_train_pred, y_train))
# test
print("Test F1 Score is: ", metrics.f1_score(y_test, y_pred))
print("Test Accuracy is: ", metrics.accuracy_score(y_test, y_pred))
test_F1.append(metrics.f1_score(y_test, y_pred))
test_Accuracy.append(metrics.accuracy_score(y_test, y_pred))

# 그래프
export_graphviz(dtree, out_file="dtree.dot", 
                class_names=['PN affected','COVID affected'],
                feature_names=['PN','COVID'], impurity=False, filled=True)

(graph,)=pydot.graph_from_dot_file('dtree.dot',encoding='utf8')
graph.write_png('C:/data/dtree.png')


## 오프라인 보건위생  ==========================================================
train=pd.read_csv("C:/data/off_sani(train).csv", sep=',', encoding='utf-8')
x_train=train[['PN','COVID']]
y_train=train['CN']

test=pd.read_csv("C:/data/off_sani(test).csv", sep=',', encoding='utf-8')
x_test=test[['PN','COVID']]
y_test=test['CN']

# 의사결정 트리 선언
dtree=DecisionTreeClassifier(random_state=0)

# 훈련 데이터를 입력해  모듈을 학습
dtree.fit(x_train, y_train)
y_train_pred=dtree.predict(x_train)

# Test data를 입력해 target data를 예측
y_pred=dtree.predict(x_test)

# 예측 결과 precision과 실제 test data의 target을 비교
print(y_pred)
print(list(y_test))

# 모델 성능 확인 : accuracy, F1 score
print("Train Score is: ", dtree.score(x_train,y_train))
print("Test Score is: ", dtree.score(x_test,y_test))
# train
print("Train F1 Score is: ", metrics.f1_score(y_train_pred, y_train))
print("Train Accuracy is: ", metrics.accuracy_score(y_train_pred, y_train))
train_F1.append(metrics.f1_score(y_train_pred, y_train))
train_Accuracy.append(metrics.accuracy_score(y_train_pred, y_train))
# test
print("Test F1 Score is: ", metrics.f1_score(y_test, y_pred))
print("Test Accuracy is: ", metrics.accuracy_score(y_test, y_pred))
test_F1.append(metrics.f1_score(y_test, y_pred))
test_Accuracy.append(metrics.accuracy_score(y_test, y_pred))

# 그래프
export_graphviz(dtree, out_file="dtree.dot", 
                class_names=['PN affected','COVID affected'],
                feature_names=['PN','COVID'], impurity=False, filled=True)

(graph,)=pydot.graph_from_dot_file('dtree.dot',encoding='utf8')
graph.write_png('C:/data/dtree.png')


## 온라인 숙박 ==========================================================
train=pd.read_csv("C:/data/on_acco(train).csv", sep=',', encoding='utf-8')
x_train=train[['PN','COVID']]
y_train=train['CN']

test=pd.read_csv("C:/data/on_acco(test).csv", sep=',', encoding='utf-8')
x_test=test[['PN','COVID']]
y_test=test['CN']

# 의사결정 트리 선언
dtree=DecisionTreeClassifier(random_state=0)

# 훈련 데이터를 입력해  모듈을 학습
dtree.fit(x_train, y_train)
y_train_pred=dtree.predict(x_train)

# Test data를 입력해 target data를 예측
y_pred=dtree.predict(x_test)

# 예측 결과 precision과 실제 test data의 target을 비교
print(y_pred)
print(list(y_test))

# 모델 성능 확인 : accuracy, F1 score
print("Train Score is: ", dtree.score(x_train,y_train))
print("Test Score is: ", dtree.score(x_test,y_test))
# train
print("Train F1 Score is: ", metrics.f1_score(y_train_pred, y_train))
print("Train Accuracy is: ", metrics.accuracy_score(y_train_pred, y_train))
train_F1.append(metrics.f1_score(y_train_pred, y_train))
train_Accuracy.append(metrics.accuracy_score(y_train_pred, y_train))
# test
print("Test F1 Score is: ", metrics.f1_score(y_test, y_pred))
print("Test Accuracy is: ", metrics.accuracy_score(y_test, y_pred))
test_F1.append(metrics.f1_score(y_test, y_pred))
test_Accuracy.append(metrics.accuracy_score(y_test, y_pred))

# 그래프
export_graphviz(dtree, out_file="dtree.dot", 
                class_names=['PN affected','COVID affected'],
                feature_names=['PN','COVID'], impurity=False, filled=True)

(graph,)=pydot.graph_from_dot_file('dtree.dot',encoding='utf8')
graph.write_png('C:/data/dtree.png')


## 온라인 문화취미 ==========================================================
train=pd.read_csv("C:/data/on_cul(train).csv", sep=',', encoding='utf-8')
x_train=train[['PN','COVID']]
y_train=train['CN']

test=pd.read_csv("C:/data/on_cul(test).csv", sep=',', encoding='utf-8')
x_test=test[['PN','COVID']]
y_test=test['CN']

# 의사결정 트리 선언
dtree=DecisionTreeClassifier(random_state=0)

# 훈련 데이터를 입력해  모듈을 학습
dtree.fit(x_train, y_train)
y_train_pred=dtree.predict(x_train)

# Test data를 입력해 target data를 예측
y_pred=dtree.predict(x_test)

# 예측 결과 precision과 실제 test data의 target을 비교
print(y_pred)
print(list(y_test))

# 모델 성능 확인 : accuracy, F1 score
print("Train Score is: ", dtree.score(x_train,y_train))
print("Test Score is: ", dtree.score(x_test,y_test))
# train
print("Train F1 Score is: ", metrics.f1_score(y_train_pred, y_train))
print("Train Accuracy is: ", metrics.accuracy_score(y_train_pred, y_train))
train_F1.append(metrics.f1_score(y_train_pred, y_train))
train_Accuracy.append(metrics.accuracy_score(y_train_pred, y_train))
# test
print("Test F1 Score is: ", metrics.f1_score(y_test, y_pred))
print("Test Accuracy is: ", metrics.accuracy_score(y_test, y_pred))
test_F1.append(metrics.f1_score(y_test, y_pred))
test_Accuracy.append(metrics.accuracy_score(y_test, y_pred))

# 그래프
export_graphviz(dtree, out_file="dtree.dot", 
                class_names=['PN affected','COVID affected'],
                feature_names=['PN','COVID'], impurity=False, filled=True)

(graph,)=pydot.graph_from_dot_file('dtree.dot',encoding='utf8')
graph.write_png('C:/data/dtree.png')


## 온라인 식품 ==========================================================
train=pd.read_csv("C:/data/on_food(train).csv", sep=',', encoding='utf-8')
x_train=train[['PN','COVID']]
y_train=train['CN']

test=pd.read_csv("C:/data/on_food(test).csv", sep=',', encoding='utf-8')
x_test=test[['PN','COVID']]
y_test=test['CN']

# 의사결정 트리 선언
dtree=DecisionTreeClassifier(random_state=0)

# 훈련 데이터를 입력해  모듈을 학습
dtree.fit(x_train, y_train)
y_train_pred=dtree.predict(x_train)

# Test data를 입력해 target data를 예측
y_pred=dtree.predict(x_test)

# 예측 결과 precision과 실제 test data의 target을 비교
print(y_pred)
print(list(y_test))

# 모델 성능 확인 : accuracy, F1 score
print("Train Score is: ", dtree.score(x_train,y_train))
print("Test Score is: ", dtree.score(x_test,y_test))
# train
print("Train F1 Score is: ", metrics.f1_score(y_train_pred, y_train))
print("Train Accuracy is: ", metrics.accuracy_score(y_train_pred, y_train))
train_F1.append(metrics.f1_score(y_train_pred, y_train))
train_Accuracy.append(metrics.accuracy_score(y_train_pred, y_train))
# test
print("Test F1 Score is: ", metrics.f1_score(y_test, y_pred))
print("Test Accuracy is: ", metrics.accuracy_score(y_test, y_pred))
test_F1.append(metrics.f1_score(y_test, y_pred))
test_Accuracy.append(metrics.accuracy_score(y_test, y_pred))

# 그래프
export_graphviz(dtree, out_file="dtree.dot", 
                class_names=['PN affected','COVID affected'],
                feature_names=['PN','COVID'], impurity=False, filled=True)

(graph,)=pydot.graph_from_dot_file('dtree.dot',encoding='utf8')
graph.write_png('C:/data/dtree.png')


## 온라인 레저 ==========================================================
train=pd.read_csv("C:/data/on_lei(train).csv", sep=',', encoding='utf-8')
x_train=train[['PN','COVID']]
y_train=train['CN']

test=pd.read_csv("C:/data/on_lei(test).csv", sep=',', encoding='utf-8')
x_test=test[['PN','COVID']]
y_test=test['CN']

# 의사결정 트리 선언
dtree=DecisionTreeClassifier(random_state=0)

# 훈련 데이터를 입력하고 모듈을 학습
dtree.fit(x_train, y_train)
y_train_pred=dtree.predict(x_train)

# Test data를 입력해 target data를 예측
y_pred=dtree.predict(x_test)

# 예측 결과 precision과 실제 test data의 target을 비교
print(y_pred)
print(list(y_test))

# 모델 성능 확인 : accuracy, F1 score
print("Train Score is: ", dtree.score(x_train,y_train))
print("Test Score is: ", dtree.score(x_test,y_test))
# train
print("Train F1 Score is: ", metrics.f1_score(y_train_pred, y_train))
print("Train Accuracy is: ", metrics.accuracy_score(y_train_pred, y_train))
train_F1.append(metrics.f1_score(y_train_pred, y_train))
train_Accuracy.append(metrics.accuracy_score(y_train_pred, y_train))
# test
print("Test F1 Score is: ", metrics.f1_score(y_test, y_pred))
print("Test Accuracy is: ", metrics.accuracy_score(y_test, y_pred))
test_F1.append(metrics.f1_score(y_test, y_pred))
test_Accuracy.append(metrics.accuracy_score(y_test, y_pred))

# 그래프
export_graphviz(dtree, out_file="dtree.dot", 
                class_names=['PN affected','COVID affected'],
                feature_names=['PN','COVID'], impurity=False, filled=True)

(graph,)=pydot.graph_from_dot_file('dtree.dot',encoding='utf8')
graph.write_png('C:/data/dtree.png')


## 온라인 보건위생 ==========================================================
train=pd.read_csv("C:/data/on_sani(train).csv", sep=',', encoding='utf-8')
x_train=train[['PN','COVID']]
y_train=train['CN']

test=pd.read_csv("C:/data/on_sani(test).csv", sep=',', encoding='utf-8')
x_test=test[['PN','COVID']]
y_test=test['CN']

# 의사결정 트리 선언
dtree=DecisionTreeClassifier(random_state=0)

# 훈련 데이터를 입력해 모듈을 학습
dtree.fit(x_train, y_train)
y_train_pred=dtree.predict(x_train)

# Test data를 입력해 target data를 예측
y_pred=dtree.predict(x_test)

# 예측 결과 precision과 실제 test data의 target을 비교
print(y_pred)
print(list(y_test))

# 모델 성능 확인 : accuracy, F1 score
print("Train Score is: ", dtree.score(x_train,y_train))
print("Test Score is: ", dtree.score(x_test,y_test))
# train
print("Train F1 Score is: ", metrics.f1_score(y_train_pred, y_train))
print("Train Accuracy is: ", metrics.accuracy_score(y_train_pred, y_train))
train_F1.append(metrics.f1_score(y_train_pred, y_train))
train_Accuracy.append(metrics.accuracy_score(y_train_pred, y_train))
# test
print("Test F1 Score is: ", metrics.f1_score(y_test, y_pred))
print("Test Accuracy is: ", metrics.accuracy_score(y_test, y_pred))
test_F1.append(metrics.f1_score(y_test, y_pred))
test_Accuracy.append(metrics.accuracy_score(y_test, y_pred))

# 그래프
export_graphviz(dtree, out_file="dtree.dot", 
                class_names=['PN affected','COVID affected'],
                feature_names=['PN','COVID'], impurity=False, filled=True)

(graph,)=pydot.graph_from_dot_file('dtree.dot',encoding='utf8')
graph.write_png('C:/data/dtree.png')


## 결과 파일로 저장 ==========================================================
result=DataFrame({'name':['off_acco','off_cul','off_food','off_lei','off_medi','off_sani',
                          'on_acco','on_cul','on_food','on_lei','on_sani'],
                  'train_acc':train_Accuracy, 'train_F1':train_F1,
                  'test_acc':test_Accuracy, 'test_F1': test_F1})

result.to_csv("C:/data/dtree_accuracy.csv")

# 7-3) Random Forest

from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sklearn.metrics as metrics
from pandas import Series, DataFrame
import mglearn

train_F1=[]
train_Accuracy=[]
test_F1=[]
test_Accuracy=[]

## 오프라인 숙박 ==========================================================
train=pd.read_csv("C:/data/off_acco(train).csv", sep=',', encoding='utf-8')
x_train=train[['PN','COVID']]
y_train=train['CN']

test=pd.read_csv("C:/data/off_acco(test).csv", sep=',', encoding='utf-8')
x_test=test[['PN','COVID']]
y_test=test['CN']

# 랜덤포레스트 선언: 트리개수 10개 
forest = RandomForestClassifier(n_estimators=10, random_state=0)

# 훈련 데이터를 입력해 Random Forest 모듈을 학습
forest.fit(x_train, y_train)
y_train_pred=forest.predict(x_train)

# Test data를 입력해 target data를 예측
y_pred=forest.predict(x_test)

# 예측 결과 precision과 실제 test data의 target을 비교
print(y_pred)
print(list(y_test))

# 모델 성능 확인 : accuracy, F1 score
print("Train Score is: ", forest.score(x_train,y_train))
print("Test Score is: ", forest.score(x_test,y_test))
# train
print("Train F1 Score is: ", metrics.f1_score(y_train_pred, y_train))
print("Train Accuracy is: ", metrics.accuracy_score(y_train_pred, y_train))
train_F1.append(metrics.f1_score(y_train_pred, y_train))
train_Accuracy.append(metrics.accuracy_score(y_train_pred, y_train))
#test
print("Test F1 Score is: ", metrics.f1_score(y_test, y_pred))
print("Test Accuracy is: ", metrics.accuracy_score(y_test, y_pred))
test_F1.append(metrics.f1_score(y_test, y_pred))
test_Accuracy.append(metrics.accuracy_score(y_test, y_pred))


## 오프라인 문화취미 ==========================================================
train=pd.read_csv("C:/data/off_cul(train).csv", sep=',', encoding='utf-8')
x_train=train[['PN','COVID']]
y_train=train['CN']

test=pd.read_csv("C:/data/off_cul(test).csv", sep=',', encoding='utf-8')
x_test=test[['PN','COVID']]
y_test=test['CN']

# 랜덤포레스트 선언: 트리개수 10개 
forest = RandomForestClassifier(n_estimators=10, random_state=0)

# 훈련 데이터를 입력해 Random Forest 모듈을 학습
forest.fit(x_train, y_train)
y_train_pred=forest.predict(x_train)

# Test data를 입력해 target data를 예측
y_pred=forest.predict(x_test)

# 예측 결과 precision과 실제 test data의 target을 비교
print(y_pred)
print(list(y_test))

# 모델 성능 확인 : accuracy, F1 score
print("Train Score is: ", forest.score(x_train,y_train))
print("Test Score is: ", forest.score(x_test,y_test))
# train
print("Train F1 Score is: ", metrics.f1_score(y_train_pred, y_train))
print("Train Accuracy is: ", metrics.accuracy_score(y_train_pred, y_train))
train_F1.append(metrics.f1_score(y_train_pred, y_train))
train_Accuracy.append(metrics.accuracy_score(y_train_pred, y_train))
# test
print("Test F1 Score is: ", metrics.f1_score(y_test, y_pred))
print("Test Accuracy is: ", metrics.accuracy_score(y_test, y_pred))
test_F1.append(metrics.f1_score(y_test, y_pred))
test_Accuracy.append(metrics.accuracy_score(y_test, y_pred))


## 오프라인 식품 ==========================================================
train=pd.read_csv("C:/data/off_food(train).csv", sep=',', encoding='utf-8')
x_train=train[['PN','COVID']]
y_train=train['CN']

test=pd.read_csv("C:/data/off_food(test).csv", sep=',', encoding='utf-8')
x_test=test[['PN','COVID']]
y_test=test['CN']

# 랜덤포레스트 선언: 트리개수 10개 
forest = RandomForestClassifier(n_estimators=10, random_state=0)

# 훈련 데이터를 입력해 Random Forest 모듈을 학습
forest.fit(x_train, y_train)
y_train_pred=forest.predict(x_train)

# Test data를 입력해 target data를 예측
y_pred=forest.predict(x_test)

# 예측 결과 precision과 실제 test data의 target을 비교
print(y_pred)
print(list(y_test))

# 모델 성능 확인 : accuracy, F1 score
print("Train Score is: ", forest.score(x_train,y_train))
print("Test Score is: ", forest.score(x_test,y_test))
# train
print("Train F1 Score is: ", metrics.f1_score(y_train_pred, y_train))
print("Train Accuracy is: ", metrics.accuracy_score(y_train_pred, y_train))
train_F1.append(metrics.f1_score(y_train_pred, y_train))
train_Accuracy.append(metrics.accuracy_score(y_train_pred, y_train))
# test
print("Test F1 Score is: ", metrics.f1_score(y_test, y_pred))
print("Test Accuracy is: ", metrics.accuracy_score(y_test, y_pred))
test_F1.append(metrics.f1_score(y_test, y_pred))
test_Accuracy.append(metrics.accuracy_score(y_test, y_pred))


## 오프라인 레저 ==========================================================
train=pd.read_csv("C:/data/off_lei(train).csv", sep=',', encoding='utf-8')
x_train=train[['PN','COVID']]
y_train=train['CN']

test=pd.read_csv("C:/data/off_lei(test).csv", sep=',', encoding='utf-8')
x_test=test[['PN','COVID']]
y_test=test['CN']

# 랜덤포레스트 선언: 트리개수 10개 
forest = RandomForestClassifier(n_estimators=10, random_state=0)

# 훈련 데이터를 입력해 Random Forest 모듈을 학습
forest.fit(x_train, y_train)
y_train_pred=forest.predict(x_train)

# Test data를 입력해 target data를 예측
y_pred=forest.predict(x_test)

# 예측 결과 precision과 실제 test data의 target을 비교
print(y_pred)
print(list(y_test))

# 모델 성능 확인 : accuracy, F1 score
print("Train Score is: ", forest.score(x_train,y_train))
print("Test Score is: ", forest.score(x_test,y_test))
# train
print("Train F1 Score is: ", metrics.f1_score(y_train_pred, y_train))
print("Train Accuracy is: ", metrics.accuracy_score(y_train_pred, y_train))
train_F1.append(metrics.f1_score(y_train_pred, y_train))
train_Accuracy.append(metrics.accuracy_score(y_train_pred, y_train))
# test
print("Test F1 Score is: ", metrics.f1_score(y_test, y_pred))
print("Test Accuracy is: ", metrics.accuracy_score(y_test, y_pred))
test_F1.append(metrics.f1_score(y_test, y_pred))
test_Accuracy.append(metrics.accuracy_score(y_test, y_pred))


## 오프라인 의료 ==========================================================
train=pd.read_csv("C:/data/off_medi(train).csv", sep=',', encoding='utf-8')
x_train=train[['PN','COVID']]
y_train=train['CN']

test=pd.read_csv("C:/data/off_medi(test).csv", sep=',', encoding='utf-8')
x_test=test[['PN','COVID']]
y_test=test['CN']

# 랜덤포레스트 선언: 트리개수 10개 
forest = RandomForestClassifier(n_estimators=10, random_state=0)

# 훈련 데이터를 입력해 Random Forest 모듈을 학습
forest.fit(x_train, y_train)
y_train_pred=forest.predict(x_train)

# Test data를 입력해 target data를 예측
y_pred=forest.predict(x_test)

# 예측 결과 precision과 실제 test data의 target을 비교
print(y_pred)
print(list(y_test))

# 모델 성능 확인 : accuracy, F1 score
print("Train Score is: ", forest.score(x_train,y_train))
print("Test Score is: ", forest.score(x_test,y_test))
# train
print("Train F1 Score is: ", metrics.f1_score(y_train_pred, y_train))
print("Train Accuracy is: ", metrics.accuracy_score(y_train_pred, y_train))
train_F1.append(metrics.f1_score(y_train_pred, y_train))
train_Accuracy.append(metrics.accuracy_score(y_train_pred, y_train))
# test
print("Test F1 Score is: ", metrics.f1_score(y_test, y_pred))
print("Test Accuracy is: ", metrics.accuracy_score(y_test, y_pred))
test_F1.append(metrics.f1_score(y_test, y_pred))
test_Accuracy.append(metrics.accuracy_score(y_test, y_pred))


## 오프라인 보건위생  ==========================================================
train=pd.read_csv("C:/data/off_sani(train).csv", sep=',', encoding='utf-8')
x_train=train[['PN','COVID']]
y_train=train['CN']

test=pd.read_csv("C:/data/off_sani(test).csv", sep=',', encoding='utf-8')
x_test=test[['PN','COVID']]
y_test=test['CN']

# 랜덤포레스트 선언: 트리개수 10개 
forest = RandomForestClassifier(n_estimators=10, random_state=0)

# 훈련 데이터를 입력해 Random Forest 모듈을 학습
forest.fit(x_train, y_train)
y_train_pred=forest.predict(x_train)

# Test data를 입력해 target data를 예측
y_pred=forest.predict(x_test)

# 예측 결과 precision과 실제 test data의 target을 비교
print(y_pred)
print(list(y_test))

# 모델 성능 확인 : accuracy, F1 score
print("Train Score is: ", forest.score(x_train,y_train))
print("Test Score is: ", forest.score(x_test,y_test))
# train
print("Train F1 Score is: ", metrics.f1_score(y_train_pred, y_train))
print("Train Accuracy is: ", metrics.accuracy_score(y_train_pred, y_train))
train_F1.append(metrics.f1_score(y_train_pred, y_train))
train_Accuracy.append(metrics.accuracy_score(y_train_pred, y_train))
# test
print("Test F1 Score is: ", metrics.f1_score(y_test, y_pred))
print("Test Accuracy is: ", metrics.accuracy_score(y_test, y_pred))
test_F1.append(metrics.f1_score(y_test, y_pred))
test_Accuracy.append(metrics.accuracy_score(y_test, y_pred))


## 온라인 숙박 ==========================================================
train=pd.read_csv("C:/data/on_acco(train).csv", sep=',', encoding='utf-8')
x_train=train[['PN','COVID']]
y_train=train['CN']

test=pd.read_csv("C:/data/on_acco(test).csv", sep=',', encoding='utf-8')
x_test=test[['PN','COVID']]
y_test=test['CN']

# 랜덤포레스트 선언: 트리개수 10개 
forest = RandomForestClassifier(n_estimators=10, random_state=0)

# 훈련 데이터를 입력해 Random Forest 모듈을 학습
forest.fit(x_train, y_train)
y_train_pred=forest.predict(x_train)

# Test data를 입력해 target data를 예측
y_pred=forest.predict(x_test)

# 예측 결과 precision과 실제 test data의 target을 비교
print(y_pred)
print(list(y_test))

# 모델 성능 확인 : accuracy, F1 score
print("Train Score is: ", forest.score(x_train,y_train))
print("Test Score is: ", forest.score(x_test,y_test))
# train
print("Train F1 Score is: ", metrics.f1_score(y_train_pred, y_train))
print("Train Accuracy is: ", metrics.accuracy_score(y_train_pred, y_train))
train_F1.append(metrics.f1_score(y_train_pred, y_train))
train_Accuracy.append(metrics.accuracy_score(y_train_pred, y_train))
# test
print("Test F1 Score is: ", metrics.f1_score(y_test, y_pred))
print("Test Accuracy is: ", metrics.accuracy_score(y_test, y_pred))
test_F1.append(metrics.f1_score(y_test, y_pred))
test_Accuracy.append(metrics.accuracy_score(y_test, y_pred))


## 온라인 문화취미 ==========================================================
train=pd.read_csv("C:/data/on_cul(train).csv", sep=',', encoding='utf-8')
x_train=train[['PN','COVID']]
y_train=train['CN']

test=pd.read_csv("C:/data/on_cul(test).csv", sep=',', encoding='utf-8')
x_test=test[['PN','COVID']]
y_test=test['CN']

# 랜덤포레스트 선언: 트리개수 10개 
forest = RandomForestClassifier(n_estimators=10, random_state=0)

# 훈련 데이터를 입력해 Random Forest 모듈을 학습
forest.fit(x_train, y_train)
y_train_pred=forest.predict(x_train)

# Test data를 입력해 target data를 예측
y_pred=forest.predict(x_test)

# 예측 결과 precision과 실제 test data의 target을 비교
print(y_pred)
print(list(y_test))

# 모델 성능 확인 : accuracy, F1 score
print("Train Score is: ", forest.score(x_train,y_train))
print("Test Score is: ", forest.score(x_test,y_test))
# train
print("Train F1 Score is: ", metrics.f1_score(y_train_pred, y_train))
print("Train Accuracy is: ", metrics.accuracy_score(y_train_pred, y_train))
train_F1.append(metrics.f1_score(y_train_pred, y_train))
train_Accuracy.append(metrics.accuracy_score(y_train_pred, y_train))
# test
print("Test F1 Score is: ", metrics.f1_score(y_test, y_pred))
print("Test Accuracy is: ", metrics.accuracy_score(y_test, y_pred))
test_F1.append(metrics.f1_score(y_test, y_pred))
test_Accuracy.append(metrics.accuracy_score(y_test, y_pred))


## 온라인 식품 ==========================================================
train=pd.read_csv("C:/data/on_food(train).csv", sep=',', encoding='utf-8')
x_train=train[['PN','COVID']]
y_train=train['CN']

test=pd.read_csv("C:/data/on_food(test).csv", sep=',', encoding='utf-8')
x_test=test[['PN','COVID']]
y_test=test['CN']

# 랜덤포레스트 선언: 트리개수 10개 
forest = RandomForestClassifier(n_estimators=10, random_state=0)

# 훈련 데이터를 입력해 Random Forest 모듈을 학습
forest.fit(x_train, y_train)
y_train_pred=forest.predict(x_train)

# Test data를 입력해 target data를 예측
y_pred=forest.predict(x_test)

# 예측 결과 precision과 실제 test data의 target을 비교
print(y_pred)
print(list(y_test))

# 모델 성능 확인 : accuracy, F1 score
print("Train Score is: ", forest.score(x_train,y_train))
print("Test Score is: ", forest.score(x_test,y_test))
# train
print("Train F1 Score is: ", metrics.f1_score(y_train_pred, y_train))
print("Train Accuracy is: ", metrics.accuracy_score(y_train_pred, y_train))
train_F1.append(metrics.f1_score(y_train_pred, y_train))
train_Accuracy.append(metrics.accuracy_score(y_train_pred, y_train))
# test
print("Test F1 Score is: ", metrics.f1_score(y_test, y_pred))
print("Test Accuracy is: ", metrics.accuracy_score(y_test, y_pred))
test_F1.append(metrics.f1_score(y_test, y_pred))
test_Accuracy.append(metrics.accuracy_score(y_test, y_pred))


## 온라인 레저 ==========================================================
train=pd.read_csv("C:/data/on_lei(train).csv", sep=',', encoding='utf-8')
x_train=train[['PN','COVID']]
y_train=train['CN']

test=pd.read_csv("C:/data/on_lei(test).csv", sep=',', encoding='utf-8')
x_test=test[['PN','COVID']]
y_test=test['CN']

# 랜덤포레스트 선언: 트리개수 10개 
forest = RandomForestClassifier(n_estimators=10, random_state=0)

# 훈련 데이터를 입력해 Random Forest 모듈을 학습
forest.fit(x_train, y_train)
y_train_pred=forest.predict(x_train)

# Test data를 입력해 target data를 예측
y_pred=forest.predict(x_test)

# 예측 결과 precision과 실제 test data의 target을 비교
print(y_pred)
print(list(y_test))

# 모델 성능 확인 : accuracy, F1 score
print("Train Score is: ", forest.score(x_train,y_train))
print("Test Score is: ", forest.score(x_test,y_test))
# train
print("Train F1 Score is: ", metrics.f1_score(y_train_pred, y_train))
print("Train Accuracy is: ", metrics.accuracy_score(y_train_pred, y_train))
train_F1.append(metrics.f1_score(y_train_pred, y_train))
train_Accuracy.append(metrics.accuracy_score(y_train_pred, y_train))
# test
print("Test F1 Score is: ", metrics.f1_score(y_test, y_pred))
print("Test Accuracy is: ", metrics.accuracy_score(y_test, y_pred))
test_F1.append(metrics.f1_score(y_test, y_pred))
test_Accuracy.append(metrics.accuracy_score(y_test, y_pred))


## 온라인 보건위생 ==========================================================
train=pd.read_csv("C:/data/on_sani(train).csv", sep=',', encoding='utf-8')
x_train=train[['PN','COVID']]
y_train=train['CN']

test=pd.read_csv("C:/data/on_sani(test).csv", sep=',', encoding='utf-8')
x_test=test[['PN','COVID']]
y_test=test['CN']

# 랜덤포레스트 선언: 트리개수 10개 
forest = RandomForestClassifier(n_estimators=10, random_state=0)

# 훈련 데이터를 입력해 Random Forest 모듈을 학습
forest.fit(x_train, y_train)
y_train_pred=forest.predict(x_train)

# Test data를 입력해 target data를 예측
y_pred=forest.predict(x_test)

# 예측 결과 precision과 실제 test data의 target을 비교
print(y_pred)
print(list(y_test))

# 모델 성능 확인 : accuracy, F1 score
print("Train Score is: ", forest.score(x_train,y_train))
print("Test Score is: ", forest.score(x_test,y_test))
# train
print("Train F1 Score is: ", metrics.f1_score(y_train_pred, y_train))
print("Train Accuracy is: ", metrics.accuracy_score(y_train_pred, y_train))
train_F1.append(metrics.f1_score(y_train_pred, y_train))
train_Accuracy.append(metrics.accuracy_score(y_train_pred, y_train))
# test
print("Test F1 Score is: ", metrics.f1_score(y_test, y_pred))
print("Test Accuracy is: ", metrics.accuracy_score(y_test, y_pred))
test_F1.append(metrics.f1_score(y_test, y_pred))
test_Accuracy.append(metrics.accuracy_score(y_test, y_pred))


## 결과 파일로 저장 ==========================================================
result=DataFrame({'name':['off_acco','off_cul','off_food','off_lei','off_medi','off_sani',
                          'on_acco','on_cul','on_food','on_lei','on_sani'],
                  'train_acc':train_Accuracy, 'train_F1':train_F1,
                  'test_acc':test_Accuracy, 'test_F1': test_F1})

result.to_csv("C:/data/rforest_accuracy")


# 7-4) KNN

import glob
from pandas import *
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
import sklearn.metrics as metrics
import numpy as np

#classifier= KNeighborsClassifier(n_neighbors=10)
classifier= KNeighborsClassifier(n_neighbors=5)
accuracy=pd.DataFrame(columns=['name','train_acc','train_f1','test_acc','test_f1'])

file="C:/data/off_acco*.csv"
#off_acco(train).csv
off_acco_lst=['off_acco']
off_acco_train=pd.read_csv(glob.glob(file)[0])
training_points=off_acco_train[['PN','COVID']]
training_labels=off_acco_train['CN']
classifier.fit(training_points,training_labels)
y=training_labels
p=classifier.predict(training_points)
#classifier.score(training_points,training_labels)
#confusion_matrix(classifier.predict(training_points),training_labels)
#n_neighbors=10일때
#y=training_labels
#p=classifier.predict(training_points)
#metrics.accuracy_score(y,p)#0.54292343387471
#metrics.f1_score(y,p)#0.6716666666666666

#n_neighbors=5일때
off_acco_lst.append(metrics.accuracy_score(y,p))#0.54292343387471
off_acco_lst.append(metrics.f1_score(y,p))#0.690251572327044

#off_acco(test).csv
off_acco_test=pd.read_csv(glob.glob(file)[1])
test_points=off_acco_test[['PN','COVID']]
test_labels=off_acco_test['CN']
y=test_labels
p=classifier.predict(test_points)
off_acco_lst.append(metrics.accuracy_score(y,p))#0.52 (k =5) (k=10)
off_acco_lst.append(metrics.f1_score(y,p)) #0.6722090261282659 (k=5)(k=10)
accuracy=accuracy.append(Series(off_acco_lst,index=accuracy.columns),ignore_index=True)
off_acco_lst
#k=5채택

file="C:/data/off_cul*"
#off_cul(train).csv
off_cul_lst=['off_cul']
off_cul_train=pd.read_csv(glob.glob(file)[1])
training_points=off_cul_train[['PN','COVID']]
training_labels=off_cul_train['CN']
classifier.fit(training_points,training_labels)
y=training_labels
p=classifier.predict(training_points)
off_cul_lst.append(metrics.accuracy_score(y,p))
off_cul_lst.append(metrics.f1_score(y,p))
#off_cul(test).csv
off_cul_test=pd.read_csv(glob.glob(file)[0])
test_points=off_cul_test[['PN','COVID']]
test_labels=off_cul_test['CN']
y=test_labels
p=classifier.predict(test_points)
off_cul_lst.append(metrics.accuracy_score(y,p))#0.52 (k =5) (k=10)
off_cul_lst.append(metrics.f1_score(y,p))
accuracy=accuracy.append(Series(off_cul_lst,index=accuracy.columns),ignore_index=True)
off_cul_lst

file="C:/data/off_food*"
#off_food(train).csv
off_food_train=pd.read_csv(glob.glob(file)[0])
off_food_lst=['off_food']
training_points=off_food_train[['PN','COVID']]
training_labels=off_food_train['CN']
classifier.fit(training_points,training_labels)
y=training_labels
p=classifier.predict(training_points)
off_food_lst.append(metrics.accuracy_score(y,p))
off_food_lst.append(metrics.f1_score(y,p))

#off_food(test).csv
off_food_test=pd.read_csv(glob.glob(file)[1])
test_points=off_food_test[['PN','COVID']]
test_labels=off_food_test['CN']
y=test_labels
p=classifier.predict(test_points)
off_food_lst.append(metrics.accuracy_score(y,p))
off_food_lst.append(metrics.f1_score(y,p))
accuracy=accuracy.append(Series(off_food_lst,index=accuracy.columns),ignore_index=True)
off_food_lst

file="C:/data/off_lei*"
#off_lei(train).csv
off_lei_train=pd.read_csv(glob.glob(file)[1])
off_lei_lst=['off_lei']
training_points=off_lei_train[['PN','COVID']]
training_labels=off_lei_train['CN']
classifier.fit(training_points,training_labels)
y=training_labels
p=classifier.predict(training_points)
off_lei_lst.append(metrics.accuracy_score(y,p))
off_lei_lst.append(metrics.f1_score(y,p))

#off_lei(test).csv
off_lei_test=pd.read_csv(glob.glob(file)[0])
test_points=off_lei_test[['PN','COVID']]
test_labels=off_lei_test['CN']
y=test_labels
p=classifier.predict(test_points)
off_lei_lst.append(metrics.accuracy_score(y,p))
off_lei_lst.append(metrics.f1_score(y,p))
accuracy=accuracy.append(Series(off_lei_lst,index=accuracy.columns),ignore_index=True)
off_lei_lst

file="C:/data/off_medi*"
#off_medi(train).csv
off_medi_train=pd.read_csv(glob.glob(file)[0])
off_medi_lst=['off_medi']
training_points=off_medi_train[['PN','COVID']]
training_labels=off_medi_train['CN']
classifier.fit(training_points,training_labels)
y=training_labels
p=classifier.predict(training_points)
off_medi_lst.append(metrics.accuracy_score(y,p))
off_medi_lst.append(metrics.f1_score(y,p))

#off_medi(test).csv
off_medi_test=pd.read_csv(glob.glob(file)[1])
test_points=off_medi_test[['PN','COVID']]
test_labels=off_medi_test['CN']
y=test_labels
p=classifier.predict(test_points)
off_medi_lst.append(metrics.accuracy_score(y,p))
off_medi_lst.append(metrics.f1_score(y,p))
accuracy=accuracy.append(Series(off_medi_lst,index=accuracy.columns),ignore_index=True)
off_medi_lst

file="C:/data/off_sani*"
#off_sani(train).csv
off_sani_train=pd.read_csv(glob.glob(file)[0])
off_sani_lst=['off_sani']
training_points=off_sani_train[['PN','COVID']]
training_labels=off_sani_train['CN']
classifier.fit(training_points,training_labels)
y=training_labels
p=classifier.predict(training_points)
off_sani_lst.append(metrics.accuracy_score(y,p))
off_sani_lst.append(metrics.f1_score(y,p))

#off_sani(test).csv
off_sani_test=pd.read_csv(glob.glob(file)[1])
test_points=off_sani_test[['PN','COVID']]
test_labels=off_sani_test['CN']
y=test_labels
p=classifier.predict(test_points)
off_sani_lst.append(metrics.accuracy_score(y,p))
off_sani_lst.append(metrics.f1_score(y,p))
accuracy=accuracy.append(Series(off_sani_lst,index=accuracy.columns),ignore_index=True)
off_sani_lst

file="C:/data/on_acco*"
#on_acco(train).csv
on_acco_train=pd.read_csv(glob.glob(file)[1])
on_acco_lst=['on_acco']
training_points=on_acco_train[['PN','COVID']]
training_labels=on_acco_train['CN']
classifier.fit(training_points,training_labels)
y=training_labels
p=classifier.predict(training_points)
on_acco_lst.append(metrics.accuracy_score(y,p))
on_acco_lst.append(metrics.f1_score(y,p))

#on_acco(test).csv
on_acco_test=pd.read_csv(glob.glob(file)[0])
test_points=on_acco_test[['PN','COVID']]
test_labels=on_acco_test['CN']
y=test_labels
p=classifier.predict(test_points)
on_acco_lst.append(metrics.accuracy_score(y,p))
on_acco_lst.append(metrics.f1_score(y,p))
accuracy=accuracy.append(Series(on_acco_lst,index=accuracy.columns),ignore_index=True)
on_acco_lst

file="C:/data/on_cul*"
#on_cul(train).csv
on_cul_train=pd.read_csv(glob.glob(file)[0])
on_cul_lst=['on_cul']
training_points=on_cul_train[['PN','COVID']]
training_labels=on_cul_train['CN']
classifier.fit(training_points,training_labels)
y=training_labels
p=classifier.predict(training_points)
on_cul_lst.append(metrics.accuracy_score(y,p))
on_cul_lst.append(metrics.f1_score(y,p))

#on_cul(test).csv
on_cul_test=pd.read_csv(glob.glob(file)[1])
test_points=on_cul_test[['PN','COVID']]
test_labels=on_cul_test['CN']
y=test_labels
p=classifier.predict(test_points)
on_cul_lst.append(metrics.accuracy_score(y,p))
on_cul_lst.append(metrics.f1_score(y,p))
accuracy=accuracy.append(Series(on_cul_lst,index=accuracy.columns),ignore_index=True)
on_cul_lst

file="C:/data/on_food*"
#on_food(train).csv
on_food_train=pd.read_csv(glob.glob(file)[1])
on_food_lst=['on_food']
training_points=on_food_train[['PN','COVID']]
training_labels=on_food_train['CN']
classifier.fit(training_points,training_labels)
y=training_labels
p=classifier.predict(training_points)
on_food_lst.append(metrics.accuracy_score(y,p))
on_food_lst.append(metrics.f1_score(y,p))

#on_food(test).csv
on_food_test=pd.read_csv(glob.glob(file)[0])
test_points=on_food_test[['PN','COVID']]
test_labels=on_food_test['CN']
y=test_labels
p=classifier.predict(test_points)
on_food_lst.append(metrics.accuracy_score(y,p))
on_food_lst.append(metrics.f1_score(y,p))
accuracy=accuracy.append(Series(on_food_lst,index=accuracy.columns),ignore_index=True)
on_food_lst

#on_lei(train).csv
on_lei_train=pd.read_csv(glob.glob(file)[0])
on_lei_lst=['on_lei']
training_points=on_lei_train[['PN','COVID']]
training_labels=on_lei_train['CN']
classifier.fit(training_points,training_labels)
y=training_labels
p=classifier.predict(training_points)
on_lei_lst.append(metrics.accuracy_score(y,p))
on_lei_lst.append(metrics.f1_score(y,p))

#on_lei(test).csv
on_lei_test=pd.read_csv(glob.glob(file)[1])
test_points=on_lei_test[['PN','COVID']]
test_labels=on_lei_test['CN']
y=test_labels
p=classifier.predict(test_points)
on_lei_lst.append(metrics.accuracy_score(y,p))
on_lei_lst.append(metrics.f1_score(y,p))
accuracy=accuracy.append(Series(on_lei_lst,index=accuracy.columns),ignore_index=True)
on_lei_lst

file="C:/data/on_sani*"
#on_sani(train).csv
on_sani_train=pd.read_csv(glob.glob(file)[1])
on_sani_lst=['on_sani']
training_points=on_sani_train[['PN','COVID']]
training_labels=on_sani_train['CN']
classifier.fit(training_points,training_labels)
y=training_labels
p=classifier.predict(training_points)
on_sani_lst.append(metrics.accuracy_score(y,p))
on_sani_lst.append(metrics.f1_score(y,p))

#on_sani(test).csv
on_sani_test=pd.read_csv(glob.glob(file)[0])
test_points=on_sani_test[['PN','COVID']]
test_labels=on_sani_test['CN']
y=test_labels
p=classifier.predict(test_points)
on_sani_lst.append(metrics.accuracy_score(y,p))
on_sani_lst.append(metrics.f1_score(y,p))
accuracy=accuracy.append(Series(on_sani_lst,index=accuracy.columns),ignore_index=True)
on_sani_lst

# 8. 매출 예상 모델

# 8-1) LSTM

# anaconda prompt에서 
pip install -keras
pip install -tensorflow

from pandas import *
import pandas as pd
import numpy as np
import math
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
import matplotlib.pylab as plt
from matplotlib import font_manager, rc
font_name= font_manager.FontProperties(fname="C:/data/a옛날사진관3.ttf").get_name()
rc('font',family=font_name)

def create_dataset(dataset,look_back=1):
    dataX,dataY=[],[]
    for i in range(len(dataset)-look_back-1):
        a=dataset[i:(i+look_back),0]
        dataX.append(a)
        dataY.append(dataset[i+look_back,0])
    return np.array(dataX), np.array(dataY)

accuracy=pd.DataFrame(columns=['name','train','test'])
lst=['off_acc']
#off_acc1
off_acc1=pd.read_csv("C:/data/off_acc1.csv",parse_dates=["DATE"])
off_acc1.info()
#off_acc1_2019=off_acc1[off_acc1['DATE'].dt.year==2019]
off_acc1_2020=off_acc1[off_acc1['DATE'].dt.year==2020]
dataset=off_acc1_2020.loc[:,'CN']
dataset=dataset.values
dataset.astype("float32")
scaler=MinMaxScaler(feature_range=(0,1))
dataset=scaler.fit_transform(dataset.reshape(-1,1))

train_size=int(len(dataset)*0.6)
test_size=len(dataset)-train_size
train,test=dataset[0:train_size,:], dataset[train_size:len(dataset),:]
#print(len(train),len(test))

look_back=1
trainX,trainY = create_dataset(train, look_back)
testX, testY = create_dataset(test,look_back)
trainX = np.reshape(trainX,(trainX.shape[0],1,trainX.shape[1]))
testX = np.reshape(testX,(testX.shape[0],1,testX.shape[1]))

model= Sequential()
model.add(LSTM(4,input_shape=(1,look_back)))
model.add(Dense(1))
model.compile(loss='mean_squared_error',optimizer="adam")
model.fit(trainX,trainY,epochs=100,batch_size=1,verbose=2)

trainPredict = model.predict(trainX)
testPredict=model.predict(testX)

trainPredict = scaler.inverse_transform(trainPredict)
trainY = scaler.inverse_transform([trainY])
testPredict = scaler.inverse_transform(testPredict)
testY=scaler.inverse_transform([testY])

#calculate root mean squared error
lst.append(math.sqrt(mean_squared_error(trainY[0],trainPredict[:,0])))
lst.append(math.sqrt(mean_squared_error(testY[0],testPredict[:,0])))

accuracy=accuracy.append(Series(lst,index=accuracy.columns),ignore_index=True)

trainPredictPlot = np.empty_like(dataset)
trainPredictPlot[:, :] = np.nan
trainPredictPlot[look_back:len(trainPredict)+look_back, :] = trainPredict
testPredictPlot = np.empty_like(dataset)
testPredictPlot[:, :] = np.nan
testPredictPlot[len(trainPredict)+(look_back*2)+1:len(dataset)-1, :] = testPredict

plt.figure(figsize=(8,6))
plt.plot(scaler.inverse_transform(dataset),color="gray",label="real data")
plt.plot(trainPredictPlot,color="blue",label="train predict",linestyle="-.")
plt.plot(testPredictPlot,color="red",label="test predict",linestyle="-.")
plt.legend(loc="lower right")
plt.title("오프라인 숙박 LSTM")
plt.show()

#off_cul1
lst=['off_cul']
off_cul1=pd.read_csv("C:/data/off_cul1.csv")
off_cul1['DATE']=pd.to_datetime(off_cul1['DATE'],format="%Y-%m-%d")
off_cul1_2020=off_cul1[off_cul1['DATE'].dt.year==2020]
dataset=off_cul1_2020.loc[:,'CN']
dataset=dataset.values
dataset.astype("float32")
scaler=MinMaxScaler(feature_range=(0,1))
dataset=scaler.fit_transform(dataset.reshape(-1,1))
train_size=int(len(dataset)*0.6)
test_size=len(dataset)-train_size
train,test=dataset[0:train_size,:], dataset[train_size:len(dataset),:]

look_back=1
trainX,trainY = create_dataset(train, look_back)
testX, testY = create_dataset(test,look_back)
trainX = np.reshape(trainX,(trainX.shape[0],1,trainX.shape[1]))
testX = np.reshape(testX,(testX.shape[0],1,testX.shape[1]))

model= Sequential()
model.add(LSTM(4,input_shape=(1,look_back)))
model.add(Dense(1))
model.compile(loss='mean_squared_error',optimizer="adam")
model.fit(trainX,trainY,epochs=100,batch_size=1,verbose=2)

trainPredict = model.predict(trainX)
testPredict=model.predict(testX)

trainPredict = scaler.inverse_transform(trainPredict)
trainY = scaler.inverse_transform([trainY])
testPredict = scaler.inverse_transform(testPredict)
testY=scaler.inverse_transform([testY])

#calculate root mean squared error
lst.append(math.sqrt(mean_squared_error(trainY[0],trainPredict[:,0])))
lst.append(math.sqrt(mean_squared_error(testY[0],testPredict[:,0])))

accuracy=accuracy.append(Series(lst,index=accuracy.columns),ignore_index=True)

trainPredictPlot = np.empty_like(dataset)
trainPredictPlot[:, :] = np.nan
trainPredictPlot[look_back:len(trainPredict)+look_back, :] = trainPredict
testPredictPlot = np.empty_like(dataset)
testPredictPlot[:, :] = np.nan
testPredictPlot[len(trainPredict)+(look_back*2)+1:len(dataset)-1, :] = testPredict

plt.figure(figsize=(8,6))
plt.plot(scaler.inverse_transform(dataset),color="gray",label="real data")
plt.plot(trainPredictPlot,color="blue",label="train predict",linestyle="-.")
plt.plot(testPredictPlot,color="red",label="test predict",linestyle="-.")
plt.legend(loc="lower right")
plt.title("오프라인 문화취미 LSTM")
plt.show()

#off_food1
lst=['off_food']
off_food1=pd.read_csv("C:/data/off_food2.csv",parse_dates=["DATE"])
off_food1_2020=off_food1[off_food1['DATE'].dt.year==2020]
dataset=off_food1_2020.loc[:,'CN']
dataset=dataset.values
dataset.astype("float32")
scaler=MinMaxScaler(feature_range=(0,1))
dataset=scaler.fit_transform(dataset.reshape(-1,1))
train_size=int(len(dataset)*0.6)
test_size=len(dataset)-train_size
train,test=dataset[0:train_size,:], dataset[train_size:len(dataset),:]
#print(len(train),len(test))

look_back=1
trainX,trainY = create_dataset(train, look_back)
testX, testY = create_dataset(test,look_back)
trainX = np.reshape(trainX,(trainX.shape[0],1,trainX.shape[1]))
testX = np.reshape(testX,(testX.shape[0],1,testX.shape[1]))

model= Sequential()
model.add(LSTM(4,input_shape=(1,look_back)))
model.add(Dense(1))
model.compile(loss='mean_squared_error',optimizer="adam")
model.fit(trainX,trainY,epochs=100,batch_size=1,verbose=2)

trainPredict = model.predict(trainX)
testPredict=model.predict(testX)

trainPredict = scaler.inverse_transform(trainPredict)
trainY = scaler.inverse_transform([trainY])
testPredict = scaler.inverse_transform(testPredict)
testY=scaler.inverse_transform([testY])

#calculate root mean squared error
lst.append(math.sqrt(mean_squared_error(trainY[0],trainPredict[:,0])))
lst.append(math.sqrt(mean_squared_error(testY[0],testPredict[:,0])))

accuracy=accuracy.append(Series(lst,index=accuracy.columns),ignore_index=True)

trainPredictPlot = np.empty_like(dataset)
trainPredictPlot[:, :] = np.nan
trainPredictPlot[look_back:len(trainPredict)+look_back, :] = trainPredict
testPredictPlot = np.empty_like(dataset)
testPredictPlot[:, :] = np.nan
testPredictPlot[len(trainPredict)+(look_back*2)+1:len(dataset)-1, :] = testPredict

plt.figure(figsize=(8,6))
plt.plot(scaler.inverse_transform(dataset),color="gray",label="real data")
plt.plot(trainPredictPlot,color="blue",label="train predict",linestyle="-.")
plt.plot(testPredictPlot,color="red",label="test predict",linestyle="-.")
plt.legend(loc="lower right")
plt.title("오프라인 요식업소 LSTM")
plt.show()

#off_lei1
lst=['off_lei']
off_lei1=pd.read_csv("C:/data/off_lei1.csv",parse_dates=["DATE"])
off_lei1_2020=off_lei1[off_lei1['DATE'].dt.year==2020]
dataset=off_lei1_2020.loc[:,'CN']
dataset=dataset.values
dataset.astype("float32")
scaler=MinMaxScaler(feature_range=(0,1))
dataset=scaler.fit_transform(dataset.reshape(-1,1))

train_size=int(len(dataset)*0.6)
test_size=len(dataset)-train_size
train,test=dataset[0:train_size,:], dataset[train_size:len(dataset),:]
print(len(train),len(test))

look_back=1
trainX,trainY = create_dataset(train, look_back)
testX, testY = create_dataset(test,look_back)
trainX = np.reshape(trainX,(trainX.shape[0],1,trainX.shape[1]))
testX = np.reshape(testX,(testX.shape[0],1,testX.shape[1]))

model= Sequential()
model.add(LSTM(4,input_shape=(1,look_back)))
model.add(Dense(1))
model.compile(loss='mean_squared_error',optimizer="adam")
model.fit(trainX,trainY,epochs=100,batch_size=1,verbose=2)

trainPredict = model.predict(trainX)
testPredict=model.predict(testX)

trainPredict = scaler.inverse_transform(trainPredict)
trainY = scaler.inverse_transform([trainY])
testPredict = scaler.inverse_transform(testPredict)
testY=scaler.inverse_transform([testY])

#calculate root mean squared error
lst.append(math.sqrt(mean_squared_error(trainY[0],trainPredict[:,0])))
lst.append(math.sqrt(mean_squared_error(testY[0],testPredict[:,0])))

accuracy=accuracy.append(Series(lst,index=accuracy.columns),ignore_index=True)

trainPredictPlot = np.empty_like(dataset)
trainPredictPlot[:, :] = np.nan
trainPredictPlot[look_back:len(trainPredict)+look_back, :] = trainPredict
testPredictPlot = np.empty_like(dataset)
testPredictPlot[:, :] = np.nan
testPredictPlot[len(trainPredict)+(look_back*2)+1:len(dataset)-1, :] = testPredict

plt.figure(figsize=(8,6))
plt.plot(scaler.inverse_transform(dataset),color="gray",label="real data") # 진짜 데이터 셋
plt.plot(trainPredictPlot,color="blue",label="train predict",linestyle="-.") # train 예측 데이터 그래프
plt.plot(testPredictPlot,color="red",label="test predict",linestyle="-.") # test 테스트 데이터 그래프
plt.legend(loc="lower right")
plt.title("오프라인 레저 LSTM")
plt.show()

#off_medi1
lst=['off_medi']
off_medi1=pd.read_csv("C:/data/off_medi1.csv",parse_dates=["DATE"])
off_medi1_2020=off_medi1[off_medi1['DATE'].dt.year==2020]

dataset=off_medi1_2020.loc[:,'CN']
dataset=dataset.values
dataset.astype("float32")
scaler=MinMaxScaler(feature_range=(0,1))
dataset=scaler.fit_transform(dataset.reshape(-1,1))

train_size=int(len(dataset)*0.6)
test_size=len(dataset)-train_size
train,test=dataset[0:train_size,:], dataset[train_size:len(dataset),:]

look_back=1
trainX,trainY = create_dataset(train, look_back)
testX, testY = create_dataset(test,look_back)
trainX = np.reshape(trainX,(trainX.shape[0],1,trainX.shape[1]))
testX = np.reshape(testX,(testX.shape[0],1,testX.shape[1]))

model= Sequential()
model.add(LSTM(4,input_shape=(1,look_back)))
model.add(Dense(1))
model.compile(loss='mean_squared_error',optimizer="adam")
model.fit(trainX,trainY,epochs=100,batch_size=1,verbose=2)

trainPredict = model.predict(trainX)
testPredict=model.predict(testX)

trainPredict = scaler.inverse_transform(trainPredict)
trainY = scaler.inverse_transform([trainY])
testPredict = scaler.inverse_transform(testPredict)
testY=scaler.inverse_transform([testY])

#calculate root mean squared error
lst.append(math.sqrt(mean_squared_error(trainY[0],trainPredict[:,0])))
lst.append(math.sqrt(mean_squared_error(testY[0],testPredict[:,0])))

accuracy=accuracy.append(Series(lst,index=accuracy.columns),ignore_index=True)

trainPredictPlot = np.empty_like(dataset)
trainPredictPlot[:, :] = np.nan
trainPredictPlot[look_back:len(trainPredict)+look_back, :] = trainPredict
testPredictPlot = np.empty_like(dataset)
testPredictPlot[:, :] = np.nan
testPredictPlot[len(trainPredict)+(look_back*2)+1:len(dataset)-1, :] = testPredict

plt.figure(figsize=(8,6))
plt.plot(scaler.inverse_transform(dataset),color="gray",label="real data")
plt.plot(trainPredictPlot,color="blue",label="train predict",linestyle="-.")
plt.plot(testPredictPlot,color="red",label="test predict",linestyle="-.")
plt.legend(loc="lower right")
plt.title("오프라인 의료기관 LSTM")
plt.show()

#off_sani1
lst=['off_sani']
off_sani1=pd.read_csv("C:/data/off_sani1.csv",parse_dates=["DATE"])
off_sani1_2020=off_sani1[off_sani1['DATE'].dt.year==2020]

dataset=off_sani1_2020.loc[:,'CN']
dataset=dataset.values
dataset.astype("float32")
scaler=MinMaxScaler(feature_range=(0,1))
dataset=scaler.fit_transform(dataset.reshape(-1,1))

train_size=int(len(dataset)*0.6)
test_size=len(dataset)-train_size
train,test=dataset[0:train_size,:], dataset[train_size:len(dataset),:]
#print(len(train),len(test))

look_back=1
trainX,trainY = create_dataset(train, look_back)
testX, testY = create_dataset(test,look_back)
trainX = np.reshape(trainX,(trainX.shape[0],1,trainX.shape[1]))
testX = np.reshape(testX,(testX.shape[0],1,testX.shape[1]))

model= Sequential()
model.add(LSTM(4,input_shape=(1,look_back)))
model.add(Dense(1))
model.compile(loss='mean_squared_error',optimizer="adam")
model.fit(trainX,trainY,epochs=100,batch_size=1,verbose=2)

trainPredict = model.predict(trainX)
testPredict=model.predict(testX)

trainPredict = scaler.inverse_transform(trainPredict)
trainY = scaler.inverse_transform([trainY])
testPredict = scaler.inverse_transform(testPredict)
testY=scaler.inverse_transform([testY])

#calculate root mean squared error
lst.append(math.sqrt(mean_squared_error(trainY[0],trainPredict[:,0])))
lst.append(math.sqrt(mean_squared_error(testY[0],testPredict[:,0])))

accuracy=accuracy.append(Series(lst,index=accuracy.columns),ignore_index=True)

trainPredictPlot = np.empty_like(dataset)
trainPredictPlot[:, :] = np.nan
trainPredictPlot[look_back:len(trainPredict)+look_back, :] = trainPredict
testPredictPlot = np.empty_like(dataset)
testPredictPlot[:, :] = np.nan
testPredictPlot[len(trainPredict)+(look_back*2)+1:len(dataset)-1, :] = testPredict

plt.figure(figsize=(8,6))
plt.plot(scaler.inverse_transform(dataset),color="gray",label="real data")
plt.plot(trainPredictPlot,color="blue",label="train predict",linestyle="-.")
plt.plot(testPredictPlot,color="red",label="test predict",linestyle="-.")
plt.legend(loc="lower right")
plt.title("오프라인 보건위생 LSTM")
plt.show()

#on_acc1
lst=['on_acc']
on_acc1=pd.read_csv("C:/data/on_acc1.csv")
on_acc1['DATE']=pd.to_datetime(on_acc1['DATE'],format="%y%m%d")
on_acc1_2020=on_acc1[on_acc1['DATE'].dt.year==2020]

dataset=on_acc1_2020.loc[:,'CN']
dataset=dataset.values
dataset.astype("float32")
scaler=MinMaxScaler(feature_range=(0,1))
dataset=scaler.fit_transform(dataset.reshape(-1,1))

train_size=int(len(dataset)*0.6)
test_size=len(dataset)-train_size
train,test=dataset[0:train_size,:], dataset[train_size:len(dataset),:]
#print(len(train),len(test))

look_back=1
trainX,trainY = create_dataset(train, look_back)
testX, testY = create_dataset(test,look_back)
trainX = np.reshape(trainX,(trainX.shape[0],1,trainX.shape[1]))
testX = np.reshape(testX,(testX.shape[0],1,testX.shape[1]))

model= Sequential()
model.add(LSTM(4,input_shape=(1,look_back)))
model.add(Dense(1))
model.compile(loss='mean_squared_error',optimizer="adam")
model.fit(trainX,trainY,epochs=100,batch_size=1,verbose=2)

trainPredict = model.predict(trainX)
testPredict=model.predict(testX)

trainPredict = scaler.inverse_transform(trainPredict)
trainY = scaler.inverse_transform([trainY])
testPredict = scaler.inverse_transform(testPredict)
testY=scaler.inverse_transform([testY])

#calculate root mean squared error
lst.append(math.sqrt(mean_squared_error(trainY[0],trainPredict[:,0])))
lst.append(math.sqrt(mean_squared_error(testY[0],testPredict[:,0])))

accuracy=accuracy.append(Series(lst,index=accuracy.columns),ignore_index=True)

trainPredictPlot = np.empty_like(dataset)
trainPredictPlot[:, :] = np.nan
trainPredictPlot[look_back:len(trainPredict)+look_back, :] = trainPredict
testPredictPlot = np.empty_like(dataset)
testPredictPlot[:, :] = np.nan
testPredictPlot[len(trainPredict)+(look_back*2)+1:len(dataset)-1, :] = testPredict

plt.figure(figsize=(8,6))
plt.plot(scaler.inverse_transform(dataset),color="gray",label="real data")
plt.plot(trainPredictPlot,color="blue",label="train predict",linestyle="-.")
plt.plot(testPredictPlot,color="red",label="test predict",linestyle="-.")
plt.legend(loc="lower right")
plt.title("온라인 숙박 LSTM")
plt.show()


#on_cul1
lst=['on_cul']
on_cul1=pd.read_csv("C:/data/on_cul1.csv")
on_cul1['DATE']=pd.to_datetime(on_cul1['DATE'],format="%y%m%d")
on_cul1_2020=on_cul1[on_cul1['DATE'].dt.year==2020]

dataset=on_cul1_2020.loc[:,'CN']
dataset=dataset.values
dataset.astype("float32")
scaler=MinMaxScaler(feature_range=(0,1))
dataset=scaler.fit_transform(dataset.reshape(-1,1))

train_size=int(len(dataset)*0.6)
test_size=len(dataset)-train_size
train,test=dataset[0:train_size,:], dataset[train_size:len(dataset),:]
#print(len(train),len(test))

look_back=1
trainX,trainY = create_dataset(train, look_back)
testX, testY = create_dataset(test,look_back)
trainX = np.reshape(trainX,(trainX.shape[0],1,trainX.shape[1]))
testX = np.reshape(testX,(testX.shape[0],1,testX.shape[1]))

model= Sequential()
model.add(LSTM(4,input_shape=(1,look_back)))
model.add(Dense(1))
model.compile(loss='mean_squared_error',optimizer="adam")
model.fit(trainX,trainY,epochs=100,batch_size=1,verbose=2)

trainPredict = model.predict(trainX)
testPredict=model.predict(testX)

trainPredict = scaler.inverse_transform(trainPredict)
trainY = scaler.inverse_transform([trainY])
testPredict = scaler.inverse_transform(testPredict)
testY=scaler.inverse_transform([testY])

#calculate root mean squared error
lst.append(math.sqrt(mean_squared_error(trainY[0],trainPredict[:,0])))
lst.append(math.sqrt(mean_squared_error(testY[0],testPredict[:,0])))

accuracy=accuracy.append(Series(lst,index=accuracy.columns),ignore_index=True)

trainPredictPlot = np.empty_like(dataset)
trainPredictPlot[:, :] = np.nan
trainPredictPlot[look_back:len(trainPredict)+look_back, :] = trainPredict
testPredictPlot = np.empty_like(dataset)
testPredictPlot[:, :] = np.nan
testPredictPlot[len(trainPredict)+(look_back*2)+1:len(dataset)-1, :] = testPredict

plt.figure(figsize=(8,6))
plt.plot(scaler.inverse_transform(dataset),color="gray",label="real data")
plt.plot(trainPredictPlot,color="blue",label="train predict",linestyle="-.")
plt.plot(testPredictPlot,color="red",label="test predict",linestyle="-.")
plt.legend(loc="lower right")
plt.title("온라인 문화취미 LSTM")
plt.show()

#on_food1
lst=['on_food']
on_food1=pd.read_csv("C:/data/on_food1.csv")
on_food1['DATE']=pd.to_datetime(on_food1['DATE'],format="%y%m%d")
on_food1_2020=on_food1[on_food1['DATE'].dt.year==2020]
dataset=on_food1_2020.loc[:,'CN']

dataset=dataset.values
dataset.astype("float32")
scaler=MinMaxScaler(feature_range=(0,1))
dataset=scaler.fit_transform(dataset.reshape(-1,1))

train_size=int(len(dataset)*0.6)
test_size=len(dataset)-train_size
train,test=dataset[0:train_size,:], dataset[train_size:len(dataset),:]
#print(len(train),len(test))

look_back=1
trainX,trainY = create_dataset(train, look_back)
testX, testY = create_dataset(test,look_back)
trainX = np.reshape(trainX,(trainX.shape[0],1,trainX.shape[1]))
testX = np.reshape(testX,(testX.shape[0],1,testX.shape[1]))

model= Sequential()
model.add(LSTM(4,input_shape=(1,look_back)))
model.add(Dense(1))
model.compile(loss='mean_squared_error',optimizer="adam")
model.fit(trainX,trainY,epochs=100,batch_size=1,verbose=2)

trainPredict = model.predict(trainX)
testPredict=model.predict(testX)

trainPredict = scaler.inverse_transform(trainPredict)
trainY = scaler.inverse_transform([trainY])
testPredict = scaler.inverse_transform(testPredict)
testY=scaler.inverse_transform([testY])

#calculate root mean squared error
lst.append(math.sqrt(mean_squared_error(trainY[0],trainPredict[:,0])))
lst.append(math.sqrt(mean_squared_error(testY[0],testPredict[:,0])))

accuracy=accuracy.append(Series(lst,index=accuracy.columns),ignore_index=True)

trainPredictPlot = np.empty_like(dataset)
trainPredictPlot[:, :] = np.nan
trainPredictPlot[look_back:len(trainPredict)+look_back, :] = trainPredict
testPredictPlot = np.empty_like(dataset)
testPredictPlot[:, :] = np.nan
testPredictPlot[len(trainPredict)+(look_back*2)+1:len(dataset)-1, :] = testPredict

plt.figure(figsize=(8,6))
plt.plot(scaler.inverse_transform(dataset),color="gray",label="real data")
plt.plot(trainPredictPlot,color="blue",label="train predict",linestyle="-.")
plt.plot(testPredictPlot,color="red",label="test predict",linestyle="-.")
plt.legend(loc="lower right")
plt.title("온라인 요식업소 LSTM")
plt.show()

#on_lei1
lst=['on_lei']
on_lei1=pd.read_csv("C:/data/on_lei1.csv")
on_lei1['DATE']=pd.to_datetime(on_lei1['DATE'],format="%y%m%d")
on_lei1_2020=on_lei1[on_lei1['DATE'].dt.year==2020]

dataset=on_lei1_2020.loc[:,'CN']
dataset=dataset.values
dataset.astype("float32")
scaler=MinMaxScaler(feature_range=(0,1))
dataset=scaler.fit_transform(dataset.reshape(-1,1))

train_size=int(len(dataset)*0.6)
test_size=len(dataset)-train_size
train,test=dataset[0:train_size,:], dataset[train_size:len(dataset),:]
#print(len(train),len(test))

look_back=1
trainX,trainY = create_dataset(train, look_back)
testX, testY = create_dataset(test,look_back)
trainX = np.reshape(trainX,(trainX.shape[0],1,trainX.shape[1]))
testX = np.reshape(testX,(testX.shape[0],1,testX.shape[1]))

model= Sequential()
model.add(LSTM(4,input_shape=(1,look_back)))
model.add(Dense(1))
model.compile(loss='mean_squared_error',optimizer="adam")
model.fit(trainX,trainY,epochs=100,batch_size=1,verbose=2)

trainPredict = model.predict(trainX)
testPredict=model.predict(testX)

trainPredict = scaler.inverse_transform(trainPredict)
trainY = scaler.inverse_transform([trainY])
testPredict = scaler.inverse_transform(testPredict)
testY=scaler.inverse_transform([testY])

#calculate root mean squared error
lst.append(math.sqrt(mean_squared_error(trainY[0],trainPredict[:,0])))
lst.append(math.sqrt(mean_squared_error(testY[0],testPredict[:,0])))

accuracy=accuracy.append(Series(lst,index=accuracy.columns),ignore_index=True)

trainPredictPlot = np.empty_like(dataset)
trainPredictPlot[:, :] = np.nan
trainPredictPlot[look_back:len(trainPredict)+look_back, :] = trainPredict
testPredictPlot = np.empty_like(dataset)
testPredictPlot[:, :] = np.nan
testPredictPlot[len(trainPredict)+(look_back*2)+1:len(dataset)-1, :] = testPredict

plt.figure(figsize=(8,6))
plt.plot(scaler.inverse_transform(dataset),color="gray",label="real data")
plt.plot(trainPredictPlot,color="blue",label="train predict",linestyle="-.")
plt.plot(testPredictPlot,color="red",label="test predict",linestyle="-.")
plt.legend(loc="lower right")
plt.title("온라인 레저 LSTM")
plt.show()

#on_sani
lst=['on_sani']
on_sani1=pd.read_csv("C:/data/on_sani1.csv")
on_sani1['DATE']=pd.to_datetime(on_sani1['DATE'],format="%y%m%d")
on_sani1_2020=on_sani1[on_sani1['DATE'].dt.year==2020]

dataset=on_sani1_2020.loc[:,'CN']
dataset=dataset.values
dataset.astype("float32")
scaler=MinMaxScaler(feature_range=(0,1))
dataset=scaler.fit_transform(dataset.reshape(-1,1))

train_size=int(len(dataset)*0.6)
test_size=len(dataset)-train_size
train,test=dataset[0:train_size,:], dataset[train_size:len(dataset),:]
print(len(train),len(test))

look_back=1
trainX,trainY = create_dataset(train, look_back)
testX, testY = create_dataset(test,look_back)
trainX = np.reshape(trainX,(trainX.shape[0],1,trainX.shape[1]))
testX = np.reshape(testX,(testX.shape[0],1,testX.shape[1]))

model= Sequential()
model.add(LSTM(4,input_shape=(1,look_back)))
model.add(Dense(1))
model.compile(loss='mean_squared_error',optimizer="adam")
model.fit(trainX,trainY,epochs=100,batch_size=1,verbose=2)

trainPredict = model.predict(trainX)
testPredict=model.predict(testX)

trainPredict = scaler.inverse_transform(trainPredict)
trainY = scaler.inverse_transform([trainY])
testPredict = scaler.inverse_transform(testPredict)
testY=scaler.inverse_transform([testY])

#calculate root mean squared error
lst.append(math.sqrt(mean_squared_error(trainY[0],trainPredict[:,0])))
lst.append(math.sqrt(mean_squared_error(testY[0],testPredict[:,0])))

accuracy=accuracy.append(Series(lst,index=accuracy.columns),ignore_index=True)

trainPredictPlot = np.empty_like(dataset)
trainPredictPlot[:, :] = np.nan
trainPredictPlot[look_back:len(trainPredict)+look_back, :] = trainPredict
testPredictPlot = np.empty_like(dataset)
testPredictPlot[:, :] = np.nan
testPredictPlot[len(trainPredict)+(look_back*2)+1:len(dataset)-1, :] = testPredict

plt.figure(figsize=(8,6))
plt.plot(scaler.inverse_transform(dataset),color="gray",label="real data")
plt.plot(trainPredictPlot,color="blue",label="train predict",linestyle="-.")
plt.plot(testPredictPlot,color="red",label="test predict",linestyle="-.")
plt.legend(loc="lower right")
plt.title("온라인 보건위생 LSTM")
plt.show()

accuracy.to_csv("C:/data/LSTM_acc.csv",index=False)

# 8-2) ARIMA

import warnings
import itertools # 반복 가능한 데이터 스트림을 처리하는 데 유용한 많은 함수와 제네레이터가 포함
import numpy as np
import matplotlib.pyplot as plt
warnings.filterwarnings("ignore")
plt.style.use('fivethirtyeight')
import pandas as pd
import statsmodels.api as sm #통계분석 기능을 제공하는 파이썬 패키지
import matplotlib
from pylab import rcParams

#차트 기본 크기 설정
matplotlib.rcParams['axes.labelsize'] = 14
matplotlib.rcParams['xtick.labelsize'] = 12
matplotlib.rcParams['ytick.labelsize'] = 12
matplotlib.rcParams['text.color'] = 'k'

pd.set_option('display.max_columns',500) #생략없이 출력


## 오프라인 숙박===============================================================
off_acc1 = pd.read_csv("c:/data/off_acc1.csv",parse_dates=["DATE"])
off_acc1.info()

off_acc1 = off_acc1[['DATE','CN']]

# 2020년 데이터만 뽑음
off_acc2020 = off_acc1[off_acc1['DATE'].dt.year==2020]

#index를 Order Date로 한다.
off_acc2020 = off_acc2020.set_index('DATE')
off_acc2020.head()
off_acc2020.index

y=off_acc2020
y.plot(figsize = (15,6))
plt.show()

#차트 기본 크기 설정
rcParams['figure.figsize'] = 18,8

p = d = q = range(0, 2)
pdq = list(itertools.product(p, d, q))
seasonal_pdq = [(x[0], x[1], x[2], 12) for x in list(itertools.product(p, d, q))]

print('Examples of parameter combinations for Seasonal ARIMA...')
print('SARIMAX: {} x {}'.format(pdq[1], seasonal_pdq[1]))
print('SARIMAX: {} x {}'.format(pdq[1], seasonal_pdq[2]))
print('SARIMAX: {} x {}'.format(pdq[2], seasonal_pdq[3]))
print('SARIMAX: {} x {}'.format(pdq[2], seasonal_pdq[4]))

for param in pdq:
    for param_seasonal in seasonal_pdq:
        try:
            mod = sm.tsa.statespace.SARIMAX(y,
                                            order=param,
                                            seasonal_order=param_seasonal,
                                            enforce_stationarity=False,
                                            enforce_invertibility=False)
            results = mod.fit()
            print('ARIMA{}x{}12 - AIC:{}'.format(param, param_seasonal, results.aic))
        except:
            continue

# ARIMA(1, 1, 1)x(1, 1, 1, 12)12 - AIC:1479.5321555603011 

mod = sm.tsa.statespace.SARIMAX(y,
                                order=(1, 1, 1),
                                seasonal_order=(1, 1, 1, 12),
                                enforce_stationarity=False,
                                enforce_invertibility=False)
results = mod.fit()
print(results.summary().tables[1])

results.plot_diagnostics(figsize=(16, 8))
plt.show()

pred = results.get_prediction(start=pd.to_datetime('2020-02-01'), dynamic=False)
pred_ci = pred.conf_int() #추정된 계수의 신뢰구간 계산
ax = y['2020':].plot(label='observed')
pred.predicted_mean.plot(ax=ax, label='One-step ahead Forecast', alpha=.7, figsize=(14, 7))
ax.fill_between(pred_ci.index,
                pred_ci.iloc[:, 0],
                pred_ci.iloc[:, 1], color='k', alpha=.2)
ax.set_xlabel('Date')
ax.set_ylabel('CN')
plt.legend()
plt.show()

y_forecasted = pred.predicted_mean.values
y_truth = y['2020-02-01':].values
mse = ((y_forecasted - y_truth) ** 2).mean()
print('The Mean Squared Error of our forecasts is {}'.format(round(mse, 2)))

print('The Root Mean Squared Error of our forecasts is {}'.format(round(np.sqrt(mse), 2)))

off_acc_MSE = round(np.sqrt(mse), 2)


## 오프라인 문화취미===============================================================
off_cul1 = pd.read_csv("c:/data/off_cul1.csv",parse_dates=["DATE"])
off_cul1.info()

off_cul1 = off_cul1[['DATE','CN']]

# 2020년 데이터만 뽑음
off_cul2020 = off_cul1[off_cul1['DATE'].dt.year==2020]

#index를 Order Date로 한다.
off_cul2020 = off_cul2020.set_index('DATE')
off_cul2020.head()
off_cul2020.index

y=off_cul2020
y.plot(figsize = (15,6))
plt.show()

#차트 기본 크기 설정
rcParams['figure.figsize'] = 18,8

p = d = q = range(0, 2)
pdq = list(itertools.product(p, d, q))
seasonal_pdq = [(x[0], x[1], x[2], 12) for x in list(itertools.product(p, d, q))]

print('Examples of parameter combinations for Seasonal ARIMA...')
print('SARIMAX: {} x {}'.format(pdq[1], seasonal_pdq[1]))
print('SARIMAX: {} x {}'.format(pdq[1], seasonal_pdq[2]))
print('SARIMAX: {} x {}'.format(pdq[2], seasonal_pdq[3]))
print('SARIMAX: {} x {}'.format(pdq[2], seasonal_pdq[4]))

for param in pdq:
    for param_seasonal in seasonal_pdq:
        try:
            mod = sm.tsa.statespace.SARIMAX(y,
                                            order=param,
                                            seasonal_order=param_seasonal,
                                            enforce_stationarity=False,
                                            enforce_invertibility=False)
            results = mod.fit()
            print('ARIMA{}x{}12 - AIC:{}'.format(param, param_seasonal, results.aic))
        except:
            continue

# ARIMA(1, 1, 1)x(1, 1, 1, 12)12 - AIC:1642.9795636032777 

mod = sm.tsa.statespace.SARIMAX(y,
                                order=(1, 1, 1),
                                seasonal_order=(1, 1, 1, 12),
                                enforce_stationarity=False,
                                enforce_invertibility=False)
results = mod.fit()
print(results.summary().tables[1])

results.plot_diagnostics(figsize=(16, 8))
plt.show()

pred = results.get_prediction(start=pd.to_datetime('2020-02-02'), dynamic=False)
pred_ci = pred.conf_int() #추정된 계수의 신뢰구간 계산
ax = y['2020':].plot(label='observed')
pred.predicted_mean.plot(ax=ax, label='One-step ahead Forecast', alpha=.7, figsize=(14, 7))
ax.fill_between(pred_ci.index,
                pred_ci.iloc[:, 0],
                pred_ci.iloc[:, 1], color='k', alpha=.2)
ax.set_xlabel('Date')
ax.set_ylabel('CN')
plt.legend()
plt.show()

y_forecasted = pred.predicted_mean.values
y_truth = y['2020-02-01':].values
mse = ((y_forecasted - y_truth) ** 2).mean()
print('The Mean Squared Error of our forecasts is {}'.format(round(mse, 2)))

print('The Root Mean Squared Error of our forecasts is {}'.format(round(np.sqrt(mse), 2)))

off_cul_MSE = round(np.sqrt(mse), 2)

## 오프라인 요식업소===============================================================
off_food1 = pd.read_csv("c:/data/off_food1.csv",parse_dates=["DATE"])
off_food1.info()

off_food1 = off_food1[['DATE','CN']]

# 2020년 데이터만 뽑음
off_food2020 = off_food1[off_food1['DATE'].dt.year==2020]

#index를 Order Date로 한다.
off_food2020 = off_food2020.set_index('DATE')
off_food2020.head()
off_food2020.index

y=off_food2020
y.plot(figsize = (15,6))
plt.show()

#차트 기본 크기 설정
rcParams['figure.figsize'] = 18,8

p = d = q = range(0, 2)
pdq = list(itertools.product(p, d, q))
seasonal_pdq = [(x[0], x[1], x[2], 12) for x in list(itertools.product(p, d, q))]

print('Examples of parameter combinations for Seasonal ARIMA...')
print('SARIMAX: {} x {}'.format(pdq[1], seasonal_pdq[1]))
print('SARIMAX: {} x {}'.format(pdq[1], seasonal_pdq[2]))
print('SARIMAX: {} x {}'.format(pdq[2], seasonal_pdq[3]))
print('SARIMAX: {} x {}'.format(pdq[2], seasonal_pdq[4]))

for param in pdq:
    for param_seasonal in seasonal_pdq:
        try:
            mod = sm.tsa.statespace.SARIMAX(y,
                                            order=param,
                                            seasonal_order=param_seasonal,
                                            enforce_stationarity=False,
                                            enforce_invertibility=False)
            results = mod.fit()
            print('ARIMA{}x{}12 - AIC:{}'.format(param, param_seasonal, results.aic))
        except:
            continue

# ARIMA(1, 1, 1)x(1, 1, 1, 12)12 - AIC:2314.6204604255795

mod = sm.tsa.statespace.SARIMAX(y,
                                order=(1, 1, 1),
                                seasonal_order=(1, 1, 1, 12),
                                enforce_stationarity=False,
                                enforce_invertibility=False)
results = mod.fit()
print(results.summary().tables[1])

results.plot_diagnostics(figsize=(16, 8))
plt.show()

pred = results.get_prediction(start=pd.to_datetime('2020-02-02'), dynamic=False)
pred_ci = pred.conf_int() #추정된 계수의 신뢰구간 계산
ax = y['2020':].plot(label='observed')
pred.predicted_mean.plot(ax=ax, label='One-step ahead Forecast', alpha=.7, figsize=(14, 7))
ax.fill_between(pred_ci.index,
                pred_ci.iloc[:, 0],
                pred_ci.iloc[:, 1], color='k', alpha=.2)
ax.set_xlabel('Date')
ax.set_ylabel('CN')
plt.legend()
plt.show()

y_forecasted = pred.predicted_mean.values
y_truth = y['2020-02-01':].values
mse = ((y_forecasted - y_truth) ** 2).mean()
print('The Mean Squared Error of our forecasts is {}'.format(round(mse, 2)))

print('The Root Mean Squared Error of our forecasts is {}'.format(round(np.sqrt(mse), 2)))

off_food_MSE = round(np.sqrt(mse), 2)


## 오프라인 레저===============================================================
off_lei1 = pd.read_csv("c:/data/off_lei1.csv",parse_dates=["DATE"])
off_lei1.info()

off_lei1 = off_lei1[['DATE','CN']]

# 2020년 데이터만 뽑음
off_lei2020 = off_lei1[off_lei1['DATE'].dt.year==2020]

#index를 Order Date로 한다.
off_lei2020 = off_lei2020.set_index('DATE')
off_lei2020.head()
off_lei2020.index

y=off_lei2020
y.plot(figsize = (15,6))
plt.show()

#차트 기본 크기 설정
rcParams['figure.figsize'] = 18,8

p = d = q = range(0, 2)
pdq = list(itertools.product(p, d, q))
seasonal_pdq = [(x[0], x[1], x[2], 12) for x in list(itertools.product(p, d, q))]

print('Examples of parameter combinations for Seasonal ARIMA...')
print('SARIMAX: {} x {}'.format(pdq[1], seasonal_pdq[1]))
print('SARIMAX: {} x {}'.format(pdq[1], seasonal_pdq[2]))
print('SARIMAX: {} x {}'.format(pdq[2], seasonal_pdq[3]))
print('SARIMAX: {} x {}'.format(pdq[2], seasonal_pdq[4]))

for param in pdq:
    for param_seasonal in seasonal_pdq:
        try:
            mod = sm.tsa.statespace.SARIMAX(y,
                                            order=param,
                                            seasonal_order=param_seasonal,
                                            enforce_stationarity=False,
                                            enforce_invertibility=False)
            results = mod.fit()
            print('ARIMA{}x{}12 - AIC:{}'.format(param, param_seasonal, results.aic))
        except:
            continue

# ARIMA(1, 1, 1)x(1, 1, 1, 12)12 - AIC:1935.2895757630095 

mod = sm.tsa.statespace.SARIMAX(y,
                                order=(1, 1, 1),
                                seasonal_order=(1, 1, 1, 12),
                                enforce_stationarity=False,
                                enforce_invertibility=False)
results = mod.fit()
print(results.summary().tables[1])

results.plot_diagnostics(figsize=(16, 8))
plt.show()

pred = results.get_prediction(start=pd.to_datetime('2020-02-01'), dynamic=False)
pred_ci = pred.conf_int() #추정된 계수의 신뢰구간 계산
ax = y['2020':].plot(label='observed')
pred.predicted_mean.plot(ax=ax, label='One-step ahead Forecast', alpha=.7, figsize=(14, 7))
ax.fill_between(pred_ci.index,
                pred_ci.iloc[:, 0],
                pred_ci.iloc[:, 1], color='k', alpha=.2)
ax.set_xlabel('Date')
ax.set_ylabel('CN')
plt.legend()
plt.show()

y_forecasted = pred.predicted_mean.values
y_truth = y['2020-02-01':].values
mse = ((y_forecasted - y_truth) ** 2).mean()
print('The Mean Squared Error of our forecasts is {}'.format(round(mse, 2)))

print('The Root Mean Squared Error of our forecasts is {}'.format(round(np.sqrt(mse), 2)))

off_lei_MSE = round(np.sqrt(mse), 2)


## 오프라인 의료기관===============================================================
off_medi1 = pd.read_csv("c:/data/off_medi1.csv",parse_dates=["DATE"])
off_medi1.info()

off_medi1 = off_medi1[['DATE','CN']]

# 2020년 데이터만 뽑음
off_medi2020 = off_medi1[off_medi1['DATE'].dt.year==2020]

#index를 Order Date로 한다.
off_medi2020 = off_medi2020.set_index('DATE')
off_medi2020.head()
off_medi2020.index

y=off_medi2020
y.plot(figsize = (15,6))
plt.show()

#차트 기본 크기 설정
rcParams['figure.figsize'] = 18,8

p = d = q = range(0, 2)
pdq = list(itertools.product(p, d, q))
seasonal_pdq = [(x[0], x[1], x[2], 12) for x in list(itertools.product(p, d, q))]

print('Examples of parameter combinations for Seasonal ARIMA...')
print('SARIMAX: {} x {}'.format(pdq[1], seasonal_pdq[1]))
print('SARIMAX: {} x {}'.format(pdq[1], seasonal_pdq[2]))
print('SARIMAX: {} x {}'.format(pdq[2], seasonal_pdq[3]))
print('SARIMAX: {} x {}'.format(pdq[2], seasonal_pdq[4]))

for param in pdq:
    for param_seasonal in seasonal_pdq:
        try:
            mod = sm.tsa.statespace.SARIMAX(y,
                                            order=param,
                                            seasonal_order=param_seasonal,
                                            enforce_stationarity=False,
                                            enforce_invertibility=False)
            results = mod.fit()
            print('ARIMA{}x{}12 - AIC:{}'.format(param, param_seasonal, results.aic))
        except:
            continue

# ARIMA(1, 1, 1)x(1, 1, 1, 12)12 - AIC:2261.9819967985427

mod = sm.tsa.statespace.SARIMAX(y,
                                order=(1, 1, 1),
                                seasonal_order=(1, 1, 1, 12),
                                enforce_stationarity=False,
                                enforce_invertibility=False)
results = mod.fit()
print(results.summary().tables[1])

results.plot_diagnostics(figsize=(16, 8))
plt.show()

pred = results.get_prediction(start=pd.to_datetime('2020-02-01'), dynamic=False)
pred_ci = pred.conf_int() #추정된 계수의 신뢰구간 계산
ax = y['2020':].plot(label='observed')
pred.predicted_mean.plot(ax=ax, label='One-step ahead Forecast', alpha=.7, figsize=(14, 7))
ax.fill_between(pred_ci.index,
                pred_ci.iloc[:, 0],
                pred_ci.iloc[:, 1], color='k', alpha=.2)
ax.set_xlabel('Date')
ax.set_ylabel('CN')
plt.legend()
plt.show()

y_forecasted = pred.predicted_mean.values
y_truth = y['2020-02-01':].values
mse = ((y_forecasted - y_truth) ** 2).mean()
print('The Mean Squared Error of our forecasts is {}'.format(round(mse, 2)))

print('The Root Mean Squared Error of our forecasts is {}'.format(round(np.sqrt(mse), 2)))

off_medi_MSE = round(np.sqrt(mse), 2)


## 오프라인 보건위생===============================================================
off_sani1 = pd.read_csv("c:/data/off_sani1.csv",parse_dates=["DATE"])
off_sani1.info()

off_sani1 = off_sani1[['DATE','CN']]

# 2020년 데이터만 뽑음
off_sani2020 = off_sani1[off_sani1['DATE'].dt.year==2020]

#index를 Order Date로 한다.
off_sani2020 = off_sani2020.set_index('DATE')
off_sani2020.head()
off_sani2020.index

y=off_sani2020
y.plot(figsize = (15,6))
plt.show()

#차트 기본 크기 설정
rcParams['figure.figsize'] = 18,8

p = d = q = range(0, 2)
pdq = list(itertools.product(p, d, q))
seasonal_pdq = [(x[0], x[1], x[2], 12) for x in list(itertools.product(p, d, q))]

print('Examples of parameter combinations for Seasonal ARIMA...')
print('SARIMAX: {} x {}'.format(pdq[1], seasonal_pdq[1]))
print('SARIMAX: {} x {}'.format(pdq[1], seasonal_pdq[2]))
print('SARIMAX: {} x {}'.format(pdq[2], seasonal_pdq[3]))
print('SARIMAX: {} x {}'.format(pdq[2], seasonal_pdq[4]))

for param in pdq:
    for param_seasonal in seasonal_pdq:
        try:
            mod = sm.tsa.statespace.SARIMAX(y,
                                            order=param,
                                            seasonal_order=param_seasonal,
                                            enforce_stationarity=False,
                                            enforce_invertibility=False)
            results = mod.fit()
            print('ARIMA{}x{}12 - AIC:{}'.format(param, param_seasonal, results.aic))
        except:
            continue

# ARIMA(1, 1, 1)x(1, 1, 1, 12)12 - AIC:1767.0404019099792

mod = sm.tsa.statespace.SARIMAX(y,
                                order=(1, 1, 1),
                                seasonal_order=(1, 1, 1, 12),
                                enforce_stationarity=False,
                                enforce_invertibility=False)
results = mod.fit()
print(results.summary().tables[1])

results.plot_diagnostics(figsize=(16, 8))
plt.show()

pred = results.get_prediction(start=pd.to_datetime('2020-02-01'), dynamic=False)
pred_ci = pred.conf_int() #추정된 계수의 신뢰구간 계산
ax = y['2020':].plot(label='observed')
pred.predicted_mean.plot(ax=ax, label='One-step ahead Forecast', alpha=.7, figsize=(14, 7))
ax.fill_between(pred_ci.index,
                pred_ci.iloc[:, 0],
                pred_ci.iloc[:, 1], color='k', alpha=.2)
ax.set_xlabel('Date')
ax.set_ylabel('CN')
plt.legend()
plt.show()

y_forecasted = pred.predicted_mean.values
y_truth = y['2020-02-01':].values
mse = ((y_forecasted - y_truth) ** 2).mean()
print('The Mean Squared Error of our forecasts is {}'.format(round(mse, 2)))

print('The Root Mean Squared Error of our forecasts is {}'.format(round(np.sqrt(mse), 2)))

off_sani_MSE = round(np.sqrt(mse), 2)


## 온라인 숙박===============================================================
on_acc1 = pd.read_csv("c:/data/on_acc1.csv",parse_dates=["DATE"])
on_acc1.info()

on_acc1 = on_acc1[['DATE','CN']]

# 2020년 데이터만 뽑음
on_acc2020 = on_acc1[on_acc1['DATE'].dt.year==2020]

#index를 Order Date로 한다.
on_acc2020 = on_acc2020.set_index('DATE')
on_acc2020.head()
on_acc2020.index

y=on_acc2020
y.plot(figsize = (15,6))
plt.show()

#차트 기본 크기 설정
rcParams['figure.figsize'] = 18,8

p = d = q = range(0, 2)
pdq = list(itertools.product(p, d, q))
seasonal_pdq = [(x[0], x[1], x[2], 12) for x in list(itertools.product(p, d, q))]

print('Examples of parameter combinations for Seasonal ARIMA...')
print('SARIMAX: {} x {}'.format(pdq[1], seasonal_pdq[1]))
print('SARIMAX: {} x {}'.format(pdq[1], seasonal_pdq[2]))
print('SARIMAX: {} x {}'.format(pdq[2], seasonal_pdq[3]))
print('SARIMAX: {} x {}'.format(pdq[2], seasonal_pdq[4]))

for param in pdq:
    for param_seasonal in seasonal_pdq:
        try:
            mod = sm.tsa.statespace.SARIMAX(y,
                                            order=param,
                                            seasonal_order=param_seasonal,
                                            enforce_stationarity=False,
                                            enforce_invertibility=False)
            results = mod.fit()
            print('ARIMA{}x{}12 - AIC:{}'.format(param, param_seasonal, results.aic))
        except:
            continue

# ARIMA(1, 1, 1)x(1, 1, 1, 12)12 - AIC:1709.2883177706988 

mod = sm.tsa.statespace.SARIMAX(y,
                                order=(1, 1, 1),
                                seasonal_order=(1, 1, 1, 12),
                                enforce_stationarity=False,
                                enforce_invertibility=False)
results = mod.fit()
print(results.summary().tables[1])

results.plot_diagnostics(figsize=(16, 8))
plt.show()

pred = results.get_prediction(start=pd.to_datetime('2020-02-01'), dynamic=False)
pred_ci = pred.conf_int() #추정된 계수의 신뢰구간 계산
ax = y['2020':].plot(label='observed')
pred.predicted_mean.plot(ax=ax, label='One-step ahead Forecast', alpha=.7, figsize=(14, 7))
ax.fill_between(pred_ci.index,
                pred_ci.iloc[:, 0],
                pred_ci.iloc[:, 1], color='k', alpha=.2)
ax.set_xlabel('Date')
ax.set_ylabel('CN')
plt.legend()
plt.show()

y_forecasted = pred.predicted_mean.values
y_truth = y['2020-02-01':].values
mse = ((y_forecasted - y_truth) ** 2).mean()
print('The Mean Squared Error of our forecasts is {}'.format(round(mse, 2)))

print('The Root Mean Squared Error of our forecasts is {}'.format(round(np.sqrt(mse), 2)))

on_acc_MSE = round(np.sqrt(mse), 2)


## 온라인 문화취미===============================================================
on_cul1 = pd.read_csv("c:/data/on_cul1.csv",parse_dates=["DATE"])
on_cul1.info()

on_cul1 = on_cul1[['DATE','CN']]

# 2020년 데이터만 뽑음
on_cul2020 = on_cul1[on_cul1['DATE'].dt.year==2020]

#index를 Order Date로 한다.
on_cul2020 = on_cul2020.set_index('DATE')
on_cul2020.head()
on_cul2020.index

y=on_cul2020
y.plot(figsize = (15,6))
plt.show()

#차트 기본 크기 설정
rcParams['figure.figsize'] = 18,8

p = d = q = range(0, 2)
pdq = list(itertools.product(p, d, q))
seasonal_pdq = [(x[0], x[1], x[2], 12) for x in list(itertools.product(p, d, q))]

print('Examples of parameter combinations for Seasonal ARIMA...')
print('SARIMAX: {} x {}'.format(pdq[1], seasonal_pdq[1]))
print('SARIMAX: {} x {}'.format(pdq[1], seasonal_pdq[2]))
print('SARIMAX: {} x {}'.format(pdq[2], seasonal_pdq[3]))
print('SARIMAX: {} x {}'.format(pdq[2], seasonal_pdq[4]))

for param in pdq:
    for param_seasonal in seasonal_pdq:
        try:
            mod = sm.tsa.statespace.SARIMAX(y,
                                            order=param,
                                            seasonal_order=param_seasonal,
                                            enforce_stationarity=False,
                                            enforce_invertibility=False)
            results = mod.fit()
            print('ARIMA{}x{}12 - AIC:{}'.format(param, param_seasonal, results.aic))
        except:
            continue

# ARIMA(1, 1, 1)x(1, 1, 1, 12)12 - AIC:1813.1449289221637 

mod = sm.tsa.statespace.SARIMAX(y,
                                order=(1, 1, 1),
                                seasonal_order=(1, 1, 1, 12),
                                enforce_stationarity=False,
                                enforce_invertibility=False)
results = mod.fit()
print(results.summary().tables[1])

results.plot_diagnostics(figsize=(16, 8))
plt.show()

pred = results.get_prediction(start=pd.to_datetime('2020-02-02'), dynamic=False)
pred_ci = pred.conf_int() #추정된 계수의 신뢰구간 계산
ax = y['2020':].plot(label='observed')
pred.predicted_mean.plot(ax=ax, label='One-step ahead Forecast', alpha=.7, figsize=(14, 7))
ax.fill_between(pred_ci.index,
                pred_ci.iloc[:, 0],
                pred_ci.iloc[:, 1], color='k', alpha=.2)
ax.set_xlabel('Date')
ax.set_ylabel('CN')
plt.legend()
plt.show()

y_forecasted = pred.predicted_mean.values
y_truth = y['2020-02-01':].values
mse = ((y_forecasted - y_truth) ** 2).mean()
print('The Mean Squared Error of our forecasts is {}'.format(round(mse, 2)))

print('The Root Mean Squared Error of our forecasts is {}'.format(round(np.sqrt(mse), 2)))

on_cul_MSE = round(np.sqrt(mse), 2)


## 온라인 요식업소===============================================================
on_food1 = pd.read_csv("c:/data/on_food1.csv",parse_dates=["DATE"])
on_food1.info()

on_food1 = on_food1[['DATE','CN']]

# 2020년 데이터만 뽑음
on_food2020 = on_food1[on_food1['DATE'].dt.year==2020]

#index를 Order Date로 한다.
on_food2020 = on_food2020.set_index('DATE')
on_food2020.head()
on_food2020.index

y=on_food2020
y.plot(figsize = (15,6))
plt.show()

#차트 기본 크기 설정
rcParams['figure.figsize'] = 18,8

p = d = q = range(0, 2)
pdq = list(itertools.product(p, d, q))
seasonal_pdq = [(x[0], x[1], x[2], 12) for x in list(itertools.product(p, d, q))]

print('Examples of parameter combinations for Seasonal ARIMA...')
print('SARIMAX: {} x {}'.format(pdq[1], seasonal_pdq[1]))
print('SARIMAX: {} x {}'.format(pdq[1], seasonal_pdq[2]))
print('SARIMAX: {} x {}'.format(pdq[2], seasonal_pdq[3]))
print('SARIMAX: {} x {}'.format(pdq[2], seasonal_pdq[4]))

for param in pdq:
    for param_seasonal in seasonal_pdq:
        try:
            mod = sm.tsa.statespace.SARIMAX(y,
                                            order=param,
                                            seasonal_order=param_seasonal,
                                            enforce_stationarity=False,
                                            enforce_invertibility=False)
            results = mod.fit()
            print('ARIMA{}x{}12 - AIC:{}'.format(param, param_seasonal, results.aic))
        except:
            continue

# ARIMA(1, 1, 1)x(1, 1, 1, 12)12 - AIC:2117.0223375825162

mod = sm.tsa.statespace.SARIMAX(y,
                                order=(1, 1, 1),
                                seasonal_order=(1, 1, 1, 12),
                                enforce_stationarity=False,
                                enforce_invertibility=False)
results = mod.fit()
print(results.summary().tables[1])

results.plot_diagnostics(figsize=(16, 8))
plt.show()

pred = results.get_prediction(start=pd.to_datetime('2020-02-01'), dynamic=False)
pred_ci = pred.conf_int() #추정된 계수의 신뢰구간 계산
ax = y['2020':].plot(label='observed')
pred.predicted_mean.plot(ax=ax, label='One-step ahead Forecast', alpha=.7, figsize=(14, 7))
ax.fill_between(pred_ci.index,
                pred_ci.iloc[:, 0],
                pred_ci.iloc[:, 1], color='k', alpha=.2)
ax.set_xlabel('Date')
ax.set_ylabel('CN')
plt.legend()
plt.show()

y_forecasted = pred.predicted_mean.values
y_truth = y['2020-02-01':].values
mse = ((y_forecasted - y_truth) ** 2).mean()
print('The Mean Squared Error of our forecasts is {}'.format(round(mse, 2)))

print('The Root Mean Squared Error of our forecasts is {}'.format(round(np.sqrt(mse), 2)))

on_food_MSE = round(np.sqrt(mse), 2)


## 온라인 레저===============================================================
on_lei1 = pd.read_csv("c:/data/on_lei1.csv",parse_dates=["DATE"])
on_lei1.info()

on_lei1 = on_lei1[['DATE','CN']]

# 2020년 데이터만 뽑음
on_lei2020 = on_lei1[on_lei1['DATE'].dt.year==2020]

#index를 Order Date로 한다.
on_lei2020 = on_lei2020.set_index('DATE')
on_lei2020.head()
on_lei2020.index

y=on_lei2020
y.plot(figsize = (15,6))
plt.show()

#차트 기본 크기 설정
rcParams['figure.figsize'] = 18,8

p = d = q = range(0, 2)
pdq = list(itertools.product(p, d, q))
seasonal_pdq = [(x[0], x[1], x[2], 12) for x in list(itertools.product(p, d, q))]

print('Examples of parameter combinations for Seasonal ARIMA...')
print('SARIMAX: {} x {}'.format(pdq[1], seasonal_pdq[1]))
print('SARIMAX: {} x {}'.format(pdq[1], seasonal_pdq[2]))
print('SARIMAX: {} x {}'.format(pdq[2], seasonal_pdq[3]))
print('SARIMAX: {} x {}'.format(pdq[2], seasonal_pdq[4]))

for param in pdq:
    for param_seasonal in seasonal_pdq:
        try:
            mod = sm.tsa.statespace.SARIMAX(y,
                                            order=param,
                                            seasonal_order=param_seasonal,
                                            enforce_stationarity=False,
                                            enforce_invertibility=False)
            results = mod.fit()
            print('ARIMA{}x{}12 - AIC:{}'.format(param, param_seasonal, results.aic))
        except:
            continue

# ARIMA(1, 1, 1)x(1, 1, 1, 12)12 - AIC:1506.3260532297984 

mod = sm.tsa.statespace.SARIMAX(y,
                                order=(1, 1, 1),
                                seasonal_order=(1, 1, 1, 12),
                                enforce_stationarity=False,
                                enforce_invertibility=False)
results = mod.fit()
print(results.summary().tables[1])

results.plot_diagnostics(figsize=(16, 8))
plt.show()

pred = results.get_prediction(start=pd.to_datetime('2020-02-01'), dynamic=False)
pred_ci = pred.conf_int() #추정된 계수의 신뢰구간 계산
ax = y['2020':].plot(label='observed')
pred.predicted_mean.plot(ax=ax, label='One-step ahead Forecast', alpha=.7, figsize=(14, 7))
ax.fill_between(pred_ci.index,
                pred_ci.iloc[:, 0],
                pred_ci.iloc[:, 1], color='k', alpha=.2)
ax.set_xlabel('Date')
ax.set_ylabel('CN')
plt.legend()
plt.show()

y_forecasted = pred.predicted_mean.values
y_truth = y['2020-02-01':].values
mse = ((y_forecasted - y_truth) ** 2).mean()
print('The Mean Squared Error of our forecasts is {}'.format(round(mse, 2)))

print('The Root Mean Squared Error of our forecasts is {}'.format(round(np.sqrt(mse), 2)))

on_lei_MSE = round(np.sqrt(mse), 2)


## 온라인 보건위생===============================================================
on_sani1 = pd.read_csv("c:/data/on_sani1.csv",parse_dates=["DATE"])
on_sani1.info()

on_sani1 = on_sani1[['DATE','CN']]

# 2020년 데이터만 뽑음
on_sani2020 = on_sani1[on_sani1['DATE'].dt.year==2020]

#index를 Order Date로 한다.
on_sani2020 = on_sani2020.set_index('DATE')
on_sani2020.head()
on_sani2020.index

y=on_sani2020
y.plot(figsize = (15,6))
plt.show()

#차트 기본 크기 설정
rcParams['figure.figsize'] = 18,8

p = d = q = range(0, 2)
pdq = list(itertools.product(p, d, q))
seasonal_pdq = [(x[0], x[1], x[2], 12) for x in list(itertools.product(p, d, q))]

print('Examples of parameter combinations for Seasonal ARIMA...')
print('SARIMAX: {} x {}'.format(pdq[1], seasonal_pdq[1]))
print('SARIMAX: {} x {}'.format(pdq[1], seasonal_pdq[2]))
print('SARIMAX: {} x {}'.format(pdq[2], seasonal_pdq[3]))
print('SARIMAX: {} x {}'.format(pdq[2], seasonal_pdq[4]))

for param in pdq:
    for param_seasonal in seasonal_pdq:
        try:
            mod = sm.tsa.statespace.SARIMAX(y,
                                            order=param,
                                            seasonal_order=param_seasonal,
                                            enforce_stationarity=False,
                                            enforce_invertibility=False)
            results = mod.fit()
            print('ARIMA{}x{}12 - AIC:{}'.format(param, param_seasonal, results.aic))
        except:
            continue

# ARIMA(1, 1, 1)x(1, 1, 1, 12)12 - AIC:2074.345914714061 

mod = sm.tsa.statespace.SARIMAX(y,
                                order=(1, 1, 1),
                                seasonal_order=(1, 1, 1, 12),
                                enforce_stationarity=False,
                                enforce_invertibility=False)
results = mod.fit()
print(results.summary().tables[1])

results.plot_diagnostics(figsize=(16, 8))
plt.show()

pred = results.get_prediction(start=pd.to_datetime('2020-02-01'), dynamic=False)
pred_ci = pred.conf_int() #추정된 계수의 신뢰구간 계산
ax = y['2020':].plot(label='observed')
pred.predicted_mean.plot(ax=ax, label='One-step ahead Forecast', alpha=.7, figsize=(14, 7))
ax.fill_between(pred_ci.index,
                pred_ci.iloc[:, 0],
                pred_ci.iloc[:, 1], color='k', alpha=.2)
ax.set_xlabel('Date')
ax.set_ylabel('CN')
plt.legend()
plt.show()

y_forecasted = pred.predicted_mean.values
y_truth = y['2020-02-01':].values
mse = ((y_forecasted - y_truth) ** 2).mean()
print('The Mean Squared Error of our forecasts is {}'.format(round(mse, 2)))



print('The Root Mean Squared Error of our forecasts is {}'.format(round(np.sqrt(mse), 2)))

on_sani_MSE = round(np.sqrt(mse), 2)


'''
df = pd.DataFrame(index=['off_acc_MSE','off_cul_MSE','off_food_MSE','off_lei_MSE',
                                           'off_medi_MSE','off_sani_MSE','on_acc_MSE','on_cul_MSE',
                                           'on_food_MSE','on_lei_MSE','on_sani_MSE'],
                  data = {'root_MSE' : [off_acc_MSE,off_cul_MSE,off_food_MSE,off_lei_MSE,
                                           off_medi_MSE,off_sani_MSE,on_acc_MSE,on_cul_MSE,
                                           on_food_MSE,on_lei_MSE,on_sani_MSE]})

df
'''

# 파일로 떨어트리기
df.to_csv('c:/data/ARIMA_RMSE.csv',index=True)
