import glob
from pandas import *
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
import sklearn.metrics as metrics
import numpy as np

#classifier= KNeighborsClassifier(n_neighbors=10)
classifier= KNeighborsClassifier(n_neighbors=5)
accuracy=pd.DataFrame(columns=['name','train_acc','train_f1','test_acc','test_f1'])

file="/users/solhee/bigcondata1/off_acco*.csv"
#off_acco(train).csv
off_acco_lst=['off_acco']
off_acco_train=pd.read_csv(glob.glob(file)[0])
training_points=off_acco_train[['PN','COVID']]
training_labels=off_acco_train['CN']
classifier.fit(training_points,training_labels)
y=training_labels
p=classifier.predict(training_points)
#classifier.score(training_points,training_labels)
#confusion_matrix(classifier.predict(training_points),training_labels)
#n_neighbors=10일때
#y=training_labels
#p=classifier.predict(training_points)
#metrics.accuracy_score(y,p)#0.54292343387471
#metrics.f1_score(y,p)#0.6716666666666666

#n_neighbors=5일때
off_acco_lst.append(metrics.accuracy_score(y,p))#0.54292343387471
off_acco_lst.append(metrics.f1_score(y,p))#0.690251572327044

#off_acco(test).csv
off_acco_test=pd.read_csv(glob.glob(file)[1])
test_points=off_acco_test[['PN','COVID']]
test_labels=off_acco_test['CN']
y=test_labels
p=classifier.predict(test_points)
off_acco_lst.append(metrics.accuracy_score(y,p))#0.52 (k =5) (k=10)
off_acco_lst.append(metrics.f1_score(y,p)) #0.6722090261282659 (k=5)(k=10)
accuracy=accuracy.append(Series(off_acco_lst,index=accuracy.columns),ignore_index=True)
#k=5채택

file="/users/solhee/bigcondata1/off_cul*"
#off_cul(train).csv
off_cul_lst=['off_cul']
off_cul_train=pd.read_csv(glob.glob(file)[1])
training_points=off_cul_train[['PN','COVID']]
training_labels=off_cul_train['CN']
classifier.fit(training_points,training_labels)
y=training_labels
p=classifier.predict(training_points)
off_cul_lst.append(metrics.accuracy_score(y,p))
off_cul_lst.append(metrics.f1_score(y,p))
#off_cul(test).csv
off_cul_test=pd.read_csv(glob.glob(file)[0])
test_points=off_cul_test[['PN','COVID']]
test_labels=off_cul_test['CN']
y=test_labels
p=classifier.predict(test_points)
off_cul_lst.append(metrics.accuracy_score(y,p))#0.52 (k =5) (k=10)
off_cul_lst.append(metrics.f1_score(y,p))
accuracy=accuracy.append(Series(off_cul_lst,index=accuracy.columns),ignore_index=True)

file="/users/solhee/bigcondata1/off_food*"
#off_food(train).csv
off_food_train=pd.read_csv(glob.glob(file)[0])
off_food_lst=['off_food']
training_points=off_food_train[['PN','COVID']]
training_labels=off_food_train['CN']
classifier.fit(training_points,training_labels)
y=training_labels
p=classifier.predict(training_points)
off_food_lst.append(metrics.accuracy_score(y,p))
off_food_lst.append(metrics.f1_score(y,p))

#off_food(test).csv
off_food_test=pd.read_csv(glob.glob(file)[1])
test_points=off_food_test[['PN','COVID']]
test_labels=off_food_test['CN']
y=test_labels
p=classifier.predict(test_points)
off_food_lst.append(metrics.accuracy_score(y,p))
off_food_lst.append(metrics.f1_score(y,p))
accuracy=accuracy.append(Series(off_food_lst,index=accuracy.columns),ignore_index=True)

file="/users/solhee/bigcondata1/off_lei*"
#off_lei(train).csv
off_lei_train=pd.read_csv(glob.glob(file)[1])
off_lei_lst=['off_lei']
training_points=off_lei_train[['PN','COVID']]
training_labels=off_lei_train['CN']
classifier.fit(training_points,training_labels)
y=training_labels
p=classifier.predict(training_points)
off_lei_lst.append(metrics.accuracy_score(y,p))
off_lei_lst.append(metrics.f1_score(y,p))

#off_lei(test).csv
off_lei_test=pd.read_csv(glob.glob(file)[0])
test_points=off_lei_test[['PN','COVID']]
test_labels=off_lei_test['CN']
y=test_labels
p=classifier.predict(test_points)
off_lei_lst.append(metrics.accuracy_score(y,p))
off_lei_lst.append(metrics.f1_score(y,p))
accuracy=accuracy.append(Series(off_lei_lst,index=accuracy.columns),ignore_index=True)

file="/users/solhee/bigcondata1/off_medi*"
#off_medi(train).csv
off_medi_train=pd.read_csv(glob.glob(file)[0])
off_medi_lst=['off_medi']
training_points=off_medi_train[['PN','COVID']]
training_labels=off_medi_train['CN']
classifier.fit(training_points,training_labels)
y=training_labels
p=classifier.predict(training_points)
off_medi_lst.append(metrics.accuracy_score(y,p))
off_medi_lst.append(metrics.f1_score(y,p))

#off_medi(test).csv
off_medi_test=pd.read_csv(glob.glob(file)[1])
test_points=off_medi_test[['PN','COVID']]
test_labels=off_medi_test['CN']
y=test_labels
p=classifier.predict(test_points)
off_medi_lst.append(metrics.accuracy_score(y,p))
off_medi_lst.append(metrics.f1_score(y,p))
accuracy=accuracy.append(Series(off_medi_lst,index=accuracy.columns),ignore_index=True)

file="/users/solhee/bigcondata1/off_sani*"
#off_sani(train).csv
off_sani_train=pd.read_csv(glob.glob(file)[0])
off_sani_lst=['off_sani']
training_points=off_sani_train[['PN','COVID']]
training_labels=off_sani_train['CN']
classifier.fit(training_points,training_labels)
y=training_labels
p=classifier.predict(training_points)
off_sani_lst.append(metrics.accuracy_score(y,p))
off_sani_lst.append(metrics.f1_score(y,p))

#off_sani(test).csv
off_sani_test=pd.read_csv(glob.glob(file)[1])
test_points=off_sani_test[['PN','COVID']]
test_labels=off_sani_test['CN']
y=test_labels
p=classifier.predict(test_points)
off_sani_lst.append(metrics.accuracy_score(y,p))
off_sani_lst.append(metrics.f1_score(y,p))
accuracy=accuracy.append(Series(off_sani_lst,index=accuracy.columns),ignore_index=True)

file="/users/solhee/bigcondata1/on_acco*"
#on_acco(train).csv
on_acco_train=pd.read_csv(glob.glob(file)[1])
on_acco_lst=['on_acco']
training_points=on_acco_train[['PN','COVID']]
training_labels=on_acco_train['CN']
classifier.fit(training_points,training_labels)
y=training_labels
p=classifier.predict(training_points)
on_acco_lst.append(metrics.accuracy_score(y,p))
on_acco_lst.append(metrics.f1_score(y,p))

#on_acco(test).csv
on_acco_test=pd.read_csv(glob.glob(file)[0])
test_points=on_acco_test[['PN','COVID']]
test_labels=on_acco_test['CN']
y=test_labels
p=classifier.predict(test_points)
on_acco_lst.append(metrics.accuracy_score(y,p))
on_acco_lst.append(metrics.f1_score(y,p))
accuracy=accuracy.append(Series(on_acco_lst,index=accuracy.columns),ignore_index=True)

file="/users/solhee/bigcondata1/on_cul*"
#on_cul(train).csv
on_cul_train=pd.read_csv(glob.glob(file)[0])
on_cul_lst=['on_cul']
training_points=on_cul_train[['PN','COVID']]
training_labels=on_cul_train['CN']
classifier.fit(training_points,training_labels)
y=training_labels
p=classifier.predict(training_points)
on_cul_lst.append(metrics.accuracy_score(y,p))
on_cul_lst.append(metrics.f1_score(y,p))

#on_cul(test).csv
on_cul_test=pd.read_csv(glob.glob(file)[1])
test_points=on_cul_test[['PN','COVID']]
test_labels=on_cul_test['CN']
y=test_labels
p=classifier.predict(test_points)
on_cul_lst.append(metrics.accuracy_score(y,p))
on_cul_lst.append(metrics.f1_score(y,p))
accuracy=accuracy.append(Series(on_cul_lst,index=accuracy.columns),ignore_index=True)

file="/users/solhee/bigcondata1/on_food*"
#on_food(train).csv
on_food_train=pd.read_csv(glob.glob(file)[1])
on_food_lst=['on_food']
training_points=on_food_train[['PN','COVID']]
training_labels=on_food_train['CN']
classifier.fit(training_points,training_labels)
y=training_labels
p=classifier.predict(training_points)
on_food_lst.append(metrics.accuracy_score(y,p))
on_food_lst.append(metrics.f1_score(y,p))

#on_food(test).csv
on_food_test=pd.read_csv(glob.glob(file)[0])
test_points=on_food_test[['PN','COVID']]
test_labels=on_food_test['CN']
y=test_labels
p=classifier.predict(test_points)
on_food_lst.append(metrics.accuracy_score(y,p))
on_food_lst.append(metrics.f1_score(y,p))
accuracy=accuracy.append(Series(on_food_lst,index=accuracy.columns),ignore_index=True)

file="/users/solhee/bigcondata1/on_lei*"
#on_lei(train).csv
on_lei_train=pd.read_csv(glob.glob(file)[0])
on_lei_lst=['on_lei']
training_points=on_lei_train[['PN','COVID']]
training_labels=on_lei_train['CN']
classifier.fit(training_points,training_labels)
y=training_labels
p=classifier.predict(training_points)
on_lei_lst.append(metrics.accuracy_score(y,p))
on_lei_lst.append(metrics.f1_score(y,p))

#on_lei(test).csv
on_lei_test=pd.read_csv(glob.glob(file)[1])
test_points=on_lei_test[['PN','COVID']]
test_labels=on_lei_test['CN']
y=test_labels
p=classifier.predict(test_points)
on_lei_lst.append(metrics.accuracy_score(y,p))
on_lei_lst.append(metrics.f1_score(y,p))
accuracy=accuracy.append(Series(on_lei_lst,index=accuracy.columns),ignore_index=True)

file="/users/solhee/bigcondata1/on_sani*"
#on_sani(train).csv
on_sani_train=pd.read_csv(glob.glob(file)[1])
on_sani_lst=['on_sani']
training_points=on_sani_train[['PN','COVID']]
training_labels=on_sani_train['CN']
classifier.fit(training_points,training_labels)
y=training_labels
p=classifier.predict(training_points)
on_sani_lst.append(metrics.accuracy_score(y,p))
on_sani_lst.append(metrics.f1_score(y,p))

#on_sani(test).csv
on_sani_test=pd.read_csv(glob.glob(file)[0])
test_points=on_sani_test[['PN','COVID']]
test_labels=on_sani_test['CN']
y=test_labels
p=classifier.predict(test_points)
on_sani_lst.append(metrics.accuracy_score(y,p))
on_sani_lst.append(metrics.f1_score(y,p))
accuracy=accuracy.append(Series(on_sani_lst,index=accuracy.columns),ignore_index=True)

#accuracy.to_csv("/users/solhee/bigcondata1/KNN_accuracy.csv",index=False)