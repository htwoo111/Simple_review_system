# -*- coding: utf-8 -*

import time
from component.setter import Setter
from component.shower import Shower
from component.finish import Finish
from component.reviser import Reviser
from component.tester import Tester
from component.emailer import Emailer
from multiprocessing import Process


class Scheduler(object):
    def scheduler_setter(self, FLAG, items):
        setter = Setter()
        setter.run(FLAG, items)

    def scheduler_shower(self):
        shower = Shower()
        shower.run()

    def scheduler_finish(self):
        finish = Finish()
        finish.run()

    def scheduler_reviser(self):
        reviser = Reviser()
        reviser.run()

    def scheduler_tester(self):
        tester = Tester()
        tester.run()

    def scheduler_emailer(self):
        title = input('请输入邮件标题:')
        content = input('请输入邮件内容:')
        emailer = Emailer(title, content)
        emailer.run()

    @staticmethod
    def scheduler_printer():
        # print('请选择要进行的操作（确认请按回车）：')
        print('1.添加复习项目')
        print('2.查看要复习的项目')
        print('3.开始复习')
        print('4.邮件提示')
        print('5.完成复习')
        print('0.退出')

    def run(self):
        """
        FLAG:退出条件
        ENABLED：开关
        item: 要复习的条目

        """
        print('*'*25 + '调度器开始运作' + '*'*25)
        # 每次开机都检测一次，删除分数为0的项目
        self.scheduler_tester()
        while True:
            self.scheduler_printer()
            ENABLED = input('请选择要进行的操作（确认请按回车，退出请按0）：')
            print('*'*50)  # 分割线

            # 设置复习项目
            if ENABLED == '1':
                try:
                    FLAG = int(input("请输入要插入的复习项目数："))
                except:
                    FLAG = 1  # 默认情况下复习的条目为1
                items = []  # 定义一个空列表接收多个要复习的项目
                while FLAG:
                    item = input("请输入要复习的项目（{}）：".format(FLAG))
                    IMPORTANCE_FLAG = input("请确定要复习的项目是否重要（{}）：".format(FLAG))
                    items.append([item, IMPORTANCE_FLAG])
                    FLAG -= 1
                # setter_process = Process(target=self.scheduler_setter,args=(FLAG,items))
                # setter_process.start()
                self.scheduler_setter(FLAG, items)
                time.sleep(1)

            # 查看要复习的项目
            if ENABLED == '2':
                self.scheduler_shower()
                time.sleep(1)

            if ENABLED == '3':
                self.scheduler_reviser()
                time.sleep(1)

            if ENABLED == '4':
                self.scheduler_emailer()
                time.sleep(1)

            # 完成复习
            if ENABLED == '5':
                self.scheduler_finish()
                time.sleep(1)

            # 退出
            if ENABLED == '0':
                break
