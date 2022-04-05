import pymysql
import pandas as pd
import numpy as np
file = "tianhe.xls"
data = pd.read_excel(file)
# 首先将pandas读取的数据转化为array
data_array = np.array(data)
# 然后转化为list形式
data_list =data_array.tolist()

import pymysql
# 第一步：建立连接
conn = pymysql.connect(host='gz-cynosdbmysql-grp-18whccs3.sql.tencentcdb.com',port=24561,
                      user='root',password='1qazxsw@',
                       database='Hopsital',charset='utf8')
# print(conn)
try:
    # 第二步：获得游标对象
    # cursor = conn.cursor()       #返回一个游标对象   这个对象可以执行sql语句
    with conn.cursor() as cursor: # 将默认的输出元组改为输出为字典
        # 第三步：通过游标向数据库服务器发出sql语句，获取执行结果
        i = 0
        for i in range(len(data_list)):
            sql = '''
                   insert ignore into `su` (`su_lon`,`su_lat`,`su_name`,`su_adress`,`au_adname`)
                   value ('%s','%s','%s','%s','%s')
                   '''  % (data_list[i][0], data_list[i][1], data_list[i][2], data_list[i][3],data_list [i][4])
            print("写入" + str(i + 1) + "行")
            cursor.execute(sql)

        # 第四步：提交上面的操作
        conn.commit()
except pymysql.MySQLError as err:
    # 第四步：回滚（提交失败）  不需要增删改时，不使用回滚
    conn.rollback()
finally:
    # 关闭连接（释放资源）
    conn.close()


