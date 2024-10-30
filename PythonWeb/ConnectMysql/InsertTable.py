import pymysql

Connection=pymysql.connect(
    host='localhost',
    user='root',
    password='123456',
    db='db_liul',
    charset='utf8',
    cursorclass = pymysql.cursors.DictCursor
)

data = [("0501","零基础学Python",'Python','79.80','2018-5-20'),
        ("0502","Python从入门到待通",'Python','69.80','2018-6-18'),
        ("0503","零基础学PHP",'PHP','69.80','2017-5-21'),
        ("0504","PHP项目开发实战入门",'PHP','79.80','2016-5-21'),
        ("0505","零基础学Java",'Java','69.80','2017-5-21'),
        ]
cursor = Connection.cursor() # 获取游标対象
try:
    # 执行sql语句r插入多条数据
    cursor.executemany("insert into books_229980501(id,name, category, price, publish_time) values (%s,%s,%s,%s,%s)",data)# 提交数据
    Connection.commit()
except:
    # 发生错误时回滚
    cursor.rollback()

cursor.close()
Connection.close() 