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