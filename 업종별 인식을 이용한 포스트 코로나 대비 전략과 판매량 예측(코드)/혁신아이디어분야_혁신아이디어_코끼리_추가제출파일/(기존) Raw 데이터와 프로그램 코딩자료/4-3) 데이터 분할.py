# 4-3) 데이터 분할

z = pd.read_csv("c:/big/corona/g/off_acc1.csv",)
s = pd.read_csv("c:/big/corona/g/off_cul1.csv")
d = pd.read_csv("c:/big/corona/g/off_food2.csv")
f = pd.read_csv("c:/big/corona/g/off_lei1.csv")
g = pd.read_csv("c:/big/corona/g/off_medi1.csv")
h = pd.read_csv("c:/big/corona/g/off_sani1.csv")
q = pd.read_csv("c:/big/corona/g/on_acc1.csv")
w = pd.read_csv("c:/big/corona/g/on_cul1.csv")
e = pd.read_csv("c:/big/corona/g/on_food1.csv")
r = pd.read_csv("c:/big/corona/g/on_lei1.csv")
t = pd.read_csv("c:/big/corona/g/on_sani1.csv")

# off_acc 데이터 분할
z[:int(len(z)*0.6)].to_csv("c:/big/corona/off_acci(train).csv", mode='w', index=False, encoding='utf-8')
train_data = pd.read_csv('c:/big/corona/off_acci(train).csv')
z[int(len(z)*0.6):].to_csv("C:/big/corona/off_acci(test).csv", mode='w', index=False, encoding='utf-8')   
test_data = pd.read_csv('c:/big/corona/off_acci(test).csv')

# off_cul 데이터 분할
s[:int(len(s)*0.6)].to_csv("c:/big/corona/off_cul(train).csv", mode='w', index=False, encoding='utf-8')
train_data = pd.read_csv('c:/big/corona/off_cul(train).csv')
s[int(len(s)*0.6):].to_csv("C:/big/corona/off_cul(test).csv", mode='w', index=False, encoding='utf-8')   
test_data = pd.read_csv('c:/big/corona/off_cul(test).csv')

# off_food 데이터 분할
d[:int(len(d)*0.6)].to_csv("c:/big/corona/off_food(train).csv", mode='w', index=False, encoding='utf-8')
train_data = pd.read_csv('c:/big/corona/off_food(train).csv')
d[int(len(d)*0.6):].to_csv("C:/big/corona/off_food(test).csv", mode='w', index=False, encoding='utf-8')   
test_data = pd.read_csv('c:/big/corona/off_food(test).csv')

# off_lei 데이터 분할
f[:int(len(f)*0.6)].to_csv("c:/big/corona/off_lei(train).csv", mode='w', index=False, encoding='utf-8')
train_data = pd.read_csv('c:/big/corona/off_lei(train).csv')
f[int(len(f)*0.6):].to_csv("C:/big/corona/off_lei(test).csv", mode='w', index=False, encoding='utf-8')   
test_data = pd.read_csv('c:/big/corona/off_lei(test).csv')

# off_medi 데이터 분할
g[:int(len(g)*0.6)].to_csv("c:/big/corona/off_medi(train).csv", mode='w', index=False, encoding='utf-8')
train_data = pd.read_csv('c:/big/corona/off_medi(train).csv')
g[int(len(g)*0.6):].to_csv("C:/big/corona/off_medi(test).csv", mode='w', index=False, encoding='utf-8')   
test_data = pd.read_csv('c:/big/corona/off_medi(test).csv')

# off_sani 데이터 분할
h[:int(len(h)*0.6)].to_csv("c:/big/corona/off_sani(train).csv", mode='w', index=False, encoding='utf-8')
train_data = pd.read_csv('c:/big/corona/off_sani(train).csv')
h[int(len(h)*0.6):].to_csv("C:/big/corona/off_sani(test).csv", mode='w', index=False, encoding='utf-8')   
test_data = pd.read_csv('c:/big/corona/off_sani(test).csv')

# on_acc 데이터 분할
q[:int(len(q)*0.6)].to_csv("c:/big/corona/on_acc(train).csv", mode='w', index=False, encoding='utf-8')
train_data = pd.read_csv('c:/big/corona/on_acc(train).csv')
q[int(len(q)*0.6):].to_csv("C:/big/corona/on_acc(test).csv", mode='w', index=False, encoding='utf-8')   
test_data = pd.read_csv('c:/big/corona/on_acc(test).csv')

# on_cul 데이터 분할
w[:int(len(w)*0.6)].to_csv("c:/big/corona/on_cul(train).csv", mode='w', index=False, encoding='utf-8')
train_data = pd.read_csv('c:/big/corona/on_cul(train).csv')
w[int(len(w)*0.6):].to_csv("C:/big/corona/on_cul(test).csv", mode='w', index=False, encoding='utf-8')   
test_data = pd.read_csv('c:/big/corona/on_cul(test).csv')

# on_food 데이터 분할
e[:int(len(e)*0.6)].to_csv("c:/big/corona/on_food(train).csv", mode='w', index=False, encoding='utf-8')
train_data = pd.read_csv('c:/big/corona/on_food(train).csv')
e[int(len(e)*0.6):].to_csv("C:/big/corona/on_food(test).csv", mode='w', index=False, encoding='utf-8')   
test_data = pd.read_csv('c:/big/corona/on_food(test).csv')

# on_lei 데이터 분할
r[:int(len(r)*0.6)].to_csv("c:/big/corona/on_lei(train).csv", mode='w', index=False, encoding='utf-8')
train_data = pd.read_csv('c:/big/corona/on_lei(train).csv')
r[int(len(r)*0.6):].to_csv("C:/big/corona/on_lei(test).csv", mode='w', index=False, encoding='utf-8')   
test_data = pd.read_csv('c:/big/corona/on_lei(test).csv')


# on_sani 데이터 분할
t[:int(len(t)*0.6)].to_csv("c:/big/corona/on_sani(train).csv", mode='w', index=False, encoding='utf-8')
train_data = pd.read_csv('c:/big/corona/on_sani(train).csv')
t[int(len(t)*0.6):].to_csv("C:/big/corona/on_sani(test).csv", mode='w', index=False, encoding='utf-8')   
test_data = pd.read_csv('c:/big/corona/on_sani(test).csv')