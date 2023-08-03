# ตัวอย่างฟังก์ชันการอ่านไฟล์
def readfile():
    try:
        with open('mydata.txt', 'r', encoding='utf8') as f:
            data = f.readlines()
            for i in data:
                print(i, end="")
    except UnicodeDecodeError:
        print('รูปแบบข้อความที่อ่านไม่รองรับ')


readfile()
