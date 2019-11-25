import pymysql
import numpy as np
from sklearn import preprocessing

def get_data(connect):
    # 创建数据库链接，分别指定主机、用户、密码和数据库名,必须保证用户有权限链接
    db = pymysql.connect(connect[0], connect[1], connect[2], connect[3])
    # 创建游标对象
    cursor = db.cursor()
    sql = "select " \
          "mix_28d_strength," \
          "mix_period," \
          "mix_concrete_variety," \
          "mix_power_level," \
          "mix_impermeability_rating," \
          "mix_material_requirements," \
          "mix_limit_expansion_rate," \
          "mix_slump," \
          "mix_expansion," \
          "mix_cement_consumption," \
          "mix_special_fine_sand_dosage," \
          "mix_medium_sand_consumption," \
          "mix_coarse_sand_consumption," \
          "mix_small_stone_dosage," \
          "mix_big_stone_dosage," \
          "mix_water_reducing_agent_dosage," \
          "mix_fly_ash_dosage," \
          "mix_slag_powder_consumption," \
          "mix_limestone_powder_consumption," \
          "mix_expansion_agent_dosage," \
          "mix_water_consumption," \
          "cement_breed_grade," \
          "cement_28d_compression," \
          "reduce_breed_grade," \
          "reduce_recommended_dosage," \
          "reduce_water_reduction_rate," \
          "reduce_gas_content," \
          "reduce_28d_compressive_strength_ratio," \
          "reduce_bleeding_rate_ratio," \
          "fly_sample_category," \
          "fly_breed_grade," \
          "fly_fineness," \
          "fly_water_demand_ratio," \
          "fly_loss_on_ignition," \
          "fly_activity_index," \
          "slag_breed_grade," \
          "slag_28d_activity_index," \
          "limestone_fineness," \
          "limestone_methylene_blue_value," \
          "limestone_28d_activity_index," \
          "expansion_breed_grade," \
          "expansion_28d_compressive_strength," \
          "expansion_limit_expansion_rate" \
          " from 混凝土配合比" \
          " where mix_28d_strength != -1"
    # 使用execute()方法执行SQL语句
    cursor.execute(sql)

    # 获取所有数据，序列形式
    all_data = []
    data_ser = cursor.fetchall()
    for row in data_ser:
        all_data.append(list(row))

    # 关闭游标
    cursor.close()
    # 关闭链接
    db.close()
    return all_data


# 把特征转换为数字，无返回值
def data_transform(feature):
    # 月份转温度段
    if feature[0] in [5, 6, 7, 8, 9, '高']:
        feature[0] = 1
    elif feature[0] in [12, 1, 2, '中']:
        feature[0] = 2
    else:
        feature[0] = 3
    # 混凝土品种
    mix_concrete_variety_di = {"常规混凝土": 1, "抗渗混凝土": 2, "防水混凝土": 3, "补偿收缩混凝土": 4, "水下混凝土": 5, "大体积混凝土": 6, "透水混凝土": 7,
                               "自密实混凝土": 8, "铁路混凝土": 9, "钢纤维混凝土": 10, "聚丙烯纤维混凝土": 11, "轻骨料混凝土": 12, "重混凝土": 13}
    try:
        feature[1] = mix_concrete_variety_di.get(feature[1].split('\\')[0])
    except:
        feature[1] = -1
    # 强度等级
    try:
        feature[2] = int(feature[2][1:])
    except:
        feature[2] = -1
    # 抗渗等级
    try:
        feature[3] = int(feature[3][1:])
    except:
        feature[3] = -1
    # 材料要求
    mix_material_requirements_di = {"细石": 1, "低碱水泥": 2, "GNA": 3, "ZY": 4, "UEA": 5}
    try:
        feature[4] = mix_material_requirements_di.get(feature[4].split("\\")[0])
    except:
        feature[4] = -1
    # 水泥品种等级
    cement_breed_grade_di = {"P·O42.5R": 1, "P·O42.5": 2, "P·O42.5（低碱）": 3}
    try:
        feature[20] = cement_breed_grade_di.get(feature[20])
    except:
        feature[20] = -1
    # 减水剂品种等级
    reduce_breed_grade = {"聚羧酸高性能减水剂-缓凝型": 1, "聚羧酸高性能减水剂-标准型": 2}
    try:
        feature[22] = reduce_breed_grade.get(feature[22])
    except:
        feature[22] = -1
    # 粉煤灰品种类别
    fly_sample_category_di = {"F类": 1, "C类": 2}
    try:
        feature[28] = fly_sample_category_di.get(feature[28])
    except:
        feature[28] = -1
    # 粉煤灰品种类别
    fly_breed_grade_di = {"Ⅰ级": 1, "Ⅱ级": 2, "Ⅲ级": 3}
    try:
        feature[29] = fly_breed_grade_di.get(feature[29])
    except:
        feature[29] = -1
    # 矿渣粉品种等级
    try:
        feature[34] = int(feature[34])
    except:
        feature[34] = -1
    # 膨胀剂品种等级
    expansion_breed_grade_di = {"Ⅰ型硫铝酸钙类": 1, "Ⅱ型氧化钙类": 2, "Ⅱ型硫铝酸钙-氧化钙类": 3}
    try:
        feature[39] = expansion_breed_grade_di.get(feature[39])
    except:
        feature[39] = -1
    # 规范数据
    for i in range(len(feature)):
        if feature[i] == None or feature[i] == -1:
            feature[i] = 0

# 特征归一化
def get_standard_scaler(features):
    scaler = preprocessing.StandardScaler().fit(features)
    return scaler

# 训练时获取数据与标签
def main_get_data(connect, data_or_scaler):
    #connect = ['0.0.0.0', 'root', '123456', 'test']
    all_data = get_data(connect)
    features = []  # 特征
    lables = []  # 标签
    for i in range(len(all_data)):
        features.append(all_data[i][1:])
        lables.append([all_data[i][0]])
        data_transform(features[i])
    features = np.array(features)
    # 数据归一化
    scaler = get_standard_scaler(features)
    if data_or_scaler:  # 获取数据
        features = scaler.transform(features)
        lables = np.array(lables)
        return features, lables
    else:  # 获取归一化参数
        return scaler


if __name__ == '__main__':
    connect = ['0.0.0.0', 'root', '123456', 'test']
    features, lable = main_get_data(connect, True)
    for line in features:
        print(line)
