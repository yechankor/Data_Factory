# 7-1) Ridge Lasso Regression

from sklearn.linear_model import Ridge, RidgeCV, Lasso, LassoCV, ElasticNet,ElasticNetCV
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# 오프라인 숙박================================================================
data=pd.read_csv("C:/data/off_acc1.csv", encoding='utf-8')
data=data.sample(frac=1).reset_index(drop=True)
train=data[:int(len(data)*0.6)]
test=data[int(len(data)*0.6):]

X_train = train[['PN','COVID']]
y_train = train['CN']
X_test = test[['PN','COVID']]
y_test = test['CN']

# Ridge
ridge = Ridge()
ridge.fit(X_train, y_train)

# Lasso
lasso = Lasso()
lasso.fit(X_train, y_train)

# Ridge 정확도
r_off_acc_train_score = ridge.score(X_train, y_train)
r_off_acc_test_score = ridge.score(X_test, y_test)
display('Ridge', r_off_acc_train_score, r_off_acc_test_score)

# Lasso 정확도
l_off_acc_train_score = lasso.score(X_train, y_train)
l_off_acc_test_score = lasso.score(X_test, y_test)
display('Lasso', l_off_acc_train_score, l_off_acc_test_score)

alphas = [10, 1, 0.1, 0.01, 0.001, 0.0001]
train_scores = []
test_scores = []
ws = []

for alpha in alphas:
    lasso = Lasso(alpha=alpha)
    lasso.fit(X_train, y_train)
    ws.append(lasso.coef_)
    
    s1 = lasso.score(X_train, y_train)
    s2 = lasso.score(X_test, y_test)
    train_scores.append(s1)
    test_scores.append(s2)
    
display(train_scores, test_scores, ws)


# lasso
# run Lasso cross validation test to find the best alpha based on training data
lasso_cv=LassoCV(alphas=alphas, cv=5)
model = lasso_cv.fit(X_train, y_train)
print(model.alpha_)

# calculate Lasso R2, MSE, RMSE from test data
lasso=Lasso(alpha=10).fit(X_train, y_train)
ypred_lasso = lasso.predict(X_test)
l_off_acc_score_lasso = lasso.score(X_test, y_test)
l_off_acc_mse_lasso = mean_squared_error(y_test, ypred_lasso)
print("Final Result: Lasso R2:{0:.3f}, MSE:{1:.2f}, RMSE:{2:.2f}".format(l_off_acc_score_lasso, l_off_acc_mse_lasso, np.sqrt(l_off_acc_mse_lasso)))

# ridge
# run Ridge cross validation test to find the best alpha based on training data
ridge_cv=RidgeCV(alphas=alphas, cv=5)
model = ridge_cv.fit(X_train, y_train)
print(model.alpha_)

# calculate Ridge R2, MSE, RMSE from test data
ridge=Ridge(alpha=0.0001).fit(X_train, y_train)
ypred_ridge = ridge.predict(X_test)
r_off_acc_score_ridge = ridge.score(X_test, y_test)
r_off_acc_mse_ridge = mean_squared_error(y_test, ypred_ridge)
print("Final Result: Ridge R2:{0:.3f}, MSE:{1:.2f}, RMSE:{2:.2f}".format(r_off_acc_score_ridge, r_off_acc_mse_ridge, np.sqrt(r_off_acc_mse_ridge)))


# 오프라인 문화================================================================
data=pd.read_csv("C:/data/off_cul1.csv", encoding='utf-8')
data=data.sample(frac=1).reset_index(drop=True)
train=data[:int(len(data)*0.6)]
test=data[int(len(data)*0.6):]

X_train = train[['PN','COVID']]
y_train = train['CN']
X_test = test[['PN','COVID']]
y_test = test['CN']

# Ridge
ridge = Ridge()
ridge.fit(X_train, y_train)

# Lasso
lasso = Lasso()
lasso.fit(X_train, y_train)

# Ridge 정확도
r_off_cul_train_score = ridge.score(X_train, y_train)
r_off_cul_test_score = ridge.score(X_test, y_test)
display('Ridge', r_off_cul_train_score, r_off_cul_test_score)

# Lasso 정확도
l_off_cul_train_score = lasso.score(X_train, y_train)
l_off_cul_test_score = lasso.score(X_test, y_test)
display('Lasso', l_off_cul_train_score, l_off_cul_test_score)

alphas = [10, 1, 0.1, 0.01, 0.001, 0.0001]
train_scores = []
test_scores = []
ws = []

for alpha in alphas:
    lasso = Lasso(alpha=alpha)
    lasso.fit(X_train, y_train)
    ws.append(lasso.coef_)
    
    s1 = lasso.score(X_train, y_train)
    s2 = lasso.score(X_test, y_test)
    train_scores.append(s1)
    test_scores.append(s2)
    
display(train_scores, test_scores, ws)

# lasso
# run Lasso cross validation test to find the best alpha based on training data
lasso_cv=LassoCV(alphas=alphas, cv=5)
model = lasso_cv.fit(X_train, y_train)
print(model.alpha_)

# calculate Lasso R2, MSE, RMSE from test data
lasso=Lasso(alpha=0.0001).fit(X_train, y_train)
ypred_lasso = lasso.predict(X_test)
l_off_cul_score_lasso = lasso.score(X_test, y_test)
l_off_cul_mse_lasso = mean_squared_error(y_test, ypred_lasso)
print("Final Result: Lasso R2:{0:.3f}, MSE:{1:.2f}, RMSE:{2:.2f}".format(l_off_cul_score_lasso, l_off_cul_mse_lasso, np.sqrt(l_off_cul_mse_lasso)))

# ridge
# run Ridge cross validation test to find the best alpha based on training data
ridge_cv=RidgeCV(alphas=alphas, cv=5)
model = ridge_cv.fit(X_train, y_train)
print(model.alpha_)

# calculate Ridge R2, MSE, RMSE from test data
ridge=Ridge(alpha=0.0001).fit(X_train, y_train)
ypred_ridge = ridge.predict(X_test)
r_off_cul_score_ridge = ridge.score(X_test, y_test)
r_off_cul_mse_ridge = mean_squared_error(y_test, ypred_ridge)
print("Final Result: Ridge R2:{0:.3f}, MSE:{1:.2f}, RMSE:{2:.2f}".format(r_off_cul_score_ridge, r_off_cul_mse_ridge, np.sqrt(r_off_cul_mse_ridge)))


# 오프라인 식품================================================================
data=pd.read_csv("C:/data/off_food2.csv", encoding='utf-8')
data=data.sample(frac=1).reset_index(drop=True)
train=data[:int(len(data)*0.6)]
test=data[int(len(data)*0.6):]

X_train = train[['PN','COVID']]
y_train = train['CN']
X_test = test[['PN','COVID']]
y_test = test['CN']

# Ridge
ridge = Ridge()
ridge.fit(X_train, y_train)

# Lasso
lasso = Lasso()
lasso.fit(X_train, y_train)

# Ridge 정확도
r_off_food_train_score = ridge.score(X_train, y_train)
r_off_food_test_score = ridge.score(X_test, y_test)
display('Ridge', r_off_food_train_score, r_off_food_test_score)

# Lasso 정확도
l_off_food_train_score = lasso.score(X_train, y_train)
l_off_food_test_score = lasso.score(X_test, y_test)
display('Lasso', l_off_food_train_score, l_off_food_test_score)

alphas = [10, 1, 0.1, 0.01, 0.001, 0.0001]
train_scores = []
test_scores = []
ws = []

for alpha in alphas:
    lasso = Lasso(alpha=alpha)
    lasso.fit(X_train, y_train)
    ws.append(lasso.coef_)
    
    s1 = lasso.score(X_train, y_train)
    s2 = lasso.score(X_test, y_test)
    train_scores.append(s1)
    test_scores.append(s2)
    
display(train_scores, test_scores, ws)


# lasso
# run Lasso cross validation test to find the best alpha based on training data
lasso_cv=LassoCV(alphas=alphas, cv=5)
model = lasso_cv.fit(X_train, y_train)
print(model.alpha_)

# calculate Lasso R2, MSE, RMSE from test data
lasso=Lasso(alpha=0.0001).fit(X_train, y_train)
ypred_lasso = lasso.predict(X_test)
l_off_food_score_lasso = lasso.score(X_test, y_test)
l_off_food_mse_lasso = mean_squared_error(y_test, ypred_lasso)
print("Final Result: Lasso R2:{0:.3f}, MSE:{1:.2f}, RMSE:{2:.2f}".format(l_off_food_score_lasso, l_off_food_mse_lasso, np.sqrt(l_off_food_mse_lasso)))

# ridge
# run Ridge cross validation test to find the best alpha based on training data
ridge_cv=RidgeCV(alphas=alphas, cv=5)
model = ridge_cv.fit(X_train, y_train)
print(model.alpha_)

# calculate Ridge R2, MSE, RMSE from test data
ridge=Ridge(alpha=0.1).fit(X_train, y_train)
ypred_ridge = ridge.predict(X_test)
r_off_food_score_ridge = ridge.score(X_test, y_test)
r_off_food_mse_ridge = mean_squared_error(y_test, ypred_ridge)
print("Final Result: Ridge R2:{0:.3f}, MSE:{1:.2f}, RMSE:{2:.2f}".format(r_off_food_score_ridge, r_off_food_mse_ridge, np.sqrt(r_off_food_mse_ridge)))


# 오프라인 레저================================================================
data=pd.read_csv("C:/data/off_lei1.csv", encoding='utf-8')
data=data.sample(frac=1).reset_index(drop=True)
train=data[:int(len(data)*0.6)]
test=data[int(len(data)*0.6):]

X_train = train[['PN','COVID']]
y_train = train['CN']
X_test = test[['PN','COVID']]
y_test = test['CN']

# Ridge
ridge = Ridge()
ridge.fit(X_train, y_train)

# Lasso
lasso = Lasso()
lasso.fit(X_train, y_train)

# Ridge 정확도
r_off_lei_train_score = ridge.score(X_train, y_train)
r_off_lei_test_score = ridge.score(X_test, y_test)
display('Ridge', r_off_lei_train_score, r_off_lei_test_score)

# Lasso 정확도
l_off_lei_train_score = lasso.score(X_train, y_train)
l_off_lei_test_score = lasso.score(X_test, y_test)
display('Lasso', l_off_lei_train_score, l_off_lei_test_score)

alphas = [10, 1, 0.1, 0.01, 0.001, 0.0001]
train_scores = []
test_scores = []
ws = []

for alpha in alphas:
    lasso = Lasso(alpha=alpha)
    lasso.fit(X_train, y_train)
    ws.append(lasso.coef_)
    
    s1 = lasso.score(X_train, y_train)
    s2 = lasso.score(X_test, y_test)
    train_scores.append(s1)
    test_scores.append(s2)
    
display(train_scores, test_scores, ws)

# lasso
# run Lasso cross validation test to find the best alpha based on training data
lasso_cv=LassoCV(alphas=alphas, cv=5)
model = lasso_cv.fit(X_train, y_train)
print(model.alpha_)

# calculate Lasso R2, MSE, RMSE from test data
lasso=Lasso(alpha=10).fit(X_train, y_train)
ypred_lasso = lasso.predict(X_test)
l_off_lei_score_lasso = lasso.score(X_test, y_test)
l_off_lei_mse_lasso = mean_squared_error(y_test, ypred_lasso)
print("Final Result: Lasso R2:{0:.3f}, MSE:{1:.2f}, RMSE:{2:.2f}".format(l_off_lei_score_lasso, l_off_lei_mse_lasso, np.sqrt(l_off_lei_mse_lasso)))

# ridge
# run Ridge cross validation test to find the best alpha based on training data
ridge_cv=RidgeCV(alphas=alphas, cv=5)
model = ridge_cv.fit(X_train, y_train)
print(model.alpha_)

# calculate Ridge R2, MSE, RMSE from test data
ridge=Ridge(alpha=10).fit(X_train, y_train)
ypred_ridge = ridge.predict(X_test)
r_off_lei_score_ridge = ridge.score(X_test, y_test)
r_off_lei_mse_ridge = mean_squared_error(y_test, ypred_ridge)
print("Final Result: Ridge R2:{0:.3f}, MSE:{1:.2f}, RMSE:{2:.2f}".format(r_off_lei_score_ridge, r_off_lei_mse_ridge, np.sqrt(r_off_lei_mse_ridge)))


# 오프라인 의료기관================================================================
data=pd.read_csv("C:/data/off_medi1.csv", encoding='utf-8')
data=data.sample(frac=1).reset_index(drop=True)
train=data[:int(len(data)*0.6)]
test=data[int(len(data)*0.6):]

X_train = train[['PN','COVID']]
y_train = train['CN']
X_test = test[['PN','COVID']]
y_test = test['CN']

# Ridge
ridge = Ridge()
ridge.fit(X_train, y_train)

# Lasso
lasso = Lasso()
lasso.fit(X_train, y_train)

# Ridge 정확도
r_off_medi_train_score = ridge.score(X_train, y_train)
r_off_medi_test_score = ridge.score(X_test, y_test)
display('Ridge', r_off_medi_train_score, r_off_medi_test_score)

# Lasso 정확도
l_off_medi_train_score = lasso.score(X_train, y_train)
l_off_medi_test_score = lasso.score(X_test, y_test)
display('Lasso', l_off_medi_train_score, l_off_medi_test_score)

alphas = [10, 1, 0.1, 0.01, 0.001, 0.0001]
train_scores = []
test_scores = []
ws = []

for alpha in alphas:
    lasso = Lasso(alpha=alpha)
    lasso.fit(X_train, y_train)
    ws.append(lasso.coef_)
    
    s1 = lasso.score(X_train, y_train)
    s2 = lasso.score(X_test, y_test)
    train_scores.append(s1)
    test_scores.append(s2)
    
display(train_scores, test_scores, ws)


# lasso
# run Lasso cross validation test to find the best alpha based on training data
lasso_cv=LassoCV(alphas=alphas, cv=5)
model = lasso_cv.fit(X_train, y_train)
print(model.alpha_)

# calculate Lasso R2, MSE, RMSE from test data
lasso=Lasso(alpha=10).fit(X_train, y_train)
ypred_lasso = lasso.predict(X_test)
l_off_medi_score_lasso = lasso.score(X_test, y_test)
l_off_medi_mse_lasso = mean_squared_error(y_test, ypred_lasso)
print("Final Result: Lasso R2:{0:.3f}, MSE:{1:.2f}, RMSE:{2:.2f}".format(l_off_medi_score_lasso, l_off_medi_mse_lasso, np.sqrt(l_off_medi_mse_lasso)))


# ridge
# run Ridge cross validation test to find the best alpha based on training data
ridge_cv=RidgeCV(alphas=alphas, cv=5)
model = ridge_cv.fit(X_train, y_train)
print(model.alpha_)

# calculate Ridge R2, MSE, RMSE from test data
ridge=Ridge(alpha=0.0001).fit(X_train, y_train)
ypred_ridge = ridge.predict(X_test)
r_off_medi_score_ridge = ridge.score(X_test, y_test)
r_off_medi_mse_ridge = mean_squared_error(y_test, ypred_ridge)
print("Final Result: Ridge R2:{0:.3f}, MSE:{1:.2f}, RMSE:{2:.2f}".format(r_off_medi_score_ridge, r_off_medi_mse_ridge, np.sqrt(r_off_medi_mse_ridge)))


# 오프라인 보건위생================================================================
data=pd.read_csv("C:/data/off_sani1.csv", encoding='utf-8')
data=data.sample(frac=1).reset_index(drop=True)
train=data[:int(len(data)*0.6)]
test=data[int(len(data)*0.6):]

X_train = train[['PN','COVID']]
y_train = train['CN']
X_test = test[['PN','COVID']]
y_test = test['CN']

# Ridge
ridge = Ridge()
ridge.fit(X_train, y_train)

# Lasso
lasso = Lasso()
lasso.fit(X_train, y_train)

# Ridge 정확도
r_off_sani_train_score = ridge.score(X_train, y_train)
r_off_sani_test_score = ridge.score(X_test, y_test)
display('Ridge', r_off_sani_train_score, r_off_sani_test_score)

# Lasso 정확도
l_off_sani_train_score = lasso.score(X_train, y_train)
l_off_sani_test_score = lasso.score(X_test, y_test)
display('Lasso', l_off_sani_train_score, l_off_sani_test_score)

alphas = [10, 1, 0.1, 0.01, 0.001, 0.0001]
train_scores = []
test_scores = []
ws = []

for alpha in alphas:
    lasso = Lasso(alpha=alpha)
    lasso.fit(X_train, y_train)
    ws.append(lasso.coef_)
    
    s1 = lasso.score(X_train, y_train)
    s2 = lasso.score(X_test, y_test)
    train_scores.append(s1)
    test_scores.append(s2)
    
display(train_scores, test_scores, ws)


# lasso
# run Lasso cross validation test to find the best alpha based on training data
lasso_cv=LassoCV(alphas=alphas, cv=5)
model = lasso_cv.fit(X_train, y_train)
print(model.alpha_)

# calculate Lasso R2, MSE, RMSE from test data
lasso=Lasso(alpha=0.0001).fit(X_train, y_train)
ypred_lasso = lasso.predict(X_test)
l_off_sani_score_lasso = lasso.score(X_test, y_test)
l_off_sani_mse_lasso = mean_squared_error(y_test, ypred_lasso)
print("Final Result: Lasso R2:{0:.3f}, MSE:{1:.2f}, RMSE:{2:.2f}".format(l_off_sani_score_lasso, l_off_sani_mse_lasso, np.sqrt(l_off_sani_mse_lasso)))


# ridge
# run Ridge cross validation test to find the best alpha based on training data
ridge_cv=RidgeCV(alphas=alphas, cv=5)
model = ridge_cv.fit(X_train, y_train)
print(model.alpha_)

# calculate Ridge R2, MSE, RMSE from test data
ridge=Ridge(alpha=0.0001).fit(X_train, y_train)
ypred_ridge = ridge.predict(X_test)
r_off_sani_score_ridge = ridge.score(X_test, y_test)
r_off_sani_mse_ridge = mean_squared_error(y_test, ypred_ridge)
print("Final Result: Ridge R2:{0:.3f}, MSE:{1:.2f}, RMSE:{2:.2f}".format(r_off_sani_score_ridge, r_off_sani_mse_ridge, np.sqrt(r_off_sani_mse_ridge)))


# 온라인 숙박================================================================
data=pd.read_csv("C:/data/on_acc1.csv", encoding='utf-8')
data=data.sample(frac=1).reset_index(drop=True)
train=data[:int(len(data)*0.6)]
test=data[int(len(data)*0.6):]

X_train = train[['PN','COVID']]
y_train = train['CN']
X_test = test[['PN','COVID']]
y_test = test['CN']

# Ridge
ridge = Ridge()
ridge.fit(X_train, y_train)

# Lasso
lasso = Lasso()
lasso.fit(X_train, y_train)

# Ridge 정확도
r_on_acc_train_score = ridge.score(X_train, y_train)
r_on_acc_test_score = ridge.score(X_test, y_test)
display('Ridge', r_on_acc_train_score, r_on_acc_test_score)

# Lasso 정확도
l_on_acc_train_score = lasso.score(X_train, y_train)
l_on_acc_test_score = lasso.score(X_test, y_test)
display('Lasso', l_on_acc_train_score, l_on_acc_test_score)

alphas = [10, 1, 0.1, 0.01, 0.001, 0.0001]
train_scores = []
test_scores = []
ws = []

for alpha in alphas:
    lasso = Lasso(alpha=alpha)
    lasso.fit(X_train, y_train)
    ws.append(lasso.coef_)
    
    s1 = lasso.score(X_train, y_train)
    s2 = lasso.score(X_test, y_test)
    train_scores.append(s1)
    test_scores.append(s2)
    
display(train_scores, test_scores, ws)


# lasso
# run Lasso cross validation test to find the best alpha based on training data
lasso_cv=LassoCV(alphas=alphas, cv=5)
model = lasso_cv.fit(X_train, y_train)
print(model.alpha_)

# calculate Lasso R2, MSE, RMSE from test data
lasso=Lasso(alpha=0.0001).fit(X_train, y_train)
ypred_lasso = lasso.predict(X_test)
l_on_acc_score_lasso = lasso.score(X_test, y_test)
l_on_acc_mse_lasso = mean_squared_error(y_test, ypred_lasso)
print("Final Result: Lasso R2:{0:.3f}, MSE:{1:.2f}, RMSE:{2:.2f}".format(l_on_acc_score_lasso, l_on_acc_mse_lasso, np.sqrt(l_on_acc_mse_lasso)))

# ridge
# run Ridge cross validation test to find the best alpha based on training data
ridge_cv=RidgeCV(alphas=alphas, cv=5)
model = ridge_cv.fit(X_train, y_train)
print(model.alpha_)

# calculate Ridge R2, MSE, RMSE from test data
ridge=Ridge(alpha=10).fit(X_train, y_train)
ypred_ridge = ridge.predict(X_test)
r_on_acc_score_ridge = ridge.score(X_test, y_test)
r_on_acc_mse_ridge = mean_squared_error(y_test, ypred_ridge)
print("Final Result: Ridge R2:{0:.3f}, MSE:{1:.2f}, RMSE:{2:.2f}".format(r_on_acc_score_ridge, r_on_acc_mse_ridge, np.sqrt(r_on_acc_mse_ridge)))


# 온라인 문화취미================================================================
data=pd.read_csv("C:/data/on_cul1.csv", encoding='utf-8')
data=data.sample(frac=1).reset_index(drop=True)
train=data[:int(len(data)*0.6)]
test=data[int(len(data)*0.6):]

X_train = train[['PN','COVID']]
y_train = train['CN']
X_test = test[['PN','COVID']]
y_test = test['CN']

# Ridge
ridge = Ridge()
ridge.fit(X_train, y_train)

# Lasso
lasso = Lasso()
lasso.fit(X_train, y_train)

# Ridge 정확도
r_on_cul_train_score = ridge.score(X_train, y_train)
r_on_cul_test_score = ridge.score(X_test, y_test)
display('Ridge', r_on_cul_train_score, r_on_cul_test_score)

# Lasso 정확도
l_on_cul_train_score = lasso.score(X_train, y_train)
l_on_cul_test_score = lasso.score(X_test, y_test)
display('Lasso', l_on_cul_train_score, l_on_cul_test_score)

alphas = [10, 1, 0.1, 0.01, 0.001, 0.0001]
train_scores = []
test_scores = []
ws = []

for alpha in alphas:
    lasso = Lasso(alpha=alpha)
    lasso.fit(X_train, y_train)
    ws.append(lasso.coef_)
    
    s1 = lasso.score(X_train, y_train)
    s2 = lasso.score(X_test, y_test)
    train_scores.append(s1)
    test_scores.append(s2)
    
display(train_scores, test_scores, ws)


# lasso
# run Lasso cross validation test to find the best alpha based on training data
lasso_cv=LassoCV(alphas=alphas, cv=5)
model = lasso_cv.fit(X_train, y_train)
print(model.alpha_)

# calculate Lasso R2, MSE, RMSE from test data
lasso=Lasso(alpha=0.0001).fit(X_train, y_train)
ypred_lasso = lasso.predict(X_test)
l_on_cul_score_lasso = lasso.score(X_test, y_test)
l_on_cul_mse_lasso = mean_squared_error(y_test, ypred_lasso)
print("Final Result: Lasso R2:{0:.3f}, MSE:{1:.2f}, RMSE:{2:.2f}".format(l_on_cul_score_lasso, l_on_cul_mse_lasso, np.sqrt(l_on_cul_mse_lasso)))


# ridge
# run Ridge cross validation test to find the best alpha based on training data
ridge_cv=RidgeCV(alphas=alphas, cv=5)
model = ridge_cv.fit(X_train, y_train)
print(model.alpha_)

# calculate Ridge R2, MSE, RMSE from test data
ridge=Ridge(alpha=10).fit(X_train, y_train)
ypred_ridge = ridge.predict(X_test)
r_on_cul_score_ridge = ridge.score(X_test, y_test)
r_on_cul_mse_ridge = mean_squared_error(y_test, ypred_ridge)
print("Final Result: Ridge R2:{0:.3f}, MSE:{1:.2f}, RMSE:{2:.2f}".format(r_on_cul_score_ridge, r_on_cul_mse_ridge, np.sqrt(r_on_cul_mse_ridge)))


# 온라인 요식업소================================================================
data=pd.read_csv("C:/data/on_food1.csv", encoding='utf-8')
data=data.sample(frac=1).reset_index(drop=True)
train=data[:int(len(data)*0.6)]
test=data[int(len(data)*0.6):]

X_train = train[['PN','COVID']]
y_train = train['CN']
X_test = test[['PN','COVID']]
y_test = test['CN']

# Ridge
ridge = Ridge()
ridge.fit(X_train, y_train)

# Lasso
lasso = Lasso()
lasso.fit(X_train, y_train)

# Ridge 정확도
r_on_food_train_score = ridge.score(X_train, y_train)
r_on_food_test_score = ridge.score(X_test, y_test)
display('Ridge', r_on_food_train_score, r_on_food_test_score)

# Lasso 정확도
l_on_food_train_score = lasso.score(X_train, y_train)
l_on_food_test_score = lasso.score(X_test, y_test)
display('Lasso', l_on_food_train_score, l_on_food_test_score)

alphas = [10, 1, 0.1, 0.01, 0.001, 0.0001]
train_scores = []
test_scores = []
ws = []

for alpha in alphas:
    lasso = Lasso(alpha=alpha)
    lasso.fit(X_train, y_train)
    ws.append(lasso.coef_)
    
    s1 = lasso.score(X_train, y_train)
    s2 = lasso.score(X_test, y_test)
    train_scores.append(s1)
    test_scores.append(s2)
    
display(train_scores, test_scores, ws)


# lasso
# run Lasso cross validation test to find the best alpha based on training data
lasso_cv=LassoCV(alphas=alphas, cv=5)
model = lasso_cv.fit(X_train, y_train)
print(model.alpha_)

# calculate Lasso R2, MSE, RMSE from test data
lasso=Lasso(alpha=0.0001).fit(X_train, y_train)
ypred_lasso = lasso.predict(X_test)
l_on_food_score_lasso = lasso.score(X_test, y_test)
l_on_food_mse_lasso = mean_squared_error(y_test, ypred_lasso)
print("Final Result: Lasso R2:{0:.3f}, MSE:{1:.2f}, RMSE:{2:.2f}".format(l_on_food_score_lasso, l_on_food_mse_lasso, np.sqrt(l_on_food_mse_lasso)))


# ridge
# run Ridge cross validation test to find the best alpha based on training data
ridge_cv=RidgeCV(alphas=alphas, cv=5)
model = ridge_cv.fit(X_train, y_train)
print(model.alpha_)

# calculate Ridge R2, MSE, RMSE from test data
ridge=Ridge(alpha=0.0001).fit(X_train, y_train)
ypred_ridge = ridge.predict(X_test)
r_on_food_score_ridge = ridge.score(X_test, y_test)
r_on_food_mse_ridge = mean_squared_error(y_test, ypred_ridge)
print("Final Result: Ridge R2:{0:.3f}, MSE:{1:.2f}, RMSE:{2:.2f}".format(r_on_food_score_ridge, r_on_food_mse_ridge, np.sqrt(r_on_food_mse_ridge)))


# 온라인 레저================================================================
data=pd.read_csv("C:/data/on_lei1.csv", encoding='utf-8')
data=data.sample(frac=1).reset_index(drop=True)
train=data[:int(len(data)*0.6)]
test=data[int(len(data)*0.6):]

X_train = train[['PN','COVID']]
y_train = train['CN']
X_test = test[['PN','COVID']]
y_test = test['CN']

# Ridge
ridge = Ridge()
ridge.fit(X_train, y_train)

# Lasso
lasso = Lasso()
lasso.fit(X_train, y_train)

# Ridge 정확도
r_on_lei_train_score = ridge.score(X_train, y_train)
r_on_lei_test_score = ridge.score(X_test, y_test)
display('Ridge', r_on_lei_train_score, r_on_lei_test_score)

# Lasso 정확도
l_on_lei_train_score = lasso.score(X_train, y_train)
l_on_lei_test_score = lasso.score(X_test, y_test)
display('Lasso', l_on_lei_train_score, l_on_lei_test_score)

alphas = [10, 1, 0.1, 0.01, 0.001, 0.0001]
train_scores = []
test_scores = []
ws = []

for alpha in alphas:
    lasso = Lasso(alpha=alpha)
    lasso.fit(X_train, y_train)
    ws.append(lasso.coef_)
    
    s1 = lasso.score(X_train, y_train)
    s2 = lasso.score(X_test, y_test)
    train_scores.append(s1)
    test_scores.append(s2)
    
display(train_scores, test_scores, ws)


# lasso
# run Lasso cross validation test to find the best alpha based on training data
lasso_cv=LassoCV(alphas=alphas, cv=5)
model = lasso_cv.fit(X_train, y_train)
print(model.alpha_)

# calculate Lasso R2, MSE, RMSE from test data
lasso=Lasso(alpha=10).fit(X_train, y_train)
ypred_lasso = lasso.predict(X_test)
l_on_lei_score_lasso = lasso.score(X_test, y_test)
l_on_lei_mse_lasso = mean_squared_error(y_test, ypred_lasso)
print("Final Result: Lasso R2:{0:.3f}, MSE:{1:.2f}, RMSE:{2:.2f}".format(l_on_lei_score_lasso, l_on_lei_mse_lasso, np.sqrt(l_on_lei_mse_lasso)))


# ridge
# run Ridge cross validation test to find the best alpha based on training data
ridge_cv=RidgeCV(alphas=alphas, cv=5)
model = ridge_cv.fit(X_train, y_train)
print(model.alpha_)

# calculate Ridge R2, MSE, RMSE from test data
ridge=Ridge(alpha=10).fit(X_train, y_train)
ypred_ridge = ridge.predict(X_test)
r_on_lei_score_ridge = ridge.score(X_test, y_test)
r_on_lei_mse_ridge = mean_squared_error(y_test, ypred_ridge)
print("Final Result: Ridge R2:{0:.3f}, MSE:{1:.2f}, RMSE:{2:.2f}".format(r_on_lei_score_ridge, r_on_lei_mse_ridge, np.sqrt(r_on_lei_mse_ridge)))


# 온라인 보건위생================================================================
data=pd.read_csv("C:/data/on_sani1.csv", encoding='utf-8')
data=data.sample(frac=1).reset_index(drop=True)
train=data[:int(len(data)*0.6)]
test=data[int(len(data)*0.6):]

X_train = train[['PN','COVID']]
y_train = train['CN']
X_test = test[['PN','COVID']]
y_test = test['CN']

# Ridge
ridge = Ridge()
ridge.fit(X_train, y_train)

# Lasso
lasso = Lasso()
lasso.fit(X_train, y_train)

# Ridge 정확도
r_on_sani_train_score = ridge.score(X_train, y_train)
r_on_sani_test_score = ridge.score(X_test, y_test)
display('Ridge', r_on_sani_train_score, r_on_sani_test_score)

# Lasso 정확도
l_on_sani_train_score = lasso.score(X_train, y_train)
l_on_sani_test_score = lasso.score(X_test, y_test)
display('Lasso', l_on_sani_train_score, l_on_sani_test_score)

alphas = [10, 1, 0.1, 0.01, 0.001, 0.0001]
train_scores = []
test_scores = []
ws = []

for alpha in alphas:
    lasso = Lasso(alpha=alpha)
    lasso.fit(X_train, y_train)
    ws.append(lasso.coef_)
    
    s1 = lasso.score(X_train, y_train)
    s2 = lasso.score(X_test, y_test)
    train_scores.append(s1)
    test_scores.append(s2)
    
display(train_scores, test_scores, ws)


# lasso
# run Lasso cross validation test to find the best alpha based on training data
lasso_cv=LassoCV(alphas=alphas, cv=5)
model = lasso_cv.fit(X_train, y_train)
print(model.alpha_)

# calculate Lasso R2, MSE, RMSE from test data
lasso=Lasso(alpha=0.0001).fit(X_train, y_train)
ypred_lasso = lasso.predict(X_test)
l_on_sani_score_lasso = lasso.score(X_test, y_test)
l_on_sani_mse_lasso = mean_squared_error(y_test, ypred_lasso)
print("Final Result: Lasso R2:{0:.3f}, MSE:{1:.2f}, RMSE:{2:.2f}".format(l_on_sani_score_lasso, l_on_sani_mse_lasso, np.sqrt(l_on_sani_mse_lasso)))




# ridge
# run Ridge cross validation test to find the best alpha based on training data
ridge_cv=RidgeCV(alphas=alphas, cv=5)
model = ridge_cv.fit(X_train, y_train)
print(model.alpha_)

# calculate Ridge R2, MSE, RMSE from test data
ridge=Ridge(alpha=0.0001).fit(X_train, y_train)
ypred_ridge = ridge.predict(X_test)
r_on_sani_score_ridge = ridge.score(X_test, y_test)
r_on_sani_mse_ridge = mean_squared_error(y_test, ypred_ridge)
print("Final Result: Ridge R2:{0:.3f}, MSE:{1:.2f}, RMSE:{2:.2f}".format(r_on_sani_score_ridge, r_on_sani_mse_ridge, np.sqrt(r_on_sani_mse_ridge)))

l_off_acc_train_score
l_off_acc_test_score
r_off_acc_train_score
r_off_acc_test_score

l_off_acc_score_lasso 
l_off_acc_mse_lasso 
np.sqrt(l_off_acc_mse_lasso)
r_off_acc_score_ridge
r_off_acc_mse_ridge 
np.sqrt(r_off_acc_mse_ridge)


df = pd.DataFrame(index=['off_acc','off_cul','off_food','off_lei','off_medi',
                         'off_sano','on_acc', 'on_cul', 'on_food', 'on_lei','on_sani'],
                  data = {'Lasso train모델점수' : [l_off_acc_train_score,l_off_cul_train_score,l_off_food_train_score,
                                          l_off_lei_train_score,l_off_medi_train_score,l_off_sani_train_score,
                                          l_on_acc_train_score,l_on_cul_train_score,l_on_food_train_score,
                                          l_on_lei_train_score,l_on_sani_train_score],
                          'Ridge train모델점수' : [r_off_acc_train_score,r_off_cul_train_score,r_off_food_train_score,
                                          r_off_lei_train_score,r_off_medi_train_score,r_off_sani_train_score,
                                          r_on_acc_train_score,r_on_cul_train_score,r_on_food_train_score,
                                          r_on_lei_train_score,r_on_sani_train_score],
                          'Lasso test모델점수' : [l_off_acc_test_score,l_off_cul_test_score,l_off_food_test_score,
                                          l_off_lei_test_score,l_off_medi_test_score,l_off_sani_test_score,
                                          l_on_acc_test_score,l_on_cul_test_score,l_on_food_test_score,
                                          l_on_lei_test_score,l_on_sani_test_score],
                          'Ridge test모델점수' : [r_off_acc_test_score,r_off_cul_test_score,r_off_food_test_score,
                                          r_off_lei_test_score,r_off_medi_test_score,r_off_sani_test_score,
                                          r_on_acc_test_score,r_on_cul_test_score,r_on_food_test_score,
                                          r_on_lei_test_score,r_on_sani_test_score],
                          'Lasso MSE' : [l_off_acc_mse_lasso,l_off_cul_mse_lasso,l_off_food_mse_lasso,
                                         l_off_lei_mse_lasso,l_off_medi_mse_lasso,l_off_sani_mse_lasso,
                                         l_on_acc_mse_lasso,l_on_cul_mse_lasso,l_on_food_mse_lasso,
                                         l_on_lei_mse_lasso,l_on_sani_mse_lasso],
                          'Ridge MSE' : [r_off_acc_mse_ridge,r_off_cul_mse_ridge,r_off_food_mse_ridge,
                                         r_off_lei_mse_ridge,r_off_medi_mse_ridge,r_off_sani_mse_ridge,
                                         r_on_acc_mse_ridge,r_on_cul_mse_ridge,r_on_food_mse_ridge,
                                         r_on_lei_mse_ridge,r_on_sani_mse_ridge],
                          'Lasso RMSE' : [np.sqrt(l_off_acc_mse_lasso),np.sqrt(l_off_cul_mse_lasso),np.sqrt(l_off_food_mse_lasso),
                                                                               np.sqrt(l_off_lei_mse_lasso),np.sqrt(l_off_medi_mse_lasso),np.sqrt(l_off_sani_mse_lasso),
                                                                               np.sqrt(l_on_acc_mse_lasso),np.sqrt(l_on_cul_mse_lasso),np.sqrt(l_on_food_mse_lasso),
                                                                               np.sqrt(l_on_lei_mse_lasso),np.sqrt(l_on_sani_mse_lasso)],
                          'Ridge RMSE' : [np.sqrt(r_off_acc_mse_ridge),np.sqrt(r_off_cul_mse_ridge),np.sqrt(r_off_food_mse_ridge),
                                                                               np.sqrt(r_off_lei_mse_ridge),np.sqrt(r_off_medi_mse_ridge),np.sqrt(r_off_sani_mse_ridge),
                                                                               np.sqrt(r_on_acc_mse_ridge),np.sqrt(r_on_cul_mse_ridge),np.sqrt(r_on_food_mse_ridge),
                                                                               np.sqrt(r_on_lei_mse_ridge),np.sqrt(r_on_sani_mse_ridge)]})


df

# 파일로 떨어트리기
df.to_csv('c:/data/Ridge_Lasso_MSE.csv',index=True)