## 온라인 매출과 업종별 긍정부정정도와의 관계 ###############################
library(ggplot2)
off_acco<-read.csv("C:/data/off_acco.csv",header=T,encoding = 'utf-8')
off_cul<-read.csv("C:/data/off_cul.csv",header=T,encoding = 'utf-8')
off_food<-read.csv("C:/data/off_food.csv",header=T,encoding = 'utf-8')
off_lei<-read.csv("C:/data/off_lei.csv",header=T,encoding = 'utf-8')
off_medi<-read.csv("C:/data/off_medi.csv",header=T,encoding = 'utf-8')
off_sani<-read.csv("C:/data/off_sani.csv",header=T,encoding = 'utf-8')

# CN: 오프라인/온라인 매출건수 
# DATE:시간
# PN: 업종에 대한 긍정부정정도 (업종에 대한 긍정부정 게시량과 신문기사에서의 긍정부정 키워드 벡터값)

## 오프라인 숙박 ====================================================================
## 회귀분석: p-value< 0.05 -> PN 유의미
fit = lm(CN ~ DATE + PN, data= off_acco)
summary(fit)
coef(fit)

par(mfrow = c(2, 2))
plot(CN ~ PN, data= off_acco)

## 상관분석: p-value<0.05 -> 상관관계 존재
cor.test(off_acco$CN,off_acco$PN)


## 오프라인 문화취미 ====================================================================
## 회귀분석: p-value < 0.05 -> 유의미 
fit = lm(CN ~ DATE + PN, data= off_cul)
summary(fit)
coef(fit)

par(mfrow = c(2, 2))
plot(CN ~ PN, data= off_cul)

## 상관분석: p-value < 0.05 -> 상관관계 존재
cor.test(off_cul$CN,off_cul$PN)


## 오프라인 식품 ====================================================================
## 회귀분석: p-value > 0.05 
fit = lm(CN ~ DATE + PN, data= off_food)
summary(fit)
coef(fit)

par(mfrow = c(2, 2))
plot(CN ~ PN, data= off_food)

## 상관분석: p-value < 0.05 -> 상관관계 존재
cor.test(off_food$CN,off_food$PN)


## 오프라인 레저 ====================================================================
## 회귀분석: p-value > 0.05 
fit = lm(CN ~ DATE + PN, data= off_lei)
summary(fit)
coef(fit)

par(mfrow = c(2, 2))
plot(CN ~ PN, data= off_lei)

## 상관분석: p-value > 0.05
cor.test(off_lei$CN,off_lei$PN)


## 오프라인 의료기관 ====================================================================
## 회귀분석: p-value < 0.05 -> 유의미
fit = lm(CN ~ DATE + PN, data= off_medi)
summary(fit)
coef(fit)

par(mfrow = c(2, 2))
plot(CN ~ PN, data= off_medi)

## 상관분석: p-value < 0.05  -> 상관관계 존재
cor.test(off_medi$CN,off_medi$PN)


## 오프라인 보건위생 ====================================================================
## 회귀분석: p-value < 0.05 -> 유의미
fit = lm(CN ~ DATE + PN, data= off_sani)
summary(fit)
coef(fit)

par(mfrow = c(2, 2))
plot(CN ~ PN, data= off_sani)

## 상관분석: p-value < 0.05 -> 상관관계 존재
cor.test(off_sani$CN,off_sani$PN)




on_acco<-read.csv("C:/data/on_acco.csv",header=T,encoding = 'utf-8')
on_cul<-read.csv("C:/data/on_cul.csv",header=T,encoding = 'utf-8')
on_food<-read.csv("C:/data/on_food.csv",header=T,encoding = 'utf-8')
on_lei<-read.csv("C:/data/on_lei.csv",header=T,encoding = 'utf-8')
on_sani<-read.csv("C:/data/on_sani.csv",header=T,encoding = 'utf-8')

## 온라인 숙박 ====================================================================
## 회귀분석: p-value < 0.05 -> 유의미
fit = lm(CN ~ DATE + PN, data= on_acco)
summary(fit)
coef(fit)

par(mfrow = c(2, 2))
plot(CN ~ PN, data= on_acco)


## 상관분석: p-value < 0.05 -> 상관관계 존재
cor.test(on_acco$CN,on_acco$PN)


## 온라인 문화취미 ====================================================================
## 회귀분석: p-value < 0.05 -> 유의미
fit = lm(CN ~ DATE + PN, data= on_cul)
summary(fit)
coef(fit)

par(mfrow = c(2, 2))
plot(CN ~ PN, data= on_cul)


## 상관분석: p-value < 0.05 -> 상관관계 존재
cor.test(on_cul$CN,on_cul$PN)


## 온라인 식품 ====================================================================
## 회귀분석: p-value < 0.05 -> 유의미
fit = lm(CN ~ DATE + PN, data= on_food)
summary(fit)
coef(fit)

par(mfrow = c(2, 2))
plot(CN ~ PN, data= on_food)


## 상관분석: p-value < 0.05 -> 상관관계 존재
cor.test(on_acco$CN,on_acco$PN)



## 온라인 레저 ====================================================================
## 회귀분석: p-value < 0.05 -> 유의미
fit = lm(CN ~ DATE + PN, data= on_lei)
summary(fit)
coef(fit)

par(mfrow = c(2, 2))
plot(CN ~ PN, data= on_lei)


## 상관분석: p-value < 0.05 -> 상관관계 존재
cor.test(on_acco$CN,on_acco$PN)


## 온라인 보건위생 ====================================================================
## 회귀분석: p-value < 0.05 -> 유의미
fit = lm(CN ~ DATE + PN, data= on_sani)
summary(fit)
coef(fit)

par(mfrow = c(2, 2))
plot(CN ~ PN, data= on_sani)


## 상관분석: p-value < 0.05 -> 상관관계 존재
cor.test(on_acco$CN,on_acco$PN)

## PN변수 유의미 O, 상관관계 O : 오프라인 숙박/문화취미/의료기관/보건위생, 
##                               온라인 숙박/문화취미/식품/레저/보건위생
## PN변수 유의미 X, 상관관계 O : 오프라인 식품
## PN변수 유의미 X, 상관관계 X : 오프라인 레저
