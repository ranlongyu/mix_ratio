import numpy as np
import re
import copy
from deep_model_strength.strength_prediction import presiction

# 计算记录的单位价格
def compute_unit_price(jprice, record):
    unit_price = record.mix_special_fine_sand_dosage * jprice[
        "mix_special_fine_sand_dosage"] + record.mix_medium_sand_consumption * jprice[
                     "mix_medium_sand_consumption"] + record.mix_coarse_sand_consumption * jprice[
                     "mix_coarse_sand_consumption"] + record.mix_small_stone_dosage * jprice[
                     "mix_rocklet_consumption"] + record.mix_big_stone_dosage * jprice[
                     "mix_boulder_consumption"] + record.mix_limestone_powder_consumption * jprice[
                     "limestone_powder"] + record.mix_water_reducing_agent_dosage * jprice[
                     "water_reduce_agent"] + record.mix_fly_ash_dosage * jprice[
                     "fly_ash"] + record.mix_cement_consumption * jprice[
                     "cement"] + record.mix_water_consumption * jprice[
                     "water"] + record.mix_expansion_agent_dosage * jprice[
                     "expansion_agent"] + record.mix_slag_powder_consumption * jprice["slag_powder"]
    return unit_price

# 通过价格优化record记录中配合比
def mix_ratio_optimization(joption, jprice, record, model, scaler):
    regex1 = re.compile("^C(.+)")
    user_mix_power_level = float(regex1.findall(joption["mix_power_level"])[0])  # 用户要求的强度等级

    if joption["fine_aggregate_1"] == "特细沙":
        jprice["mix_special_fine_sand_dosage"] = jprice["fine_aggregate_1"]
    elif joption["fine_aggregate_1"] == "中沙":
        jprice["mix_medium_sand_consumption"] = jprice["fine_aggregate_1"]
    elif joption["fine_aggregate_1"] == "粗沙":
        jprice["mix_coarse_sand_consumption"] = jprice["fine_aggregate_1"]

    if joption["fine_aggregate_2"] == "特细沙":
        jprice["mix_special_fine_sand_dosage"] = jprice["fine_aggregate_2"]
    elif joption["fine_aggregate_2"] == "中沙":
        jprice["mix_medium_sand_consumption"] = jprice["fine_aggregate_2"]
    elif joption["fine_aggregate_2"] == "粗沙":
        jprice["mix_coarse_sand_consumption"] = jprice["fine_aggregate_2"]

    if joption["fine_aggregate_3"] == "特细沙":
        jprice["mix_special_fine_sand_dosage"] = jprice["fine_aggregate_3"]
    elif joption["fine_aggregate_3"] == "中沙":
        jprice["mix_medium_sand_consumption"] = jprice["fine_aggregate_3"]
    elif joption["fine_aggregate_3"] == "粗沙":
        jprice["mix_coarse_sand_consumption"] = jprice["fine_aggregate_3"]

    if joption["coarse_aggregate_1"] == "小石":
        jprice["mix_rocklet_consumption"] = jprice["coarse_aggregate_1"]
    elif joption["coarse_aggregate_1"] == "大石":
        jprice["mix_boulder_consumption"] = jprice["coarse_aggregate_1"]

    if joption["coarse_aggregate_2"] == "小石":
        jprice["mix_rocklet_consumption"] = jprice["coarse_aggregate_2"]
    elif joption["coarse_aggregate_2"] == "大石":
        jprice["mix_boulder_consumption"] = jprice["coarse_aggregate_2"]

    if joption["coarse_aggregate_3"] == "小石":
        jprice["mix_rocklet_consumption"] = jprice["coarse_aggregate_3"]
    elif joption["coarse_aggregate_3"] == "大石":
        jprice["mix_boulder_consumption"] = jprice["coarse_aggregate_3"]

    # 查询得到的记录的单位价格
    unit_price = compute_unit_price(jprice, record)
    # 初始化best_record，记录最优值
    best_record = copy.deepcopy(record)
    # best_unit_price，记录最优值
    best_unit_price = unit_price
    # 改变原材料用量，生成新的配合比
    for i in range(1000):
        # 初始化new_record，每次循环都改变该值
        new_record = copy.deepcopy(record)
        # 取随机值
        new_record.mix_limestone_powder_consumption += 10 * (-1 * np.random.rand())
        new_record.mix_water_reducing_agent_dosage += 3 * (-1 + 2 * np.random.rand())
        new_record.mix_fly_ash_dosage += 10 * (-1 * np.random.rand())
        new_record.mix_cement_consumption += 10 * (-1 + 2 * np.random.rand())
        new_record.mix_water_consumption += 20 * (2 * np.random.rand() - 1)
        # 计算水胶比，看是否满足要求
        design_max_water_binder_ratio = new_record.mix_water_consumption / (
                new_record.mix_limestone_powder_consumption + new_record.mix_fly_ash_dosage + new_record.mix_cement_consumption + new_record.mix_expansion_agent_dosage + new_record.mix_slag_powder_consumption)
        if design_max_water_binder_ratio <= max(0.36, 0.6 - (user_mix_power_level - 25) / 100):  # 水胶比合理性判断
            # 计算生成的配合比的价格
            new_unit_price = compute_unit_price(jprice, new_record)
            new_record.mix_28d_strength = float(presiction(new_record, scaler=scaler, model=model)["strength"])
            if new_record.mix_28d_strength > user_mix_power_level and new_unit_price < best_unit_price:
                best_record = new_record
                best_unit_price = new_unit_price

    jdata = {}

    if joption["fine_aggregate_1"] == "特细沙":
        jdata["fine_aggregate_1"] = record.mix_special_fine_sand_dosage
    elif joption["fine_aggregate_1"] == "中沙":
        jdata["fine_aggregate_1"] = record.mix_medium_sand_consumption
    elif joption["fine_aggregate_1"] == "粗沙":
        jdata["fine_aggregate_1"] = record.mix_coarse_sand_consumption
    else:
        jdata["fine_aggregate_1"] = 0

    if joption["fine_aggregate_2"] == "特细沙":
        jdata["fine_aggregate_2"] = record.mix_special_fine_sand_dosage
    elif joption["fine_aggregate_2"] == "中沙":
        jdata["fine_aggregate_2"] = record.mix_medium_sand_consumption
    elif joption["fine_aggregate_2"] == "粗沙":
        jdata["fine_aggregate_2"] = record.mix_coarse_sand_consumption
    else:
        jdata["fine_aggregate_2"] = 0

    if joption["fine_aggregate_3"] == "特细沙":
        jdata["fine_aggregate_3"] = record.mix_special_fine_sand_dosage
    elif joption["fine_aggregate_3"] == "中沙":
        jdata["fine_aggregate_3"] = record.mix_medium_sand_consumption
    elif joption["fine_aggregate_3"] == "粗沙":
        jdata["fine_aggregate_3"] = record.mix_coarse_sand_consumption
    else:
        jdata["fine_aggregate_3"] = 0

    if joption["coarse_aggregate_1"] == "小石":
        jdata["coarse_aggregate_1"] = record.mix_small_stone_dosage
    elif joption["coarse_aggregate_1"] == "大石":
        jdata["coarse_aggregate_1"] = record.mix_big_stone_dosage
    else:
        jdata["coarse_aggregate_1"] = 0

    if joption["coarse_aggregate_2"] == "小石":
        jdata["coarse_aggregate_2"] = record.mix_small_stone_dosage
    elif joption["coarse_aggregate_2"] == "大石":
        jdata["coarse_aggregate_2"] = record.mix_big_stone_dosage
    else:
        jdata["coarse_aggregate_2"] = 0

    if joption["coarse_aggregate_3"] == "小石":
        jdata["coarse_aggregate_3"] = record.mix_small_stone_dosage
    elif joption["coarse_aggregate_3"] == "大石":
        jdata["coarse_aggregate_3"] = record.mix_big_stone_dosage
    else:
        jdata["coarse_aggregate_3"] = 0

    jdata["mix_cement_consumption"] = round(best_record.mix_cement_consumption)
    jdata["mix_water_consumption"] = round(best_record.mix_water_consumption)
    jdata["mix_water_reducing_agent_dosage"] = round(best_record.mix_water_reducing_agent_dosage)
    jdata["mix_fly_ash_dosage"] = round(best_record.mix_fly_ash_dosage)
    jdata["mix_slag_powder_consumption"] = round(best_record.mix_slag_powder_consumption)
    jdata["mix_limestone_powder_consumption"] = round(best_record.mix_limestone_powder_consumption)
    jdata["mix_expansion_agent_dosage"] = round(best_record.mix_expansion_agent_dosage)
    jdata["mix_other_materials"] = 0
    jdata["mix_apparent_density"] = round(
        best_record.mix_small_stone_dosage + best_record.mix_big_stone_dosage + best_record.mix_limestone_powder_consumption + best_record.mix_water_consumption + best_record.mix_special_fine_sand_dosage + best_record.mix_medium_sand_consumption + best_record.mix_coarse_sand_consumption + best_record.mix_fly_ash_dosage + best_record.mix_cement_consumption + best_record.mix_water_reducing_agent_dosage + best_record.mix_expansion_agent_dosage + best_record.mix_slag_powder_consumption)
    jdata["unit_price"] = round(best_unit_price / 1000)
    jdata["mix_28d_strength"] = round(best_record.mix_28d_strength)
    return jdata

# 推送配合比主函数
def result_package(joption, jprice, lrecord, scaler, model):
    jresult = {}
    jresult["result_long"] = min(len(lrecord), 10)
    jresult["result"] = []
    for record in lrecord[:10]:
        jone = {}
        jone["mix_cement_consumption"] = record.mix_cement_consumption  # 水泥用量

        if joption["fine_aggregate_1"] == "特细沙":
            jone["fine_aggregate_1"] = record.mix_special_fine_sand_dosage
        elif joption["fine_aggregate_1"] == "中沙":
            jone["fine_aggregate_1"] = record.mix_medium_sand_consumption
        elif joption["fine_aggregate_1"] == "粗沙":
            jone["fine_aggregate_1"] = record.mix_coarse_sand_consumption
        else:
            jone["fine_aggregate_1"] = 0

        if joption["fine_aggregate_2"] == "特细沙":
            jone["fine_aggregate_2"] = record.mix_special_fine_sand_dosage
        elif joption["fine_aggregate_2"] == "中沙":
            jone["fine_aggregate_2"] = record.mix_medium_sand_consumption
        elif joption["fine_aggregate_2"] == "粗沙":
            jone["fine_aggregate_2"] = record.mix_coarse_sand_consumption
        else:
            jone["fine_aggregate_2"] = 0

        if joption["fine_aggregate_3"] == "特细沙":
            jone["fine_aggregate_3"] = record.mix_special_fine_sand_dosage
        elif joption["fine_aggregate_3"] == "中沙":
            jone["fine_aggregate_3"] = record.mix_medium_sand_consumption
        elif joption["fine_aggregate_3"] == "粗沙":
            jone["fine_aggregate_3"] = record.mix_coarse_sand_consumption
        else:
            jone["fine_aggregate_3"] = 0

        if joption["coarse_aggregate_1"] == "小石":
            jone["coarse_aggregate_1"] = record.mix_small_stone_dosage
        elif joption["coarse_aggregate_1"] == "大石":
            jone["coarse_aggregate_1"] = record.mix_big_stone_dosage
        else:
            jone["coarse_aggregate_1"] = 0

        if joption["coarse_aggregate_2"] == "小石":
            jone["coarse_aggregate_2"] = record.mix_small_stone_dosage
        elif joption["coarse_aggregate_2"] == "大石":
            jone["coarse_aggregate_2"] = record.mix_big_stone_dosage
        else:
            jone["coarse_aggregate_2"] = 0

        if joption["coarse_aggregate_3"] == "小石":
            jone["coarse_aggregate_3"] = record.mix_small_stone_dosage
        elif joption["coarse_aggregate_3"] == "大石":
            jone["coarse_aggregate_3"] = record.mix_big_stone_dosage
        else:
            jone["coarse_aggregate_3"] = 0

        jone["mix_water_consumption"] = record.mix_water_consumption # 水用量
        jone["mix_water_reducing_agent_dosage"] = record.mix_water_reducing_agent_dosage  # 减水剂用量

        if joption["fly_sample_category"] != "":
            jone["mix_fly_ash_dosage"] = record.mix_fly_ash_dosage  # 粉煤灰用量
        else:
            jone["mix_fly_ash_dosage"] = 0

        if joption["slag_breed_grade"] != "":
            jone["mix_slag_powder_consumption"] = record.mix_slag_powder_consumption  # 矿渣粉用量
        else:
            jone["mix_slag_powder_consumption"] = 0

        if joption["limestone_fineness"] != -1:
            jone["mix_limestone_powder_consumption"] = record.mix_limestone_powder_consumption  # 石灰石粉用量
        else:
            jone["mix_limestone_powder_consumption"] = 0

        if joption["expansion_breed_grade"] != "":
            jone["mix_expansion_agent_dosage"] = record.mix_expansion_agent_dosage  # 膨胀剂用量
        else:
            jone["mix_expansion_agent_dosage"] = 0

        jone["mix_other_materials"] = 0

        '''28d抗压强度，表观密度，价格'''
        jone["mix_28d_strength"] = record.mix_28d_strength
        jone["mix_apparent_density"] = jone["mix_cement_consumption"] + jone["fine_aggregate_1"] + jone[
            "fine_aggregate_2"] + jone["fine_aggregate_3"] + jone["coarse_aggregate_1"] + jone["coarse_aggregate_2"] + \
                                       jone["coarse_aggregate_3"] + jone["mix_water_consumption"] + jone[
                                           "mix_water_reducing_agent_dosage"] + jone["mix_fly_ash_dosage"] + jone[
                                           "mix_slag_powder_consumption"] + jone["mix_limestone_powder_consumption"] + \
                                       jone["mix_expansion_agent_dosage"] + jone["mix_other_materials"]
        jone["unit_price"] = jone["mix_cement_consumption"] * jprice["cement"] + jone["fine_aggregate_1"] * jprice[
            "fine_aggregate_1"] + jone["fine_aggregate_2"] * jprice["fine_aggregate_2"] + jone["fine_aggregate_3"] * \
                             jprice["fine_aggregate_3"] + jone["coarse_aggregate_1"] * jprice["coarse_aggregate_1"] + \
                             jone["coarse_aggregate_2"] * jprice["coarse_aggregate_2"] + jone["coarse_aggregate_3"] * \
                             jprice["coarse_aggregate_3"] + jone["mix_water_consumption"] * jprice["water"] + jone[
                                 "mix_water_reducing_agent_dosage"] * jprice["water_reduce_agent"] + jone[
                                 "mix_fly_ash_dosage"] * jprice["fly_ash"] + jone["mix_slag_powder_consumption"] * \
                             jprice["slag_powder"] + jone["mix_limestone_powder_consumption"] * jprice[
                                 "limestone_powder"] + jone["mix_expansion_agent_dosage"] * jprice["expansion_agent"] + \
                             jone["mix_other_materials"] * jprice["other_materials"]

        jone["unit_price"] = round(jone["unit_price"] / 1000)
        jresult["result"].append(jone)

    if len(jresult["result"]) > 0:
        jresult["result"][0] = mix_ratio_optimization(joption, jprice, lrecord[0], scaler, model)
    return jresult
