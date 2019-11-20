
from sqlalchemy import create_engine

HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'gong'
USERNAME = 'root'
PASSWORD = 'shutdown'

# mysql + pymysql://username:password@hostname:port/database?charset=utf8

db_url = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(
    USERNAME,
    PASSWORD,
    HOSTNAME,
    PORT,
    DATABASE
)
SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://root:shutdown@localhost/StudentManage"

engine = create_engine(db_url)

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base(engine)


from sqlalchemy.orm import sessionmaker


Session = sessionmaker(engine)
session = Session()

if __name__ == '__main__':
    connetion = engine.connect()
    result = connetion.execute('select 1')
    print(result.fetchone())