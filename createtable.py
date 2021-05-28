import pymysql
from dbpackage import ConnectMySQL as con


def create_table():
    connection = con.connectdb()
    cursor = connection.cursor()
    sql = """
           CREATE TABLE person(
            id int PRIMARY KEY AUTO_INCREMENT,
            fullname varchar(255),
            weight float,
            height float
        )
        """
    try:
        cursor.execute(sql)
        connection.commit()
        print("Create table success")
    except pymysql.err:
        print(pymysql.err)

create_table()