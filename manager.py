"""
项目配置信息：
1、mysql数据库
2、配置redis：储存session，图片验证码，短信验证码，或者缓存操作
3、session：用来保存用户的登陆状态
4、csrf配置，主要对以下请求方式做保护：GET,POST,DELETE,PATCH
5、日志文件配置
6、数据库迁移配置
"""""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import redis

app = Flask(__name__)


# 配置信息类
class Config(object):
    # 配置数据库链接信息，追踪信息
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:kaikai.@127.0.0.1:3306/information"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # 配置redis的ip地址和端口
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379


# 通过类的方式加载配置信息
app.config.from_object(Config)
# 创建SQLAlchemy对象，关联app
db = SQLAlchemy(app)

# 创建redis对象
redis_store = redis.StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT)


@app.route("/")
def hello():
    # 测试redis存储数据
    redis_store.set("name", "二狗")

    return "hello world"


if __name__ == '__main__':
    app.run(debug=True)
