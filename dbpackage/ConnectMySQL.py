import pymysql


def connectdb():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='1234',
        db='pythondb',
        port=3306,
        charset='utf8',
        cursorclass=pymysql.cursors.DictCursor,
    )


#print(connectdb())