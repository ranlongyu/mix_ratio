# -*-coding:utf-8-*-
from main_app import app
from flask import render_template, jsonify, request
import json
from package_mix_ratio import result_package_new, package_best
from initial_screen import main_initial
from deep_model_strength.strength_prediction import presiction, load_torch_model
from main_util import change_joption_jprice
from mix_ratio_optimization import main_mix_ratio_optimization

model_strength = load_torch_model()  # 让模型一直在内存中
model_strength.eval()


# 设置route
@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    ip = request.remote_addr
    return render_template('index.html', user_ip=ip)


# 请求配合比
@app.route('/mixratio', methods=['POST'])
def create_task_test():
    data = json.loads(request.get_data())
    joption = data["option"]
    jprice = data["price"]
    # 获取石和砂是否使用、价格和位置等信息
    joption, jprice = change_joption_jprice(joption, jprice)
    lrecord = main_initial(joption)[:10]
    jresult = result_package_new(joption, jprice, lrecord)
    if len(jresult["result"]) > 0:
        best_record, best_apparent_density, best_unit_price = main_mix_ratio_optimization(joption, jprice, lrecord, model=model_strength)
        if best_record != None:
            jdata = package_best(joption, best_record, best_apparent_density, best_unit_price)  # 优化之后打包
            jresult["result"].insert(0, jdata)  # 优化后的数据插入到最前面
        else:
            print("生成数据失败!")
    return jsonify(jresult), 201


# 混凝土强度预测
@app.route('/mixratio/strength', methods=['POST'])
def strength_prediction():
    data = json.loads(request.get_data())
    jresult = presiction(data, model=model_strength)
    return jsonify(jresult), 201
