#-*- coding:utf-8 _*-
import csv


""" 
@desc: 文件操作类
@version: python3.5
@author: Yuanjp
@file: file_api.py 
@time: 2018/5/24 0024 16:08
"""

#词条数据读取 返回
def readword(file_url):
    wordList = [] #词条列表
    with open(file_url, "r+",encoding='utf-8') as f:
        for line in f:
            wordList.append(line.split(" ")[0])
    return wordList

#写请求接口失败/正常的 词条
def write_word(file_url, text):
    with open(file_url, "a+",encoding='utf-8') as f:
        f.write(text+'\n')

#写请求接口数据
def write_baike(file_url, text):
    with open(file_url,"a+",encoding='utf-8') as f:
        f.write(text+'\n')

# 写csv header
def write_csv_header(file_url):
    with open(file_url, "a+", encoding="utf-8",newline="") as f:
        writer = csv.writer(f, dialect='excel')
        writer.writerow(['title', 'desc', 'url', 'image', 'detail'])  # abstract -> detail

#导出csv 数据
def write_csv(file_url, data):
    with open(file_url, "a+", encoding="utf-8", newline="") as f:
        writer = csv.writer(f, dialect='excel')
        writer.writerow(data)