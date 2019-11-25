# -*-coding:utf-8-*-
from main_app import app
from flask import render_template, jsonify, request
import json
from push_mix_ratio import result_package
from initial_screen import main_initial
from deep_model_strength.strength_prediction import presiction, load_torch_model
from deep_model_strength.get_data import main_get_data
import config

model_strength = load_torch_model()
scaler = main_get_data(config.CONNECT, False)


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
    lrecord = main_initial(data["option"])
    jresult = result_package(data["option"], data["price"], lrecord, scaler=scaler, model=model_strength)
    return jsonify(jresult), 201


# 混凝土强度预测
@app.route('/mixratio/strength', methods=['POST'])
def strength_prediction():
    data = json.loads(request.get_data())
    jresult = presiction(data, scaler=scaler, model=model_strength)
    return jsonify(jresult), 201
