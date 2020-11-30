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