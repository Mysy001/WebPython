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
#修改数据
sql="""
UPDATE student SET s_class='22网工1班' WHERE s_name='张三';
"""
cursor = Connection.cursor() # 获取游标対象
cursor.execute(sql)#执行SQL语句

sql1 ='select * from student;'
with Connection. cursor() as cursor:
    cursor.execute(sql1)   #执行SQL语句
    data = cursor . fetchall() #获取全部数据
#遍历图书数据
for student in data:
    print(f'姓名:{student['s_name']},学号: {student["s_id" ]}，班级: {student["s_class"]},性别: {student["s_sex"]},电话:{student["s_phone"]}')

cursor.close()