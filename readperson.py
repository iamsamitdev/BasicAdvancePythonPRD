import pymysql
from dbpackage import ConnectMySQL as con


def read_person():
    connection = con.connectdb()
    cursor = connection.cursor()
    sql = """
         SELECT * FROM person ORDER BY id ASC
        """
    try:
        cursor.execute(sql)
        connection.commit()
        # loop data
        for row in cursor:
            # print(row)
            print("ID:", row['id'])
            print("Fullname:", row['fullname'])
            print("Weight:", row['weight'])
            print("Height:", row['height'])
            print('------------------')
    except pymysql.err:
        print(pymysql.err)


read_person()
