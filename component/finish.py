# -*- coding: utf-8 -*

from component.redis_db import RedisClient


class Finish(object):
    def __init__(self):
        """
        初始化数据库
        """
        self.redis = RedisClient()

    def run(self):
        print('-'*25 + '完成复习' + '-'*25)
        item = input('请输入完成复习的项目：')
        self.redis.decrease(item)
        print('-'*25 + '完成复习' + '-'*25)
