# -*- coding: utf-8 -*

from component.redis_db import RedisClient


class Finish(object):
    def __init__(self):
        """
        初始化数据库
        """
        self.redis = RedisClient()

#    def run(self):
#        print('-'*25 + '完成复习' + '-'*25)
#        item = input('请输入完成复习的项目：')
#        self.redis.decrease(item)
#        print('-'*25 + '完成复习' + '-'*25)

    def run(self):
        """
        REVIEW_FLAG:判断是否做笔记
        """
        print('-'*25 + '完成复习' + '-'*25)
        while True:
            item = input('请输入完成复习的项目：')
            ret = self.redis.decrease(item)
            if (ret is not None) or (item == ''):
                break
        REVIEW_FLAG = input('是否做笔记（做笔记输入 1 ：）')
        if REVIEW_FLAG == '1':
            print('-'*25 + '开始输入笔记内容' + '-'*25)
            while True:
                content = input('请输入笔记内容：（按回车退出）')
                if content != '':
                    self.redis.ladd(item, content)
                    print('输入的笔记内容为：{}'.format(content))
                else:
                    break
        print('-'*25 + '完成复习' + '-'*25)
