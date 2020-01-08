from get_data_from_db import main_get_data, data_transform
import torch
import torch.utils.data as Data
import numpy as np
import config
import os, shutil
import matplotlib.pyplot as plt
from tensorboardX import SummaryWriter
from sklearn import preprocessing

TORCH_MODEL_WEIGHTS_FILE = os.path.dirname(__file__) + '/torch_model_params.pkl'


# 创建模型
def creat_torch_model():
    model = torch.nn.Sequential(
        torch.nn.Linear(39, 60),
        #torch.nn.Dropout(0.1),
        torch.nn.LeakyReLU(),
        torch.nn.BatchNorm1d(60),
        torch.nn.Linear(60, 20),
        #torch.nn.Dropout(0.1),
        torch.nn.LeakyReLU(),
        torch.nn.BatchNorm1d(20),
        torch.nn.Linear(20, 1)
    )
    return model


# 训练模型
def train_torch_model():
    model = creat_torch_model()
    # 参数初始化
    model.apply(weights_init)
    # 获取数据
    fetures, lable = main_get_data(config.CONNECT)
    # 先转换成 torch 能识别的 Dataset
    fetures = torch.from_numpy(fetures).float()
    lable = torch.from_numpy(lable).float()
    torch_dataset = Data.TensorDataset(fetures[:-8000], lable[:-8000])
    # 测试数据集
    fetures_test, lable_test = fetures[-8000:], lable[-8000:]
    # 把 dataset 放入 DataLoader
    loader = Data.DataLoader(
        dataset=torch_dataset,
        batch_size=16,
        shuffle=True,  # 打乱数据
        num_workers=4,  # 多线程来读数据
        drop_last=True
    )
    # 优化器
    optimizer = torch.optim.Adam(model.parameters(), lr=0.006)  # 传入 net 的所有参数, 学习率
    loss_func = torch.nn.MSELoss()  # 预测值和真实值的误差计算公式 (均方差)
    # 画图
    try:
        shutil.rmtree('logs/')  # 递归删除文件夹
    except:
        print("没有发现logs文件目录!")
    writer = SummaryWriter("logs/")
    # 训练
    step = 0
    for epoch in range(5):
        for batch_x, batch_y in loader:  # 每一步 loader 释放一小批数据用来学习
            step += 1
            model.train()
            prediction = model(batch_x)  # 喂给 net 训练数据 x, 输出预测值
            loss = loss_func(prediction, batch_y)  # 计算两者的误差
            optimizer.zero_grad()  # 清空上一步的残余更新参数值
            loss.backward()  # 误差反向传播, 计算参数更新值
            optimizer.step()  # 将参数更新值施加到 net 的 parameters 上
            # 打出来一些数据
            if step % 100 == 0:
                # 训练集
                writer.add_scalar('LossTrain', loss.detach().numpy(), step)
                print('Epoch: ', epoch, '| Step: ', step, '| Loss_train: ', loss.data.numpy())
    torch.save(model.state_dict(), TORCH_MODEL_WEIGHTS_FILE)  # 只保存网络中的参数
    print("Model saved!")
    # 测试集
    lossli = []
    model.eval()
    for i, feture in enumerate(fetures_test):
        prediction = model(feture.unsqueeze(0))  # 数据增加一维，喂给 net 训练数据 x, 输出预测值
        lossli.append((abs(prediction - lable_test[i])).tolist()[0][0])
    print(len(lossli))
    print(lossli)
    print("均值： ", sum(lossli) / len(lossli))
    plt.plot(lossli[-50:])
    plt.ylabel('Loss')
    plt.show()


# 初始化网络参数
def weights_init(m):
    if isinstance(m, torch.nn.Linear):
        torch.nn.init.xavier_normal_(m.weight)
        m.bias.data.fill_(0.01)


# 加载训练好的模型
def load_torch_model():
    model = creat_torch_model()  # 加载model
    model.load_state_dict(torch.load(TORCH_MODEL_WEIGHTS_FILE))  # 将保存的参数复制到 model
    return model


# 预测强度
def presiction(data, model):
    try:
        feature = [data["mix_impermeability_rating"],
                   data["mix_material_requirements"],
                   data["mix_limit_expansion_rate"],
                   data["mix_slump"],
                   data["mix_expansion"],
                   data["mix_cement_consumption"],
                   data["mix_special_fine_sand_dosage"],
                   data["mix_medium_sand_consumption"],
                   data["mix_coarse_sand_consumption"],
                   data["mix_small_stone_dosage"],
                   data["mix_big_stone_dosage"],
                   data["mix_water_reducing_agent_dosage"],
                   data["mix_fly_ash_dosage"],
                   data["mix_slag_powder_consumption"],
                   data["mix_limestone_powder_consumption"],
                   data["mix_expansion_agent_dosage"],
                   data["mix_water_consumption"],
                   data["cement_breed_grade"],
                   data["cement_28d_compression"],
                   data["reduce_breed_grade"],
                   data["reduce_recommended_dosage"],
                   data["reduce_water_reduction_rate"],
                   data["reduce_gas_content"],
                   data["reduce_28d_compressive_strength_ratio"],
                   data["reduce_bleeding_rate_ratio"],
                   data["fly_sample_category"],
                   data["fly_breed_grade"],
                   data["fly_fineness"],
                   data["fly_water_demand_ratio"],
                   data["fly_loss_on_ignition"],
                   data["fly_activity_index"],
                   data["slag_breed_grade"],
                   data["slag_28d_activity_index"],
                   data["limestone_fineness"],
                   data["limestone_methylene_blue_value"],
                   data["limestone_28d_activity_index"],
                   data["expansion_breed_grade"],
                   data["expansion_28d_compressive_strength"],
                   data["expansion_limit_expansion_rate"]]
        data_transform(feature)
        feature = np.array([feature], dtype=float)
        val = round(model(torch.from_numpy(feature).float()).data.numpy()[0][0], 1)  # 预测
        jresult = {"state": "1", "strength": str(val)}
    except:
        jresult = {"state": "-1", "strength": "0"}
    return jresult


if __name__ == '__main__':
    train_torch_model()
