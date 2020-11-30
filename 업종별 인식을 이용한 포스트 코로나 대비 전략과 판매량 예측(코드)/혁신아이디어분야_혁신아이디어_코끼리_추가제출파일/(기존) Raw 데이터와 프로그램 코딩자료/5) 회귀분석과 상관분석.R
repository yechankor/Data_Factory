# Rstudio에서 회귀분석과 상관분석 진행
# 온라인 매출과 업종별 긍정부정정도와의 관계 확인하기

# CN: 오프라인/온라인 매출건수 
# DATE:시간
# PN: 업종에 대한 긍정부정정도 (업종에 대한 긍정부정 게시량과 신문기사에서의 긍정부정 키워드 벡터값)
# COVID: 코로나의 영향


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

