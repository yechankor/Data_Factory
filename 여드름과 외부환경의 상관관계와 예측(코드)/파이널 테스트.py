import datetime
import math
from wordcloud import WordCloud, STOPWORDS
import collections
from numpy import nan as na
from pandas import Series, DataFrame
import statsmodels.api as sm
import statsmodels.formula.api as smf
import matplotlib.pylab as plt
from matplotlib import font_manager, rc # 한글 깨질 때
import matplotlib.font_manager as fm
from bs4 import BeautifulSoup
from bs4 import NavigableString
import glob
import pandas as pd
import sklearn.metrics as metrics
import numpy as np
import scipy.stats as stats
import pandas_datareader.data as web
import itertools
from keras.layers import Dense
from keras.layers import LSTM
import json
from fake_useragent import UserAgent
import requests
from bs4 import BeautifulSoup
from matplotlib import rc
from sklearn.preprocessing import scale
from nltk import NaiveBayesClassifier
from nltk.tokenize import word_tokenize
import nltk
from sklearn import utils
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sklearn.naive_bayes import MultinomialNB # 다항분포 나이브 베이즈 모델
from sklearn.metrics import accuracy_score #정확도 계산
pd.set_option("display.max_rows", 1400) # 보여지는 행 개수 조정
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules
from sklearn.tree import DecisionTreeClassifier
import tensorflow as tf
import graphviz
from sklearn.tree import export_graphviz
from IPython.display import Image
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import RandomForestClassifier
from scipy import stats
from sklearn import linear_model
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import re
from sklearn.ensemble import GradientBoostingRegressor 
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer
from collections import Counter
from sklearn.datasets import load_iris
import seaborn as sns
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import Ridge, RidgeCV, Lasso, LassoCV, ElasticNet,ElasticNetCV
from sklearn.model_selection import KFold
from sklearn.datasets import make_regression
import random
from keras.layers.core import Dense, Activation, Dropout
from keras.layers.recurrent import LSTM
from tensorflow.keras.models import Model
from keras.models import Sequential
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Input, Dense, GRU, Embedding
from tensorflow.python.keras.optimizers import RMSprop
from keras.callbacks import EarlyStopping
from pandas.tseries.offsets import MonthEnd
import keras.backend as K
from sklearn.compose import make_column_transformer
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import MinMaxScaler
from statsmodels.tsa.arima_model import ARIMA
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import ModelCheckpoint
from keras.layers import BatchNormalization
from sklearn.metrics import accuracy_score
from sklearn.tree import export_graphviz
from IPython.core.display import Image
from fbprophet.plot import add_changepoints_to_plot


acne_df3 = pd.read_csv('c:/data/final/acne_df3.csv', encoding='cp949')

# ========================================================================

X = acne_df3.iloc[:,1:]
y = acne_df3.iloc[:,0]

estimator = RandomForestRegressor()
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

e = Lasso()
e.fit(X_train, y_train)


kf = KFold(random_state=30,
           n_splits=10,
           shuffle=True)

param_grid = {
    'n_estimators': [100, 150, 200, 250],
    'max_depth': [None, 6, 9, 12],
    'min_samples_split': [0.01, 0.05, 0.1],
    'max_features': ['auto', 'sqrt'],
}

grid_search = GridSearchCV(estimator=estimator, 
                           param_grid=param_grid, 
                           cv=kf, 
                           n_jobs=-1, 
                           verbose=2
                          )
grid_search.fit(X_train, y_train)

grid_search.best_estimator_
cvres = grid_search.cv_results_
for mean_score, params in zip(cvres['mean_test_score'], cvres['params']):
    print(np.sqrt(-mean_score), params)


feature_import = grid_search.best_estimator_.feature_importances_
feature_import

estimator = RandomForestRegressor()

kf = KFold(random_state=30,
           n_splits=10,
           shuffle=True)

param_grid = {
    'n_estimators': [100, 150, 200, 250],
    'max_depth': [None, 6, 9, 12],
    'min_samples_split': [0.01, 0.05, 0.1],
    'max_features': ['auto', 'sqrt'],
}

grid_search = GridSearchCV(estimator=estimator, 
                           param_grid=param_grid, 
                           cv=kf, 
                           n_jobs=-1, 
                           verbose=2
                          )
grid_search.fit(X_train, y_train)

model = grid_search.best_estimator_
score = model.score(X_test, y_test)

print('테스트셋에서의 정확도 : {0:.2f}'.format(score))

cvres = grid_search.cv_results_
for mean_score, params in zip(cvres['mean_test_score'], cvres['params']):
    print(np.sqrt(-mean_score), params)


acne_data3 =acne_df3.sample(frac=1).reset_index(drop=True)
train=acne_df3[:int(len(acne_df3)*0.6)]
test=acne_df3[int(len(acne_df3)*0.6):]

train = np.array(train)
test = np.array(test)

x = tf.constant(train[:,[3, 4, -1]], dtype=tf.int32) # 원하는 열 출력, tf.one_hot을 할때는 정수형(int)만 가능! 입력변수
y = tf.constant(train[:,[0]], dtype=tf.int32)
x.shape
y.shape
y_one_hot = tf.one_hot(y,3)
y_one_hot.shape
y_one_hot.ndim # 3차원, 하지만 2차원이 필요

y_one_hot = tf.reshape(y_one_hot, [-1,3]) # -1은 모든 행을 의미
y_one_hot

model = Sequential()
model.add(Dense(64, input_dim=3, activation='relu')) # 3층 신경망, relu: 0 보다 크면 값 리턴, 작거나 같으면 리턴x
# input_dim은 처음에만! 그리고 x값의 열의 수와 맞춘다.
model.add(Dense(64, activation='relu')) # 하나의 층에 3개의 뉴런
model.add(Dense(3, activation='softmax')) # input_dim : 열의 수, 마지막 층은 중요하다. 주의! 3인 이유는 분류 개수와 맞추는 것
model.summary()
model.compile(optimizer='sgd', loss='binary_crossentropy', metrics=['accuracy'])
# categirucal_crossentropy : 다중분류에 사용
model.fit(x, y_one_hot, epochs=100, batch_size=10, shuffle=False) # 오차값을 줄일 수
x_test = tf.constant(np.array(2), dtype=tf.float32, shape=(1,3))
model.predict(x_test)


# 상관관계 분석===========================
acne_df3.corr()
acne_df3.cov()

a1 = tf.Variable(tf.random.uniform([1], 0, 10, dtype = tf.float32))
a2 = tf.Variable(tf.random.uniform([1], 0, 10, dtype = tf.float32))
b = tf.Variable(tf.random.uniform([1], 0, 100, dtype = tf.float32))


x = acne_df3.iloc[:,1:]
y = acne_df3.iloc[:,0]
x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.7, test_size=0.3)
mlr = LinearRegression()
mlr.fit(x_train, y_train) 
my = [[14252, 1, 18, 7.0, 3.4]]
y_predict = mlr.predict(x_test)
plt.scatter(y_test, y_predict, alpha=0.4)
plt.xlabel("Actual Rent")
plt.ylabel("Predicted Rent")
plt.title("MULTIPLE LINEAR REGRESSION")
plt.show()

print(mlr.coef_)
((y - y.mean()) ** 2).sum()
print(mlr.score(x_train, y_train))

print(mlr.score(x_train, y_train)) # train R2 score를 출력합니다.
print(mlr.score(x_test, y_test)) 


plt.figure(figsize=(15, 10))
plt.subplot(221)
plt.scatter(x = acne_df3['temp'], y=acne_df3['total'])
plt.xlabel('평균 기온', fontsize=12)
plt.ylabel('총 환자 수', fontsize=12)
plt.title('평균 기온과 환자 수 상관관계', fontsize=16)
plt.subplot(222)
plt.scatter(x = acne_df3['pm2_5'], y=acne_df3['total'])
plt.xlabel('평균 미세먼지 농도', fontsize=12)
plt.ylabel('총 환자 수', fontsize=12)
plt.title('미세먼지와 환자 수 상관관계', fontsize=16)
plt.subplot(223)
plt.scatter(x = acne_df3['rain'], y=acne_df3['total'])
plt.xlabel('평균 강수량', fontsize=12)
plt.ylabel('총 환자 수', fontsize=12)
plt.title('강수량과 환자 수 상관관계', fontsize=16)
plt.subplot(224)
plt.scatter(x = acne_df3['uv'], y=acne_df3['total'])
plt.xlabel('평균 자외선 지수', fontsize=12)
plt.ylabel('총 환자 수', fontsize=12)
plt.title('자외선 지수와 환자 수 상관관계', fontsize=16)


plt.figure(figsize=(15, 10))
acne_df3_corr1 = acne_df3.corr()
sns.heatmap(acne_df3_corr1)
plt.xlabel('총합')




# 회귀분석  
X = acne_df3.iloc[:,1:]
y = acne_df3.iloc[:,0]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)


log = LogisticRegression() #로지스틱 회귀분석 시행
log.fit(X_train, y_train) #모델의 정확도 확인
print('학습 데이터셋 정확도 : %.2f' % log.score(X_train, y_train))
print('검증 데이터셋 정확도 : %.2f' % log.score(X_test, y_test)) 
print(log.coef_)

#==================================================================================


# 의사결정 나무

X = acne_df3.iloc[:,1:]
y = acne_df3.iloc[:,0]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=0)
from collections import Counter
Counter(y_train)
Counter(y_test)

acne_model = DecisionTreeClassifier(criterion='entropy', max_depth = 2)
acne_model.fit(X_train, y_train)
acne_pred = acne_model.predict(X_test)
acne_model.score(X_train, y_train)
#정확도 계산
acne_model.score(X_test, y_test)
accuracy_score(y_test, acne_pred)
acne_model.feature_importances_
# 중요도 확인
pd.DataFrame({'feature' : acne_df3.iloc[:,1:],
              'importance' : acne_model.feature_importances_})
acne_model.classes_


dot = export_graphviz(acne_model, out_file=None,
                filled=True, rounded=True)
dot
graph = pydotplus.graph_from_dot_data(dot)
graph.write_png('save.png')

#Regression==========================================

from sklearn.metrics import r2_score,mean_absolute_error, mean_squared_error
X = acne_df3.iloc[:,1:]
y = acne_df3.iloc[:,0]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

ridge_alpha = 1
lasso_alpha = 0.1

linear = LinearRegression()
ridge = Ridge(alpha = ridge_alpha)
lasso = Lasso(alpha = lasso_alpha)

linear.fit(X_train,y_train)
ridge.fit(X_train,y_train)
lasso.fit(X_train,y_train)

linear_y_hat = linear.predict(X_test)
ridge_y_hat = ridge.predict(X_test)
lasso_y_hat = lasso.predict(X_test)

linear_r2, ridge_r2, lasso_r2 = r2_score(y_test,linear_y_hat), r2_score(y_test,ridge_y_hat), r2_score(y_test,lasso_y_hat)
linear_MSE, ridge_MSE, lasso_MSE = mean_squared_error(y_test,linear_y_hat), mean_squared_error(y_test,ridge_y_hat), mean_squared_error(y_test,lasso_y_hat)
linear_MAE, ridge_MAE, lasso_MAE = mean_absolute_error(y_test,linear_y_hat), mean_absolute_error(y_test,ridge_y_hat), mean_absolute_error(y_test,lasso_y_hat)

print('R2 score - Linear: %.2f, Ridge: %.2f, Lasso: %.2f' %(linear_r2, ridge_r2, lasso_r2))
print('MSE - Linear: %.2f, Ridge: %.2f, Lasso: %.2f' %(linear_MSE, ridge_MSE, lasso_MSE))
print('MAE - Linear: %.2f, Ridge: %.2f, Lasso: %.2f' %(linear_MAE, ridge_MAE, lasso_MAE))

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(range(len(y_test)), y_test, '-', label="Original Y")
ax.plot(range(len(y_test)), linear_y_hat, '-x', label="linear_y_hat")
ax.plot(range(len(y_test)), ridge_y_hat, '-x', label="ridge_y_hat")
ax.plot(range(len(y_test)), lasso_y_hat, '-x', label="lasso_y_hat")
plt.legend(loc='upper right')
plt.show()

ridge_result = []
lasso_result = []
alpha = [0.001,0.01,0.1,1,10]

for a in alpha:
  ridge = Ridge(alpha = a)
  lasso = Lasso(alpha = a)

  ridge.fit(X_train,y_train)
  lasso.fit(X_train,y_train)

  ridge_y_hat = ridge.predict(X_test)
  lasso_y_hat = lasso.predict(X_test)

  ridge_r2, lasso_r2 = r2_score(y_test,ridge_y_hat), r2_score(y_test,lasso_y_hat)
  ridge_result.append(ridge_r2)
  lasso_result.append(lasso_r2)
  
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(range(5), ridge_result, '-x', c='blue', label="R2 of Ridge")
ax.plot(range(5), lasso_result, '-x', c='red', label="R2 of Lasso")
plt.xticks(range(5), alpha)
plt.xlabel('alpha')
plt.ylabel('R2')
plt.legend(loc='upper right')
plt.show()


#LINEAR==========================================
from sklearn.metrics import r2_score,mean_absolute_error, mean_squared_error
X = acne_df3.iloc[:,1:]
y = acne_df3.iloc[:,0]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)


linear = LinearRegression()
linear.fit(X_train,y_train)

linear_y_hat = linear.predict(X_test)

linear_r2 = r2_score(y_test,linear_y_hat)
linear_MSE = mean_squared_error(y_test,linear_y_hat)
linear_MAE = mean_absolute_error(y_test,linear_y_hat)

print('R2 score - Linear: %.2f' %(linear_r2))
print('MSE - Linear: %.2f' %(linear_MSE))
print('MAE - Linear: %.2f' %(linear_MAE))

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(range(len(y_test)), y_test, '-', label="Original Y")
ax.plot(range(len(y_test)), linear_y_hat, '-x', label="linear_y_hat")
plt.legend(loc='upper right')
plt.show()

#RIDGE==========================================
from sklearn.metrics import r2_score,mean_absolute_error, mean_squared_error
X = acne_df3.iloc[:,1:]
y = acne_df3.iloc[:,0]


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
ridge_alpha = 1
ridge = Ridge(alpha = ridge_alpha)
ridge.fit(X_train,y_train)
ridge_y_hat = ridge.predict(X_test)

ridge_r2 = r2_score(y_test,ridge_y_hat)
ridge_MSE = mean_squared_error(y_test,ridge_y_hat)
ridge_MAE = mean_absolute_error(y_test,ridge_y_hat)

print('R2 score -  Ridge: %.2f' %(ridge_r2))
print('MSE - Ridge: %.2f ' %(ridge_MSE))
print('MAE - Ridge: %.2f' %(ridge_MAE))

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(range(len(y_test)), y_test, '-', label="Original Y")
ax.plot(range(len(y_test)), ridge_y_hat, '-x', label="ridge_y_hat")
plt.legend(loc='upper right')
plt.show()

ridge_result = []
alpha = [0.001,0.01,0.1,1,10]

for a in alpha:
  ridge = Ridge(alpha = a)
  ridge.fit(X_train,y_train)
  ridge_y_hat = ridge.predict(X_test)
  ridge_r2 = r2_score(y_test,ridge_y_hat)
  ridge_result.append(ridge_r2)
  lasso_result.append(lasso_r2)
  
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(range(5), ridge_result, '-x', c='blue', label="R2 of Ridge")
plt.xticks(range(5), alpha)
plt.xlabel('alpha')
plt.ylabel('R2')
plt.legend(loc='upper right')
plt.show()

#LASSO==========================================
from sklearn.metrics import r2_score,mean_absolute_error, mean_squared_error
X = acne_df3.iloc[:,1:]
y = acne_df3.iloc[:,0]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
lasso_alpha = 0.1
lasso = Lasso(alpha = lasso_alpha)
lasso.fit(X_train,y_train)
lasso_y_hat = lasso.predict(X_test)
linear_MAE, ridge_MAE, lasso_MAE = mean_absolute_error(y_test,linear_y_hat), mean_absolute_error(y_test,ridge_y_hat), mean_absolute_error(y_test,lasso_y_hat)

print('R2 score - Lasso: %.2f' %(lasso_r2))
print('MSE - Lasso: %.2f' %(lasso_MSE))
print('MAE - Lasso: %.2f' %(lasso_MAE))

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(range(len(y_test)), y_test, '-', label="Original Y")
ax.plot(range(len(y_test)), lasso_y_hat, '-x', label="lasso_y_hat")
plt.legend(loc='upper right')
plt.show()
plt.savefig('R2_lasso1.png')

lasso_result = []
alpha = [0.001,0.01,0.1,1,10]

for a in alpha:
  lasso = Lasso(alpha = a)
  lasso.fit(X_train,y_train)
  lasso_y_hat = lasso.predict(X_test)
  lasso_r2 = r2_score(y_test,lasso_y_hat)
  lasso_result.append(lasso_r2)
  
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(range(5), lasso_result, '-x', c='red', label="R2 of Lasso")
plt.xticks(range(5), alpha)
plt.xlabel('alpha')
plt.ylabel('R2')
plt.legend(loc='upper right')
plt.show()
plt.savefig('R2_lasso2.png')

model = KMeans(n_clusters=4)
model.fit(acne.iloc[:,0:])
model.labels_
model.cluster_centers_



#heatmap==================================================================================

features = acne_df3[['temp', 'pm2_5', 'rain', 'uv', '-10s', '10s', '20s', '30s', '40s', '50s']]
target = acne_df3['total']

acne_df3.columns = [['total', 'temp', 'pm2_5', 'rain', 'uv', '-10s', '10s', '20s', '30s', '40s', '50s']]

X = acne_df3.iloc[:,1:]
y = acne_df3.iloc[:,0]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
mlr = LinearRegression()
mlr.fit(X_train, y_train) 
y_predict = mlr.predict(X_test)

print(mlr.coef_)
((y - y.mean()) ** 2).sum()
print(mlr.score(X_train, y_train))

plt.scatter(y_test, y_predict, alpha=0.4)
plt.xlabel("Actual Rent")
plt.ylabel("Predicted Rent")
plt.title("MULTIPLE LINEAR REGRESSION")
plt.show()

#시계열=======================================================

acne_df3 = pd.read_csv('c:/data/final/acne_df3.csv', encoding='cp949')

acne_df3['date'] = ['2016-01-01', '2016-02-01', '2016-03-01', '2016-04-01', '2016-05-01', '2016-06-01', '2016-07-01', '2016-08-01', '2016-09-01', '2016-10-01', '2016-11-01', '2016-12-01',
                    '2017-01-01', '2017-02-01', '2017-03-01', '2017-04-01', '2017-05-01', '2017-06-01', '2017-07-01', '2017-08-01', '2017-09-01', '2017-10-01', '2017-11-01', '2017-12-01',
                    '2018-01-01', '2018-02-01', '2018-03-01', '2018-04-01', '2018-05-01', '2018-06-01', '2018-07-01', '2018-08-01', '2018-09-01', '2018-10-01', '2018-11-01', '2018-12-01',
                    '2019-01-01', '2019-02-01', '2019-03-01', '2019-04-01', '2019-05-01', '2019-06-01', '2019-07-01', '2019-08-01', '2019-09-01', '2019-10-01', '2019-11-01', '2019-12-01',
                    '2020-01-01', '2020-02-01']
acne_df3['date'] = pd.to_datetime(acne_df3['date']) + MonthEnd(1)
acne_df3.set_index('date', inplace=True)

scaler = MinMaxScaler()
scale_cols = ['total', 'temp', 'pm2_5', 'rain', 'uv']
df_scaled = scaler.fit_transform(acne_df3[scale_cols])
df_scaled = pd.DataFrame(df_scaled)
df_scaled.columns = scale_cols
print(df_scaled)

split_date = pd.Timestamp('2019-02-28')
train = acne_df3.loc[:split_date, ['total', 'temp', 'pm2_5', 'rain', 'uv']]
test = acne_df3.loc[split_date:, ['total', 'temp', 'pm2_5', 'rain', 'uv']]


ax = train.plot()
test.plot(ax=ax)
plt.legend(['train', 'test'])

sc = MinMaxScaler()

train_sc = sc.fit_transform(train)
test_sc = sc.transform(test)

train_sc_df = pd.DataFrame(train_sc, columns=['total', 'temp', 'pm2_5', 'rain', 'uv'], index=train.index)
test_sc_df = pd.DataFrame(test_sc, columns=['total', 'temp', 'pm2_5', 'rain', 'uv'], index=test.index)
train_sc_df.head()

for s in range(1, 13):
    train_sc_df['shift_{}'.format(s)] = train_sc_df['total'].shift(s)
    test_sc_df['shift_{}'.format(s)] = test_sc_df['total'].shift(s)
    train_sc_df['shift_{}'.format(s)] = train_sc_df['temp'].shift(s)
    test_sc_df['shift_{}'.format(s)] = test_sc_df['temp'].shift(s)
    train_sc_df['shift_{}'.format(s)] = train_sc_df['pm2_5'].shift(s)
    test_sc_df['shift_{}'.format(s)] = test_sc_df['pm2_5'].shift(s)
    train_sc_df['shift_{}'.format(s)] = train_sc_df['rain'].shift(s)
    test_sc_df['shift_{}'.format(s)] = test_sc_df['rain'].shift(s)
    train_sc_df['shift_{}'.format(s)] = train_sc_df['uv'].shift(s)
    test_sc_df['shift_{}'.format(s)] = test_sc_df['uv'].shift(s)

train_sc_df.head(13)


X_train = train_sc_df.dropna().drop(['total', 'temp', 'pm2_5', 'rain', 'uv'], axis=1)
y_train = train_sc_df.dropna()[['total', 'temp', 'pm2_5', 'rain', 'uv']]

X_test = test_sc_df.dropna().drop(['total', 'temp', 'pm2_5', 'rain', 'uv'], axis=1)
y_test = test_sc_df.dropna()[['total', 'temp', 'pm2_5', 'rain', 'uv']]

print(type(X_train))
X_train = X_train.values
print(type(X_train))
X_test= X_test.values

y_train = y_train.values
y_test = y_test.values
print(X_train.shape)
#print(X_train)
print(y_train.shape)
#print(y_train)


X_train_t = X_train.reshape(X_train.shape[0], 12, 1)
X_test_t = X_test.reshape(X_test.shape[0], 12, 1)

print("최종 DATA")
print(X_train_t.shape)
print(X_train_t)
print(y_train)

K.clear_session()
    
model = Sequential() # Sequeatial Model 
model.add(LSTM(20, input_shape=(12, 1))) # (timestep, feature) 
model.add(Dense(5)) # output = 1 
model.add(Dense(3)) # output = 1 
model.add(Dense(1)) # output = 1 
model.compile(loss='mean_squared_error', optimizer='adam') 
model.summary()

early_stop = EarlyStopping(monitor='loss', patience=1, verbose=1)

model.fit(X_train_t, y_train, epochs=100,
          batch_size=45, verbose=1, callbacks=[early_stop])

y_hat = model.predict(X_test_t, batch_size=45)
y_hat

a_axis = np.arange(0, len(y_train))
b_axis = np.arange(len(y_train), len(y_train) + len(y_hat))

plt.figure(figsize=(10,6))
plt.plot(a_axis, y_train, 'o-')
plt.plot(b_axis, y_hat, 'o-', color='red', label='Predicted')
plt.plot(b_axis, y_test, 'o-', color='white', alpha=0.2, label='Actual')
plt.legend()
plt.show()

lm = LinearRegression(fit_intercept=True, normalize=True, n_jobs=None)
lm.fit(X_train, y_train)
accuracy = lm.score(X_test, y_test)
print("Linear Regression test file accuracy:" + str(accuracy))


#LSTM==========================================================================

acne_df3 = pd.read_csv('c:/data/final/acne_df3.csv', encoding='cp949')

acne_df3['date'] = ['2016-01-01', '2016-02-01', '2016-03-01', '2016-04-01', '2016-05-01', '2016-06-01', '2016-07-01', '2016-08-01', '2016-09-01', '2016-10-01', '2016-11-01', '2016-12-01',
                    '2017-01-01', '2017-02-01', '2017-03-01', '2017-04-01', '2017-05-01', '2017-06-01', '2017-07-01', '2017-08-01', '2017-09-01', '2017-10-01', '2017-11-01', '2017-12-01',
                    '2018-01-01', '2018-02-01', '2018-03-01', '2018-04-01', '2018-05-01', '2018-06-01', '2018-07-01', '2018-08-01', '2018-09-01', '2018-10-01', '2018-11-01', '2018-12-01',
                    '2019-01-01', '2019-02-01', '2019-03-01', '2019-04-01', '2019-05-01', '2019-06-01', '2019-07-01', '2019-08-01', '2019-09-01', '2019-10-01', '2019-11-01', '2019-12-01',
                    '2020-01-01', '2020-02-01']
acne_df3['date'] = pd.to_datetime(acne_df3['date']) + MonthEnd(1)
acne_df3.set_index('date', inplace=True)
acne_df3.plot(subplots=True)

scaler = MinMaxScaler()
scale_cols = ['total']
df_scaled = scaler.fit_transform(acne_df3[scale_cols])
df_scaled = pd.DataFrame(df_scaled)
df_scaled.columns = scale_cols
print(df_scaled)

split_date = pd.Timestamp('2019-02-28')
train = acne_df3.loc[:split_date, ['total']]
test = acne_df3.loc[split_date:, ['total']]


ax = train.plot()
test.plot(ax=ax)
plt.legend(['train', 'test'])

sc = MinMaxScaler()

train_sc = sc.fit_transform(train)
test_sc = sc.transform(test)

train_sc_df = pd.DataFrame(train_sc, columns=['total'], index=train.index)
test_sc_df = pd.DataFrame(test_sc, columns=['total'], index=test.index)
train_sc_df.head()

for s in range(1, 13):
    train_sc_df['shift_{}'.format(s)] = train_sc_df['total'].shift(s)
    test_sc_df['shift_{}'.format(s)] = test_sc_df['total'].shift(s)


train_sc_df.head(13)


X_train = train_sc_df.dropna().drop(['total'], axis=1)
y_train = train_sc_df.dropna()[['total']]

X_test = test_sc_df.dropna().drop(['total'], axis=1)
y_test = test_sc_df.dropna()[['total']]

print(type(X_train))
X_train = X_train.values
print(type(X_train))
X_test= X_test.values

y_train = y_train.values
y_test = y_test.values
print(X_train.shape)
#print(X_train)
print(y_train.shape)
#print(y_train)


X_train_t = X_train.reshape(X_train.shape[0], 12, 1)
X_test_t = X_test.reshape(X_test.shape[0], 12, 1)

print("최종 DATA")
print(X_train_t.shape)
print(X_train_t)
print(y_train)

K.clear_session()
    
model = Sequential() # Sequeatial Model 
model.add(LSTM(20, input_shape=(12, 1))) # (timestep, feature) 
model.add(Dense(5)) # output = 1 
model.add(Dense(3)) # output = 1 
model.add(Dense(1)) # output = 1 
model.compile(loss='mean_squared_error', optimizer='adam') 
model.summary()

early_stop = EarlyStopping(monitor='loss', patience=1, verbose=1)

model.fit(X_train_t, y_train, epochs=1000,
          batch_size=45, verbose=1, callbacks=[early_stop])

y_hat = model.predict(X_test_t, batch_size=1)
y_hat

a_axis = np.arange(0, len(y_train))
b_axis = np.arange(len(y_train), len(y_train) + len(y_hat))

plt.figure(figsize=(10,6))
plt.plot(a_axis, y_train, 'x-')
plt.plot(b_axis, y_hat, 'o-', color='red', label='Predicted')
plt.plot(b_axis, y_test, 'o-', color='black', alpha=0.2, label='Actual')
plt.legend()
plt.show()

#prophet=================================================================================


acne_prophet = acne_df3[['date', 'total']]
acne_prophet = acne_prophet.rename(columns = {'date' : 'ds', 'total' : 'y'})
acne_prophet = acne_prophet[['ds', 'y']].reset_index(drop=True)
model = Prophet(growth='linear',
                  changepoint_range=0.7, # 데이터의 70% 정도에서 changepoint
                  changepoint_prior_scale=0.3)
model.fit(acne_prophet) 
future = model.make_future_dataframe(periods=365)
forcast = model.predict(future)
forcast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()
fig = model.plot(forcast)
a = add_changepoints_to_plot(fig.gca(), model, forcast)
accne = model.plot(forcast)
sns.set(font_scale=1.1)
fig1 = model.plot_components(forcast)
plt.tight_layout()


#statemodel=================================================================================

y = acne_df3['total'].resample('MS').mean()
y.plot(figsize = (15,6))
plt.show()
decomposition = sm.tsa.seasonal_decompose(y, model='additive') # tsa.seasonal_decompose : 시계열 분할로 순환, 계절성, 잔차로 분해
fig = decomposition.plot()
plt.show()



# ARIMA : ARIMA는 자기진행적 통합 이동 평균, ARIMA 모델은 표기법 ARIMA(p, d, q)로 표시된다. 세 가지 파라미터: 계절성, 추세, 노이즈
p = d = q = range(0, 2)
pdq = list(itertools.product(p, d, q)) # itertools : 자신만의 반복자를 만드는 모듈
seasonal_pdq = [(x[0], x[1], x[2], 12) for x in list(itertools.product(p, d, q))]

print('Examples of parameter combinations for Seasonal ARIMA...')
print('SARIMAX: {} x {}'.format(pdq[1], seasonal_pdq[1]))
print('SARIMAX: {} x {}'.format(pdq[1], seasonal_pdq[2]))
print('SARIMAX: {} x {}'.format(pdq[2], seasonal_pdq[3]))
print('SARIMAX: {} x {}'.format(pdq[2], seasonal_pdq[4]))

# grid search를 사용하여 최적의 매개변수 집합 찾는 것
# 최저 AIC 값 찾기
for param in pdq:
    for param_seasonal in seasonal_pdq:
        try:
            mod = sm.tsa.statespace.SARIMAX(y,
                                            order=param,
                                            seasonal_order=param_seasonal,
                                            enforce_stationarity=False,
                                            enforce_invertibility=False)
            results = mod.fit()
            print('ARIMA{}x{}12 - AIC:{}'.format(param, param_seasonal, results.aic))
        except:
            continue

# 결과로는 -> ARIMA(1, 1, 1)x(1, 1, 1, 12)12 가 AIC:357.8329187473011 최저값 산축 

# Standardized residual : 표준화 잔차 -> 실제 관찰값과 예측값의 차이
# Density : 밀도추정 -> 어떤 변수가 가질 수 있는 값 및 그 값을 가질 가능성의 정도를 추정
# Normal Q-Q : 정규분포 확인
# Correlogram : 오차 확인

mod = sm.tsa.statespace.SARIMAX(y,
                                order=(1, 1, 1), # 최적의 값 입력
                                seasonal_order=(1, 1, 1, 12), # 최적의 값 입력
                                enforce_stationarity=False,
                                enforce_invertibility=False)
results = mod.fit()
print(results.summary().tables[1])
results.plot_diagnostics(figsize=(16, 8))
plt.show()

pred = results.get_prediction(start=pd.to_datetime('2019-02-01'), dynamic=False) # 예측할 시작 날짜 입력
pred_ci = pred.conf_int() #추정된 계수의 신뢰구간 계산
ax = y['2016':].plot(label='observed')
pred.predicted_mean.plot(ax=ax, label='One-step ahead Forecast', alpha=.7, figsize=(14, 7))
ax.fill_between(pred_ci.index,
                pred_ci.iloc[:, 0],
                pred_ci.iloc[:, 1], color='k', alpha=.2)
ax.set_xlabel('Date')
ax.set_ylabel('Patients Count')
plt.legend()
plt.show()

y_forecasted = pred.predicted_mean
y_truth = y['2019-02-01':]
mse = ((y_forecasted - y_truth) ** 2).mean()
print('The Mean Squared Error of our forecasts is {}'.format(round(mse, 2)))

print('The Root Mean Squared Error of our forecasts is {}'.format(round(np.sqrt(mse), 2)))

pred_uc = results.get_forecast(steps=100)
pred_ci = pred_uc.conf_int() #추정된 계수의 신뢰구간 계산
ax = y.plot(label='observed', figsize=(14, 7)) # observed : 관찰값
pred_uc.predicted_mean.plot(ax=ax, label='Forecast') # Forecast : 예측값
ax.fill_between(pred_ci.index,
                pred_ci.iloc[:, 0],
                pred_ci.iloc[:, 1], color='k', alpha=.25)
ax.set_xlabel('Date')
ax.set_ylabel('Patients Count')
plt.legend()
plt.show()