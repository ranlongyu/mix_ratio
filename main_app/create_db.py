import sys
import os

sys.path.append(os.path.abspath('..'))

from main_app import db

if __name__ == '__main__':
    #删除所有和db相关联的表
    db.drop_all()
    # 创建所有和db相关联的表
    db.create_all()