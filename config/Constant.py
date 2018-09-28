#-*- coding:utf-8 _*-  
""" 
常量封装类
@version: python3.5
@author: Yuanjp
@file: Constant.py 
@time: 2018/5/25 0025 16:40
"""
class Constant:
    # 本地词条
    file_url = 'D:/Yuan/baike_data/word.txt'

    # 接口请求失败词条
    error_word_url = 'D:/Yuan/baike_data/error_word.txt'

    # 接口请求返回为空词条
    return_null_word_url = 'D:/Yuan/baike_data/return_null_word.txt'

    # 接口请求正常词条
    right_word_url = 'D:/Yuan/baike_data/right_word.txt'

    # 抓取到的数据
    baike_file_url = 'D:/Yuan/baike_data/baidubaike_data'

    # 百科接口地址
    baike_api_url = "http://baike.baidu.com/api/openapi/BaikeLemmaCardApi"