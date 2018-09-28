#-*- coding:utf-8 _*-  
""" 
日志配置封装类
@version: python3.5
@author: Yuanjp
@file: log_config.py 
@time: 2018/5/25 0025 10:39
"""
import logging
import os

def singleton(cls):
    instances = {}
    def getinstance(*args,**kwargs):
        if cls not in instances:
            instances[cls] = cls(*args,**kwargs)
        return instances[cls]
    return getinstance


class log_config(object):

    def __init__(self, logger):
        # 日志文件路径
        __log_path = 'D:/gitHubRes/python/关系抽取/Agriculture_KnowledgeGraph/word_api/logs/'
        # 日志文件名称
        __log_name = __log_path+'log.log'
        # 输出格式
        __fmt = "%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s"

        # 第一步，创建一个__loger
        self.__loger = logging.getLogger(logger)
        self.__loger.setLevel(logging.DEBUG)  # Log等级总开关

        # 第二步，创建一个handler，用于写入日志文件
        __fh = logging.FileHandler(__log_name, mode='a+')
        __fh.setLevel(logging.DEBUG)

        # 第三步，再创建一个handler，用于输出到控制台
        __ch = logging.StreamHandler()
        __ch.setLevel(logging.DEBUG)

        # 第四步，定义handler的输出格式
        formatter = logging.Formatter(__fmt)
        __fh.setFormatter(formatter)
        __ch.setFormatter(formatter)

        # 第五步，将logger添加到handler里面
        self.__loger.addHandler(__fh)
        self.__loger.addHandler(__ch)

    def get_logger(self):
        return  self.__loger






