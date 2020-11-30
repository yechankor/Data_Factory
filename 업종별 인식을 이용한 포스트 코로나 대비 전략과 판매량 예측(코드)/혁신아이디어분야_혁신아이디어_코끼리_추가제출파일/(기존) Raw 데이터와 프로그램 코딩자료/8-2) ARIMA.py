# 8-2) ARIMA

import warnings
import itertools # 반복 가능한 데이터 스트림을 처리하는 데 유용한 많은 함수와 제네레이터가 포함
import numpy as np
import matplotlib.pyplot as plt
warnings.filterwarnings("ignore")
plt.style.use('fivethirtyeight')
import pandas as pd
import statsmodels.api as sm #통계분석 기능을 제공하는 파이썬 패키지
import matplotlib
from pylab import rcParams

#차트 기본 크기 설정
matplotlib.rcParams['axes.labelsize'] = 14
matplotlib.rcParams['xtick.labelsize'] = 12
matplotlib.rcParams['ytick.labelsize'] = 12
matplotlib.rcParams['text.color'] = 'k'

pd.set_option('display.max_columns',500) #생략없이 출력


## 오프라인 숙박===============================================================
off_acc1 = pd.read_csv("c:/data/off_acc1.csv",parse_dates=["DATE"])
off_acc1.info()

off_acc1 = off_acc1[['DATE','CN']]

# 2020년 데이터만 뽑음
off_acc2020 = off_acc1[off_acc1['DATE'].dt.year==2020]

#index를 Order Date로 한다.
off_acc2020 = off_acc2020.set_index('DATE')
off_acc2020.head()
off_acc2020.index

y=off_acc2020
y.plot(figsize = (15,6))
plt.show()

#차트 기본 크기 설정
rcParams['figure.figsize'] = 18,8

p = d = q = range(0, 2)
pdq = list(itertools.product(p, d, q))
seasonal_pdq = [(x[0], x[1], x[2], 12) for x in list(itertools.product(p, d, q))]

print('Examples of parameter combinations for Seasonal ARIMA...')
print('SARIMAX: {} x {}'.format(pdq[1], seasonal_pdq[1]))
print('SARIMAX: {} x {}'.format(pdq[1], seasonal_pdq[2]))
print('SARIMAX: {} x {}'.format(pdq[2], seasonal_pdq[3]))
print('SARIMAX: {} x {}'.format(pdq[2], seasonal_pdq[4]))

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

# ARIMA(1, 1, 1)x(1, 1, 1, 12)12 - AIC:1479.5321555603011 

mod = sm.tsa.statespace.SARIMAX(y,
                                order=(1, 1, 1),
                                seasonal_order=(1, 1, 1, 12),
                                enforce_stationarity=False,
                                enforce_invertibility=False)
results = mod.fit()
print(results.summary().tables[1])

results.plot_diagnostics(figsize=(16, 8))
plt.show()

pred = results.get_prediction(start=pd.to_datetime('2020-02-01'), dynamic=False)
pred_ci = pred.conf_int() #추정된 계수의 신뢰구간 계산
ax = y['2020':].plot(label='observed')
pred.predicted_mean.plot(ax=ax, label='One-step ahead Forecast', alpha=.7, figsize=(14, 7))
ax.fill_between(pred_ci.index,
                pred_ci.iloc[:, 0],
                pred_ci.iloc[:, 1], color='k', alpha=.2)
ax.set_xlabel('Date')
ax.set_ylabel('CN')
plt.legend()
plt.show()

y_forecasted = pred.predicted_mean.values
y_truth = y['2020-02-01':].values
mse = ((y_forecasted - y_truth) ** 2).mean()
print('The Mean Squared Error of our forecasts is {}'.format(round(mse, 2)))

print('The Root Mean Squared Error of our forecasts is {}'.format(round(np.sqrt(mse), 2)))

off_acc_MSE = round(np.sqrt(mse), 2)


## 오프라인 문화취미===============================================================
off_cul1 = pd.read_csv("c:/data/off_cul1.csv",parse_dates=["DATE"])
off_cul1.info()

off_cul1 = off_cul1[['DATE','CN']]

# 2020년 데이터만 뽑음
off_cul2020 = off_cul1[off_cul1['DATE'].dt.year==2020]

#index를 Order Date로 한다.
off_cul2020 = off_cul2020.set_index('DATE')
off_cul2020.head()
off_cul2020.index

y=off_cul2020
y.plot(figsize = (15,6))
plt.show()

#차트 기본 크기 설정
rcParams['figure.figsize'] = 18,8

p = d = q = range(0, 2)
pdq = list(itertools.product(p, d, q))
seasonal_pdq = [(x[0], x[1], x[2], 12) for x in list(itertools.product(p, d, q))]

print('Examples of parameter combinations for Seasonal ARIMA...')
print('SARIMAX: {} x {}'.format(pdq[1], seasonal_pdq[1]))
print('SARIMAX: {} x {}'.format(pdq[1], seasonal_pdq[2]))
print('SARIMAX: {} x {}'.format(pdq[2], seasonal_pdq[3]))
print('SARIMAX: {} x {}'.format(pdq[2], seasonal_pdq[4]))

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

# ARIMA(1, 1, 1)x(1, 1, 1, 12)12 - AIC:1642.9795636032777 

mod = sm.tsa.statespace.SARIMAX(y,
                                order=(1, 1, 1),
                                seasonal_order=(1, 1, 1, 12),
                                enforce_stationarity=False,
                                enforce_invertibility=False)
results = mod.fit()
print(results.summary().tables[1])

results.plot_diagnostics(figsize=(16, 8))
plt.show()

pred = results.get_prediction(start=pd.to_datetime('2020-02-02'), dynamic=False)
pred_ci = pred.conf_int() #추정된 계수의 신뢰구간 계산
ax = y['2020':].plot(label='observed')
pred.predicted_mean.plot(ax=ax, label='One-step ahead Forecast', alpha=.7, figsize=(14, 7))
ax.fill_between(pred_ci.index,
                pred_ci.iloc[:, 0],
                pred_ci.iloc[:, 1], color='k', alpha=.2)
ax.set_xlabel('Date')
ax.set_ylabel('CN')
plt.legend()
plt.show()

y_forecasted = pred.predicted_mean.values
y_truth = y['2020-02-01':].values
mse = ((y_forecasted - y_truth) ** 2).mean()
print('The Mean Squared Error of our forecasts is {}'.format(round(mse, 2)))

print('The Root Mean Squared Error of our forecasts is {}'.format(round(np.sqrt(mse), 2)))

off_cul_MSE = round(np.sqrt(mse), 2)

## 오프라인 요식업소===============================================================
off_food1 = pd.read_csv("c:/data/off_food1.csv",parse_dates=["DATE"])
off_food1.info()

off_food1 = off_food1[['DATE','CN']]

# 2020년 데이터만 뽑음
off_food2020 = off_food1[off_food1['DATE'].dt.year==2020]

#index를 Order Date로 한다.
off_food2020 = off_food2020.set_index('DATE')
off_food2020.head()
off_food2020.index

y=off_food2020
y.plot(figsize = (15,6))
plt.show()

#차트 기본 크기 설정
rcParams['figure.figsize'] = 18,8

p = d = q = range(0, 2)
pdq = list(itertools.product(p, d, q))
seasonal_pdq = [(x[0], x[1], x[2], 12) for x in list(itertools.product(p, d, q))]

print('Examples of parameter combinations for Seasonal ARIMA...')
print('SARIMAX: {} x {}'.format(pdq[1], seasonal_pdq[1]))
print('SARIMAX: {} x {}'.format(pdq[1], seasonal_pdq[2]))
print('SARIMAX: {} x {}'.format(pdq[2], seasonal_pdq[3]))
print('SARIMAX: {} x {}'.format(pdq[2], seasonal_pdq[4]))

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

# ARIMA(1, 1, 1)x(1, 1, 1, 12)12 - AIC:2314.6204604255795

mod = sm.tsa.statespace.SARIMAX(y,
                                order=(1, 1, 1),
                                seasonal_order=(1, 1, 1, 12),
                                enforce_stationarity=False,
                                enforce_invertibility=False)
results = mod.fit()
print(results.summary().tables[1])

results.plot_diagnostics(figsize=(16, 8))
plt.show()

pred = results.get_prediction(start=pd.to_datetime('2020-02-02'), dynamic=False)
pred_ci = pred.conf_int() #추정된 계수의 신뢰구간 계산
ax = y['2020':].plot(label='observed')
pred.predicted_mean.plot(ax=ax, label='One-step ahead Forecast', alpha=.7, figsize=(14, 7))
ax.fill_between(pred_ci.index,
                pred_ci.iloc[:, 0],
                pred_ci.iloc[:, 1], color='k', alpha=.2)
ax.set_xlabel('Date')
ax.set_ylabel('CN')
plt.legend()
plt.show()

y_forecasted = pred.predicted_mean.values
y_truth = y['2020-02-01':].values
mse = ((y_forecasted - y_truth) ** 2).mean()
print('The Mean Squared Error of our forecasts is {}'.format(round(mse, 2)))

print('The Root Mean Squared Error of our forecasts is {}'.format(round(np.sqrt(mse), 2)))

off_food_MSE = round(np.sqrt(mse), 2)


## 오프라인 레저===============================================================
off_lei1 = pd.read_csv("c:/data/off_lei1.csv",parse_dates=["DATE"])
off_lei1.info()

off_lei1 = off_lei1[['DATE','CN']]

# 2020년 데이터만 뽑음
off_lei2020 = off_lei1[off_lei1['DATE'].dt.year==2020]

#index를 Order Date로 한다.
off_lei2020 = off_lei2020.set_index('DATE')
off_lei2020.head()
off_lei2020.index

y=off_lei2020
y.plot(figsize = (15,6))
plt.show()

#차트 기본 크기 설정
rcParams['figure.figsize'] = 18,8

p = d = q = range(0, 2)
pdq = list(itertools.product(p, d, q))
seasonal_pdq = [(x[0], x[1], x[2], 12) for x in list(itertools.product(p, d, q))]

print('Examples of parameter combinations for Seasonal ARIMA...')
print('SARIMAX: {} x {}'.format(pdq[1], seasonal_pdq[1]))
print('SARIMAX: {} x {}'.format(pdq[1], seasonal_pdq[2]))
print('SARIMAX: {} x {}'.format(pdq[2], seasonal_pdq[3]))
print('SARIMAX: {} x {}'.format(pdq[2], seasonal_pdq[4]))

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

# ARIMA(1, 1, 1)x(1, 1, 1, 12)12 - AIC:1935.2895757630095 

mod = sm.tsa.statespace.SARIMAX(y,
                                order=(1, 1, 1),
                                seasonal_order=(1, 1, 1, 12),
                                enforce_stationarity=False,
                                enforce_invertibility=False)
results = mod.fit()
print(results.summary().tables[1])

results.plot_diagnostics(figsize=(16, 8))
plt.show()

pred = results.get_prediction(start=pd.to_datetime('2020-02-01'), dynamic=False)
pred_ci = pred.conf_int() #추정된 계수의 신뢰구간 계산
ax = y['2020':].plot(label='observed')
pred.predicted_mean.plot(ax=ax, label='One-step ahead Forecast', alpha=.7, figsize=(14, 7))
ax.fill_between(pred_ci.index,
                pred_ci.iloc[:, 0],
                pred_ci.iloc[:, 1], color='k', alpha=.2)
ax.set_xlabel('Date')
ax.set_ylabel('CN')
plt.legend()
plt.show()

y_forecasted = pred.predicted_mean.values
y_truth = y['2020-02-01':].values
mse = ((y_forecasted - y_truth) ** 2).mean()
print('The Mean Squared Error of our forecasts is {}'.format(round(mse, 2)))

print('The Root Mean Squared Error of our forecasts is {}'.format(round(np.sqrt(mse), 2)))

off_lei_MSE = round(np.sqrt(mse), 2)


## 오프라인 의료기관===============================================================
off_medi1 = pd.read_csv("c:/data/off_medi1.csv",parse_dates=["DATE"])
off_medi1.info()

off_medi1 = off_medi1[['DATE','CN']]

# 2020년 데이터만 뽑음
off_medi2020 = off_medi1[off_medi1['DATE'].dt.year==2020]

#index를 Order Date로 한다.
off_medi2020 = off_medi2020.set_index('DATE')
off_medi2020.head()
off_medi2020.index

y=off_medi2020
y.plot(figsize = (15,6))
plt.show()

#차트 기본 크기 설정
rcParams['figure.figsize'] = 18,8

p = d = q = range(0, 2)
pdq = list(itertools.product(p, d, q))
seasonal_pdq = [(x[0], x[1], x[2], 12) for x in list(itertools.product(p, d, q))]

print('Examples of parameter combinations for Seasonal ARIMA...')
print('SARIMAX: {} x {}'.format(pdq[1], seasonal_pdq[1]))
print('SARIMAX: {} x {}'.format(pdq[1], seasonal_pdq[2]))
print('SARIMAX: {} x {}'.format(pdq[2], seasonal_pdq[3]))
print('SARIMAX: {} x {}'.format(pdq[2], seasonal_pdq[4]))

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

# ARIMA(1, 1, 1)x(1, 1, 1, 12)12 - AIC:2261.9819967985427

mod = sm.tsa.statespace.SARIMAX(y,
                                order=(1, 1, 1),
                                seasonal_order=(1, 1, 1, 12),
                                enforce_stationarity=False,
                                enforce_invertibility=False)
results = mod.fit()
print(results.summary().tables[1])

results.plot_diagnostics(figsize=(16, 8))
plt.show()

pred = results.get_prediction(start=pd.to_datetime('2020-02-01'), dynamic=False)
pred_ci = pred.conf_int() #추정된 계수의 신뢰구간 계산
ax = y['2020':].plot(label='observed')
pred.predicted_mean.plot(ax=ax, label='One-step ahead Forecast', alpha=.7, figsize=(14, 7))
ax.fill_between(pred_ci.index,
                pred_ci.iloc[:, 0],
                pred_ci.iloc[:, 1], color='k', alpha=.2)
ax.set_xlabel('Date')
ax.set_ylabel('CN')
plt.legend()
plt.show()

y_forecasted = pred.predicted_mean.values
y_truth = y['2020-02-01':].values
mse = ((y_forecasted - y_truth) ** 2).mean()
print('The Mean Squared Error of our forecasts is {}'.format(round(mse, 2)))

print('The Root Mean Squared Error of our forecasts is {}'.format(round(np.sqrt(mse), 2)))

off_medi_MSE = round(np.sqrt(mse), 2)


## 오프라인 보건위생===============================================================
off_sani1 = pd.read_csv("c:/data/off_sani1.csv",parse_dates=["DATE"])
off_sani1.info()

off_sani1 = off_sani1[['DATE','CN']]

# 2020년 데이터만 뽑음
off_sani2020 = off_sani1[off_sani1['DATE'].dt.year==2020]

#index를 Order Date로 한다.
off_sani2020 = off_sani2020.set_index('DATE')
off_sani2020.head()
off_sani2020.index

y=off_sani2020
y.plot(figsize = (15,6))
plt.show()

#차트 기본 크기 설정
rcParams['figure.figsize'] = 18,8

p = d = q = range(0, 2)
pdq = list(itertools.product(p, d, q))
seasonal_pdq = [(x[0], x[1], x[2], 12) for x in list(itertools.product(p, d, q))]

print('Examples of parameter combinations for Seasonal ARIMA...')
print('SARIMAX: {} x {}'.format(pdq[1], seasonal_pdq[1]))
print('SARIMAX: {} x {}'.format(pdq[1], seasonal_pdq[2]))
print('SARIMAX: {} x {}'.format(pdq[2], seasonal_pdq[3]))
print('SARIMAX: {} x {}'.format(pdq[2], seasonal_pdq[4]))

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

# ARIMA(1, 1, 1)x(1, 1, 1, 12)12 - AIC:1767.0404019099792

mod = sm.tsa.statespace.SARIMAX(y,
                                order=(1, 1, 1),
                                seasonal_order=(1, 1, 1, 12),
                                enforce_stationarity=False,
                                enforce_invertibility=False)
results = mod.fit()
print(results.summary().tables[1])

results.plot_diagnostics(figsize=(16, 8))
plt.show()

pred = results.get_prediction(start=pd.to_datetime('2020-02-01'), dynamic=False)
pred_ci = pred.conf_int() #추정된 계수의 신뢰구간 계산
ax = y['2020':].plot(label='observed')
pred.predicted_mean.plot(ax=ax, label='One-step ahead Forecast', alpha=.7, figsize=(14, 7))
ax.fill_between(pred_ci.index,
                pred_ci.iloc[:, 0],
                pred_ci.iloc[:, 1], color='k', alpha=.2)
ax.set_xlabel('Date')
ax.set_ylabel('CN')
plt.legend()
plt.show()

y_forecasted = pred.predicted_mean.values
y_truth = y['2020-02-01':].values
mse = ((y_forecasted - y_truth) ** 2).mean()
print('The Mean Squared Error of our forecasts is {}'.format(round(mse, 2)))

print('The Root Mean Squared Error of our forecasts is {}'.format(round(np.sqrt(mse), 2)))

off_sani_MSE = round(np.sqrt(mse), 2)


## 온라인 숙박===============================================================
on_acc1 = pd.read_csv("c:/data/on_acc1.csv",parse_dates=["DATE"])
on_acc1.info()

on_acc1 = on_acc1[['DATE','CN']]

# 2020년 데이터만 뽑음
on_acc2020 = on_acc1[on_acc1['DATE'].dt.year==2020]

#index를 Order Date로 한다.
on_acc2020 = on_acc2020.set_index('DATE')
on_acc2020.head()
on_acc2020.index

y=on_acc2020
y.plot(figsize = (15,6))
plt.show()

#차트 기본 크기 설정
rcParams['figure.figsize'] = 18,8

p = d = q = range(0, 2)
pdq = list(itertools.product(p, d, q))
seasonal_pdq = [(x[0], x[1], x[2], 12) for x in list(itertools.product(p, d, q))]

print('Examples of parameter combinations for Seasonal ARIMA...')
print('SARIMAX: {} x {}'.format(pdq[1], seasonal_pdq[1]))
print('SARIMAX: {} x {}'.format(pdq[1], seasonal_pdq[2]))
print('SARIMAX: {} x {}'.format(pdq[2], seasonal_pdq[3]))
print('SARIMAX: {} x {}'.format(pdq[2], seasonal_pdq[4]))

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

# ARIMA(1, 1, 1)x(1, 1, 1, 12)12 - AIC:1709.2883177706988 

mod = sm.tsa.statespace.SARIMAX(y,
                                order=(1, 1, 1),
                                seasonal_order=(1, 1, 1, 12),
                                enforce_stationarity=False,
                                enforce_invertibility=False)
results = mod.fit()
print(results.summary().tables[1])

results.plot_diagnostics(figsize=(16, 8))
plt.show()

pred = results.get_prediction(start=pd.to_datetime('2020-02-01'), dynamic=False)
pred_ci = pred.conf_int() #추정된 계수의 신뢰구간 계산
ax = y['2020':].plot(label='observed')
pred.predicted_mean.plot(ax=ax, label='One-step ahead Forecast', alpha=.7, figsize=(14, 7))
ax.fill_between(pred_ci.index,
                pred_ci.iloc[:, 0],
                pred_ci.iloc[:, 1], color='k', alpha=.2)
ax.set_xlabel('Date')
ax.set_ylabel('CN')
plt.legend()
plt.show()

y_forecasted = pred.predicted_mean.values
y_truth = y['2020-02-01':].values
mse = ((y_forecasted - y_truth) ** 2).mean()
print('The Mean Squared Error of our forecasts is {}'.format(round(mse, 2)))

print('The Root Mean Squared Error of our forecasts is {}'.format(round(np.sqrt(mse), 2)))

on_acc_MSE = round(np.sqrt(mse), 2)


## 온라인 문화취미===============================================================
on_cul1 = pd.read_csv("c:/data/on_cul1.csv",parse_dates=["DATE"])
on_cul1.info()

on_cul1 = on_cul1[['DATE','CN']]

# 2020년 데이터만 뽑음
on_cul2020 = on_cul1[on_cul1['DATE'].dt.year==2020]

#index를 Order Date로 한다.
on_cul2020 = on_cul2020.set_index('DATE')
on_cul2020.head()
on_cul2020.index

y=on_cul2020
y.plot(figsize = (15,6))
plt.show()

#차트 기본 크기 설정
rcParams['figure.figsize'] = 18,8

p = d = q = range(0, 2)
pdq = list(itertools.product(p, d, q))
seasonal_pdq = [(x[0], x[1], x[2], 12) for x in list(itertools.product(p, d, q))]

print('Examples of parameter combinations for Seasonal ARIMA...')
print('SARIMAX: {} x {}'.format(pdq[1], seasonal_pdq[1]))
print('SARIMAX: {} x {}'.format(pdq[1], seasonal_pdq[2]))
print('SARIMAX: {} x {}'.format(pdq[2], seasonal_pdq[3]))
print('SARIMAX: {} x {}'.format(pdq[2], seasonal_pdq[4]))

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

# ARIMA(1, 1, 1)x(1, 1, 1, 12)12 - AIC:1813.1449289221637 

mod = sm.tsa.statespace.SARIMAX(y,
                                order=(1, 1, 1),
                                seasonal_order=(1, 1, 1, 12),
                                enforce_stationarity=False,
                                enforce_invertibility=False)
results = mod.fit()
print(results.summary().tables[1])

results.plot_diagnostics(figsize=(16, 8))
plt.show()

pred = results.get_prediction(start=pd.to_datetime('2020-02-02'), dynamic=False)
pred_ci = pred.conf_int() #추정된 계수의 신뢰구간 계산
ax = y['2020':].plot(label='observed')
pred.predicted_mean.plot(ax=ax, label='One-step ahead Forecast', alpha=.7, figsize=(14, 7))
ax.fill_between(pred_ci.index,
                pred_ci.iloc[:, 0],
                pred_ci.iloc[:, 1], color='k', alpha=.2)
ax.set_xlabel('Date')
ax.set_ylabel('CN')
plt.legend()
plt.show()

y_forecasted = pred.predicted_mean.values
y_truth = y['2020-02-01':].values
mse = ((y_forecasted - y_truth) ** 2).mean()
print('The Mean Squared Error of our forecasts is {}'.format(round(mse, 2)))

print('The Root Mean Squared Error of our forecasts is {}'.format(round(np.sqrt(mse), 2)))

on_cul_MSE = round(np.sqrt(mse), 2)


## 온라인 요식업소===============================================================
on_food1 = pd.read_csv("c:/data/on_food1.csv",parse_dates=["DATE"])
on_food1.info()

on_food1 = on_food1[['DATE','CN']]

# 2020년 데이터만 뽑음
on_food2020 = on_food1[on_food1['DATE'].dt.year==2020]

#index를 Order Date로 한다.
on_food2020 = on_food2020.set_index('DATE')
on_food2020.head()
on_food2020.index

y=on_food2020
y.plot(figsize = (15,6))
plt.show()

#차트 기본 크기 설정
rcParams['figure.figsize'] = 18,8

p = d = q = range(0, 2)
pdq = list(itertools.product(p, d, q))
seasonal_pdq = [(x[0], x[1], x[2], 12) for x in list(itertools.product(p, d, q))]

print('Examples of parameter combinations for Seasonal ARIMA...')
print('SARIMAX: {} x {}'.format(pdq[1], seasonal_pdq[1]))
print('SARIMAX: {} x {}'.format(pdq[1], seasonal_pdq[2]))
print('SARIMAX: {} x {}'.format(pdq[2], seasonal_pdq[3]))
print('SARIMAX: {} x {}'.format(pdq[2], seasonal_pdq[4]))

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

# ARIMA(1, 1, 1)x(1, 1, 1, 12)12 - AIC:2117.0223375825162

mod = sm.tsa.statespace.SARIMAX(y,
                                order=(1, 1, 1),
                                seasonal_order=(1, 1, 1, 12),
                                enforce_stationarity=False,
                                enforce_invertibility=False)
results = mod.fit()
print(results.summary().tables[1])

results.plot_diagnostics(figsize=(16, 8))
plt.show()

pred = results.get_prediction(start=pd.to_datetime('2020-02-01'), dynamic=False)
pred_ci = pred.conf_int() #추정된 계수의 신뢰구간 계산
ax = y['2020':].plot(label='observed')
pred.predicted_mean.plot(ax=ax, label='One-step ahead Forecast', alpha=.7, figsize=(14, 7))
ax.fill_between(pred_ci.index,
                pred_ci.iloc[:, 0],
                pred_ci.iloc[:, 1], color='k', alpha=.2)
ax.set_xlabel('Date')
ax.set_ylabel('CN')
plt.legend()
plt.show()

y_forecasted = pred.predicted_mean.values
y_truth = y['2020-02-01':].values
mse = ((y_forecasted - y_truth) ** 2).mean()
print('The Mean Squared Error of our forecasts is {}'.format(round(mse, 2)))

print('The Root Mean Squared Error of our forecasts is {}'.format(round(np.sqrt(mse), 2)))

on_food_MSE = round(np.sqrt(mse), 2)


## 온라인 레저===============================================================
on_lei1 = pd.read_csv("c:/data/on_lei1.csv",parse_dates=["DATE"])
on_lei1.info()

on_lei1 = on_lei1[['DATE','CN']]

# 2020년 데이터만 뽑음
on_lei2020 = on_lei1[on_lei1['DATE'].dt.year==2020]

#index를 Order Date로 한다.
on_lei2020 = on_lei2020.set_index('DATE')
on_lei2020.head()
on_lei2020.index

y=on_lei2020
y.plot(figsize = (15,6))
plt.show()

#차트 기본 크기 설정
rcParams['figure.figsize'] = 18,8

p = d = q = range(0, 2)
pdq = list(itertools.product(p, d, q))
seasonal_pdq = [(x[0], x[1], x[2], 12) for x in list(itertools.product(p, d, q))]

print('Examples of parameter combinations for Seasonal ARIMA...')
print('SARIMAX: {} x {}'.format(pdq[1], seasonal_pdq[1]))
print('SARIMAX: {} x {}'.format(pdq[1], seasonal_pdq[2]))
print('SARIMAX: {} x {}'.format(pdq[2], seasonal_pdq[3]))
print('SARIMAX: {} x {}'.format(pdq[2], seasonal_pdq[4]))

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

# ARIMA(1, 1, 1)x(1, 1, 1, 12)12 - AIC:1506.3260532297984 

mod = sm.tsa.statespace.SARIMAX(y,
                                order=(1, 1, 1),
                                seasonal_order=(1, 1, 1, 12),
                                enforce_stationarity=False,
                                enforce_invertibility=False)
results = mod.fit()
print(results.summary().tables[1])

results.plot_diagnostics(figsize=(16, 8))
plt.show()

pred = results.get_prediction(start=pd.to_datetime('2020-02-01'), dynamic=False)
pred_ci = pred.conf_int() #추정된 계수의 신뢰구간 계산
ax = y['2020':].plot(label='observed')
pred.predicted_mean.plot(ax=ax, label='One-step ahead Forecast', alpha=.7, figsize=(14, 7))
ax.fill_between(pred_ci.index,
                pred_ci.iloc[:, 0],
                pred_ci.iloc[:, 1], color='k', alpha=.2)
ax.set_xlabel('Date')
ax.set_ylabel('CN')
plt.legend()
plt.show()

y_forecasted = pred.predicted_mean.values
y_truth = y['2020-02-01':].values
mse = ((y_forecasted - y_truth) ** 2).mean()
print('The Mean Squared Error of our forecasts is {}'.format(round(mse, 2)))

print('The Root Mean Squared Error of our forecasts is {}'.format(round(np.sqrt(mse), 2)))

on_lei_MSE = round(np.sqrt(mse), 2)


## 온라인 보건위생===============================================================
on_sani1 = pd.read_csv("c:/data/on_sani1.csv",parse_dates=["DATE"])
on_sani1.info()

on_sani1 = on_sani1[['DATE','CN']]

# 2020년 데이터만 뽑음
on_sani2020 = on_sani1[on_sani1['DATE'].dt.year==2020]

#index를 Order Date로 한다.
on_sani2020 = on_sani2020.set_index('DATE')
on_sani2020.head()
on_sani2020.index

y=on_sani2020
y.plot(figsize = (15,6))
plt.show()

#차트 기본 크기 설정
rcParams['figure.figsize'] = 18,8

p = d = q = range(0, 2)
pdq = list(itertools.product(p, d, q))
seasonal_pdq = [(x[0], x[1], x[2], 12) for x in list(itertools.product(p, d, q))]

print('Examples of parameter combinations for Seasonal ARIMA...')
print('SARIMAX: {} x {}'.format(pdq[1], seasonal_pdq[1]))
print('SARIMAX: {} x {}'.format(pdq[1], seasonal_pdq[2]))
print('SARIMAX: {} x {}'.format(pdq[2], seasonal_pdq[3]))
print('SARIMAX: {} x {}'.format(pdq[2], seasonal_pdq[4]))

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

# ARIMA(1, 1, 1)x(1, 1, 1, 12)12 - AIC:2074.345914714061 

mod = sm.tsa.statespace.SARIMAX(y,
                                order=(1, 1, 1),
                                seasonal_order=(1, 1, 1, 12),
                                enforce_stationarity=False,
                                enforce_invertibility=False)
results = mod.fit()
print(results.summary().tables[1])

results.plot_diagnostics(figsize=(16, 8))
plt.show()

pred = results.get_prediction(start=pd.to_datetime('2020-02-01'), dynamic=False)
pred_ci = pred.conf_int() #추정된 계수의 신뢰구간 계산
ax = y['2020':].plot(label='observed')
pred.predicted_mean.plot(ax=ax, label='One-step ahead Forecast', alpha=.7, figsize=(14, 7))
ax.fill_between(pred_ci.index,
                pred_ci.iloc[:, 0],
                pred_ci.iloc[:, 1], color='k', alpha=.2)
ax.set_xlabel('Date')
ax.set_ylabel('CN')
plt.legend()
plt.show()

y_forecasted = pred.predicted_mean.values
y_truth = y['2020-02-01':].values
mse = ((y_forecasted - y_truth) ** 2).mean()
print('The Mean Squared Error of our forecasts is {}'.format(round(mse, 2)))



print('The Root Mean Squared Error of our forecasts is {}'.format(round(np.sqrt(mse), 2)))

on_sani_MSE = round(np.sqrt(mse), 2)


'''
df = pd.DataFrame(index=['off_acc_MSE','off_cul_MSE','off_food_MSE','off_lei_MSE',
                                           'off_medi_MSE','off_sani_MSE','on_acc_MSE','on_cul_MSE',
                                           'on_food_MSE','on_lei_MSE','on_sani_MSE'],
                  data = {'root_MSE' : [off_acc_MSE,off_cul_MSE,off_food_MSE,off_lei_MSE,
                                           off_medi_MSE,off_sani_MSE,on_acc_MSE,on_cul_MSE,
                                           on_food_MSE,on_lei_MSE,on_sani_MSE]})

df
'''

# 파일로 떨어트리기
df.to_csv('c:/data/ARIMA_RMSE.csv',index=True)