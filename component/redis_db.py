# -*- coding: utf-8 -*

from random import choice
import redis
# import re
try:
    from component.error import ItemEmptyError
except:
    from error import ItemEmptyError
# from component.settings import REDIS_HOST, REDIS_PORT, REDIS_KEY, REDIS_PASSWORD
# from component.settings import INITIAL_SCORE, MIN_SCORE
MIN_SCORE = 0
INITIAL_SCORE = 4
MAX_SCORE = 4
REDIS_HOST = 'localhost'
REDIS_PORT = 6379
REDIS_PASSWORD = ''
REDIS_KEY = 'revier'


class RedisClient(object):
    def __init__(self, host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD):
        """
        初始化
        host：地址
        post：端口号
        password：密码
        """
        self.db = redis.StrictRedis(
            host=host, port=port, password=password, decode_responses=True)

    def add(self, item, score=INITIAL_SCORE):
        """
        添加复习的项目
        item：复习的项目
        score：复习项目的分数
        return：返回添加结果
        """
        if not self.exists(item):
            print('successfully, 添加复习项目：{}， 要复习的次数为{}'.format(item, score))
            return self.db.zadd(REDIS_KEY, {item: score})

    def exists(self, item):
        """
        判断复习的项目是否存在
        item：复习的项目
        return：是否存在
        """
        if self.db.zscore(REDIS_KEY, item):
            return True
        return False

    def random(self):
        """
        随机获取复习的项目，先从获取分数最高的复习的项目，如果不存在，则按照排名获取
        return：随机复习的项目
        """
        result = self.db.zrangebyscore(REDIS_KEY, MAX_SCORE, MAX_SCORE)
        if len(result):
            return choice(result)
        else:
            result = self.db.zrevrange(REDIS_KEY, MIN_SCORE, MAX_SCORE)
            if len(result):
                return choice(result)
            else:
                raise ItemEmptyError

    def decrease(self, item):
        """
        扣分，如果复习的项目分数小于最小值则删除
        item：复习的项目
        return：修改后的分数
        """
        score = self.db.zscore(REDIS_KEY, item)
        if score and score > MIN_SCORE:
            print("复习的项目：{} 分数减1， 当前分数为{}".format(item, score-1))
            return self.db.zincrby(REDIS_KEY, -1, item)
        elif score is None:
            print('输入的复习项目有误，请重新输入')
        else:
            print('复习的项目：{} 当前分数为{}, 移除'.format(item, score))
            return self.db.zrem(REDIS_KEY, item)

    def rem(self):
        """
        删除分数为0的项
        """
        return self.db.zremrangebyscore(REDIS_KEY, min=0, max=0)

    def count(self):
        """
        return：复习的项目的数量
        """
        return self.db.zcard(REDIS_KEY)

    def all(self):
        """
        return：全部复习的项目列表
        """
        # return self.db.zrangebyscore(REDIS_KEY, MIN_SCORE, MAX_SCORE)
        # start=0：表示开始的索引， end=-1:表示结束的索引
        return self.db.zrange(REDIS_KEY, 0, -1, withscores=True)

    # def batch(self, start, stop):
    #     """
    #     批量获取
    #     start：开始的索引
    #     stop：结束的索引
    #     return：搜索的复习的项目的列表
    #     """
    #     return self.db.zrevrange(REDIS_KEY, start, stop-1)


if __name__ == "__main__":
    conn = RedisClient()
    result = conn.all()
    print(result)
