from component.redis_db import RedisClient


class Setter(object):
    def __init__(self):
        """
        初始化数据库
        """
        self.redis = RedisClient()

    def run(self, FLAG, items):
        """
        :FLAG 设置退出条件
        """
        print("-"*25 + "开始设置复习条目" + "-"*25)

        while items:
            item = items.pop()
            try:
                IMPORTANCE_FLAG = int(item[1])
            except:
                IMPORTANCE_FLAG = False
            item = item[0]
            if not IMPORTANCE_FLAG:
                # print('successfulli, 添加复习{}， 要复习的次数为{}'.format(item, 2))
                self.redis.add(item, 2)
            self.redis.add(item)
            # print('successfulli, 添加复习{}， 要复习的次数为{}'.format(item, 4))
        print("-"*25 + "设置复习条目完成" + "-"*25)
