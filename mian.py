#-*- coding:utf-8 _*-  
""" 
@desc: 
@version: python3.5
@author: Yuanjp
@file: mian.py 
@time: 2018/5/24 0024 15:09
"""
import json
from word_api.entity.baidubaike import baidubaike as bdbk
from word_api.baike.file_api import *
from word_api.baike.baike_api import baike_api as bk_api
from word_api.config.log_config import log_config
from word_api.config.Constant import Constant

logger = log_config(logger="main").get_logger()



#"请求数据"
values ={'bk_key': "会计",
               'scope':103,
               'format':'json',
               'appid':379020,
               'bk_length':600}

list = readword(Constant.file_url)
logger.info("词条数目：%d" %list.__len__())

image=""; baike_url=""
write_csv_header(Constant.baike_file_url + '.csv') #写入表头
for word in list:
    s_word = word.strip().replace("\n", "")
    values['bk_key'] = s_word
    result = bk_api.getbaikedata(Constant.baike_api_url, values)
    logger.info("接口参数:%s ,返回:%s" %(s_word,result))
    if len(result) != 0:
        if 'errno' in result: #接口异常
            logger.info("接口请求失败: word=%s" %s_word)
            write_word(Constant.error_word_url,s_word) #接口异常词条
            continue
        if 'image' in result:
            image = result['image']
        if 'url' in result:
            baike_url = result['url']
        write_word(Constant.right_word_url,s_word) #接口正常词条
        bd = bdbk(word, result['desc'], result['abstract'], image, baike_url)
        text = json.dumps(bd, ensure_ascii=False, default=bdbk.obj_2_json)
        write_baike(Constant.baike_file_url+'.txt',text)
        write_csv(Constant.baike_file_url+'.csv',bd.obj_list()) #写入表数据
    else:
        write_word(Constant.return_null_word_url, s_word)  #接口返回为空词条