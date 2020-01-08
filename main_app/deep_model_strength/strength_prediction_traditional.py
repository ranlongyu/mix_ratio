from get_data_from_db import main_get_data, data_transform
import numpy as np
import config
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn import svm


# 训练模型
def train_svm_model():
    # 获取数据
    fetures, lable = main_get_data(config.CONNECT)
    lable = lable.reshape(1, -1)[0]
    print(fetures.shape)
    print(lable.shape)
    # 数据归一化
    preprocessing.scale(fetures)
    # 数据集划分
    fetures_train, lable_train = fetures[:-8000], lable[:-8000]
    fetures_test, lable_test = fetures[-8000:], lable[-8000:]
    # svm模型
    clf = svm.SVR(gamma='auto')
    clf.fit(fetures_train, lable_train)
    print("Model trained!")
    # 测试集
    prediction = clf.predict(fetures_test)  # 数据增加一维，喂给 net 训练数据 x, 输出预测值
    print("均值： ", np.average(prediction))
    plt.plot(prediction[-50:])
    plt.ylabel('Loss')
    plt.show()


if __name__ == '__main__':
    train_svm_model()
