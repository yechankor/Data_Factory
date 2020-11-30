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
