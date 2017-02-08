#! usr/bin/python
# coding=utf-8

from pymongo import MongoClient

conn = MongoClient('localhost', 27017)
db = conn.pyGirls #连接数据库