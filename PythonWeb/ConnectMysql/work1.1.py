import pymysql

#连接MySQL 的 '网工2班' 数据库
Connection=pymysql.connect(
    host='localhost',
    user='root',
    password='123456',
    db='网工2班',
    charset='utf8',
    cursorclass = pymysql.cursors.DictCursor
)

#SQL语句(创建数据库表)
sql="""
CREATE Table IF NOT EXISTS student(
    s_name CHARACTER(10) COMMENT '姓名',
    s_id INT PRIMARY KEY COMMENT '学号' AUTO_INCREMENT,
    s_class CHARACTER(255) COMMENT '班级',
    s_sex CHARACTER(2) COMMENT '性别',
    s_phone CHARACTER(11) COMMENT '电话'
);
"""
cursor = Connection.cursor() # 获取游标対象
cursor.execute(sql)#执行SQL语句

#添加数据
data = [("张三","229980501",'22网工2班','男','19135732048'),
        ("李四","229980502",'22网工2班','男','19135732047'),
        ("王五","229980503",'22网工2班','男','19135732046'),
        ("李雅","229980504",'22网工2班','女','19135732045'),
        ]

cursor = Connection.cursor() # 获取游标対象
try:
    # 执行sql语句r插入多条数据
    cursor.executemany("insert into student values (%s,%s,%s,%s,%s)",data)# 提交数据
    Connection.commit()
except:
    # 发生错误时回滚
    cursor.rollback()


cursor.close()