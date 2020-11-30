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