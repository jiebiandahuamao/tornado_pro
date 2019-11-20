import tornado.web
import asyncio
from tornado import gen
from api_user import query_user_many,add_user_one,query_page,query_count
from model import User
import json
from tool import _json
from bson import json_util
import time
from tornado_request import TorRequestHandler

class IndexHandler(TorRequestHandler):
    def get(self):
        self.write('index')


async def doing():
    await asyncio.sleep(20)  # here are doing some things
    # print('yyyyyyyyyyyyyyyyyyyyyyy')
    return 'Non-Blocking'


class NonBlockingHandler(tornado.web.RequestHandler):
    async def get(self):
        result = await doing()
        print(result,11111111)
        self.write('hahha')


class Comments(TorRequestHandler):

    def get(self):
        # condition = [User.username=='李四']
        # condition = {'username':'张三'}
        # all_users = query_user_many()
        # data = [{'username':i[0],'password':i[1],'createtime':i[2],'id':i[3]} for i in all_users]
        
        page = self.get_argument('page')

        all_users = query_page(page=int(page))
        data = [{'username':i[0],'password':i[1],'createtime':i[2],'id':i[3]} for i in all_users]

        count = query_count()

        self.write(json_util.dumps({'code':0,'data':{"data":data,'count':count},'msg':'succ'},ensure_ascii=False))
    
    def post(self):
        data = json.loads(self.request.body)
        username = data.get('username')
        password = data.get('password')
        data['creatime'] = time.strftime("%Y-%m-%d %H:%M:%S")

        add_user_one(data)
        self.write({'code':0,'data':'','msg':''})


application = tornado.web.Application([
    (r"/index", IndexHandler),
    (r"/nonblocking", NonBlockingHandler),
    (r"/user",Comments)
])
if __name__ == "__main__":
    application.listen(8080)
    tornado.ioloop.IOLoop.instance().start()