import pymysql

Connection=pymysql.connect(
    host='localhost',
    user='root',
    password='123456',
    db='db_liul',
    charset='utf8',
    cursorclass = pymysql.cursors.DictCursor
)

sql='select * from books_229980501 order by id'
with Connection. cursor() as cursor:
    cursor.execute(sql)   #执行SQL语句
    data = cursor . fetchall() #获取全部数据
#遍历图书数据
for books in data:
    print(f'id:{books['id']},图书: {books["name" ]}，价格: {books["price"]}')
cursor = Connection.cursor()#获取游标对象
cursor.execute(sql)#执行SQL语句
cursor.close()