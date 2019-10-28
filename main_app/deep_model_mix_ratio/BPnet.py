from keras.models import Sequential
from keras.layers.core import Dense
import keras


def creat_model():
    global model
    model = Sequential()  # 层次模型
    keras.backend.clear_session()
    model.add(Dense(units=35, input_dim=14, activation='relu'))
    model.add(Dense(units=1, activation='relu'))
    # modelfile = 'weight.h6'
    # feature = ['小石用量','大石用量', '石灰石粉用量', '减水剂用量', '细砂用量','中砂用量','粗砂用量','粉煤灰用量',
    #            '水泥用量', '水用量','膨胀剂用量','矿渣粉用量','混凝土品种', '3d强度']
    model.load_weights('main_app/deep_model_mix_ratio/weight.h6')
    model._make_predict_function()
    return model
