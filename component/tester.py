# -*- coding: utf-8 -*

from component.redis_db import RedisClient


class Tester(object):
    def __init__(self):
        """
        初始化数据库
        """
        self.redis = RedisClient()

    def run(self):
        # print('-'*25 + '开始检测' + '-'*25)
        while True:
            if not self.redis.rem():
                break
        # print('-'*25 + '完成检测' + '-'*25)
