import pymysql

Connection=pymysql.connect(
    host='localhost',
    user='root',
    password='123456',
    db='db_liul',
    charset='utf8',
    cursorclass = pymysql.cursors.DictCursor
)

sql="""
CREATE Table books_229980501(
    id int NOT NUll AUTO_INCREMENT,
    name VARCHAR(255) not null,
    category VARCHAR(50) NOT NULL,
    price DECIMAL(10,2) DEFAULT '0',
    publish_time DATE DEFAULT NULL,
    PRIMARY KEY (id)
);
"""
cursor = Connection.cursor()#获取游标对象
cursor.execute(sql)#执行SQL语句
cursor.close()