import random
try:
    from component.redis_db import RedisClient
except:
    from redis_db import RedisClient

class Reviser(object):
    def __init__(self):
        """
        初始化数据库
        """
        self.redis = RedisClient()
        
    def run(self):
        print('-'*25 + '开始复习' + '-'*25)
        item = self.redis.random()
        print('需要复习的项目为：{}'.format(item))
        print('-'*25 + 'end' + '-'*25)
        return item