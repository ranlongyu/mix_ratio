import re
from main_app.model import Mix_ratio_table as Mix


# 根据条件筛选记录
def filter_mix(joption):
    if joption["mix_period"] == "高":
        mix_period = [5, 6, 7, 8, 9]
    elif joption["mix_period"] == "低":
        mix_period = [12, 1, 2]
    elif joption["mix_period"] == "中":
        mix_period = [3, 4, 10, 11]
    else:
        mix_period = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

    regex1 = re.compile("^C(.+)")
    mix_power_level = float(regex1.findall(joption["mix_power_level"])[0])

    lrecord = Mix.query.filter(
        Mix.mix_period.in_(mix_period),  # 温度段
        Mix.mix_concrete_variety == joption["mix_concrete_variety"],  # 混凝土品种
        Mix.mix_power_level == joption["mix_power_level"],  # 强度等级
        Mix.mix_impermeability_rating == joption["mix_impermeability_rating"],  # 抗渗等级
        Mix.mix_28d_strength >= mix_power_level,  # 检测强度不低于标准值
    ).all()

    match_lrecord = []
    for record in lrecord:
        if record.cement_breed_grade == joption["cement_breed_grade"]:
            match_lrecord.append(record)
    if len(match_lrecord) != 0:
        lrecord = match_lrecord

    match_lrecord = []
    for record in lrecord:
        if record.slag_breed_grade == joption["slag_breed_grade"]:
            match_lrecord.append(record)
    if len(match_lrecord) != 0:
        lrecord = match_lrecord

    match_lrecord = []
    for record in lrecord:
        if record.fly_sample_category == joption["fly_sample_category"]:
            match_lrecord.append(record)
    if len(match_lrecord) != 0:
        lrecord = match_lrecord

    match_lrecord = []
    for record in lrecord:
        if record.fly_breed_grade == joption["fly_breed_grade"]:
            match_lrecord.append(record)
    if len(match_lrecord) != 0:
        lrecord = match_lrecord

    return lrecord  # 一个记录列表，可能为空


# 对配合比列表中的记录进行评分,根据评分进行排序,返回排好序的配合比列表
def score_mix(joption, lrecord):
    # 评分规则1
    rule1 = {
        "mix_material_requirements": 10,  # 材料要求
        "work_performence": 5,  # 工作性能
        "mix_power_level": 20,  # 强度检测数据
        "mix_limit_expansion_rate": 7,  # 限制膨胀率
        # 耐久性技术要求没有
        "cement_supply_unit": 5,  # 水泥生产厂家
        "fine_aggregate": 8,  # 细集料品种、类型
        "coarse_aggregate": 8,  # 粗集料品种、类型
        "cement_28dcompression": 10,  # 水泥的抗压强度等级
        "slag_28d_activity_index": 3,  # 矿渣粉28d活性指数
        "fly_fineness": 3,  # 粉煤灰细度，需水量比
        "expansion_limit_expansion_rate": 3,  # 膨胀剂限制膨胀率
        "reduce_water_reduction_rate": 3,  # 减水剂减水率
        "limestone_fineness": 2,  # 石灰石粉细度
        "limestone_methylene_blue_value": 2,  # 石灰石粉亚甲蓝值
        "fly_loss_on_ignition": 2,  # 粉煤灰烧适量
        "expansion_28d_compressive_strength": 2,  # 膨胀剂28d抗压强度
    }

    # 评分规则2
    rule2 = {
        "work_performence": 5,  # 工作性能
        "mix_power_level": 25,  # 强度检测数据
        "mix_limit_expansion_rate": 7,  # 限制膨胀率
        # 耐久性技术要求没有
        "cement_supply_unit": 8,  # 水泥生产厂家
        "fine_aggregate": 8,  # 细集料品种、类型
        "coarse_aggregate": 8,  # 粗集料品种、类型
        "cement_28dcompression": 12,  # 水泥的抗压强度等级
        "slag_28d_activity_index": 3,  # 矿渣粉28d活性指数
        "fly_fineness": 3,  # 粉煤灰细度，需水量比
        "expansion_limit_expansion_rate": 3,  # 膨胀剂限制膨胀率
        "reduce_water_reduction_rate": 3,  # 减水剂减水率
        "limestone_fineness": 2,  # 石灰石粉细度
        "limestone_methylene_blue_value": 2,  # 石灰石粉亚甲蓝值
        "fly_loss_on_ignition": 2,  # 粉煤灰烧适量
        "expansion_28d_compressive_strength": 2,  # 膨胀剂28d抗压强度
    }

    lscore = []

    regex1 = re.compile("^C(.+)")
    mix_power_level = float(regex1.findall(joption["mix_power_level"])[0])

    for record in lrecord:
        score = 100
        if joption["mix_material_requirements"] != '':  # 如果用户选了材料要求
            # 材料要求没有匹配上
            if record.mix_material_requirements != joption["mix_material_requirements"]:
                score -= rule1["mix_material_requirements"]
            rule = rule1
        else:
            rule = rule2

        # 工作性能包括坍落度和扩展度
        if joption["mix_slump"] - 30 > record.mix_slump or joption["mix_expansion"] - 10 > record.mix_expansion:
            score -= rule["work_performence"]

        # 强度检测数据
        if mix_power_level < record.mix_28d_strength < mix_power_level * 1.1 or mix_power_level * 1.25 < record.mix_28d_strength < mix_power_level * 1.8:
            score -= 5
        elif mix_power_level * 1.8 < record.mix_28d_strength:
            score -= 10

        # 限制膨胀率
        if record.mix_limit_expansion_rate >= joption["mix_limit_expansion_rate"]:
            score -= rule["mix_limit_expansion_rate"]

        # 水泥生产厂家
        if record.cement_supply_unit != joption["cement_supply_unit"]:
            score -= rule["cement_supply_unit"]

        # 水泥28d抗压强度
        if record.cement_breed_grade in ["P·O42.5", "P·O42.5R"]:
            if 42.5 < record.cement_28d_compression < 47:
                score -= rule["cement_28dcompression"] / 2
            elif record.cement_28d_compression < 42.5:
                score -= rule["cement_28dcompression"]

        # 砂
        fine_joption = [0, 0, 0]
        if joption["fine_aggregate_1"] == "特细砂":
            fine_joption[0] = 1
        elif joption["fine_aggregate_1"] == "中砂":
            fine_joption[1] = 1
        elif joption["fine_aggregate_1"] == "粗砂":
            fine_joption[2] = 1

        if joption["fine_aggregate_2"] == "特细砂":
            fine_joption[0] = 1
        elif joption["fine_aggregate_2"] == "中砂":
            fine_joption[1] = 1
        elif joption["fine_aggregate_2"] == "粗砂":
            fine_joption[2] = 1

        if joption["fine_aggregate_3"] == "特细砂":
            fine_joption[0] = 1
        elif joption["fine_aggregate_3"] == "中砂":
            fine_joption[1] = 1
        elif joption["fine_aggregate_3"] == "粗砂":
            fine_joption[2] = 1

        fine_record = [0, 0, 0]
        if record.mix_special_fine_sand_dosage != -1:
            fine_record[0] = 1
        if record.mix_medium_sand_consumption != -1:
            fine_record[1] = 1
        if record.mix_coarse_sand_consumption != -1:
            fine_record[2] = 1

        if fine_joption == fine_record:  # 三个元素都相等
            pass
        else:
            sign = 0
            for j, l in zip(fine_joption, fine_record):
                if j == l:
                    sign = 1
                    break
            if sign == 1:
                score -= rule["fine_aggregate"] / 2
            else:
                score -= rule["fine_aggregate"]

        # 石
        coarse_joption = [0, 0]
        if joption["coarse_aggregate_1"] == "小石":
            coarse_joption[0] = 1
        elif joption["coarse_aggregate_1"] == "大石":
            coarse_joption[1] = 1

        if joption["coarse_aggregate_2"] == "小石":
            coarse_joption[0] = 1
        elif joption["coarse_aggregate_2"] == "大石":
            coarse_joption[1] = 1

        if joption["coarse_aggregate_3"] == "小石":
            coarse_joption[0] = 1
        elif joption["coarse_aggregate_3"] == "大石":
            coarse_joption[1] = 1

        coarse_record = [0, 0]
        if record.mix_small_stone_dosage != -1:
            coarse_record[0] = 1
        if record.mix_big_stone_dosage != -1:
            coarse_record[1] = 1

        if coarse_joption == coarse_record:  # 两个元素都相等
            pass
        else:
            sign = 0
            for j, l in zip(coarse_joption, coarse_record):
                if j == l:
                    sign = 1
                    break
            if sign == 1:
                score -= rule["coarse_aggregate"] / 2
            else:
                score -= rule["fcoarse_aggregate"]

        # 矿渣粉28d活性指数
        # if (record.slag_breed_grade == "S105" and record.slag_28d_activity_index < 105) or (
        #         record.slag_breed_grade == "S95" and record.slag_28d_activity_index < 95) or (
        #         record.slag_breed_grade == "S75" and record.slag_28d_activity_index < 75):
        if record.slag_breed_grade == -1:
            score -= rule["slag_28d_activity_index"]

        # 粉煤灰细度、需水量比
        # if (record.fly_breed_grade == "Ⅰ级" and (record.fly_fineness > 12 or record.fly_water_demand_ratio > 95)) or (
        #         record.fly_breed_grade == "Ⅱ级" and (
        #         record.fly_fineness > 30 or record.fly_water_demand_ratio > 95)) or (
        #         record.fly_breed_grade == "Ⅲ级" and (
        #         record.fly_fineness > 45 or record.fly_water_demand_ratio > 115)) or (
        #         record.fly_breed_grade not in ["Ⅰ级", "Ⅱ级", "Ⅲ级"]):
        if record.fly_fineness == -1 or record.fly_water_demand_ratio == -1:
            score -= rule["fly_fineness"]

        # 粉煤灰烧失量
        # if (record.fly_breed_grade == "Ⅰ级" and record.fly_loss_on_ignition > 5) or (
        #         record.fly_breed_grade == "Ⅱ级" and record.fly_loss_on_ignition > 8) or (
        #         record.fly_breed_grade == "Ⅲ级" and record.fly_loss_on_ignition > 10) or (
        #         record.fly_breed_grade not in ["Ⅰ级", "Ⅱ级", "Ⅲ级"]):
        if record.fly_loss_on_ignition == -1:
            score -= rule["fly_loss_on_ignition"]

        # 膨胀剂限制膨胀率：水中7d限制膨胀率
        # if (record.expansion_breed_grade == "Ⅰ级" and record.expansion_limit_expansion_rate < 0.035) or (
        #         record.expansion_breed_grade == "Ⅱ级" and record.expansion_limit_expansion_rate < 0.05):
        if record.expansion_limit_expansion_rate == -1:
            score -= rule["expansion_limit_expansion_rate"]

        # 膨胀剂限制膨胀率28d抗压强度
        # if (record.expansion_breed_grade == "Ⅰ级" and record.expansion_28d_compressive_strength < 22.5) or (
        #         record.expansion_breed_grade == "Ⅱ级" and record.expansion_28d_compressive_strength < 42.5):
        if record.expansion_28d_compressive_strength == -1:
            score -= rule["expansion_28d_compressive_strength"]

        # 外加剂（减水剂）减水率
        if record.reduce_water_reduction_rate == -1:
            score -= rule["reduce_water_reduction_rate"]

        # 石灰石粉细度
        if record.limestone_fineness == -1:
            score -= rule["limestone_fineness"]

        # 石灰石粉亚甲蓝值
        if record.limestone_methylene_blue_value == -1:
            score -= rule["limestone_methylene_blue_value"]
        lscore.append(score)

    # 从大到小排序,返回排序列表的索引
    lscore_index = sorted(range(len(lscore)), key=lambda k: lscore[k], reverse=True)

    print("打印评分")
    new_lrecord = []  # 排好序的记录
    for i in lscore_index:
        new_lrecord.append(lrecord[i])
        print(lscore[i])

    return new_lrecord


def main_initial(joption):
    lrecord = filter_mix(joption)
    lrecord = score_mix(joption, lrecord)
    return lrecord

