#  การสร้างฟังก์ชันใน Python
def hello(name):
    print("Hello %s " % name)


# ฟังก์ชันแบบมี return value
def area(width, height):
    total = width * height
    return total


# ฟังก์ชันแบบมีการกำหนดค่าเริ่มต้นให้กับ ตัวแปรที่รับค่า
def show_info(name, salary=0, lang="Unknow"):
    print('Name: %s' % name)
    print('Salary: %s' % salary)
    print('Language: %s' % lang)

# เรียกใช้ฟังก์ชัน hello(name)
hello("Samit")
hello("Wichai")
hello("สมคิด")

# เรียกใช้ฟังก์ชัน area(width, height)
print(area(10, 20))
print(area(50, 60))
print(area(12.5, 10.5))

# เรียกใช้ฟังก์ชัน show_info(name, salary=0, lang="Unknow")
show_info("Samit")
print("------------")
show_info("Somkid", 20000)
print("------------")
show_info("Artit", 30000, "Java")


