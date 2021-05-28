# ตัวอย่างฟังก์ชันการอ่านไฟล์
def readfile():
    try:
        f = open('mydata.txt', 'r', encoding='utf8')
        data = f.readlines()
        for i in data:
            print(i, end="")
        f.close()
    except UnicodeDecodeError:
        print('รูปแบบข้อความที่อ่านไม่รองรับ')


readfile()
