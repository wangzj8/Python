#!/usr/bin/env python3
import csv
import pymysql

# 连接MySQL数据库（注意：charset参数是utf8而不是utf-8）
conn = pymysql.connect(host='localhost', user='root', password='MySQL密码', db='dbmovie_top100', charset='utf8')

# 创建游标对象
cursor = conn.cursor()

# 读取csv文件
with open('豆瓣电影Top100.csv', 'r', encoding='utf-8') as f:
	read = csv.reader(f)
	
	# 一行一行地存，除去第一行和第一列
	for each in list(read)[1:]:
		i = tuple(each[1:])        
		# 使用SQL语句添加数据
		sql = "INSERT INTO db_top100 VALUES" + str(i) # db_top100是表的名称
		cursor.execute(sql) #执行SQL语句
		
	conn.commit() # 提交数据
	cursor.close() # 关闭游标
	conn.close() # 关闭数据库
	
