class Config():
    usuario = "guilhermebg"
    senha = "Gui188496Gui"
    host = "db4free.net"
    porta = "3306"
    banco = "bibliotecagui"
    SECRET_KEY = 'uotfu6tlhkgteytrtgfderohgfvbfcfytfyruyghf213786354,1873çyukytrjgfchfdhjgfgdytrfdytythgdytdhgd5uihd'
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://{}:{}@{}:{}/{}".format(usuario,senha,host,porta,banco)
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    DEBUG = True

class TestConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False

app_config = { 'development' :DevelopmentConfig,
               'test' :TestConfig,
               'production' :ProductionConfig}
