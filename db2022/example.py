import pymysql
stu_id = int(input('学号'))
stu_name = input('姓名')
stu_sex = input('性别')
stu_birth = input('生日')
# 1.创建连接获得连接对象
conn = pymysql.connect(host='gz-cynosdbmysql-grp-18whccs3.sql.tencentcdb.com',port=24561,
                      user='root',password='1qazxsw@',
                       database='school',charset='utf8')
try:
    # 2.获取游标对象（通过游标对象可以向数据库服务器发送SQL语句）
    with conn.cursor() as cursor:
        #  3.通过游标对象可以向数据库服务器发出SQL语句
        affected_rows = cursor.execute(
            # 安全占位符，不能采用字符串拼接的格式
            f"insert into tb_student values (%s,%s,%s,%s)",
            #  元组
            (stu_id,stu_name,stu_sex,stu_birth)
    )
        if affected_rows == 1:
             print('新增数据成功！！')
    # 4.提交事务(将输入的数据提交到数据库）
    conn.commit()
except pymysql.MySQLError as err:
    # 4. 回滚事务
    conn.rollback()
    print(type(err),err)
finally:
    # 5.关闭连接
    conn.close()

