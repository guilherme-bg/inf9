class Config():
    SECRET_KEY = 'uotfu6tlhkgteytrtgfderohgfvbfcfytfyruyghf213786354,1873çyukytrjgfchfdhjgfgdytrfdytythgdytdhgd5uihd'

class DevelopmentConfig(Config):
    DEBUG = True

class TestConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False

app_config = { 'development' :DevelopmentConfig,
               'test' :TestConfig,
               'production' :ProductionConfig}
