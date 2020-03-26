import numpy as np
import re, copy
from deep_model_strength.strength_prediction import presiction


# 计算记录的单位价格
def compute_unit_price(jprice, record):
    unit_price = record.mix_special_fine_sand_dosage * jprice[
        "mix_special_fine_sand"] + record.mix_medium_sand_consumption * jprice[
                     "mix_medium_sand"] + record.mix_coarse_sand_consumption * jprice[
                     "mix_coarse_sand"] + record.mix_small_stone_dosage * jprice[
                     "mix_rocklet"] + record.mix_big_stone_dosage * jprice[
                     "mix_boulder"] + record.mix_limestone_powder_consumption * jprice[
                     "limestone_powder"] + record.mix_water_reducing_agent_dosage * jprice[
                     "water_reduce_agent"] + record.mix_fly_ash_dosage * jprice[
                     "fly_ash"] + record.mix_cement_consumption * jprice[
                     "cement"] + record.mix_water_consumption * jprice[
                     "water"] + record.mix_expansion_agent_dosage * jprice[
                     "expansion_agent"] + record.mix_slag_powder_consumption * jprice["slag_powder"]
    return unit_price


# 计算水泥、参合料、水、砂、石的均值、最小值、最大值
# 参合料：粉煤灰、矿渣粉、石灰石粉、膨胀剂
def compute_min_max(lrecord, joption):
    # 获取有值的记录的值
    value_di = {}
    for record in lrecord:

        # 调整记录中的砂用量
        # 如果用户没有选粗砂，但是选了另外两种砂，把粗砂用量放到中沙上
        if joption["mix_special_fine_sand_use"] == 1 and joption["mix_medium_sand_use"] == 1 and joption[
            "mix_coarse_sand_use"] == 0:
            record.mix_medium_sand_consumption += record.mix_coarse_sand_consumption
            record.mix_coarse_sand_consumption = 0
        # 如果用户没有选中砂，但是选了另外两种砂，把中砂用量放到粗沙上
        elif joption["mix_special_fine_sand_use"] == 1 and joption["mix_medium_sand_use"] == 0 and joption[
            "mix_coarse_sand_use"] == 1:
            record.mix_coarse_sand_consumption += record.mix_medium_sand_consumption
            record.mix_medium_sand_consumption = 0
        # 如果用户没有选特细砂，但是选了另外两种砂，把特细砂用量放到中沙上
        elif joption["mix_special_fine_sand_use"] == 0 and joption["mix_medium_sand_use"] == 1 and joption[
            "mix_coarse_sand_use"] == 1:
            record.mix_medium_sand_consumption += record.mix_special_fine_sand_dosage
            record.mix_special_fine_sand_dosage = 0
        # 如果用户只选了特细砂，则把中砂、粗砂用量加到特细砂
        elif joption["mix_special_fine_sand_use"] == 1 and joption["mix_medium_sand_use"] == 0 and joption[
            "mix_coarse_sand_use"] == 0:
            record.mix_special_fine_sand_dosage += record.mix_medium_sand_consumption + record.mix_coarse_sand_consumption
            record.mix_medium_sand_consumption = 0
            record.mix_coarse_sand_consumption = 0
        # 如果用户只选了粗砂，把中砂、特细砂用量加到粗砂
        elif joption["mix_special_fine_sand_use"] == 0 and joption["mix_medium_sand_use"] == 0 and joption[
            "mix_coarse_sand_use"] == 1:
            record.mix_coarse_sand_consumption += record.mix_medium_sand_consumption + record.mix_special_fine_sand_dosage
            record.mix_medium_sand_consumption = 0
            record.mix_special_fine_sand_dosage = 0
        # 如果用户只选了中砂，把特细砂、粗砂用量加到中砂
        elif joption["mix_special_fine_sand_use"] == 0 and joption["mix_medium_sand_use"] == 1 and joption[
            "mix_coarse_sand_use"] == 0:
            record.mix_medium_sand_consumption += record.mix_coarse_sand_consumption + record.mix_special_fine_sand_dosage
            record.mix_coarse_sand_consumption = 0
            record.mix_special_fine_sand_dosage = 0

        # 调整记录中的石用量
        # 如果用户只选了大石，把小石用量放到大石
        if joption["mix_rocklet_use"] == 0 and joption["mix_boulder_use"] == 1:
            record.mix_big_stone_dosage += record.mix_small_stone_dosage
            record.mix_small_stone_dosage = 0
        # 如果用户只选了小石，把大石用量放到小石
        elif joption["mix_boulder_use"] == 0 and joption["mix_rocklet_use"] == 1:
            record.mix_small_stone_dosage += record.mix_big_stone_dosage
            record.mix_big_stone_dosage = 0

        if record.mix_cement_consumption > 0.1:
            if value_di.get("mix_cement_consumption"):
                value_di["mix_cement_consumption"].append(record.mix_cement_consumption)
            else:
                value_di["mix_cement_consumption"] = [record.mix_cement_consumption]
        if record.mix_fly_ash_dosage > 0.1:
            if value_di.get("mix_fly_ash_dosage"):
                value_di["mix_fly_ash_dosage"].append(record.mix_fly_ash_dosage)
            else:
                value_di["mix_fly_ash_dosage"] = [record.mix_fly_ash_dosage]
        if record.mix_slag_powder_consumption > 0.1:
            if value_di.get("mix_slag_powder_consumption"):
                value_di["mix_slag_powder_consumption"].append(record.mix_slag_powder_consumption)
            else:
                value_di["mix_slag_powder_consumption"] = [record.mix_slag_powder_consumption]
        if record.mix_limestone_powder_consumption > 0.1:
            if value_di.get("mix_limestone_powder_consumption"):
                value_di["mix_limestone_powder_consumption"].append(record.mix_limestone_powder_consumption)
            else:
                value_di["mix_limestone_powder_consumption"] = [record.mix_limestone_powder_consumption]
        if record.mix_expansion_agent_dosage > 0.1:
            if value_di.get("mix_expansion_agent_dosage"):
                value_di["mix_expansion_agent_dosage"].append(record.mix_expansion_agent_dosage)
            else:
                value_di["mix_expansion_agent_dosage"] = [record.mix_expansion_agent_dosage]
        if record.mix_water_consumption > 0.1:
            if value_di.get("mix_water_consumption"):
                value_di["mix_water_consumption"].append(record.mix_water_consumption)
            else:
                value_di["mix_water_consumption"] = [record.mix_water_consumption]
        if record.mix_special_fine_sand_dosage > 0.1:
            if value_di.get("mix_special_fine_sand_dosage"):
                value_di["mix_special_fine_sand_dosage"].append(record.mix_special_fine_sand_dosage)
            else:
                value_di["mix_special_fine_sand_dosage"] = [record.mix_special_fine_sand_dosage]
        if record.mix_medium_sand_consumption > 0.1:
            if value_di.get("mix_medium_sand_consumption"):
                value_di["mix_medium_sand_consumption"].append(record.mix_medium_sand_consumption)
            else:
                value_di["mix_medium_sand_consumption"] = [record.mix_medium_sand_consumption]
        if record.mix_coarse_sand_consumption > 0.1:
            if value_di.get("mix_coarse_sand_consumption"):
                value_di["mix_coarse_sand_consumption"].append(record.mix_coarse_sand_consumption)
            else:
                value_di["mix_coarse_sand_consumption"] = [record.mix_coarse_sand_consumption]
        if record.mix_small_stone_dosage > 0.1:
            if value_di.get("mix_small_stone_dosage"):
                value_di["mix_small_stone_dosage"].append(record.mix_small_stone_dosage)
            else:
                value_di["mix_small_stone_dosage"] = [record.mix_small_stone_dosage]
        if record.mix_big_stone_dosage > 0.1:
            if value_di.get("mix_big_stone_dosage"):
                value_di["mix_big_stone_dosage"].append(record.mix_big_stone_dosage)
            else:
                value_di["mix_big_stone_dosage"] = [record.mix_big_stone_dosage]

    # 计算均值、最小值、最大值
    itemli = ["mix_cement_consumption", "mix_fly_ash_dosage", "mix_slag_powder_consumption",
              "mix_limestone_powder_consumption", "mix_expansion_agent_dosage", "mix_water_consumption",
              "mix_special_fine_sand_dosage", "mix_medium_sand_consumption", "mix_coarse_sand_consumption",
              "mix_small_stone_dosage", "mix_big_stone_dosage"]
    min_max = {}
    for item in itemli:
        if value_di.get(item):  # 如果有值
            min_max[item] = [min(value_di.get(item)), max(value_di.get(item))]
        else:  # 如果没有值，设为0
            if item in ["mix_special_fine_sand_dosage", "mix_medium_sand_consumption", "mix_coarse_sand_consumption"]:
                min_max[item] = [10, 1000]
            if item in ["mix_small_stone_dosage", "mix_big_stone_dosage"]:
                min_max[item] = [50, 1200]
            else:
                min_max[item] = [0, 0]

    # 参合料40到60判断
    itemli = ["mix_fly_ash_dosage", "mix_slag_powder_consumption",
              "mix_limestone_powder_consumption", "mix_expansion_agent_dosage"]
    for item in itemli:
        min_max[item][0] = 10 #max(40, min_max[item][0])
        min_max[item][1] = 60 #min(60, min_max[item][1])
    return min_max


# 计算表观密度
def compute_apparent_density(record):
    return record.mix_small_stone_dosage + record.mix_big_stone_dosage + record.mix_limestone_powder_consumption + record.mix_water_consumption + record.mix_special_fine_sand_dosage + record.mix_medium_sand_consumption + record.mix_coarse_sand_consumption + record.mix_fly_ash_dosage + record.mix_cement_consumption + record.mix_water_reducing_agent_dosage + record.mix_expansion_agent_dosage + record.mix_slag_powder_consumption


# 表观密度限制
def judge_apparent_density(mix_power_level, mix_apparent_density):
    if mix_power_level == 15 and 2350 < mix_apparent_density < 2390:  #modify by xioayushi  2370-2390
        return True
    elif mix_power_level == 20 and 2350 < mix_apparent_density < 2390:#modify by xioayushi  2370-2390
        return True
    elif mix_power_level == 25 and 2360 < mix_apparent_density < 2400:
        return True
    elif mix_power_level == 30 and 2350 < mix_apparent_density < 2410:
        return True
    elif mix_power_level == 35 and 2360 < mix_apparent_density < 2420:
        return True
    elif mix_power_level == 40 and 2370 < mix_apparent_density < 2430:
        return True
    elif mix_power_level == 45 and 2380 < mix_apparent_density < 2440:
        return True
    elif mix_power_level == 50 and 2390 < mix_apparent_density < 2450:
        return True
    elif mix_power_level == 55 and 2400 < mix_apparent_density < 2460:
        return True
    elif mix_power_level == 60 and 2420 < mix_apparent_density < 2480:
        return True
    elif mix_power_level == 65 and 2420 < mix_apparent_density < 2480:
        return True
    elif mix_power_level > 65 and 2460 < mix_apparent_density:
        return True
    else:
        return False


# 水胶比及胶凝材料用量限制
def judge_water_binder_ratio(mix_power_level, record, joption):
    # 凝胶材料总用量
    binder_consumption = record.mix_limestone_powder_consumption + record.mix_fly_ash_dosage + record.mix_cement_consumption + record.mix_expansion_agent_dosage + record.mix_slag_powder_consumption
    # 计算水胶比，看是否满足要求
    design_max_water_binder_ratio = record.mix_water_consumption / binder_consumption
    if joption["mix_concrete_variety"] == "抗渗混凝土":
        try:
            regex1 = re.compile("^P(.+)")
            mix_impermeability_rating = float(regex1.findall(joption["mix_power_level"])[0])
            if binder_consumption <= 320:
                return False
            if mix_impermeability_rating==6:
                if 20<=mix_power_level<=30 and design_max_water_binder_ratio>0.6:
                    return False
                elif 50<=mix_power_level and design_max_water_binder_ratio>0.55:
                    return False
            elif 8<=mix_impermeability_rating<=12:
                if 20 <= mix_power_level <= 30 and design_max_water_binder_ratio > 0.55:
                    return False
                elif 50 <= mix_power_level and design_max_water_binder_ratio > 0.5:
                    return False
            elif 12 < mix_impermeability_rating:
                if 20 <= mix_power_level <= 30 and design_max_water_binder_ratio > 0.5:
                    return False
                elif 50 <= mix_power_level and design_max_water_binder_ratio > 0.45:
                    return False
            else:
                return True
        except:
            return True
    else:
        if mix_power_level < 30 and design_max_water_binder_ratio <= 0.6 and 260 <= binder_consumption <= 400:
            return True
        elif mix_power_level == 30 and design_max_water_binder_ratio <= 0.55 and 280 <= binder_consumption <= 400:
            return True
        elif mix_power_level == 35 and design_max_water_binder_ratio <= 0.5 and 300 <= binder_consumption <= 400:
            return True
        elif mix_power_level == 40 and design_max_water_binder_ratio <= 0.45 and 320 <= binder_consumption <= 450:
            return True
        elif mix_power_level == 45 and design_max_water_binder_ratio <= 0.4 and 340 <= binder_consumption <= 450:
            return True
        elif mix_power_level == 50 and design_max_water_binder_ratio <= 0.36 and 360 <= binder_consumption <= 480:
            return True
        elif mix_power_level >= 55 and design_max_water_binder_ratio <= 0.36 and 380 <= binder_consumption <= 500:
            return True
        else:
            return False


# 砂率约束
def judge_sand_ratio(record):
    sand_consumption = record.mix_special_fine_sand_dosage + record.mix_medium_sand_consumption + record.mix_coarse_sand_consumption
    stone_consumption = record.mix_small_stone_dosage + record.mix_big_stone_dosage
    sand_ratio = sand_consumption / (sand_consumption + stone_consumption)
    if 0.35 <= sand_ratio <= 0.46:
        return True
    else:
        return False


# 减水剂/水泥用量的比值约束
def judge_water_reducing_agent_cement_dosage_ratio(record):
    # 有才进行判断
    if record.mix_water_reducing_agent_dosage != 0:
        if 0.006 <= record.mix_water_reducing_agent_dosage / record.mix_cement_consumption <= 0.053:  # 数据库中统计出来
            return True
        else:
            return False
    else:
        return True


# 优化数据
def main_mix_ratio_optimization(joption, jprice, lrecord, model):
    np.random.seed(50)
    # 获取用户要求的强度等级
    regex1 = re.compile("^C(.+)")
    user_mix_power_level = float(regex1.findall(joption["mix_power_level"])[0])
    # 计算最小值、最大值
    min_max = compute_min_max(lrecord, joption)
    # 对第一条记录进行优化
    record = lrecord[0]

    '''
    # 参合料判断
    if joption["mix_fly_ash_dosage"] != -1 and record.mix_fly_ash_dosage == -1:  # 用户选了，记录中没有
        if min_max["mix_fly_ash_dosage"] == [0, 0]:  # 如果10条记录的初始化为0
            record.mix_fly_ash_dosage = np.random.randint(40, 60)
        else:
            record.mix_fly_ash_dosage = min_max["mix_fly_ash_dosage"][0]
    if joption["mix_slag_powder_consumption"] != -1 and record.mix_slag_powder_consumption == -1:  # 用户选了，记录中没有
        if min_max["mix_slag_powder_consumption"] == [0, 0]:  # 如果10条记录的初始化为0
            record.mix_slag_powder_consumption = np.random.randint(40, 60)
        else:
            record.mix_slag_powder_consumption = min_max["mix_slag_powder_consumption"][0]
    if joption[
        "mix_limestone_powder_consumption"] != -1 and record.mix_limestone_powder_consumption == -1:  # 用户选了，记录中没有
        if min_max["mix_limestone_powder_consumption"] == [0, 0]:  # 如果10条记录的初始化为0
            record.mix_limestone_powder_consumption = np.random.randint(40, 60)
        else:
            record.mix_limestone_powder_consumption = min_max["mix_limestone_powder_consumption"][0]
    if joption["mix_expansion_agent_dosage"] != -1 and record.mix_expansion_agent_dosage == -1:  # 用户选了，记录中没有
        if min_max["mix_expansion_agent_dosage"] == [0, 0]:  # 如果10条记录的初始化为0
            record.mix_expansion_agent_dosage = np.random.randint(40, 60)
        else:
            record.mix_expansion_agent_dosage = min_max["mix_expansion_agent_dosage"][0]

    # 水下混凝土特殊条件判断
    if joption["mix_concrete_variety"] == "水下混凝土":
        record.mix_cement_consumption = max(300, record.mix_cement_consumption, 365 - (
                record.mix_limestone_powder_consumption + record.mix_fly_ash_dosage + record.mix_slag_powder_consumption + record.mix_expansion_agent_dosage))
    '''
    # 记录最优记录
    best_record = None
    best_unit_price = float('inf') # 记录最优价格值
    best_apparent_density = None  # 最优表观密度
    # 改变原材料用量，生成新的配合比
    weight_min = 0.9
    weight_max = 1.1
    for i in range(10000):
        # 初始化new_record，每次循环都改变该值
        new_record = copy.deepcopy(record)

        # 调整内容：水泥、粉煤灰、矿渣粉、石灰石粉、膨胀剂、水、砂、石；
        # 调整范围：10条记录的最小最大值
        # 取随机值
        new_record.mix_cement_consumption = np.random.randint(
            int(weight_min * min_max["mix_cement_consumption"][0]),
            int(weight_max * min_max["mix_cement_consumption"][1]))

        if joption["fly_sample_category"] != "" or joption["fly_breed_grade"] != "" or joption["fly_fineness"] != -1:
            new_record.mix_fly_ash_dosage = np.random.randint(
                int(weight_min * min_max["mix_fly_ash_dosage"][0]),
                int(weight_max * min_max["mix_fly_ash_dosage"][1]))
        else:
            new_record.mix_fly_ash_dosage = 0

        if joption["slag_breed_grade"] != "" or joption["slag_28d_activity_index"] != -1:
            new_record.mix_slag_powder_consumption = np.random.randint(
                int(weight_min * min_max["mix_slag_powder_consumption"][0]),
                int(weight_max * min_max["mix_slag_powder_consumption"][1]))
        else:
            new_record.mix_slag_powder_consumption = 0

        if joption["limestone_fineness"] != -1 or joption["limestone_methylene_blue_value"] != -1:
            new_record.mix_limestone_powder_consumption = np.random.randint(
                int(weight_min * min_max["mix_limestone_powder_consumption"][0]),
                int(weight_max * min_max["mix_limestone_powder_consumption"][1]))
        else:
            new_record.mix_limestone_powder_consumption = 0

        if joption["expansion_breed_grade"] != "" or joption["expansion_28d_compressive_strength"] != -1:
            new_record.mix_expansion_agent_dosage = np.random.randint(
                int(weight_min * min_max["mix_expansion_agent_dosage"][0]),
                int(weight_max * min_max["mix_expansion_agent_dosage"][1]))
        else:
            new_record.mix_expansion_agent_dosage = 0

        new_record.mix_water_consumption = np.random.randint(
            int(weight_min * min_max["mix_water_consumption"][0]),
            int(weight_max * min_max["mix_water_consumption"][1]))

        if joption["mix_special_fine_sand_use"] == 1:
            new_record.mix_special_fine_sand_dosage = np.random.randint(
                int(weight_min * min_max["mix_special_fine_sand_dosage"][0]),
                int(weight_max * min_max["mix_special_fine_sand_dosage"][1]))
        else:
            new_record.mix_special_fine_sand_dosage = 0

        if joption["mix_medium_sand_use"] == 1:
            new_record.mix_medium_sand_consumption = np.random.randint(
                int(weight_min * min_max["mix_medium_sand_consumption"][0]),
                int(weight_max * min_max["mix_medium_sand_consumption"][1]))
        else:
            new_record.mix_medium_sand_consumption = 0

        if joption["mix_coarse_sand_use"] == 1:
            new_record.mix_coarse_sand_consumption = np.random.randint(
                int(weight_min * min_max["mix_coarse_sand_consumption"][0]),
                int(weight_max * min_max["mix_coarse_sand_consumption"][1]))
        else:
            new_record.mix_coarse_sand_consumption = 0

        if joption["mix_rocklet_use"] == 1:
            new_record.mix_small_stone_dosage = np.random.randint(
                int(weight_min * min_max["mix_small_stone_dosage"][0]),
                int(weight_max * min_max["mix_small_stone_dosage"][1]))
        else:
            new_record.mix_small_stone_dosage = 0

        if joption["mix_boulder_use"] == 1:
            new_record.mix_big_stone_dosage = np.random.randint(
                int(weight_min * min_max["mix_big_stone_dosage"][0]),
                int(weight_max * min_max["mix_big_stone_dosage"][1]))
        else:
            new_record.mix_big_stone_dosage = 0

        # 减水剂用量保留两位小数
        if joption["reduce_breed_grade"] != "" or joption["reduce_recommended_dosage"] != -1 or joption["reduce_water_reduction_rate"] != -1:
            new_record.mix_water_reducing_agent_dosage = weight_min * record.mix_water_reducing_agent_dosage + np.random.random(1) *(weight_max * record.mix_water_reducing_agent_dosage-weight_min * record.mix_water_reducing_agent_dosage)
            new_record.mix_water_reducing_agent_dosage = round(new_record.mix_water_reducing_agent_dosage[0], 2)
        else:
            new_record.mix_water_reducing_agent_dosage = 0

        '''
        # 水下混凝土特殊条件判断
        if joption["mix_concrete_variety"] == "水下混凝土":
            new_record.mix_cement_consumption = max(300, new_record.mix_cement_consumption, 365 - (
                    new_record.mix_limestone_powder_consumption + new_record.mix_fly_ash_dosage + new_record.mix_slag_powder_consumption + new_record.mix_expansion_agent_dosage))
        '''

        new_apparent_density = compute_apparent_density(record)
        # 计算生成的配合比的价格
        new_unit_price = compute_unit_price(jprice, new_record)
        if new_unit_price > best_unit_price:
            continue
        if not (judge_apparent_density(user_mix_power_level, new_apparent_density) and judge_water_binder_ratio(
                user_mix_power_level, record, joption) and judge_sand_ratio(
            record) and judge_water_reducing_agent_cement_dosage_ratio(record)):
            continue

        # 计算生成的配合比的价格
        new_record.mix_28d_strength = float(presiction(new_record, model=model)["strength"])
        if new_record.mix_28d_strength >= user_mix_power_level * 1.4:
            best_record = new_record
            best_unit_price = new_unit_price
            best_apparent_density = new_apparent_density

    return best_record, best_apparent_density, best_unit_price
