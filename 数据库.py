#!/usr/bin/env python3
import pymysql #导入模块


#远程连接数据库
try:
	db = pymysql.connect(
			host='gz-cynosdbmysql-grp-18whccs3.sql.tencentcdb.com',
			port=24561,
			user='root',
			passwd='1qazxsw@',
			db='Student',
			charset='utf8'
			)
	print('数据库连接成功')
	with conn.cursor() as cursor:
		cursor.execute("DROP TABLE IF EXISTS Student")
# 使	用预处理语句创建表
	sql = """CREATE TABLE EMPLOYEE (
			FIRST_NAME  CHAR(20) NOT NULL,
			LAST_NAME  CHAR(20),
			AGE INT,  
			SEX CHAR(1),
			INCOME FLOAT )"""
	cursor.execute(sql)
	print('表格创建成功')
except pymysql.Error as e:
		print('表格创建失败，str(e)')
				
	#cursor.execute(sql)
	#db.close()