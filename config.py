# ali服务器数据库为：'mysql+pymysql://root:root1@localhost/test'
# 本地数据库为：'mysql+pymysql://root:123456@localhost/test'
CONNECT = ['0.0.0.0', 'root', '123456', 'test']  # 数据库信息

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://' + CONNECT[1] + ':' + CONNECT[2] + '@' + CONNECT[0] + '/' + CONNECT[3]

SQLALCHEMY_COMMIT_ON_TEARDOWN = True

SQLALCHEMY_TRACK_MODIFICATIONS = False
