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
cursor = Connection.cursor() # 获取游标対象
#增加数据
try:
    # 执行sql语句r插入多条数据
    cursor.execute("INSERT INTO student VALUES('吴欣',229980719,'22网工1班','女','19290232345')")# 提交数据
    Connection.commit()
except:
    # 发生错误时回滚
    cursor.rollback()

sql ='select * from student;'
with Connection. cursor() as cursor:
    cursor.execute(sql)   #执行SQL语句
    data = cursor . fetchall() #获取全部数据
#遍历图书数据
for student in data:
    print(f'姓名:{student['s_name']},学号: {student["s_id" ]}，班级: {student["s_class"]},性别: {student["s_sex"]},电话:{student["s_phone"]}')

cursor.close()
Connection.close() 