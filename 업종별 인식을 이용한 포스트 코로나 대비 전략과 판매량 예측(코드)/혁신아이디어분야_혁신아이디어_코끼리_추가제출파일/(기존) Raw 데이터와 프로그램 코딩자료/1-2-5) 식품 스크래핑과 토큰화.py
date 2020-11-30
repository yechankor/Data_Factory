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