import numpy as np
from keras import regularizers
import pandas as pd


modelfile = 'weight.h6'  # 神经网络权重保存
data = pd.read_excel("D:\PyCharm 2018.2.3\\untitled3\mix_ratio\数据清洗.xlsx")  # excel

feature = ['小石用量','大石用量', '石灰石粉用量', '减水剂用量', '细砂用量','中砂用量','粗砂用量','粉煤灰用量',
           '水泥用量', '水用量','膨胀剂用量','矿渣粉用量','混凝土品种', '3d强度']  # 影响因素14个
label = ['28d强度']  # 标签四个，即需要进行预测的值
# data_train = data.loc[range(0,6234)].copy()#标明excel表从第0行到6500行是训练集
# # data_test0= data.loc[range(6234,7755)].copy()
# # # data_test=data_test0.sample(n=217)
# # #
# # test_mean = data_test0.mean()
# # test_std = data_test0.std()
# # # test_min=data_test0.min()
# # # test_max=data_test0.max()
# # data_test1 = (data_test0 - test_mean)/test_std #数据标准化
# # # data_test1=(data_test0-test_min)/(test_max-test_min)
# # x_test = data_test1[feature].as_matrix() #特征数据
# # y_test = data_test1[label].as_matrix() #标签数据
# # # #2 数据预处理和标注
# # data_mean = data_train.mean()
# # data_std = data_train.std()
# # data_train1 = (data_train - data_mean)/data_std #数据标准化
# # # data_min=data_train.min()
# # # data_max=data_train.max()
# # # data_train1=(data_train-data_min)/(data_max-data_min)
# # x_train = data_train1[feature].as_matrix() #特征数据
# # y_train = data_train1[label].as_matrix() #标签数据

# 3 建立一个简单BP神经网络模型
x = data[feature].as_matrix()
y = data[label].as_matrix()

from sklearn.cross_validation import train_test_split
# from sklearn.preprocessing import StandardScaler, MinMaxScaler, scale

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=520)
# ss_x = StandardScaler()
# x_train = ss_x.fit_transform(x_train)
# x_test = ss_x.transform(x_test)
#
# ss_y = StandardScaler()
# y_train = ss_y.fit_transform(y_train)
# y_test = ss_y.transform(y_test)
from keras.models import Sequential
from keras.layers.core import Dense
import keras


model = Sequential()  # 层次模型
model.add(Dense(units=35, input_dim=14, activation='relu'))
keras.layers.BatchNormalization(axis=-1, momentum=0.99, epsilon=0.001, center=True, scale=True, beta_initializer='zeros', gamma_initializer='ones', moving_mean_initializer='zeros', moving_variance_initializer='ones', beta_regularizer=None, gamma_regularizer=None, beta_constraint=None, gamma_constraint=None)
model.add(Dense(units=1, activation='linear'))

# if train:
model.compile(loss='mse', optimizer='adam', metrics=['mae', 'mape'])
print(model.summary())
# plot_model(model, to_file='bpnn_predict_model.png',show_shapes=True)
model.fit(x_train, y_train, epochs=300, batch_size=32)
model.save_weights(modelfile)  # 保存模型权重
score = model.evaluate(x_test, y_test, verbose=0)
print('Test loss:', score[0])
print('Test accuracy:', score[1])
# 4 预测，并还原结果。
# print()
# x = ((data_test0[feature] - test_mean[feature])/test_std[feature])
# x_matrix=x.as_matrix()
s = model.predict(x_test)
s2 = model.predict(x_train)


# y_test = ss_y.inverse_transform(y_test)
# y_predict = ss_y.inverse_transform(s.reshape(-1,1))
# y_train = ss_y.inverse_transform(y_train)
# y_predict1 = ss_y.inverse_transform(s2.reshape(-1,1))

def mape_cont(y_test, y_predict):
    err = abs(y_test - y_predict) / y_test
    err = np.mean(err) * 100
    return err


from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
import math

# from fbprophet.diagnostics import performance_metrics
print("R_squared：", r2_score(y_test, s))
print("MSE:", mean_squared_error(y_test, s))
print("RMSE:", math.sqrt(mean_squared_error(y_test, s)))
print("MAE:", mean_absolute_error(y_test, s))
print("MAPE:", mape_cont(y_test, s))

print("R_squared：", r2_score(y_train, s2))
print("MSE:", mean_squared_error(y_train, s2))
print("RMSE:", math.sqrt(mean_squared_error(y_train, s2)))
print("MAE:", mean_absolute_error(y_train, s2))
print("MAPE:", mape_cont(y_train, s2))

# 6 画出预测结果图
import matplotlib.pyplot as plt
plt.xlim(0, 150)
plt.ylim(0, 150)
plt.gca().set_aspect(1)
plt.scatter(s,y_test,s=1, c='b', marker='.')
plt.show()

plt.xlim(0, 150)
plt.ylim(0, 150)
plt.gca().set_aspect(1)
plt.scatter(s2,y_train,s=1, c='b', marker='.')
plt.show()
