import base64, time, requests, re
from Crypto.PublicKey import RSA as rsa
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
import config
from util import store
from datetime import date, timedelta


def get_payload(start_time, end_time):
    rsakey = rsa.importKey(config.PUB_KEY_STR)  # 导入读取到的公钥
    cipher = Cipher_pkcs1_v1_5.new(rsakey)  # 生成对象
    payload = "strNamespace=expand"
    payload += "&strClass=" + str(base64.b64encode(cipher.encrypt(config.STRCLASS.encode('utf-8'))), encoding="utf-8")
    payload += "&strFunc=" + str(base64.b64encode(cipher.encrypt(config.STRFUNC.encode('utf-8'))), encoding="utf-8")
    payload += "&strParam={\"start_time\":\"" + start_time + "\",\"end_time\":\"" + end_time + "\"}"
    payload += "&retype=1"
    payload += "&page=1"
    payload += "&rows=10"
    time_stmp = str(int(time.time()) + 28800)  # 时间加8小时
    # 通过生成的对象加密message明文，注意，在python3中加密的数据必须是bytes类型的数据，不能是str类型的数据
    payload += "&sort=" + str(base64.b64encode(cipher.encrypt(time_stmp.encode('utf-8'))), encoding="utf-8")
    payload += "&order=" + config.ORDER
    return payload


def get_data_web(start_time, end_time):
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    response = requests.request("POST", config.WEB_DATA_URL, headers=headers,
                                data=get_payload(start_time, end_time).replace('+', '%2B'))  # url中加号会被处理为空，需替换
    return response.json()


def clean_data(datadi):
    try:
        datali = eval(datadi['value'].replace("null", "None"))
    except:
        datali = []
    # 数据清洗
    new_datali = []
    print("原始数据条数:", len(datali))
    for data in datali:
        new_data = {}
        try:
            new_data['mix_period'] = float(data['mix_period'])
            mix_concrete_variety = []
            if '常规' in data['mix_concrete_variety']:
                mix_concrete_variety.append('常规混凝土')
            if '抗渗' in data['mix_concrete_variety']:
                mix_concrete_variety.append('抗渗混凝土')
            if '防水' in data['mix_concrete_variety']:
                mix_concrete_variety.append('防水混凝土')
            if '补偿' in data['mix_concrete_variety']:
                mix_concrete_variety.append('补偿混凝土')
            if '水下' in data['mix_concrete_variety']:
                mix_concrete_variety.append('水下混凝土')
            if '大体积' in data['mix_concrete_variety']:
                mix_concrete_variety.append('大体积混凝土')
            if '透水' in data['mix_concrete_variety']:
                mix_concrete_variety.append('透水混凝土')
            if '自密实' in data['mix_concrete_variety']:
                mix_concrete_variety.append('自密实混凝土')
            if '铁路' in data['mix_concrete_variety']:
                mix_concrete_variety.append('铁路混凝土')
            if '钢纤维' in data['mix_concrete_variety']:
                mix_concrete_variety.append('钢纤维混凝土')
            if '聚丙烯纤维' in data['mix_concrete_variety']:
                mix_concrete_variety.append('聚丙烯纤维混凝土')
            if '轻骨料' in data['mix_concrete_variety']:
                mix_concrete_variety.append('轻骨料混凝土')
            if '重混' in data['mix_concrete_variety']:
                mix_concrete_variety.append('重混混凝土')
            if mix_concrete_variety != []:
                new_data['mix_concrete_variety'] = ",".join(mix_concrete_variety)
            else:
                continue
            new_data['mix_power_level'] = data['mix_power_level'][:3]
            new_data['mix_impermeability_rating'] = data['mix_impermeability_rating'] if data['mix_impermeability_rating'] != None else ''
            new_data['mix_material_requirements'] = data['mix_material_requirements'] if data['mix_material_requirements'] != None else ''
            try:
                new_data['mix_limit_expansion_rate'] = float(re.search(".+(0\.[0-9]+)%", data['mix_limit_expansion_rate']).group(1))
            except:
                new_data['mix_limit_expansion_rate'] = -1
            new_data['mix_slump'] = float(data['mix_slump'][:3])
            new_data['mix_expansion'] = float(data['mix_expansion'][1:4])
            new_data['mix_cement_consumption'] = float(data['mix_cement_consumption'])
            new_data['mix_special_fine_sand_dosage'] = float(data['mix_special_fine_sand_dosage']) if data['mix_special_fine_sand_dosage'] not in [None,''] else 0.0
            new_data['mix_medium_sand_consumption'] = float(data['mix_medium_sand_consumption']) if data['mix_medium_sand_consumption'] not in [None,''] else 0.0
            new_data['mix_coarse_sand_consumption'] = float(data['mix_coarse_sand_consumption']) if data['mix_coarse_sand_consumption'] not in [None,''] else 0.0
            new_data['mix_small_stone_dosage'] = float(data['mix_small_stone_dosage']) if data['mix_small_stone_dosage'] not in [None, ''] else 0.0
            new_data['mix_big_stone_dosage'] = float(data['mix_big_stone_dosage']) if data['mix_big_stone_dosage'] not in [None, ''] else 0.0
            new_data['mix_water_reducing_agent_dosage'] = float(data['mix_water_reducing_agent_dosage']) if data['mix_water_reducing_agent_dosage'] not in [None,''] else 0.0
            new_data['mix_fly_ash_dosage'] = float(data['mix_fly_ash_dosage']) if data['mix_fly_ash_dosage'] not in [None, ''] else 0.0
            new_data['mix_slag_powder_consumption'] = float(data['mix_slag_powder_consumption']) if data['mix_slag_powder_consumption'] not in [None,''] else 0.0
            new_data['mix_limestone_powder_consumption'] = float(data['mix_limestone_powder_consumption']) if data['mix_limestone_powder_consumption'] not in [None, ''] else 0.0
            new_data['mix_expansion_agent_dosage'] = float(data['mix_expansion_agent_dosage']) if data['mix_expansion_agent_dosage'] not in [None,''] else 0.0
            new_data['mix_water_consumption'] = float(data['mix_water_consumption']) if data['mix_water_consumption'] not in [None, ''] else 0.0
            new_data['mix_apparent_density'] = float(data['mix_apparent_density']) if data['mix_apparent_density'] not in [None, ''] else -1
            new_data['mix_production_workshop'] = data['mix_production_workshop'] if data['mix_production_workshop'] != None else ''
            new_data['mix_main_workshop'] = data['mix_main_workshop'] if data['mix_main_workshop'] != None else ''
            new_data['mix_production_line'] = data['mix_production_line'] if data['mix_production_line'] != None else ''
            new_data['mix_pouring_method'] = data['mix_pouring_method'] if data['mix_pouring_method'] != None else ''
            new_data['mix_3d_intensity'] = float(data['mix_3d_intensity']) if data['mix_3d_intensity'] not in [None, ''] else -1
            new_data['mix_7d_intensity'] = float(data['mix_7d_intensity']) if data['mix_7d_intensity'] not in [None, ''] else -1
            new_data['mix_28d_strength'] = float(data['mix_28d_strength'])
            new_data['mix_60d_strength'] = float(data['mix_60d_strength']) if data['mix_60d_strength'] not in [None, ''] else -1
            new_data['cement_breed_grade'] = data['cement_breed_grade'] if data['cement_breed_grade'] != None else ''
            new_data['cement_28d_compression'] = float(data['cement_28d_compression']) if data['cement_28d_compression'] not in [None, ''] else -1
            new_data['cement_supply_unit'] = data['cement_supply_unit'] if data['cement_supply_unit'] != None else ''
            new_data['reduce_breed_grade'] = data['reduce_breed_grade'] if data['reduce_breed_grade'] != None else ''
            new_data['reduce_recommended_dosage'] = float(data['reduce_recommended_dosage']) if data['reduce_recommended_dosage'] not in [None, ''] else -1
            new_data['reduce_water_reduction_rate'] = float(data['reduce_water_reduction_rate']) if data['reduce_water_reduction_rate'] not in [None,''] else -1
            new_data['reduce_gas_content'] = float(data['reduce_gas_content']) if data['reduce_gas_content'] not in [None, ''] else -1
            new_data['reduce_28d_compressive_strength_ratio'] = float(data['reduce_28d_compressive_strength_ratio']) if data['reduce_28d_compressive_strength_ratio'] not in [None, ''] else -1
            new_data['reduce_bleeding_rate_ratio'] = float(data['reduce_bleeding_rate_ratio']) if data['reduce_bleeding_rate_ratio'] not in [None,''] else -1
            new_data['fly_sample_category'] = data['fly_sample_category'] if data['fly_sample_category'] != None else ''
            new_data['fly_breed_grade'] = data['fly_breed_grade'] if data['fly_breed_grade'] != None else ''
            new_data['fly_fineness'] = float(data['fly_fineness']) if data['fly_fineness'] not in [None, ''] else -1
            new_data['fly_water_demand_ratio'] = float(data['fly_water_demand_ratio']) if data['fly_water_demand_ratio'] not in [None, ''] else -1
            new_data['fly_loss_on_ignition'] = float(data['fly_loss_on_ignition']) if data['fly_loss_on_ignition'] not in [None, ''] else -1
            new_data['fly_activity_index'] = float(data['fly_activity_index']) if data['fly_activity_index'] not in [None, ''] else -1
            new_data['slag_breed_grade'] = data['slag_breed_grade'] if data['slag_breed_grade'] != None else ''
            new_data['slag_28d_activity_index'] = float(data['slag_28d_activity_index']) if data['slag_28d_activity_index'] not in [None, ''] else -1
            new_data['slag_supply_unit'] = data['slag_supply_unit'] if data['slag_supply_unit'] != None else ''
            new_data['limestone_fineness'] = float(data['limestone_fineness']) if data['limestone_fineness'] not in [None, ''] else -1
            new_data['limestone_methylene_blue_value'] = float(data['limestone_methylene_blue_value']) if data['limestone_methylene_blue_value'] not in [None,''] else -1
            new_data['limestone_28d_activity_index'] = float(data['limestone_28d_activity_index']) if data['limestone_28d_activity_index'] not in [None,''] else -1
            new_data['expansion_breed_grade'] = data['expansion_breed_grade'] if data['expansion_breed_grade'] != None else ''
            new_data['expansion_28d_compressive_strength'] = float(data['expansion_28d_compressive_strength']) if data['expansion_28d_compressive_strength'] not in [None, ''] else -1
            new_data['expansion_limit_expansion_rate'] = float(data['expansion_limit_expansion_rate']) if data['expansion_limit_expansion_rate'] not in [None,''] else -1
        except:
            continue
        # 合理性判断
        if new_data['mix_fly_ash_dosage']==0 and new_data["fly_sample_category"]!='' and new_data["fly_breed_grade"]!='':
            continue
        if new_data["mix_slag_powder_consumption"]==0 and new_data["slag_breed_grade"]!='':
            continue
        new_datali.append(new_data)
    return new_datali


def print_data(datali):
    for line in datali:
        print(line)


if __name__ == '__main__':
    start_day = date(2018, 12, 2)
    end_day = date(2019, 12, 31)
    while start_day <= end_day:
        start_time = start_day.strftime('%Y-%m-%d')
        datadi = get_data_web(start_time, start_time)
        datali = clean_data(datadi)
        store(datali)
        # print_data(datali)
        print(start_time + ": " + str(len(datali)))
        start_day = start_day + timedelta(days=1)
    print("存储完成！")
