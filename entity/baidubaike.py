#-*- coding:utf-8 _*-  
""" 
@desc: 百度百科实体类
@version: python3.5
@author: Yuanjp
@file: baidubaike.py 
@time: 2018/5/24 0024 14:17
"""
class baidubaike:

    #zh_name="" #中文名称

    #en_name ="" #英语名称

    # 重写构造方法
    def __init__(self, title, desc, detail, image, url):
        self.desc = desc.strip()    # 描述
        self.detail = detail.strip()    # 概念
        self.image = image.strip()  # 图片
        self.url = url.strip()      # 百科url
        self.title = title.strip()  #标题

    # 对象转json字符串
    def obj_2_json(self):
        return {
            "title":self.title,
            "desc": self.desc,
            "detail": self.detail, #detail
            "image": self.image,
            "url": self.url
        }

    # 列表
    def obj_list(self):
        return [self.title,self.desc,self.url,self.image,self.detail]