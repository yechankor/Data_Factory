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