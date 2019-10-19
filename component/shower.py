from component.redis_db import RedisClient


class Shower(object):
    def __init__(self):
        """
        初始化数据库
        """
        self.redis = RedisClient()
    
    def run(self):
        count = self.redis.count()
        print('-'*25 + "显示器" + '-'*25)
        print('当前要复习的项目总共有 {} 个'.format(count))
        items = self.redis.all()
        for item in items:
            print('需要复习的项目:{:^20}  还需要复习的次数:{}'.format(item[0], item[1]))
        print('-'*25 + "所有项目已展示" + '-'*25)
        