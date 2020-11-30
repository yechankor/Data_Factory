off_data = rbind(read.csv("C:/data/off_acci(train).csv"),
             read.csv("C:/data/off_acci(test).csv"),
             read.csv("C:/data/off_cul(train).csv"),
             read.csv("C:/data/off_cul(test).csv"),
             read.csv("C:/data/off_food(train).csv"),
             read.csv("C:/data/off_food(test).csv"),
             read.csv("C:/data/off_lei(train).csv"),
             read.csv("C:/data/off_lei(test).csv"),
             read.csv("C:/data/off_medi(train).csv"),
             read.csv("C:/data/off_medi(test).csv"),
             read.csv("C:/data/off_sani(train).csv"),
             read.csv("C:/data/off_sani(test).csv"))
write.csv(off_data,"C:/data/off_data.csv")


on_data= rbind(read.csv("C:/data/on_acc(train).csv"),
               read.csv("C:/data/on_acc(test).csv"),
               read.csv("C:/data/on_cul(train).csv"),
               read.csv("C:/data/on_cul(test).csv"),
               read.csv("C:/data/on_food(train).csv"),
               read.csv("C:/data/on_food(test).csv"),
               read.csv("C:/data/on_lei(train).csv"),
               read.csv("C:/data/on_lei(test).csv"),
               read.csv("C:/data/on_sani(train).csv"),
               read.csv("C:/data/on_sani(test).csv"))
write.csv(on_data,"C:/data/on_data.csv")


## ============================================================
## CN변수: 이전보다 50%이상 감소/증가한 경우 1, 그렇지 않은 경우 0

## PN변수: 음수인 경우 0, 양수인 경우 1로 분류
quantile(off_data[,'PN'])

## COVID 변수: 0인 경우 0으로,
## 0이외의 값 중 50%분위값 10019를 기준으로 1,2로 분류
quantile(off_data[,'COVID'][off_data[,'COVID']!=0])

##=============================================================
off_acco = rbind(read.csv("C:/data/off_acco(train).csv"),
                 read.csv("C:/data/off_acco(test).csv"))
write.csv(off_data,"C:/data/off_acco.csv")

off_cul = rbind(read.csv("C:/data/off_cul(train).csv"),
                read.csv("C:/data/off_cul(test).csv"))
write.csv(off_data,"C:/data/off_cul.csv")

off_food = rbind(read.csv("C:/data/off_food(train).csv"),
                 read.csv("C:/data/off_food(test).csv"))
write.csv(off_data,"C:/data/off_food.csv")

off_lei = rbind(read.csv("C:/data/off_lei(train).csv"),
                read.csv("C:/data/off_lei(test).csv"))
write.csv(off_data,"C:/data/off_lei.csv")

off_medi = rbind(read.csv("C:/data/off_medi(train).csv"),
                 read.csv("C:/data/off_medi(test).csv"))
write.csv(off_data,"C:/data/off_medi.csv")

off_sani = rbind(read.csv("C:/data/off_sani(train).csv"),
                 read.csv("C:/data/off_sani(test).csv"))
write.csv(off_data,"C:/data/off_sani.csv")



on_acco = rbind(read.csv("C:/BIGCON/on_acco(train).csv"),
                 read.csv("C:/BIGCON/on_acco(test).csv"))
write.csv(off_data,"C:/data/on_acco.csv")

on_cul = rbind(read.csv("C:/BIGCON/on_cul(train).csv"),
                read.csv("C:/BIGCON/on_cul(test).csv"))
write.csv(off_data,"C:/data/on_cul.csv")

on_food = rbind(read.csv("C:/BIGCON/on_food(train).csv"),
                 read.csv("C:/BIGCON/on_food(test).csv"))
write.csv(off_data,"C:/data/on_food.csv")

on_lei = rbind(read.csv("C:/BIGCON/on_lei(train).csv"),
                read.csv("C:/BIGCON/on_lei(test).csv"))
write.csv(off_data,"C:/data/on_lei.csv")

on_sani = rbind(read.csv("C:/BIGCON/on_sani(train).csv"),
                 read.csv("C:/BIGCON/on_sani(test).csv"))
write.csv(off_data,"C:/data/on_sani.csv")




