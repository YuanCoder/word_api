#-*- coding:utf-8 _*-  
""" 
@version: python3.5
@author: Yuanjp
@file: test_api.py 
@time: 2018/5/25 0025 09:08
"""

from word_api.config.log_config import log_config


log1 = log_config(logger="log1").get_logger()
log2 = log_config(logger="log2").get_logger()
log2.debug("test")
print(log1 == log2)
