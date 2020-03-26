# 包装优化的那条记录
def package_best(joption, record, mix_apparent_density, unit_price):
    jdata = {}
    jdata["fine_aggregate_1"] = 0
    jdata["fine_aggregate_2"] = 0
    jdata["fine_aggregate_3"] = 0
    jdata["coarse_aggregate_1"] = 0
    jdata["coarse_aggregate_2"] = 0
    jdata["coarse_aggregate_3"] = 0

    if joption["mix_special_fine_sand_use"] == 1:
        jdata[joption["mix_special_fine_position"]] = round(record.mix_special_fine_sand_dosage)

    if joption["mix_medium_sand_use"] == 1:
        jdata[joption["mix_medium_sand_position"]] = round(record.mix_medium_sand_consumption)

    if joption["mix_coarse_sand_use"] == 1:
        jdata[joption["mix_coarse_sand_position"]] = round(record.mix_coarse_sand_consumption)

    if joption["mix_rocklet_use"] == 1:
        jdata[joption["mix_rocklet_position"]] = round(record.mix_small_stone_dosage)
    if joption["mix_boulder_use"] == 1:
        jdata[joption["mix_boulder_position"]] = round(record.mix_big_stone_dosage)

    jdata["mix_cement_consumption"] = round(record.mix_cement_consumption)
    jdata["mix_water_consumption"] = round(record.mix_water_consumption)
    jdata["mix_water_reducing_agent_dosage"] = round(record.mix_water_reducing_agent_dosage, 2)

    jdata["mix_fly_ash_dosage"] = round(record.mix_fly_ash_dosage)
    jdata["mix_slag_powder_consumption"] = round(record.mix_slag_powder_consumption)
    jdata["mix_limestone_powder_consumption"] = round(record.mix_limestone_powder_consumption)
    jdata["mix_expansion_agent_dosage"] = round(record.mix_expansion_agent_dosage)

    jdata["mix_other_materials"] = 0
    jdata["mix_apparent_density"] = round(mix_apparent_density)
    jdata["unit_price"] = round(unit_price / 1000, 2)
    jdata["mix_28d_strength"] = round(record.mix_28d_strength)
    return jdata


# 推送配合比主函数
def result_package_new(joption, jprice, lrecord):
    jresult = {}
    jresult["result_long"] = len(lrecord)
    jresult["result"] = []
    for record in lrecord:
        jone = {}
        jone["mix_cement_consumption"] = round(record.mix_cement_consumption)  # 水泥用量

        # 调整砂
        jone["fine_aggregate_1"] = 0
        jone["fine_aggregate_2"] = 0
        jone["fine_aggregate_3"] = 0

        if joption["mix_special_fine_sand_use"] == 1:
            jone[joption["mix_special_fine_position"]] = round(record.mix_special_fine_sand_dosage)
        if joption["mix_medium_sand_use"] == 1:
            jone[joption["mix_medium_sand_position"]] = round(record.mix_medium_sand_consumption)
        if joption["mix_coarse_sand_use"] == 1:
            jone[joption["mix_coarse_sand_position"]] = round(record.mix_coarse_sand_consumption)

        # 如果用户没有选粗砂，但是选了另外两种砂，把粗砂用量放到细集料3上
        if joption["mix_special_fine_sand_use"] == 1 and joption["mix_medium_sand_use"] == 1 and joption[
            "mix_coarse_sand_use"] == 0:
            jone["fine_aggregate_3"] = record.mix_coarse_sand_consumption
        # 如果用户没有选中砂，但是选了另外两种砂，把中砂用量放到细集料3上
        elif joption["mix_special_fine_sand_use"] == 1 and joption["mix_medium_sand_use"] == 0 and joption[
            "mix_coarse_sand_use"] == 1:
            jone["fine_aggregate_3"] = record.mix_medium_sand_consumption
        # 如果用户没有选特细砂，但是选了另外两种砂，把特细砂用量放到细集料3上
        elif joption["mix_special_fine_sand_use"] == 0 and joption["mix_medium_sand_use"] == 1 and joption[
            "mix_coarse_sand_use"] == 1:
            jone["fine_aggregate_3"] = record.mix_special_fine_sand_dosage
        # 如果用户没有选中砂、粗砂，但是选了特细砂，把中砂、粗砂用量放到细集料2、细集料3上
        elif joption["mix_special_fine_sand_use"] == 1 and joption["mix_medium_sand_use"] == 0 and joption[
            "mix_coarse_sand_use"] == 0:
            jone["fine_aggregate_2"] = record.mix_medium_sand_consumption
            jone["fine_aggregate_3"] = record.mix_coarse_sand_consumption
        # 如果用户没有选中砂、特细砂，但是选了粗砂，把中砂、特细砂用量放到细集料2、细集料3上
        elif joption["mix_special_fine_sand_use"] == 0 and joption["mix_medium_sand_use"] == 0 and joption[
            "mix_coarse_sand_use"] == 1:
            jone["fine_aggregate_2"] = record.mix_medium_sand_consumption
            jone["fine_aggregate_3"] = record.mix_special_fine_sand_dosage
        # 如果用户没有选特细砂、粗砂，但是选了中砂，把特细砂、粗砂用量放到细集料2、细集料3上
        elif joption["mix_special_fine_sand_use"] == 0 and joption["mix_medium_sand_use"] == 1 and joption[
            "mix_coarse_sand_use"] == 0:
            jone["fine_aggregate_2"] = record.mix_special_fine_sand_dosage
            jone["fine_aggregate_3"] = record.mix_coarse_sand_consumption

        # 调整石
        jone["coarse_aggregate_1"] = 0
        jone["coarse_aggregate_2"] = 0
        jone["coarse_aggregate_3"] = 0

        if joption["mix_rocklet_use"] == 1:
            jone[joption["mix_rocklet_position"]] = round(record.mix_small_stone_dosage)
        if joption["mix_boulder_use"] == 1:
            jone[joption["mix_boulder_position"]] = round(record.mix_big_stone_dosage)

        # 如果用户没有选小石，但是选了大石，把小石用量放到粗集料2上
        if joption["mix_rocklet_use"] == 0 and joption["mix_boulder_use"] == 1:
            jone["fine_aggregate_2"] += record.mix_small_stone_dosage
        # 如果用户没有选大石，但是选了小石，把大石用量放到粗集料2上
        elif joption["mix_boulder_use"] == 0 and joption["mix_rocklet_use"] == 1:
            jone["fine_aggregate_2"] += record.mix_big_stone_dosage

        jone["mix_special_fine_sand_dosage"] = round(record.mix_special_fine_sand_dosage)
        jone["mix_medium_sand_consumption"] = round(record.mix_medium_sand_consumption)
        jone["mix_coarse_sand_consumption"] = round(record.mix_coarse_sand_consumption)
        jone["mix_small_stone_dosage"] = round(record.mix_small_stone_dosage)
        jone["mix_big_stone_dosage"] = round(record.mix_big_stone_dosage)

        jone["mix_water_consumption"] = round(record.mix_water_consumption)  # 水用量
        jone["mix_water_reducing_agent_dosage"] = round(record.mix_water_reducing_agent_dosage, 2)  # 减水剂用量
        jone["mix_fly_ash_dosage"] = round(record.mix_fly_ash_dosage)  # 粉煤灰用量
        jone["mix_slag_powder_consumption"] = round(record.mix_slag_powder_consumption)  # 矿渣粉用量
        jone["mix_limestone_powder_consumption"] = round(record.mix_limestone_powder_consumption)  # 石灰石粉用量
        jone["mix_expansion_agent_dosage"] = round(record.mix_expansion_agent_dosage)  # 膨胀剂用量
        jone["mix_other_materials"] = 0

        '''28d抗压强度，表观密度，价格'''
        jone["mix_28d_strength"] = round(record.mix_28d_strength)
        jone["mix_apparent_density"] = round(
            jone["mix_cement_consumption"] + jone["mix_special_fine_sand_dosage"] + jone[
                "mix_medium_sand_consumption"] + jone["mix_coarse_sand_consumption"] + jone["mix_small_stone_dosage"] +
            jone["mix_big_stone_dosage"] + \
            jone["mix_water_consumption"] + jone[
                "mix_water_reducing_agent_dosage"] + jone["mix_fly_ash_dosage"] + jone[
                "mix_slag_powder_consumption"] + jone[
                "mix_limestone_powder_consumption"] + \
            jone["mix_expansion_agent_dosage"] + jone["mix_other_materials"])
        jone["mix_apparent_density_old"] = round(jone["mix_cement_consumption"] + jone["fine_aggregate_1"] + jone[
            "fine_aggregate_2"] + jone["fine_aggregate_3"] + jone["coarse_aggregate_1"] + jone["coarse_aggregate_2"] + \
                                                 jone["coarse_aggregate_3"] + jone["mix_water_consumption"] + jone[
                                                     "mix_water_reducing_agent_dosage"] + jone["mix_fly_ash_dosage"] +
                                                 jone[
                                                     "mix_slag_powder_consumption"] + jone[
                                                     "mix_limestone_powder_consumption"] + \
                                                 jone["mix_expansion_agent_dosage"] + jone["mix_other_materials"])
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

        jone["unit_price"] = round(jone["unit_price"] / 1000, 2)

        jone["mix_invo_id"] = record.mix_invo_id
        jresult["result"].append(jone)

    return jresult


'''
# 推送配合比主函数
def result_package(joption, jprice, lrecord, model):
    jresult = {}
    jresult["result_long"] = len(lrecord)
    jresult["result"] = []
    for record in lrecord:
        jone = {}
        jone["mix_cement_consumption"] = round(record.mix_cement_consumption)  # 水泥用量

        if joption["fine_aggregate_1"] == "特细砂":
            jone["fine_aggregate_1"] = round(record.mix_special_fine_sand_dosage)
        elif joption["fine_aggregate_1"] == "中砂":
            jone["fine_aggregate_1"] = round(record.mix_medium_sand_consumption)
        elif joption["fine_aggregate_1"] == "粗砂":
            jone["fine_aggregate_1"] = round(record.mix_coarse_sand_consumption)
        else:
            jone["fine_aggregate_1"] = 0

        if joption["fine_aggregate_2"] == "特细砂":
            jone["fine_aggregate_2"] = round(record.mix_special_fine_sand_dosage)
        elif joption["fine_aggregate_2"] == "中砂":
            jone["fine_aggregate_2"] = round(record.mix_medium_sand_consumption)
        elif joption["fine_aggregate_2"] == "粗砂":
            jone["fine_aggregate_2"] = round(record.mix_coarse_sand_consumption)
        else:
            jone["fine_aggregate_2"] = 0

        if joption["fine_aggregate_3"] == "特细砂":
            jone["fine_aggregate_3"] = (record.mix_special_fine_sand_dosage)
        elif joption["fine_aggregate_3"] == "中砂":
            jone["fine_aggregate_3"] = round(record.mix_medium_sand_consumption)
        elif joption["fine_aggregate_3"] == "粗砂":
            jone["fine_aggregate_3"] = round(record.mix_coarse_sand_consumption)
        else:
            jone["fine_aggregate_3"] = 0

        if joption["coarse_aggregate_1"] == "小石":
            jone["coarse_aggregate_1"] = round(record.mix_small_stone_dosage)
        elif joption["coarse_aggregate_1"] == "大石":
            jone["coarse_aggregate_1"] = round(record.mix_big_stone_dosage)
        else:
            jone["coarse_aggregate_1"] = 0

        if joption["coarse_aggregate_2"] == "小石":
            jone["coarse_aggregate_2"] = round(record.mix_small_stone_dosage)
        elif joption["coarse_aggregate_2"] == "大石":
            jone["coarse_aggregate_2"] = round(record.mix_big_stone_dosage)
        else:
            jone["coarse_aggregate_2"] = 0

        if joption["coarse_aggregate_3"] == "小石":
            jone["coarse_aggregate_3"] = round(record.mix_small_stone_dosage)
        elif joption["coarse_aggregate_3"] == "大石":
            jone["coarse_aggregate_3"] = round(record.mix_big_stone_dosage)
        else:
            jone["coarse_aggregate_3"] = 0

        jone["mix_water_consumption"] = round(record.mix_water_consumption)  # 水用量
        jone["mix_water_reducing_agent_dosage"] = round(record.mix_water_reducing_agent_dosage, 2)  # 减水剂用量

        if joption["fly_sample_category"] != "" or joption["fly_fineness"] != "":
            jone["mix_fly_ash_dosage"] = round(record.mix_fly_ash_dosage)  # 粉煤灰用量
        else:
            jone["mix_fly_ash_dosage"] = 0

        if joption["slag_breed_grade"] != "":
            jone["mix_slag_powder_consumption"] = round(record.mix_slag_powder_consumption)  # 矿渣粉用量
        else:
            jone["mix_slag_powder_consumption"] = 0

        if joption["limestone_fineness"] != -1:
            jone["mix_limestone_powder_consumption"] = round(record.mix_limestone_powder_consumption)  # 石灰石粉用量
        else:
            jone["mix_limestone_powder_consumption"] = 0

        if joption["expansion_breed_grade"] != "":
            jone["mix_expansion_agent_dosage"] = round(record.mix_expansion_agent_dosage)  # 膨胀剂用量
        else:
            jone["mix_expansion_agent_dosage"] = 0

        jone["mix_other_materials"] = 0

        jone["mix_28d_strength"] = round(record.mix_28d_strength)
        jone["mix_apparent_density"] = round(jone["mix_cement_consumption"] + jone["fine_aggregate_1"] + jone[
            "fine_aggregate_2"] + jone["fine_aggregate_3"] + jone["coarse_aggregate_1"] + jone["coarse_aggregate_2"] + \
                                             jone["coarse_aggregate_3"] + jone["mix_water_consumption"] + jone[
                                                 "mix_water_reducing_agent_dosage"] + jone["mix_fly_ash_dosage"] + jone[
                                                 "mix_slag_powder_consumption"] + jone[
                                                 "mix_limestone_powder_consumption"] + \
                                             jone["mix_expansion_agent_dosage"] + jone["mix_other_materials"])
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

        jone["unit_price"] = round(jone["unit_price"] / 1000, 2)
        jresult["result"].append(jone)

    if len(jresult["result"]) > 0:
        jresult["result"].insert(0, mix_ratio_optimization(joption, jprice, lrecord[0], model))  # 优化后的数据插入到最前面
    return jresult
'''
