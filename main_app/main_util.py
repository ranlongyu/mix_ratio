# 获取石和砂是否使用、价格和位置等信息
def change_joption_jprice(joption, jprice):
    # 是否使用
    joption["mix_special_fine_sand_use"] = 0
    joption["mix_medium_sand_use"] = 0
    joption["mix_coarse_sand_use"] = 0
    joption["mix_rocklet_use"] = 0
    joption["mix_boulder_use"] = 0
    # 位置
    joption["mix_special_fine_position"] = None
    joption["mix_medium_sand_position"] = None
    joption["mix_coarse_sand_position"] = None
    joption["mix_rocklet_position"] = None
    joption["mix_boulder_position"] = None
    # 价格
    jprice["mix_special_fine_sand"] = 0
    jprice["mix_medium_sand"] = 0
    jprice["mix_coarse_sand"] = 0
    jprice["mix_rocklet"] = 0
    jprice["mix_boulder"] = 0

    if joption["fine_aggregate_1"] == "特细砂":
        joption["mix_special_fine_sand_use"] = 1
        joption["mix_special_fine_position"] = "fine_aggregate_1"
        jprice["mix_special_fine_sand"] = jprice["fine_aggregate_1"]
    elif joption["fine_aggregate_1"] == "中砂":
        joption["mix_medium_sand_use"] = 1
        joption["mix_medium_sand_position"] = "fine_aggregate_1"
        jprice["mix_medium_sand"] = jprice["fine_aggregate_1"]
    elif joption["fine_aggregate_1"] == "粗砂":
        joption["mix_coarse_sand_use"] = 1
        joption["mix_coarse_sand_position"] = "fine_aggregate_1"
        jprice["mix_coarse_sand"] = jprice["fine_aggregate_1"]

    if joption["fine_aggregate_2"] == "特细砂":
        joption["mix_special_fine_sand_use"] = 1
        joption["mix_special_fine_position"] = "fine_aggregate_2"
        jprice["mix_special_fine_sand"] = jprice["fine_aggregate_2"]
    elif joption["fine_aggregate_2"] == "中砂":
        joption["mix_medium_sand_use"] = 1
        joption["mix_medium_sand_position"] = "fine_aggregate_2"
        jprice["mix_medium_sand"] = jprice["fine_aggregate_2"]
    elif joption["fine_aggregate_2"] == "粗砂":
        joption["mix_coarse_sand_use"] = 1
        joption["mix_coarse_sand_position"] = "fine_aggregate_2"
        jprice["mix_coarse_sand"] = jprice["fine_aggregate_2"]

    if joption["fine_aggregate_3"] == "特细砂":
        joption["mix_special_fine_sand_use"] = 1
        joption["mix_special_fine_position"] = "fine_aggregate_3"
        jprice["mix_special_fine_sand"] = jprice["fine_aggregate_3"]
    elif joption["fine_aggregate_3"] == "中砂":
        joption["mix_medium_sand_use"] = 1
        joption["mix_medium_sand_position"] = "fine_aggregate_3"
        jprice["mix_medium_sand"] = jprice["fine_aggregate_3"]
    elif joption["fine_aggregate_3"] == "粗砂":
        joption["mix_coarse_sand_use"] = 1
        joption["mix_coarse_sand_position"] = "fine_aggregate_3"
        jprice["mix_coarse_sand"] = jprice["fine_aggregate_3"]

    if joption["coarse_aggregate_1"] == "小石":
        joption["mix_rocklet_use"] = 1
        joption["mix_rocklet_position"] = "coarse_aggregate_1"
        jprice["mix_rocklet"] = jprice["coarse_aggregate_1"]
    elif joption["coarse_aggregate_1"] == "大石":
        joption["mix_boulder_use"] = 1
        joption["mix_boulder_position"] = "coarse_aggregate_1"
        jprice["mix_boulder"] = jprice["coarse_aggregate_1"]

    if joption["coarse_aggregate_2"] == "小石":
        joption["mix_rocklet_use"] = 1
        joption["mix_rocklet_position"] = "coarse_aggregate_2"
        jprice["mix_rocklet"] = jprice["coarse_aggregate_2"]
    elif joption["coarse_aggregate_2"] == "大石":
        joption["mix_boulder_use"] = 1
        joption["mix_boulder_position"] = "coarse_aggregate_2"
        jprice["mix_boulder"] = jprice["coarse_aggregate_2"]

    # 调整记录中的砂价格
    # 如果用户没有选粗砂，但是选了另外两种砂，把粗砂价格设置为中沙价格
    if joption["mix_special_fine_sand_use"] == 1 and joption["mix_medium_sand_use"] == 1 and joption[
        "mix_coarse_sand_use"] == 0:
        jprice["mix_coarse_sand"] = jprice["mix_medium_sand"]
    # 如果用户没有选中砂，但是选了另外两种砂
    elif joption["mix_special_fine_sand_use"] == 1 and joption["mix_medium_sand_use"] == 0 and joption[
        "mix_coarse_sand_use"] == 1:
        jprice["mix_medium_sand"] = jprice["mix_coarse_sand"]
    # 如果用户没有选特细砂，但是选了另外两种砂
    elif joption["mix_special_fine_sand_use"] == 0 and joption["mix_medium_sand_use"] == 1 and joption[
        "mix_coarse_sand_use"] == 1:
        jprice["mix_special_fine_sand"] = jprice["mix_medium_sand"]
    # 如果用户只选了特细砂
    elif joption["mix_special_fine_sand_use"] == 1 and joption["mix_medium_sand_use"] == 0 and joption[
        "mix_coarse_sand_use"] == 0:
        jprice["mix_medium_sand"] = jprice["mix_special_fine_sand"]
        jprice["mix_coarse_sand"] = jprice["mix_special_fine_sand"]
    # 如果用户只选了粗砂
    elif joption["mix_special_fine_sand_use"] == 0 and joption["mix_medium_sand_use"] == 0 and joption[
        "mix_coarse_sand_use"] == 1:
        jprice["mix_medium_sand"] = jprice["mix_coarse_sand"]
        jprice["mix_special_fine_sand"] = jprice["mix_coarse_sand"]
    # 如果用户只选了中砂
    elif joption["mix_special_fine_sand_use"] == 0 and joption["mix_medium_sand_use"] == 1 and joption[
        "mix_coarse_sand_use"] == 0:
        jprice["mix_coarse_sand"] = jprice["mix_medium_sand"]
        jprice["mix_special_fine_sand"] = jprice["mix_medium_sand"]

    # 调整记录中的石用量
    # 如果用户只选了大石
    if joption["mix_rocklet_use"] == 0 and joption["mix_boulder_use"] == 1:
        jprice["mix_rocklet"] = jprice["mix_boulder"]
    # 如果用户只选了小石
    elif joption["mix_boulder_use"] == 0 and joption["mix_rocklet_use"] == 1:
        jprice["mix_boulder"] = jprice["mix_rocklet"]

    return joption, jprice