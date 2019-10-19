# -*- coding: utf-8 -*

from my_logger import logger
from component.scheduler import Scheduler


def main():
    LOGGER = logger
    try:
        # FLAG = int(input("请输入要设置的复习项目个数"))

        s = Scheduler()
        # s = Scheduler(FLAG, item='')
        s.run()
    except Exception as e:
        LOGGER.debug(e)
        print('main.py raise a error: {}'.format(e))

if __name__ == "__main__":
    main()