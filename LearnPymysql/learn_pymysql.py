import pymysql

# 封装建立连接的对象
def get_conn():
    conn = pymysql.connect(
        host="mysql.hogwarts.ceshiren.com",
        user="stu",
        password="hogwarts_stu",
        database="hogwarts_stu",
        charset="utf8mb4"
    )
    return conn
# 执行sql语句
def execute_sql(sql):
    connect = get_conn()
    cursor = connect.cursor()
    cursor.execute(sql)  # 执行SQL
    record = cursor.fetchone()  # 查询记录
    return record

if __name__ == '__main__':
    # 执行sql语句查询user123这个用户的购物车有一个名称为 hogwarts1 的商品
    data = execute_sql("select * from emp6")
    print(data)
