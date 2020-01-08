# ali服务器数据库为：'mysql+pymysql://root:root1@localhost/test'
# 本地数据库为：'mysql+pymysql://root:123456@localhost/test'
CONNECT = ['0.0.0.0', 'root', '123456', 'test']  # 数据库信息
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://' + CONNECT[1] + ':' + CONNECT[2] + '@' + CONNECT[0] + '/' + CONNECT[3]
SQLALCHEMY_COMMIT_ON_TEARDOWN = True
SQLALCHEMY_TRACK_MODIFICATIONS = False

# 是否开启debug模式
DEBUG = True

# 配合比拉取数据接口
WEB_DATA_URL = "https://wst.cqbm2007.com:9993/ws/common.asmx/ws_call"
# WEB_DATA_URL = "https://test.cqbm2007.com:4321/ws/Common.asmx/ws_call"
PUB_KEY_STR = """-----BEGIN RSA PUBLIC KEY-----
    MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCmYnlrvOTSHYq/QLwmwwT8nGxt
    rdlkJX1RL7goteyk3UDlEpjztdmbIRzEqJZFg2e2DGiAX+BaFAFdMMAuNBK7L6Hj
    RJa8/5nkcd60M+EnBmjq3MtM800DmPjfnIsjYcnKKKb9qYWZ2Tyoa4GRSAsQ+Hoj
    jhRLpQ1cQ3pMDrG0ZwIDAQAB
    -----END RSA PUBLIC KEY-----"""
STRCLASS = "KWIntelligent"
STRFUNC = "phb_zky"
ORDER = "8490DC05-1C1D-498A-B168-EAB6FE5D2716"
