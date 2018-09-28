#-*- coding:utf-8 _*-  
""" 
@desc: http 请求操作类
@version: python3.5
@author: Yuanjp
@file: baike.py 
@time: 2018/5/24 0024 09:54
"""
import requests
from requests.adapters import HTTPAdapter
from word_api.config.log_config import log_config

logger = log_config(logger="baike_api").get_logger()

class baike_api:

    #http 请求头信息
    headers = {
        'connection' :'keep-alive',
        'content-type':'application/json',
        'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.170 Mobile Safari/537.36'
    }

    #数据请求
    def getbaikedata(url, values):
        session = requests.Session()
        session.mount('http://', HTTPAdapter(max_retries=3))    #重试
        session.mount('https://', HTTPAdapter(max_retries=3))
        r = session.get(url, params=values, headers=baike_api.headers, timeout=10)
        logger.debug(r.status_code)
        return r.json() #json.decoder.JSONDecodeError



