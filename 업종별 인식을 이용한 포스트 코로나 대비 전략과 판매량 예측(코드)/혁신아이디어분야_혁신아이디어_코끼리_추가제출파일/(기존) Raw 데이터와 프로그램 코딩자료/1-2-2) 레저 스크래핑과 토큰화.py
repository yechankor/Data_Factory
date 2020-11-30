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