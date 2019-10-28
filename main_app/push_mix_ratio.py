import numpy as np
import time


# def adjust_mix_ratio
def result_package_test(joption, jprice, lrecord, model):
    time1 = time.time()
    s = joption["mix_power_level"]
    l = joption["mix_concrete_variety"]
    user_stength = []
    rocklet = []
    boulder = []
    limestone_powder = []
    water_reduce_agent = []
    fine_sand = []
    medium_sand = []
    coarse_sand = []
    fly_ash = []
    cement = []
    water = []
    expansion_agent = []
    slag_powder = []
    category = []
    threed_strength = []
    mix_28d_strength = []
    design_max_water_binder_ratio = []
    design_unit_price = []
    unit_price = []
    max_water_binder_ratio = []
    m = []
    predict_28dstrength = []
    jadjust_result = {}
    jadjust_result["result_long"] = 1
    jadjust_result["result"] = []
    jdata = {}
    if len(lrecord) == 0:
        jadjust_result["result_long"] = 0
        return jadjust_result
    else:
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

        if l == "补偿收缩混凝土":
            category = 0
            if s == "C10":
                user_stength = 10
                max_water_binder_ratio = 0.60
            elif s == "C15":
                user_stength = 15
                max_water_binder_ratio = 0.60
            elif s == "C20":
                user_stength = 20
                max_water_binder_ratio = 0.60
            elif s == "C25":
                user_stength = 25
                max_water_binder_ratio = 0.60
            elif s == "C30":
                user_stength = 30
                max_water_binder_ratio = 0.55
            elif s == "C35":
                user_stength = 35
                max_water_binder_ratio = 0.50
            elif s == "C40":
                user_stength = 40
                max_water_binder_ratio = 0.45
            elif s == "C45":
                user_stength = 45
                max_water_binder_ratio = 0.40
            elif s == "C50":
                user_stength = 50
                max_water_binder_ratio = 0.36

            if lrecord[0].mix_3d_intensity > 3:
                threed_strength = lrecord[0].mix_3d_intensity
            else:
                threed_strength = 33

            for i in range(10):
                for i in range(500):
                    rocklet = lrecord[0].mix_small_stone_dosage
                    boulder = lrecord[0].mix_big_stone_dosage
                    limestone_powder = lrecord[0].mix_limestone_powder_consumption + 10 * (-1 * np.random.rand())
                    water_reduce_agent = lrecord[0].mix_water_reducing_agent_dosage + 3 * (-1 + 2 * np.random.rand())
                    fine_sand = lrecord[0].mix_special_fine_sand_dosage
                    medium_sand = lrecord[0].mix_medium_sand_consumption
                    coarse_sand = lrecord[0].mix_coarse_sand_consumption
                    fly_ash = lrecord[0].mix_fly_ash_dosage + 10 * (-1 * np.random.rand())
                    cement = lrecord[0].mix_cement_consumption + 10 * (-1 + 2 * np.random.rand())
                    water = lrecord[0].mix_water_consumption + lrecord[0].mix_recycled_water_consumption + 20 * (
                            -1 + 2 * np.random.rand())
                    expansion_agent = lrecord[0].mix_expansion_agent_dosage
                    slag_powder = lrecord[0].mix_slag_powder_consumption

                    mix_28d_strength = lrecord[0].mix_28d_strength
                    design_max_water_binder_ratio = water / (
                            limestone_powder + fly_ash + cement + expansion_agent + slag_powder)
                    if design_max_water_binder_ratio <= 0.5 and (
                            limestone_powder + fly_ash + cement + expansion_agent + slag_powder) >= 350:
                        unit_price = (lrecord[0].mix_special_fine_sand_dosage) * (
                        jprice["mix_special_fine_sand_dosage"]) + (
                                         lrecord[0].mix_medium_sand_consumption) * (
                                     jprice["mix_medium_sand_consumption"]) + \
                                     (lrecord[0].mix_coarse_sand_consumption) * (
                                     jprice["mix_coarse_sand_consumption"]) + (
                                         lrecord[0].mix_small_stone_dosage) * (jprice["mix_rocklet_consumption"]) + \
                                     (lrecord[0].mix_big_stone_dosage) * (jprice["mix_boulder_consumption"]) + (
                                         lrecord[0].mix_limestone_powder_consumption) * (jprice["limestone_powder"]) + \
                                     (lrecord[0].mix_water_reducing_agent_dosage) * (jprice["water_reduce_agent"]) + (
                                         lrecord[0].mix_fly_ash_dosage) * (jprice["fly_ash"]) + (
                                         lrecord[0].mix_cement_consumption) * (jprice["cement"]) + \
                                     (lrecord[0].mix_water_consumption + lrecord[0].mix_recycled_water_consumption) * \
                                     jprice[
                                         "water"] + \
                                     (lrecord[0].mix_expansion_agent_dosage) * (jprice["expansion_agent"]) + (
                                         lrecord[0].mix_slag_powder_consumption) * (jprice["slag_powder"])

                        design_unit_price = (fine_sand) * (jprice["mix_special_fine_sand_dosage"]) + (medium_sand) * (
                            jprice["mix_medium_sand_consumption"]) + \
                                            (coarse_sand) * (jprice["mix_coarse_sand_consumption"]) + (rocklet) * (
                                                jprice["mix_rocklet_consumption"]) + \
                                            (boulder) * (jprice["mix_boulder_consumption"]) + (limestone_powder) * (
                                                jprice["limestone_powder"]) + \
                                            (water_reduce_agent) * (jprice["water_reduce_agent"]) + (fly_ash) * (
                                                jprice["fly_ash"]) + (cement) * (jprice["cement"]) + \
                                            (water) * jprice["water"] + (expansion_agent) * (
                                            jprice["expansion_agent"]) + (
                                                slag_powder) * (jprice["slag_powder"])
                        data = [rocklet, boulder, limestone_powder, water_reduce_agent, fine_sand, medium_sand,
                                coarse_sand,
                                fly_ash, cement, water, expansion_agent, slag_powder, category, threed_strength]
                        data = np.array(data)
                        data = data.reshape(1, 14)
                        m = model.predict(data)
                        m = m.tolist()[0][0]
                        if m >= user_stength:
                            if design_unit_price < unit_price:
                                predict_28dstrength = m
                            else:
                                predict_28dstrength = 0
        elif l == "常规混凝土":
            category = 1
            if s == "C10":
                user_stength = 10
                max_water_binder_ratio = 0.60
            elif s == "C15":
                user_stength = 15
                max_water_binder_ratio = 0.60
            elif s == "C20":
                user_stength = 20
                max_water_binder_ratio = 0.60
            elif s == "C25":
                user_stength = 25
                max_water_binder_ratio = 0.60
            elif s == "C30":
                user_stength = 30
                max_water_binder_ratio = 0.55
            elif s == "C35":
                user_stength = 35
                max_water_binder_ratio = 0.50
            elif s == "C40":
                user_stength = 40
                max_water_binder_ratio = 0.45
            elif s == "C45":
                user_stength = 45
                max_water_binder_ratio = 0.40
            elif s == "C50":
                user_stength = 50
                max_water_binder_ratio = 0.36
            if lrecord[0].mix_3d_intensity > 3:
                threed_strength = lrecord[0].mix_3d_intensity
            else:
                threed_strength = 33
            for i in range(10):
                for i in range(500):
                    rocklet = lrecord[0].mix_small_stone_dosage
                    boulder = lrecord[0].mix_big_stone_dosage
                    limestone_powder = lrecord[0].mix_limestone_powder_consumption + 10 * (-1 * np.random.rand())
                    water_reduce_agent = lrecord[0].mix_water_reducing_agent_dosage + 3 * (-1 + 2 * np.random.rand())
                    fine_sand = lrecord[0].mix_special_fine_sand_dosage
                    medium_sand = lrecord[0].mix_medium_sand_consumption
                    coarse_sand = lrecord[0].mix_coarse_sand_consumption
                    fly_ash = lrecord[0].mix_fly_ash_dosage + 10 * (-1 * np.random.rand())
                    cement = lrecord[0].mix_cement_consumption + 10 * (-1 + 2 * np.random.rand())
                    water = lrecord[0].mix_water_consumption + lrecord[0].mix_recycled_water_consumption + 20 * (
                            -1 + 2 * np.random.rand())
                    expansion_agent = lrecord[0].mix_expansion_agent_dosage
                    slag_powder = lrecord[0].mix_slag_powder_consumption
                    mix_28d_strength = lrecord[0].mix_28d_strength
                    design_max_water_binder_ratio = water / (
                            limestone_powder + fly_ash + cement + expansion_agent + slag_powder)
                    if design_max_water_binder_ratio <= max_water_binder_ratio:
                        unit_price = (lrecord[0].mix_special_fine_sand_dosage) * (
                            jprice["mix_special_fine_sand_dosage"]) + (
                                         lrecord[0].mix_medium_sand_consumption) * (
                                     jprice["mix_medium_sand_consumption"]) + \
                                     (lrecord[0].mix_coarse_sand_consumption) * (
                                     jprice["mix_coarse_sand_consumption"]) + (
                                         lrecord[0].mix_small_stone_dosage) * (jprice["mix_rocklet_consumption"]) + \
                                     (lrecord[0].mix_big_stone_dosage) * (jprice["mix_boulder_consumption"]) + (
                                         lrecord[0].mix_limestone_powder_consumption) * (jprice["limestone_powder"]) + \
                                     (lrecord[0].mix_water_reducing_agent_dosage) * (jprice["water_reduce_agent"]) + (
                                         lrecord[0].mix_fly_ash_dosage) * (jprice["fly_ash"]) + (
                                         lrecord[0].mix_cement_consumption) * (jprice["cement"]) + \
                                     (lrecord[0].mix_water_consumption + lrecord[0].mix_recycled_water_consumption) * \
                                     jprice[
                                         "water"] + \
                                     (lrecord[0].mix_expansion_agent_dosage) * (jprice["expansion_agent"]) + (
                                         lrecord[0].mix_slag_powder_consumption) * (jprice["slag_powder"])

                        design_unit_price = (fine_sand) * (jprice["mix_special_fine_sand_dosage"]) + (medium_sand) * (
                            jprice["mix_medium_sand_consumption"]) + \
                                            (coarse_sand) * (jprice["mix_coarse_sand_consumption"]) + (rocklet) * (
                                                jprice["mix_rocklet_consumption"]) + \
                                            (boulder) * (jprice["mix_boulder_consumption"]) + (limestone_powder) * (
                                                jprice["limestone_powder"]) + \
                                            (water_reduce_agent) * (jprice["water_reduce_agent"]) + (fly_ash) * (
                                                jprice["fly_ash"]) + (cement) * (jprice["cement"]) + \
                                            (water) * jprice["water"] + (expansion_agent) * (
                                            jprice["expansion_agent"]) + (
                                                slag_powder) * (jprice["slag_powder"])
                        data = [rocklet, boulder, limestone_powder, water_reduce_agent, fine_sand, medium_sand,
                                coarse_sand,
                                fly_ash, cement, water, expansion_agent, slag_powder, category, threed_strength]
                        data = np.array(data)
                        data = data.reshape(1, 14)
                        m = model.predict(data)
                        m = m.tolist()[0][0]
                        if m >= user_stength:
                            if design_unit_price < unit_price:
                                predict_28dstrength = m
                            else:
                                predict_28dstrength = 0
        elif l == "大体积混凝土":
            category = 2
            if s == "C10":
                user_stength = 10
                max_water_binder_ratio = 0.60
            elif s == "C15":
                user_stength = 15
                max_water_binder_ratio = 0.60
            elif s == "C20":
                user_stength = 20
                max_water_binder_ratio = 0.60
            elif s == "C25":
                user_stength = 25
                max_water_binder_ratio = 0.60
            elif s == "C30":
                user_stength = 30
                max_water_binder_ratio = 0.55
            elif s == "C35":
                user_stength = 35
                max_water_binder_ratio = 0.50
            elif s == "C40":
                user_stength = 40
                max_water_binder_ratio = 0.45
            elif s == "C45":
                user_stength = 45
                max_water_binder_ratio = 0.40
            elif s == "C50":
                user_stength = 50
                max_water_binder_ratio = 0.36
            if lrecord[0].mix_3d_intensity > 3:
                threed_strength = lrecord[0].mix_3d_intensity
            else:
                threed_strength = 33

            for i in range(10):
                for i in range(500):
                    rocklet = lrecord[0].mix_small_stone_dosage
                    boulder = lrecord[0].mix_big_stone_dosage
                    limestone_powder = lrecord[0].mix_limestone_powder_consumption + 10 * (-1 * np.random.rand())
                    water_reduce_agent = lrecord[0].mix_water_reducing_agent_dosage + 3 * (-1 + 2 * np.random.rand())
                    fine_sand = lrecord[0].mix_special_fine_sand_dosage
                    medium_sand = lrecord[0].mix_medium_sand_consumption
                    coarse_sand = lrecord[0].mix_coarse_sand_consumption
                    fly_ash = lrecord[0].mix_fly_ash_dosage + 10 * (-1 * np.random.rand())
                    cement = lrecord[0].mix_cement_consumption + 10 * (-1 + 2 * np.random.rand())
                    water = lrecord[0].mix_water_consumption + lrecord[0].mix_recycled_water_consumption + 20 * (
                            -1 + 2 * np.random.rand())
                    expansion_agent = lrecord[0].mix_expansion_agent_dosage
                    slag_powder = lrecord[0].mix_slag_powder_consumption

                    mix_28d_strength = lrecord[0].mix_28d_strength
                    design_max_water_binder_ratio = water / (
                            limestone_powder + fly_ash + cement + expansion_agent + slag_powder)
                    if design_max_water_binder_ratio <= 0.55 and water <= 175:
                        unit_price = (lrecord[0].mix_special_fine_sand_dosage) * (
                        jprice["mix_special_fine_sand_dosage"]) + (
                                         lrecord[0].mix_medium_sand_consumption) * (
                                     jprice["mix_medium_sand_consumption"]) + \
                                     (lrecord[0].mix_coarse_sand_consumption) * (
                                     jprice["mix_coarse_sand_consumption"]) + (
                                         lrecord[0].mix_small_stone_dosage) * (jprice["mix_rocklet_consumption"]) + \
                                     (lrecord[0].mix_big_stone_dosage) * (jprice["mix_boulder_consumption"]) + (
                                         lrecord[0].mix_limestone_powder_consumption) * (jprice["limestone_powder"]) + \
                                     (lrecord[0].mix_water_reducing_agent_dosage) * (jprice["water_reduce_agent"]) + (
                                         lrecord[0].mix_fly_ash_dosage) * (jprice["fly_ash"]) + (
                                         lrecord[0].mix_cement_consumption) * (jprice["cement"]) + \
                                     (lrecord[0].mix_water_consumption + lrecord[0].mix_recycled_water_consumption) * \
                                     jprice[
                                         "water"] + \
                                     (lrecord[0].mix_expansion_agent_dosage) * (jprice["expansion_agent"]) + (
                                         lrecord[0].mix_slag_powder_consumption) * (jprice["slag_powder"])

                        design_unit_price = (fine_sand) * (jprice["mix_special_fine_sand_dosage"]) + (medium_sand) * (
                            jprice["mix_medium_sand_consumption"]) + \
                                            (coarse_sand) * (jprice["mix_coarse_sand_consumption"]) + (rocklet) * (
                                                jprice["mix_rocklet_consumption"]) + \
                                            (boulder) * (jprice["mix_boulder_consumption"]) + (limestone_powder) * (
                                                jprice["limestone_powder"]) + \
                                            (water_reduce_agent) * (jprice["water_reduce_agent"]) + (fly_ash) * (
                                                jprice["fly_ash"]) + (cement) * (jprice["cement"]) + \
                                            (water) * jprice["water"] + (expansion_agent) * (
                                            jprice["expansion_agent"]) + (
                                                slag_powder) * (jprice["slag_powder"])
                        data = [rocklet, boulder, limestone_powder, water_reduce_agent, fine_sand, medium_sand,
                                coarse_sand,
                                fly_ash, cement, water, expansion_agent, slag_powder, category, threed_strength]
                        data = np.array(data)
                        data = data.reshape(1, 14)
                        s = model.predict(data)
                        m = model.predict(data)
                        m = m.tolist()[0][0]
                        if m >= user_stength:
                            if design_unit_price < unit_price:
                                predict_28dstrength = m
                            else:
                                predict_28dstrength = 0
        elif l == "防水混凝土":
            category = 3
            if s == "C10":
                user_stength = 10
                max_water_binder_ratio = 0.60
            elif s == "C15":
                user_stength = 15
                max_water_binder_ratio = 0.60
            elif s == "C20":
                user_stength = 20
                max_water_binder_ratio = 0.60
            elif s == "C25":
                user_stength = 25
                max_water_binder_ratio = 0.60
            elif s == "C30":
                user_stength = 30
                max_water_binder_ratio = 0.55
            elif s == "C35":
                user_stength = 35
                max_water_binder_ratio = 0.50
            elif s == "C40":
                user_stength = 40
                max_water_binder_ratio = 0.45
            elif s == "C45":
                user_stength = 45
                max_water_binder_ratio = 0.40
            elif s == "C50":
                user_stength = 50
                max_water_binder_ratio = 0.36
            if lrecord[0].mix_3d_intensity > 3:
                threed_strength = lrecord[0].mix_3d_intensity
            else:
                threed_strength = 33
            for i in range(10):
                for i in range(500):
                    rocklet = lrecord[0].mix_small_stone_dosage
                    boulder = lrecord[0].mix_big_stone_dosage
                    limestone_powder = lrecord[0].mix_limestone_powder_consumption + 10 * (-1 * np.random.rand())
                    water_reduce_agent = lrecord[0].mix_water_reducing_agent_dosage + 3 * (-1 + 2 * np.random.rand())
                    fine_sand = lrecord[0].mix_special_fine_sand_dosage
                    medium_sand = lrecord[0].mix_medium_sand_consumption
                    coarse_sand = lrecord[0].mix_coarse_sand_consumption
                    fly_ash = lrecord[0].mix_fly_ash_dosage + 10 * (-1 * np.random.rand())
                    cement = lrecord[0].mix_cement_consumption + 10 * (-1 + 2 * np.random.rand())
                    water = lrecord[0].mix_water_consumption + lrecord[0].mix_recycled_water_consumption + 20 * (
                            -1 + 2 * np.random.rand())
                    expansion_agent = lrecord[0].mix_expansion_agent_dosage
                    slag_powder = lrecord[0].mix_slag_powder_consumption

                    mix_28d_strength = lrecord[0].mix_28d_strength
                    design_max_water_binder_ratio = water / (
                            limestone_powder + fly_ash + cement + expansion_agent + slag_powder)
                    if design_max_water_binder_ratio <= 0.5 and (
                            limestone_powder + fly_ash + cement + expansion_agent + slag_powder) >= 320 and cement >= 260:
                        unit_price = (lrecord[0].mix_special_fine_sand_dosage) * (
                        jprice["mix_special_fine_sand_dosage"]) + (
                                         lrecord[0].mix_medium_sand_consumption) * (
                                     jprice["mix_medium_sand_consumption"]) + \
                                     (lrecord[0].mix_coarse_sand_consumption) * (
                                     jprice["mix_coarse_sand_consumption"]) + (
                                         lrecord[0].mix_small_stone_dosage) * (jprice["mix_rocklet_consumption"]) + \
                                     (lrecord[0].mix_big_stone_dosage) * (jprice["mix_boulder_consumption"]) + (
                                         lrecord[0].mix_limestone_powder_consumption) * (jprice["limestone_powder"]) + \
                                     (lrecord[0].mix_water_reducing_agent_dosage) * (jprice["water_reduce_agent"]) + (
                                         lrecord[0].mix_fly_ash_dosage) * (jprice["fly_ash"]) + (
                                         lrecord[0].mix_cement_consumption) * (jprice["cement"]) + \
                                     (lrecord[0].mix_water_consumption + lrecord[0].mix_recycled_water_consumption) * \
                                     jprice[
                                         "water"] + \
                                     (lrecord[0].mix_expansion_agent_dosage) * (jprice["expansion_agent"]) + (
                                         lrecord[0].mix_slag_powder_consumption) * (jprice["slag_powder"])

                        design_unit_price = (fine_sand) * (jprice["mix_special_fine_sand_dosage"]) + (medium_sand) * (
                            jprice["mix_medium_sand_consumption"]) + \
                                            (coarse_sand) * (jprice["mix_coarse_sand_consumption"]) + (rocklet) * (
                                                jprice["mix_rocklet_consumption"]) + \
                                            (boulder) * (jprice["mix_boulder_consumption"]) + (limestone_powder) * (
                                                jprice["limestone_powder"]) + \
                                            (water_reduce_agent) * (jprice["water_reduce_agent"]) + (fly_ash) * (
                                                jprice["fly_ash"]) + (cement) * (jprice["cement"]) + \
                                            (water) * jprice["water"] + (expansion_agent) * (
                                            jprice["expansion_agent"]) + (
                                                slag_powder) * (jprice["slag_powder"])
                        data = [rocklet, boulder, limestone_powder, water_reduce_agent, fine_sand, medium_sand,
                                coarse_sand,
                                fly_ash, cement, water, expansion_agent, slag_powder, category, threed_strength]
                        data = np.array(data)
                        data = data.reshape(1, 14)
                        s = model.predict(data)
                        m = model.predict(data)
                        m = m.tolist()[0][0]
                        if m >= user_stength:
                            if design_unit_price < unit_price:
                                predict_28dstrength = m
                            else:
                                predict_28dstrength = 0
        elif l == "钢纤维混凝土":
            category = 4
            if s == "C10":
                user_stength = 10
                max_water_binder_ratio = 0.60
            elif s == "C15":
                user_stength = 15
                max_water_binder_ratio = 0.60
            elif s == "C20":
                user_stength = 20
                max_water_binder_ratio = 0.60
            elif s == "C25":
                user_stength = 25
                max_water_binder_ratio = 0.60
            elif s == "C30":
                user_stength = 30
                max_water_binder_ratio = 0.55
            elif s == "C35":
                user_stength = 35
                max_water_binder_ratio = 0.50
            elif s == "C40":
                user_stength = 40
                max_water_binder_ratio = 0.45
            elif s == "C45":
                user_stength = 45
                max_water_binder_ratio = 0.40
            elif s == "C50":
                user_stength = 50
                max_water_binder_ratio = 0.36
            if lrecord[0].mix_3d_intensity > 3:
                threed_strength = lrecord[0].mix_3d_intensity
            else:
                threed_strength = 33
            for i in range(10):
                for i in range(500):
                    rocklet = lrecord[0].mix_small_stone_dosage
                    boulder = lrecord[0].mix_big_stone_dosage
                    limestone_powder = lrecord[0].mix_limestone_powder_consumption + 10 * (-1 * np.random.rand())
                    water_reduce_agent = lrecord[0].mix_water_reducing_agent_dosage + 3 * (-1 + 2 * np.random.rand())
                    fine_sand = lrecord[0].mix_special_fine_sand_dosage
                    medium_sand = lrecord[0].mix_medium_sand_consumption
                    coarse_sand = lrecord[0].mix_coarse_sand_consumption
                    fly_ash = lrecord[0].mix_fly_ash_dosage + 10 * (-1 * np.random.rand())
                    cement = lrecord[0].mix_cement_consumption + 10 * (-1 + 2 * np.random.rand())
                    water = lrecord[0].mix_water_consumption + lrecord[0].mix_recycled_water_consumption + 20 * (
                            -1 + 2 * np.random.rand())
                    expansion_agent = lrecord[0].mix_expansion_agent_dosage
                    slag_powder = lrecord[0].mix_slag_powder_consumption

                    mix_28d_strength = lrecord[0].mix_28d_strength
                    design_max_water_binder_ratio = water / (
                            limestone_powder + fly_ash + cement + expansion_agent + slag_powder)
                    if design_max_water_binder_ratio <= max_water_binder_ratio:
                        unit_price = (lrecord[0].mix_special_fine_sand_dosage) * (
                        jprice["mix_special_fine_sand_dosage"]) + (
                                         lrecord[0].mix_medium_sand_consumption) * (
                                     jprice["mix_medium_sand_consumption"]) + \
                                     (lrecord[0].mix_coarse_sand_consumption) * (
                                     jprice["mix_coarse_sand_consumption"]) + (
                                         lrecord[0].mix_small_stone_dosage) * (jprice["mix_rocklet_consumption"]) + \
                                     (lrecord[0].mix_big_stone_dosage) * (jprice["mix_boulder_consumption"]) + (
                                         lrecord[0].mix_limestone_powder_consumption) * (jprice["limestone_powder"]) + \
                                     (lrecord[0].mix_water_reducing_agent_dosage) * (jprice["water_reduce_agent"]) + (
                                         lrecord[0].mix_fly_ash_dosage) * (jprice["fly_ash"]) + (
                                         lrecord[0].mix_cement_consumption) * (jprice["cement"]) + \
                                     (lrecord[0].mix_water_consumption + lrecord[0].mix_recycled_water_consumption) * \
                                     jprice[
                                         "water"] + \
                                     (lrecord[0].mix_expansion_agent_dosage) * (jprice["expansion_agent"]) + (
                                         lrecord[0].mix_slag_powder_consumption) * (jprice["slag_powder"])

                        design_unit_price = (fine_sand) * (jprice["mix_special_fine_sand_dosage"]) + (medium_sand) * (
                            jprice["mix_medium_sand_consumption"]) + \
                                            (coarse_sand) * (jprice["mix_coarse_sand_consumption"]) + (rocklet) * (
                                                jprice["mix_rocklet_consumption"]) + \
                                            (boulder) * (jprice["mix_boulder_consumption"]) + (limestone_powder) * (
                                                jprice["limestone_powder"]) + \
                                            (water_reduce_agent) * (jprice["water_reduce_agent"]) + (fly_ash) * (
                                                jprice["fly_ash"]) + (cement) * (jprice["cement"]) + \
                                            (water) * jprice["water"] + (expansion_agent) * (
                                            jprice["expansion_agent"]) + (
                                                slag_powder) * (jprice["slag_powder"])
                        data = [rocklet, boulder, limestone_powder, water_reduce_agent, fine_sand, medium_sand,
                                coarse_sand,
                                fly_ash, cement, water, expansion_agent, slag_powder, category, threed_strength]
                        data = np.array(data)
                        data = data.reshape(1, 14)
                        m = model.predict(data)
                        m = m.tolist()[0][0]
                        if m >= user_stength:
                            if design_unit_price < unit_price:
                                predict_28dstrength = m
                            else:
                                predict_28dstrength = 0
        elif l == "聚丙烯纤维混凝土":
            category = 5
            if s == "C10":
                user_stength = 10
                max_water_binder_ratio = 0.60
            elif s == "C15":
                user_stength = 15
                max_water_binder_ratio = 0.60
            elif s == "C20":
                user_stength = 20
                max_water_binder_ratio = 0.60
            elif s == "C25":
                user_stength = 25
                max_water_binder_ratio = 0.60
            elif s == "C30":
                user_stength = 30
                max_water_binder_ratio = 0.55
            elif s == "C35":
                user_stength = 35
                max_water_binder_ratio = 0.50
            elif s == "C40":
                user_stength = 40
                max_water_binder_ratio = 0.45
            elif s == "C45":
                user_stength = 45
                max_water_binder_ratio = 0.40
            elif s == "C50":
                user_stength = 50
                max_water_binder_ratio = 0.36
            if lrecord[0].mix_3d_intensity > 3:
                threed_strength = lrecord[0].mix_3d_intensity
            else:
                threed_strength = 33
            for i in range(10):
                for i in range(500):
                    rocklet = lrecord[0].mix_small_stone_dosage
                    boulder = lrecord[0].mix_big_stone_dosage
                    limestone_powder = lrecord[0].mix_limestone_powder_consumption + 10 * (-1 * np.random.rand())
                    water_reduce_agent = lrecord[0].mix_water_reducing_agent_dosage + 3 * (-1 + 2 * np.random.rand())
                    fine_sand = lrecord[0].mix_special_fine_sand_dosage
                    medium_sand = lrecord[0].mix_medium_sand_consumption
                    coarse_sand = lrecord[0].mix_coarse_sand_consumption
                    fly_ash = lrecord[0].mix_fly_ash_dosage + 10 * (-1 * np.random.rand())
                    cement = lrecord[0].mix_cement_consumption + 10 * (-1 + 2 * np.random.rand())
                    water = lrecord[0].mix_water_consumption + lrecord[0].mix_recycled_water_consumption + 20 * (
                            -1 + 2 * np.random.rand())
                    expansion_agent = lrecord[0].mix_expansion_agent_dosage
                    slag_powder = lrecord[0].mix_slag_powder_consumption

                    mix_28d_strength = lrecord[0].mix_28d_strength
                    design_max_water_binder_ratio = water / (
                            limestone_powder + fly_ash + cement + expansion_agent + slag_powder)
                    if design_max_water_binder_ratio <= max_water_binder_ratio:
                        unit_price = (lrecord[0].mix_special_fine_sand_dosage) * (
                        jprice["mix_special_fine_sand_dosage"]) + (
                                         lrecord[0].mix_medium_sand_consumption) * (
                                     jprice["mix_medium_sand_consumption"]) + \
                                     (lrecord[0].mix_coarse_sand_consumption) * (
                                     jprice["mix_coarse_sand_consumption"]) + (
                                         lrecord[0].mix_small_stone_dosage) * (jprice["mix_rocklet_consumption"]) + \
                                     (lrecord[0].mix_big_stone_dosage) * (jprice["mix_boulder_consumption"]) + (
                                         lrecord[0].mix_limestone_powder_consumption) * (jprice["limestone_powder"]) + \
                                     (lrecord[0].mix_water_reducing_agent_dosage) * (jprice["water_reduce_agent"]) + (
                                         lrecord[0].mix_fly_ash_dosage) * (jprice["fly_ash"]) + (
                                         lrecord[0].mix_cement_consumption) * (jprice["cement"]) + \
                                     (lrecord[0].mix_water_consumption + lrecord[0].mix_recycled_water_consumption) * \
                                     jprice[
                                         "water"] + \
                                     (lrecord[0].mix_expansion_agent_dosage) * (jprice["expansion_agent"]) + (
                                         lrecord[0].mix_slag_powder_consumption) * (jprice["slag_powder"])

                        design_unit_price = (fine_sand) * (jprice["mix_special_fine_sand_dosage"]) + (medium_sand) * (
                            jprice["mix_medium_sand_consumption"]) + \
                                            (coarse_sand) * (jprice["mix_coarse_sand_consumption"]) + (rocklet) * (
                                                jprice["mix_rocklet_consumption"]) + \
                                            (boulder) * (jprice["mix_boulder_consumption"]) + (limestone_powder) * (
                                                jprice["limestone_powder"]) + \
                                            (water_reduce_agent) * (jprice["water_reduce_agent"]) + (fly_ash) * (
                                                jprice["fly_ash"]) + (cement) * (jprice["cement"]) + \
                                            (water) * jprice["water"] + (expansion_agent) * (
                                            jprice["expansion_agent"]) + (
                                                slag_powder) * (jprice["slag_powder"])
                        data = [rocklet, boulder, limestone_powder, water_reduce_agent, fine_sand, medium_sand,
                                coarse_sand,
                                fly_ash, cement, water, expansion_agent, slag_powder, category, threed_strength]
                        data = np.array(data)
                        data = data.reshape(1, 14)
                        m = model.predict(data)
                        m = m.tolist()[0][0]
                        if m >= user_stength:
                            if design_unit_price < unit_price:
                                predict_28dstrength = m
                            else:
                                predict_28dstrength = 0
        elif l == "抗渗混凝土":
            category = 6
            if s == "C10":
                user_stength = 10
                max_water_binder_ratio = 0.60
            elif s == "C15":
                user_stength = 15
                max_water_binder_ratio = 0.60
            elif s == "C20":
                user_stength = 20
                max_water_binder_ratio = 0.60
            elif s == "C25":
                user_stength = 25
                max_water_binder_ratio = 0.60
            elif s == "C30":
                user_stength = 30
                max_water_binder_ratio = 0.55
            elif s == "C35":
                user_stength = 35
                max_water_binder_ratio = 0.50
            elif s == "C40":
                user_stength = 40
                max_water_binder_ratio = 0.45
            elif s == "C45":
                user_stength = 45
                max_water_binder_ratio = 0.40
            elif s == "C50":
                user_stength = 50
                max_water_binder_ratio = 0.36
            if lrecord[0].mix_3d_intensity > 3:
                threed_strength = lrecord[0].mix_3d_intensity
            else:
                threed_strength = 33
            for i in range(10):
                for i in range(500):
                    rocklet = lrecord[0].mix_small_stone_dosage
                    boulder = lrecord[0].mix_big_stone_dosage
                    limestone_powder = lrecord[0].mix_limestone_powder_consumption + 10 * (-1 * np.random.rand())
                    water_reduce_agent = lrecord[0].mix_water_reducing_agent_dosage + 3 * (-1 + 2 * np.random.rand())
                    fine_sand = lrecord[0].mix_special_fine_sand_dosage
                    medium_sand = lrecord[0].mix_medium_sand_consumption
                    coarse_sand = lrecord[0].mix_coarse_sand_consumption
                    fly_ash = lrecord[0].mix_fly_ash_dosage + 10 * (-1 * np.random.rand())
                    cement = lrecord[0].mix_cement_consumption + 10 * (-1 + 2 * np.random.rand())
                    water = lrecord[0].mix_water_consumption + lrecord[0].mix_recycled_water_consumption + 20 * (
                            -1 + 2 * np.random.rand())
                    expansion_agent = lrecord[0].mix_expansion_agent_dosage
                    slag_powder = lrecord[0].mix_slag_powder_consumption

                    mix_28d_strength = lrecord[0].mix_28d_strength
                    design_max_water_binder_ratio = water / (
                            limestone_powder + fly_ash + cement + expansion_agent + slag_powder)
                    if design_max_water_binder_ratio <= max_water_binder_ratio:
                        unit_price = (lrecord[0].mix_special_fine_sand_dosage) * (
                        jprice["mix_special_fine_sand_dosage"]) + (
                                         lrecord[0].mix_medium_sand_consumption) * (
                                     jprice["mix_medium_sand_consumption"]) + \
                                     (lrecord[0].mix_coarse_sand_consumption) * (
                                     jprice["mix_coarse_sand_consumption"]) + (
                                         lrecord[0].mix_small_stone_dosage) * (jprice["mix_rocklet_consumption"]) + \
                                     (lrecord[0].mix_big_stone_dosage) * (jprice["mix_boulder_consumption"]) + (
                                         lrecord[0].mix_limestone_powder_consumption) * (jprice["limestone_powder"]) + \
                                     (lrecord[0].mix_water_reducing_agent_dosage) * (jprice["water_reduce_agent"]) + (
                                         lrecord[0].mix_fly_ash_dosage) * (jprice["fly_ash"]) + (
                                         lrecord[0].mix_cement_consumption) * (jprice["cement"]) + \
                                     (lrecord[0].mix_water_consumption + lrecord[0].mix_recycled_water_consumption) * \
                                     jprice[
                                         "water"] + \
                                     (lrecord[0].mix_expansion_agent_dosage) * (jprice["expansion_agent"]) + (
                                         lrecord[0].mix_slag_powder_consumption) * (jprice["slag_powder"])

                        design_unit_price = (fine_sand) * (jprice["mix_special_fine_sand_dosage"]) + (medium_sand) * (
                            jprice["mix_medium_sand_consumption"]) + \
                                            (coarse_sand) * (jprice["mix_coarse_sand_consumption"]) + (rocklet) * (
                                                jprice["mix_rocklet_consumption"]) + \
                                            (boulder) * (jprice["mix_boulder_consumption"]) + (limestone_powder) * (
                                                jprice["limestone_powder"]) + \
                                            (water_reduce_agent) * (jprice["water_reduce_agent"]) + (fly_ash) * (
                                                jprice["fly_ash"]) + (cement) * (jprice["cement"]) + \
                                            (water) * jprice["water"] + (expansion_agent) * (
                                            jprice["expansion_agent"]) + (
                                                slag_powder) * (jprice["slag_powder"])
                        data = [rocklet, boulder, limestone_powder, water_reduce_agent, fine_sand, medium_sand,
                                coarse_sand,
                                fly_ash, cement, water, expansion_agent, slag_powder, category, threed_strength]
                        data = np.array(data)
                        data = data.reshape(1, 14)
                        m = model.predict(data)
                        m = m.tolist()[0][0]
                        if m >= user_stength:
                            if design_unit_price < unit_price:
                                predict_28dstrength = m
                            else:
                                predict_28dstrength = 0
        elif l == "水下混凝土":
            category = 8
            if s == "C10":
                user_stength = 10
                max_water_binder_ratio = 0.60
            elif s == "C15":
                user_stength = 15
                max_water_binder_ratio = 0.60
            elif s == "C20":
                user_stength = 20
                max_water_binder_ratio = 0.60
            elif s == "C25":
                user_stength = 25
                max_water_binder_ratio = 0.60
            elif s == "C30":
                user_stength = 30
                max_water_binder_ratio = 0.55
            elif s == "C35":
                user_stength = 35
                max_water_binder_ratio = 0.50
            elif s == "C40":
                user_stength = 40
                max_water_binder_ratio = 0.45
            elif s == "C45":
                user_stength = 45
                max_water_binder_ratio = 0.40
            elif s == "C50":
                user_stength = 50
                max_water_binder_ratio = 0.36
            if lrecord[0].mix_3d_intensity > 3:
                threed_strength = lrecord[0].mix_3d_intensity
            else:
                threed_strength = 33
            for i in range(10):
                for i in range(500):
                    rocklet = lrecord[0].mix_small_stone_dosage
                    boulder = lrecord[0].mix_big_stone_dosage
                    limestone_powder = lrecord[0].mix_limestone_powder_consumption + 10 * (-1 * np.random.rand())
                    water_reduce_agent = lrecord[0].mix_water_reducing_agent_dosage + 3 * (-1 + 2 * np.random.rand())
                    fine_sand = lrecord[0].mix_special_fine_sand_dosage
                    medium_sand = lrecord[0].mix_medium_sand_consumption
                    coarse_sand = lrecord[0].mix_coarse_sand_consumption
                    fly_ash = lrecord[0].mix_fly_ash_dosage + 10 * (-1 * np.random.rand())
                    cement = lrecord[0].mix_cement_consumption + 10 * (-1 + 2 * np.random.rand())
                    water = lrecord[0].mix_water_consumption + lrecord[0].mix_recycled_water_consumption + 20 * (
                            -1 + 2 * np.random.rand())
                    expansion_agent = lrecord[0].mix_expansion_agent_dosage
                    slag_powder = lrecord[0].mix_slag_powder_consumption

                    mix_28d_strength = lrecord[0].mix_28d_strength
                    design_max_water_binder_ratio = water / (
                            limestone_powder + fly_ash + cement + expansion_agent + slag_powder)
                    if design_max_water_binder_ratio <= max_water_binder_ratio and (
                            limestone_powder + fly_ash + cement + expansion_agent + slag_powder) >= 360 and cement >= 300:
                        unit_price = (lrecord[0].mix_special_fine_sand_dosage) * (
                        jprice["mix_special_fine_sand_dosage"]) + (
                                         lrecord[0].mix_medium_sand_consumption) * (
                                     jprice["mix_medium_sand_consumption"]) + \
                                     (lrecord[0].mix_coarse_sand_consumption) * (
                                     jprice["mix_coarse_sand_consumption"]) + (
                                         lrecord[0].mix_small_stone_dosage) * (jprice["mix_rocklet_consumption"]) + \
                                     (lrecord[0].mix_big_stone_dosage) * (jprice["mix_boulder_consumption"]) + (
                                         lrecord[0].mix_limestone_powder_consumption) * (jprice["limestone_powder"]) + \
                                     (lrecord[0].mix_water_reducing_agent_dosage) * (jprice["water_reduce_agent"]) + (
                                         lrecord[0].mix_fly_ash_dosage) * (jprice["fly_ash"]) + (
                                         lrecord[0].mix_cement_consumption) * (jprice["cement"]) + \
                                     (lrecord[0].mix_water_consumption + lrecord[0].mix_recycled_water_consumption) * \
                                     jprice[
                                         "water"] + \
                                     (lrecord[0].mix_expansion_agent_dosage) * (jprice["expansion_agent"]) + (
                                         lrecord[0].mix_slag_powder_consumption) * (jprice["slag_powder"])

                        design_unit_price = (fine_sand) * (jprice["mix_special_fine_sand_dosage"]) + (medium_sand) * (
                            jprice["mix_medium_sand_consumption"]) + \
                                            (coarse_sand) * (jprice["mix_coarse_sand_consumption"]) + (rocklet) * (
                                                jprice["mix_rocklet_consumption"]) + \
                                            (boulder) * (jprice["mix_boulder_consumption"]) + (limestone_powder) * (
                                                jprice["limestone_powder"]) + \
                                            (water_reduce_agent) * (jprice["water_reduce_agent"]) + (fly_ash) * (
                                                jprice["fly_ash"]) + (cement) * (jprice["cement"]) + \
                                            (water) * jprice["water"] + (expansion_agent) * (
                                            jprice["expansion_agent"]) + (
                                                slag_powder) * (jprice["slag_powder"])
                        data = [rocklet, boulder, limestone_powder, water_reduce_agent, fine_sand, medium_sand,
                                coarse_sand,
                                fly_ash, cement, water, expansion_agent, slag_powder, category, threed_strength]
                        data = np.array(data)
                        data = data.reshape(1, 14)
                        m = model.predict(data)
                        m = m.tolist()[0][0]
                        if m >= user_stength:
                            if design_unit_price < unit_price:
                                predict_28dstrength = m
                            else:
                                predict_28dstrength = 0

    if joption["fine_aggregate_1"] == "特细沙":
        jdata["fine_aggregate_1"] = fine_sand
    elif joption["fine_aggregate_1"] == "中沙":
        jdata["fine_aggregate_1"] = medium_sand
    elif joption["fine_aggregate_1"] == "粗沙":
        jdata["fine_aggregate_1"] = coarse_sand
    else:
        jdata["fine_aggregate_1"] = 0

    if joption["fine_aggregate_2"] == "特细沙":
        jdata["fine_aggregate_2"] = fine_sand
    elif joption["fine_aggregate_2"] == "中沙":
        jdata["fine_aggregate_2"] = medium_sand
    elif joption["fine_aggregate_2"] == "粗沙":
        jdata["fine_aggregate_2"] = coarse_sand
    else:
        jdata["fine_aggregate_2"] = 0

    if joption["fine_aggregate_3"] == "特细沙":
        jdata["fine_aggregate_3"] = fine_sand
    elif joption["fine_aggregate_3"] == "中沙":
        jdata["fine_aggregate_3"] = medium_sand
    elif joption["fine_aggregate_3"] == "粗沙":
        jdata["fine_aggregate_3"] = coarse_sand
    else:
        jdata["fine_aggregate_3"] = 0

    if joption["coarse_aggregate_1"] == "小石":
        jdata["coarse_aggregate_1"] = rocklet
    elif joption["coarse_aggregate_1"] == "大石":
        jdata["coarse_aggregate_1"] = boulder
    else:
        jdata["coarse_aggregate_1"] = 0

    if joption["coarse_aggregate_2"] == "小石":
        jdata["coarse_aggregate_2"] = rocklet
    elif joption["coarse_aggregate_2"] == "大石":
        jdata["coarse_aggregate_2"] = boulder
    else:
        jdata["coarse_aggregate_2"] = 0

    if joption["coarse_aggregate_3"] == "小石":
        jdata["coarse_aggregate_3"] = rocklet
    elif joption["coarse_aggregate_3"] == "大石":
        jdata["coarse_aggregate_3"] = boulder
    else:
        jdata["coarse_aggregate_3"] = 0
    time2 = time.time()
    time3 = []
    time3 = time2 - time1
    water = round(water, 2)
    water_reduce_agent = round(water_reduce_agent, 2)
    fly_ash = round(fly_ash, 2)
    slag_powder = round(slag_powder, 2)
    limestone_powder = round(limestone_powder, 2)
    expansion_agent = round(expansion_agent, 2)
    design_unit_price = round(design_unit_price, 2)
    predict_28dstrength = round(predict_28dstrength, 2)
    cement = round(cement, 2)
    time3 = round(time3, 2)
    jdata["mix_cement_consumption"] = cement
    jdata["mix_water_consumption"] = water
    jdata["mix_water_reducing_agent_dosage"] = water_reduce_agent
    jdata["mix_fly_ash_dosage"] = fly_ash
    jdata["mix_slag_powder_consumption"] = slag_powder
    jdata["mix_limestone_powder_consumption"] = limestone_powder
    jdata["expansion_breed_grade"] = expansion_agent
    jdata["mix_other_materials"] = 0
    jdata["mix_water_consumption"] = water
    jdata[
        "mix_apparent_density"] = rocklet + boulder + limestone_powder + water_reduce_agent + fine_sand + medium_sand + coarse_sand + fly_ash + cement + water + expansion_agent + slag_powder
    jdata["mix_apparent_density"] = round(jdata["mix_apparent_density"], 2)
    jdata["unit_price"] = design_unit_price
    jdata["predict_28dstrength"] = predict_28dstrength
    jdata["time"] = time3
    jadjust_result["result"].append(jdata)
    if predict_28dstrength == 0:
        return lrecord[0]
    else:
        return jadjust_result


def result_package(joption, jprice, lrecord):
    jresult = {}
    jresult["result_long"] = len(lrecord)
    jresult["result"] = []
    for record in lrecord:
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

        jone["mix_water_consumption"] = record.mix_water_consumption + record.mix_recycled_water_consumption  # 水用量
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

        jresult["result"].append(jone)

    return jresult
