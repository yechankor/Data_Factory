# 8-1) LSTM

# anaconda prompt에서 
pip install -keras
pip install -tensorflow

from pandas import *
import pandas as pd
import numpy as np
import math
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
import matplotlib.pylab as plt
from matplotlib import font_manager, rc
font_name= font_manager.FontProperties(fname="C:/data/a옛날사진관3.ttf").get_name()
rc('font',family=font_name)

def create_dataset(dataset,look_back=1):
    dataX,dataY=[],[]
    for i in range(len(dataset)-look_back-1):
        a=dataset[i:(i+look_back),0]
        dataX.append(a)
        dataY.append(dataset[i+look_back,0])
    return np.array(dataX), np.array(dataY)

accuracy=pd.DataFrame(columns=['name','train','test'])
lst=['off_acc']
#off_acc1
off_acc1=pd.read_csv("C:/data/off_acc1.csv",parse_dates=["DATE"])
off_acc1.info()
#off_acc1_2019=off_acc1[off_acc1['DATE'].dt.year==2019]
off_acc1_2020=off_acc1[off_acc1['DATE'].dt.year==2020]
dataset=off_acc1_2020.loc[:,'CN']
dataset=dataset.values
dataset.astype("float32")
scaler=MinMaxScaler(feature_range=(0,1))
dataset=scaler.fit_transform(dataset.reshape(-1,1))

train_size=int(len(dataset)*0.6)
test_size=len(dataset)-train_size
train,test=dataset[0:train_size,:], dataset[train_size:len(dataset),:]
#print(len(train),len(test))

look_back=1
trainX,trainY = create_dataset(train, look_back)
testX, testY = create_dataset(test,look_back)
trainX = np.reshape(trainX,(trainX.shape[0],1,trainX.shape[1]))
testX = np.reshape(testX,(testX.shape[0],1,testX.shape[1]))

model= Sequential()
model.add(LSTM(4,input_shape=(1,look_back)))
model.add(Dense(1))
model.compile(loss='mean_squared_error',optimizer="adam")
model.fit(trainX,trainY,epochs=100,batch_size=1,verbose=2)

trainPredict = model.predict(trainX)
testPredict=model.predict(testX)

trainPredict = scaler.inverse_transform(trainPredict)
trainY = scaler.inverse_transform([trainY])
testPredict = scaler.inverse_transform(testPredict)
testY=scaler.inverse_transform([testY])

#calculate root mean squared error
lst.append(math.sqrt(mean_squared_error(trainY[0],trainPredict[:,0])))
lst.append(math.sqrt(mean_squared_error(testY[0],testPredict[:,0])))

accuracy=accuracy.append(Series(lst,index=accuracy.columns),ignore_index=True)

trainPredictPlot = np.empty_like(dataset)
trainPredictPlot[:, :] = np.nan
trainPredictPlot[look_back:len(trainPredict)+look_back, :] = trainPredict
testPredictPlot = np.empty_like(dataset)
testPredictPlot[:, :] = np.nan
testPredictPlot[len(trainPredict)+(look_back*2)+1:len(dataset)-1, :] = testPredict

plt.figure(figsize=(8,6))
plt.plot(scaler.inverse_transform(dataset),color="gray",label="real data")
plt.plot(trainPredictPlot,color="blue",label="train predict",linestyle="-.")
plt.plot(testPredictPlot,color="red",label="test predict",linestyle="-.")
plt.legend(loc="lower right")
plt.title("오프라인 숙박 LSTM")
plt.show()

#off_cul1
lst=['off_cul']
off_cul1=pd.read_csv("C:/data/off_cul1.csv")
off_cul1['DATE']=pd.to_datetime(off_cul1['DATE'],format="%Y-%m-%d")
off_cul1_2020=off_cul1[off_cul1['DATE'].dt.year==2020]
dataset=off_cul1_2020.loc[:,'CN']
dataset=dataset.values
dataset.astype("float32")
scaler=MinMaxScaler(feature_range=(0,1))
dataset=scaler.fit_transform(dataset.reshape(-1,1))
train_size=int(len(dataset)*0.6)
test_size=len(dataset)-train_size
train,test=dataset[0:train_size,:], dataset[train_size:len(dataset),:]

look_back=1
trainX,trainY = create_dataset(train, look_back)
testX, testY = create_dataset(test,look_back)
trainX = np.reshape(trainX,(trainX.shape[0],1,trainX.shape[1]))
testX = np.reshape(testX,(testX.shape[0],1,testX.shape[1]))

model= Sequential()
model.add(LSTM(4,input_shape=(1,look_back)))
model.add(Dense(1))
model.compile(loss='mean_squared_error',optimizer="adam")
model.fit(trainX,trainY,epochs=100,batch_size=1,verbose=2)

trainPredict = model.predict(trainX)
testPredict=model.predict(testX)

trainPredict = scaler.inverse_transform(trainPredict)
trainY = scaler.inverse_transform([trainY])
testPredict = scaler.inverse_transform(testPredict)
testY=scaler.inverse_transform([testY])

#calculate root mean squared error
lst.append(math.sqrt(mean_squared_error(trainY[0],trainPredict[:,0])))
lst.append(math.sqrt(mean_squared_error(testY[0],testPredict[:,0])))

accuracy=accuracy.append(Series(lst,index=accuracy.columns),ignore_index=True)

trainPredictPlot = np.empty_like(dataset)
trainPredictPlot[:, :] = np.nan
trainPredictPlot[look_back:len(trainPredict)+look_back, :] = trainPredict
testPredictPlot = np.empty_like(dataset)
testPredictPlot[:, :] = np.nan
testPredictPlot[len(trainPredict)+(look_back*2)+1:len(dataset)-1, :] = testPredict

plt.figure(figsize=(8,6))
plt.plot(scaler.inverse_transform(dataset),color="gray",label="real data")
plt.plot(trainPredictPlot,color="blue",label="train predict",linestyle="-.")
plt.plot(testPredictPlot,color="red",label="test predict",linestyle="-.")
plt.legend(loc="lower right")
plt.title("오프라인 문화취미 LSTM")
plt.show()

#off_food1
lst=['off_food']
off_food1=pd.read_csv("C:/data/off_food2.csv",parse_dates=["DATE"])
off_food1_2020=off_food1[off_food1['DATE'].dt.year==2020]
dataset=off_food1_2020.loc[:,'CN']
dataset=dataset.values
dataset.astype("float32")
scaler=MinMaxScaler(feature_range=(0,1))
dataset=scaler.fit_transform(dataset.reshape(-1,1))
train_size=int(len(dataset)*0.6)
test_size=len(dataset)-train_size
train,test=dataset[0:train_size,:], dataset[train_size:len(dataset),:]
#print(len(train),len(test))

look_back=1
trainX,trainY = create_dataset(train, look_back)
testX, testY = create_dataset(test,look_back)
trainX = np.reshape(trainX,(trainX.shape[0],1,trainX.shape[1]))
testX = np.reshape(testX,(testX.shape[0],1,testX.shape[1]))

model= Sequential()
model.add(LSTM(4,input_shape=(1,look_back)))
model.add(Dense(1))
model.compile(loss='mean_squared_error',optimizer="adam")
model.fit(trainX,trainY,epochs=100,batch_size=1,verbose=2)

trainPredict = model.predict(trainX)
testPredict=model.predict(testX)

trainPredict = scaler.inverse_transform(trainPredict)
trainY = scaler.inverse_transform([trainY])
testPredict = scaler.inverse_transform(testPredict)
testY=scaler.inverse_transform([testY])

#calculate root mean squared error
lst.append(math.sqrt(mean_squared_error(trainY[0],trainPredict[:,0])))
lst.append(math.sqrt(mean_squared_error(testY[0],testPredict[:,0])))

accuracy=accuracy.append(Series(lst,index=accuracy.columns),ignore_index=True)

trainPredictPlot = np.empty_like(dataset)
trainPredictPlot[:, :] = np.nan
trainPredictPlot[look_back:len(trainPredict)+look_back, :] = trainPredict
testPredictPlot = np.empty_like(dataset)
testPredictPlot[:, :] = np.nan
testPredictPlot[len(trainPredict)+(look_back*2)+1:len(dataset)-1, :] = testPredict

plt.figure(figsize=(8,6))
plt.plot(scaler.inverse_transform(dataset),color="gray",label="real data")
plt.plot(trainPredictPlot,color="blue",label="train predict",linestyle="-.")
plt.plot(testPredictPlot,color="red",label="test predict",linestyle="-.")
plt.legend(loc="lower right")
plt.title("오프라인 요식업소 LSTM")
plt.show()

#off_lei1
lst=['off_lei']
off_lei1=pd.read_csv("C:/data/off_lei1.csv",parse_dates=["DATE"])
off_lei1_2020=off_lei1[off_lei1['DATE'].dt.year==2020]
dataset=off_lei1_2020.loc[:,'CN']
dataset=dataset.values
dataset.astype("float32")
scaler=MinMaxScaler(feature_range=(0,1))
dataset=scaler.fit_transform(dataset.reshape(-1,1))

train_size=int(len(dataset)*0.6)
test_size=len(dataset)-train_size
train,test=dataset[0:train_size,:], dataset[train_size:len(dataset),:]
print(len(train),len(test))

look_back=1
trainX,trainY = create_dataset(train, look_back)
testX, testY = create_dataset(test,look_back)
trainX = np.reshape(trainX,(trainX.shape[0],1,trainX.shape[1]))
testX = np.reshape(testX,(testX.shape[0],1,testX.shape[1]))

model= Sequential()
model.add(LSTM(4,input_shape=(1,look_back)))
model.add(Dense(1))
model.compile(loss='mean_squared_error',optimizer="adam")
model.fit(trainX,trainY,epochs=100,batch_size=1,verbose=2)

trainPredict = model.predict(trainX)
testPredict=model.predict(testX)

trainPredict = scaler.inverse_transform(trainPredict)
trainY = scaler.inverse_transform([trainY])
testPredict = scaler.inverse_transform(testPredict)
testY=scaler.inverse_transform([testY])

#calculate root mean squared error
lst.append(math.sqrt(mean_squared_error(trainY[0],trainPredict[:,0])))
lst.append(math.sqrt(mean_squared_error(testY[0],testPredict[:,0])))

accuracy=accuracy.append(Series(lst,index=accuracy.columns),ignore_index=True)

trainPredictPlot = np.empty_like(dataset)
trainPredictPlot[:, :] = np.nan
trainPredictPlot[look_back:len(trainPredict)+look_back, :] = trainPredict
testPredictPlot = np.empty_like(dataset)
testPredictPlot[:, :] = np.nan
testPredictPlot[len(trainPredict)+(look_back*2)+1:len(dataset)-1, :] = testPredict

plt.figure(figsize=(8,6))
plt.plot(scaler.inverse_transform(dataset),color="gray",label="real data") # 진짜 데이터 셋
plt.plot(trainPredictPlot,color="blue",label="train predict",linestyle="-.") # train 예측 데이터 그래프
plt.plot(testPredictPlot,color="red",label="test predict",linestyle="-.") # test 테스트 데이터 그래프
plt.legend(loc="lower right")
plt.title("오프라인 레저 LSTM")
plt.show()

#off_medi1
lst=['off_medi']
off_medi1=pd.read_csv("C:/data/off_medi1.csv",parse_dates=["DATE"])
off_medi1_2020=off_medi1[off_medi1['DATE'].dt.year==2020]

dataset=off_medi1_2020.loc[:,'CN']
dataset=dataset.values
dataset.astype("float32")
scaler=MinMaxScaler(feature_range=(0,1))
dataset=scaler.fit_transform(dataset.reshape(-1,1))

train_size=int(len(dataset)*0.6)
test_size=len(dataset)-train_size
train,test=dataset[0:train_size,:], dataset[train_size:len(dataset),:]

look_back=1
trainX,trainY = create_dataset(train, look_back)
testX, testY = create_dataset(test,look_back)
trainX = np.reshape(trainX,(trainX.shape[0],1,trainX.shape[1]))
testX = np.reshape(testX,(testX.shape[0],1,testX.shape[1]))

model= Sequential()
model.add(LSTM(4,input_shape=(1,look_back)))
model.add(Dense(1))
model.compile(loss='mean_squared_error',optimizer="adam")
model.fit(trainX,trainY,epochs=100,batch_size=1,verbose=2)

trainPredict = model.predict(trainX)
testPredict=model.predict(testX)

trainPredict = scaler.inverse_transform(trainPredict)
trainY = scaler.inverse_transform([trainY])
testPredict = scaler.inverse_transform(testPredict)
testY=scaler.inverse_transform([testY])

#calculate root mean squared error
lst.append(math.sqrt(mean_squared_error(trainY[0],trainPredict[:,0])))
lst.append(math.sqrt(mean_squared_error(testY[0],testPredict[:,0])))

accuracy=accuracy.append(Series(lst,index=accuracy.columns),ignore_index=True)

trainPredictPlot = np.empty_like(dataset)
trainPredictPlot[:, :] = np.nan
trainPredictPlot[look_back:len(trainPredict)+look_back, :] = trainPredict
testPredictPlot = np.empty_like(dataset)
testPredictPlot[:, :] = np.nan
testPredictPlot[len(trainPredict)+(look_back*2)+1:len(dataset)-1, :] = testPredict

plt.figure(figsize=(8,6))
plt.plot(scaler.inverse_transform(dataset),color="gray",label="real data")
plt.plot(trainPredictPlot,color="blue",label="train predict",linestyle="-.")
plt.plot(testPredictPlot,color="red",label="test predict",linestyle="-.")
plt.legend(loc="lower right")
plt.title("오프라인 의료기관 LSTM")
plt.show()

#off_sani1
lst=['off_sani']
off_sani1=pd.read_csv("C:/data/off_sani1.csv",parse_dates=["DATE"])
off_sani1_2020=off_sani1[off_sani1['DATE'].dt.year==2020]

dataset=off_sani1_2020.loc[:,'CN']
dataset=dataset.values
dataset.astype("float32")
scaler=MinMaxScaler(feature_range=(0,1))
dataset=scaler.fit_transform(dataset.reshape(-1,1))

train_size=int(len(dataset)*0.6)
test_size=len(dataset)-train_size
train,test=dataset[0:train_size,:], dataset[train_size:len(dataset),:]
#print(len(train),len(test))

look_back=1
trainX,trainY = create_dataset(train, look_back)
testX, testY = create_dataset(test,look_back)
trainX = np.reshape(trainX,(trainX.shape[0],1,trainX.shape[1]))
testX = np.reshape(testX,(testX.shape[0],1,testX.shape[1]))

model= Sequential()
model.add(LSTM(4,input_shape=(1,look_back)))
model.add(Dense(1))
model.compile(loss='mean_squared_error',optimizer="adam")
model.fit(trainX,trainY,epochs=100,batch_size=1,verbose=2)

trainPredict = model.predict(trainX)
testPredict=model.predict(testX)

trainPredict = scaler.inverse_transform(trainPredict)
trainY = scaler.inverse_transform([trainY])
testPredict = scaler.inverse_transform(testPredict)
testY=scaler.inverse_transform([testY])

#calculate root mean squared error
lst.append(math.sqrt(mean_squared_error(trainY[0],trainPredict[:,0])))
lst.append(math.sqrt(mean_squared_error(testY[0],testPredict[:,0])))

accuracy=accuracy.append(Series(lst,index=accuracy.columns),ignore_index=True)

trainPredictPlot = np.empty_like(dataset)
trainPredictPlot[:, :] = np.nan
trainPredictPlot[look_back:len(trainPredict)+look_back, :] = trainPredict
testPredictPlot = np.empty_like(dataset)
testPredictPlot[:, :] = np.nan
testPredictPlot[len(trainPredict)+(look_back*2)+1:len(dataset)-1, :] = testPredict

plt.figure(figsize=(8,6))
plt.plot(scaler.inverse_transform(dataset),color="gray",label="real data")
plt.plot(trainPredictPlot,color="blue",label="train predict",linestyle="-.")
plt.plot(testPredictPlot,color="red",label="test predict",linestyle="-.")
plt.legend(loc="lower right")
plt.title("오프라인 보건위생 LSTM")
plt.show()

#on_acc1
lst=['on_acc']
on_acc1=pd.read_csv("C:/data/on_acc1.csv")
on_acc1['DATE']=pd.to_datetime(on_acc1['DATE'],format="%y%m%d")
on_acc1_2020=on_acc1[on_acc1['DATE'].dt.year==2020]

dataset=on_acc1_2020.loc[:,'CN']
dataset=dataset.values
dataset.astype("float32")
scaler=MinMaxScaler(feature_range=(0,1))
dataset=scaler.fit_transform(dataset.reshape(-1,1))

train_size=int(len(dataset)*0.6)
test_size=len(dataset)-train_size
train,test=dataset[0:train_size,:], dataset[train_size:len(dataset),:]
#print(len(train),len(test))

look_back=1
trainX,trainY = create_dataset(train, look_back)
testX, testY = create_dataset(test,look_back)
trainX = np.reshape(trainX,(trainX.shape[0],1,trainX.shape[1]))
testX = np.reshape(testX,(testX.shape[0],1,testX.shape[1]))

model= Sequential()
model.add(LSTM(4,input_shape=(1,look_back)))
model.add(Dense(1))
model.compile(loss='mean_squared_error',optimizer="adam")
model.fit(trainX,trainY,epochs=100,batch_size=1,verbose=2)

trainPredict = model.predict(trainX)
testPredict=model.predict(testX)

trainPredict = scaler.inverse_transform(trainPredict)
trainY = scaler.inverse_transform([trainY])
testPredict = scaler.inverse_transform(testPredict)
testY=scaler.inverse_transform([testY])

#calculate root mean squared error
lst.append(math.sqrt(mean_squared_error(trainY[0],trainPredict[:,0])))
lst.append(math.sqrt(mean_squared_error(testY[0],testPredict[:,0])))

accuracy=accuracy.append(Series(lst,index=accuracy.columns),ignore_index=True)

trainPredictPlot = np.empty_like(dataset)
trainPredictPlot[:, :] = np.nan
trainPredictPlot[look_back:len(trainPredict)+look_back, :] = trainPredict
testPredictPlot = np.empty_like(dataset)
testPredictPlot[:, :] = np.nan
testPredictPlot[len(trainPredict)+(look_back*2)+1:len(dataset)-1, :] = testPredict

plt.figure(figsize=(8,6))
plt.plot(scaler.inverse_transform(dataset),color="gray",label="real data")
plt.plot(trainPredictPlot,color="blue",label="train predict",linestyle="-.")
plt.plot(testPredictPlot,color="red",label="test predict",linestyle="-.")
plt.legend(loc="lower right")
plt.title("온라인 숙박 LSTM")
plt.show()


#on_cul1
lst=['on_cul']
on_cul1=pd.read_csv("C:/data/on_cul1.csv")
on_cul1['DATE']=pd.to_datetime(on_cul1['DATE'],format="%y%m%d")
on_cul1_2020=on_cul1[on_cul1['DATE'].dt.year==2020]

dataset=on_cul1_2020.loc[:,'CN']
dataset=dataset.values
dataset.astype("float32")
scaler=MinMaxScaler(feature_range=(0,1))
dataset=scaler.fit_transform(dataset.reshape(-1,1))

train_size=int(len(dataset)*0.6)
test_size=len(dataset)-train_size
train,test=dataset[0:train_size,:], dataset[train_size:len(dataset),:]
#print(len(train),len(test))

look_back=1
trainX,trainY = create_dataset(train, look_back)
testX, testY = create_dataset(test,look_back)
trainX = np.reshape(trainX,(trainX.shape[0],1,trainX.shape[1]))
testX = np.reshape(testX,(testX.shape[0],1,testX.shape[1]))

model= Sequential()
model.add(LSTM(4,input_shape=(1,look_back)))
model.add(Dense(1))
model.compile(loss='mean_squared_error',optimizer="adam")
model.fit(trainX,trainY,epochs=100,batch_size=1,verbose=2)

trainPredict = model.predict(trainX)
testPredict=model.predict(testX)

trainPredict = scaler.inverse_transform(trainPredict)
trainY = scaler.inverse_transform([trainY])
testPredict = scaler.inverse_transform(testPredict)
testY=scaler.inverse_transform([testY])

#calculate root mean squared error
lst.append(math.sqrt(mean_squared_error(trainY[0],trainPredict[:,0])))
lst.append(math.sqrt(mean_squared_error(testY[0],testPredict[:,0])))

accuracy=accuracy.append(Series(lst,index=accuracy.columns),ignore_index=True)

trainPredictPlot = np.empty_like(dataset)
trainPredictPlot[:, :] = np.nan
trainPredictPlot[look_back:len(trainPredict)+look_back, :] = trainPredict
testPredictPlot = np.empty_like(dataset)
testPredictPlot[:, :] = np.nan
testPredictPlot[len(trainPredict)+(look_back*2)+1:len(dataset)-1, :] = testPredict

plt.figure(figsize=(8,6))
plt.plot(scaler.inverse_transform(dataset),color="gray",label="real data")
plt.plot(trainPredictPlot,color="blue",label="train predict",linestyle="-.")
plt.plot(testPredictPlot,color="red",label="test predict",linestyle="-.")
plt.legend(loc="lower right")
plt.title("온라인 문화취미 LSTM")
plt.show()

#on_food1
lst=['on_food']
on_food1=pd.read_csv("C:/data/on_food1.csv")
on_food1['DATE']=pd.to_datetime(on_food1['DATE'],format="%y%m%d")
on_food1_2020=on_food1[on_food1['DATE'].dt.year==2020]
dataset=on_food1_2020.loc[:,'CN']

dataset=dataset.values
dataset.astype("float32")
scaler=MinMaxScaler(feature_range=(0,1))
dataset=scaler.fit_transform(dataset.reshape(-1,1))

train_size=int(len(dataset)*0.6)
test_size=len(dataset)-train_size
train,test=dataset[0:train_size,:], dataset[train_size:len(dataset),:]
#print(len(train),len(test))

look_back=1
trainX,trainY = create_dataset(train, look_back)
testX, testY = create_dataset(test,look_back)
trainX = np.reshape(trainX,(trainX.shape[0],1,trainX.shape[1]))
testX = np.reshape(testX,(testX.shape[0],1,testX.shape[1]))

model= Sequential()
model.add(LSTM(4,input_shape=(1,look_back)))
model.add(Dense(1))
model.compile(loss='mean_squared_error',optimizer="adam")
model.fit(trainX,trainY,epochs=100,batch_size=1,verbose=2)

trainPredict = model.predict(trainX)
testPredict=model.predict(testX)

trainPredict = scaler.inverse_transform(trainPredict)
trainY = scaler.inverse_transform([trainY])
testPredict = scaler.inverse_transform(testPredict)
testY=scaler.inverse_transform([testY])

#calculate root mean squared error
lst.append(math.sqrt(mean_squared_error(trainY[0],trainPredict[:,0])))
lst.append(math.sqrt(mean_squared_error(testY[0],testPredict[:,0])))

accuracy=accuracy.append(Series(lst,index=accuracy.columns),ignore_index=True)

trainPredictPlot = np.empty_like(dataset)
trainPredictPlot[:, :] = np.nan
trainPredictPlot[look_back:len(trainPredict)+look_back, :] = trainPredict
testPredictPlot = np.empty_like(dataset)
testPredictPlot[:, :] = np.nan
testPredictPlot[len(trainPredict)+(look_back*2)+1:len(dataset)-1, :] = testPredict

plt.figure(figsize=(8,6))
plt.plot(scaler.inverse_transform(dataset),color="gray",label="real data")
plt.plot(trainPredictPlot,color="blue",label="train predict",linestyle="-.")
plt.plot(testPredictPlot,color="red",label="test predict",linestyle="-.")
plt.legend(loc="lower right")
plt.title("온라인 요식업소 LSTM")
plt.show()

#on_lei1
lst=['on_lei']
on_lei1=pd.read_csv("C:/data/on_lei1.csv")
on_lei1['DATE']=pd.to_datetime(on_lei1['DATE'],format="%y%m%d")
on_lei1_2020=on_lei1[on_lei1['DATE'].dt.year==2020]

dataset=on_lei1_2020.loc[:,'CN']
dataset=dataset.values
dataset.astype("float32")
scaler=MinMaxScaler(feature_range=(0,1))
dataset=scaler.fit_transform(dataset.reshape(-1,1))

train_size=int(len(dataset)*0.6)
test_size=len(dataset)-train_size
train,test=dataset[0:train_size,:], dataset[train_size:len(dataset),:]
#print(len(train),len(test))

look_back=1
trainX,trainY = create_dataset(train, look_back)
testX, testY = create_dataset(test,look_back)
trainX = np.reshape(trainX,(trainX.shape[0],1,trainX.shape[1]))
testX = np.reshape(testX,(testX.shape[0],1,testX.shape[1]))

model= Sequential()
model.add(LSTM(4,input_shape=(1,look_back)))
model.add(Dense(1))
model.compile(loss='mean_squared_error',optimizer="adam")
model.fit(trainX,trainY,epochs=100,batch_size=1,verbose=2)

trainPredict = model.predict(trainX)
testPredict=model.predict(testX)

trainPredict = scaler.inverse_transform(trainPredict)
trainY = scaler.inverse_transform([trainY])
testPredict = scaler.inverse_transform(testPredict)
testY=scaler.inverse_transform([testY])

#calculate root mean squared error
lst.append(math.sqrt(mean_squared_error(trainY[0],trainPredict[:,0])))
lst.append(math.sqrt(mean_squared_error(testY[0],testPredict[:,0])))

accuracy=accuracy.append(Series(lst,index=accuracy.columns),ignore_index=True)

trainPredictPlot = np.empty_like(dataset)
trainPredictPlot[:, :] = np.nan
trainPredictPlot[look_back:len(trainPredict)+look_back, :] = trainPredict
testPredictPlot = np.empty_like(dataset)
testPredictPlot[:, :] = np.nan
testPredictPlot[len(trainPredict)+(look_back*2)+1:len(dataset)-1, :] = testPredict

plt.figure(figsize=(8,6))
plt.plot(scaler.inverse_transform(dataset),color="gray",label="real data")
plt.plot(trainPredictPlot,color="blue",label="train predict",linestyle="-.")
plt.plot(testPredictPlot,color="red",label="test predict",linestyle="-.")
plt.legend(loc="lower right")
plt.title("온라인 레저 LSTM")
plt.show()

#on_sani
lst=['on_sani']
on_sani1=pd.read_csv("C:/data/on_sani1.csv")
on_sani1['DATE']=pd.to_datetime(on_sani1['DATE'],format="%y%m%d")
on_sani1_2020=on_sani1[on_sani1['DATE'].dt.year==2020]

dataset=on_sani1_2020.loc[:,'CN']
dataset=dataset.values
dataset.astype("float32")
scaler=MinMaxScaler(feature_range=(0,1))
dataset=scaler.fit_transform(dataset.reshape(-1,1))

train_size=int(len(dataset)*0.6)
test_size=len(dataset)-train_size
train,test=dataset[0:train_size,:], dataset[train_size:len(dataset),:]
print(len(train),len(test))

look_back=1
trainX,trainY = create_dataset(train, look_back)
testX, testY = create_dataset(test,look_back)
trainX = np.reshape(trainX,(trainX.shape[0],1,trainX.shape[1]))
testX = np.reshape(testX,(testX.shape[0],1,testX.shape[1]))

model= Sequential()
model.add(LSTM(4,input_shape=(1,look_back)))
model.add(Dense(1))
model.compile(loss='mean_squared_error',optimizer="adam")
model.fit(trainX,trainY,epochs=100,batch_size=1,verbose=2)

trainPredict = model.predict(trainX)
testPredict=model.predict(testX)

trainPredict = scaler.inverse_transform(trainPredict)
trainY = scaler.inverse_transform([trainY])
testPredict = scaler.inverse_transform(testPredict)
testY=scaler.inverse_transform([testY])

#calculate root mean squared error
lst.append(math.sqrt(mean_squared_error(trainY[0],trainPredict[:,0])))
lst.append(math.sqrt(mean_squared_error(testY[0],testPredict[:,0])))

accuracy=accuracy.append(Series(lst,index=accuracy.columns),ignore_index=True)

trainPredictPlot = np.empty_like(dataset)
trainPredictPlot[:, :] = np.nan
trainPredictPlot[look_back:len(trainPredict)+look_back, :] = trainPredict
testPredictPlot = np.empty_like(dataset)
testPredictPlot[:, :] = np.nan
testPredictPlot[len(trainPredict)+(look_back*2)+1:len(dataset)-1, :] = testPredict

plt.figure(figsize=(8,6))
plt.plot(scaler.inverse_transform(dataset),color="gray",label="real data")
plt.plot(trainPredictPlot,color="blue",label="train predict",linestyle="-.")
plt.plot(testPredictPlot,color="red",label="test predict",linestyle="-.")
plt.legend(loc="lower right")
plt.title("온라인 보건위생 LSTM")
plt.show()

accuracy.to_csv("C:/data/LSTM_acc.csv",index=False)