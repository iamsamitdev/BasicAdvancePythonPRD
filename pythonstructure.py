import os, sys


# การสร้างฟังก์ชัน main สำหรับเริ่มรันโปรแกรมที่นี่
def main():
    print("This is python program")

    cwd = os.getcwd()
    print(cwd)

    path = "D:\TrainingDocument"
    dir_list = os.listdir(path)
    print(dir_list)

    temp = os.walk(sys.argv[1], topdown=False)
    for root, dirs, files in temp:
        for i in dirs:
            dir = os.path.join(root, i)

    # การสร้างตัวแปร
    fullname = "Samit Koyom"
    age = 40
    print(fullname, age)

    # การเขียนเงื่อนไข
    if age >= 18:
        print("Allow to access")
    else:
        print("Not allow to this area!")

    # สร้างตัวแปร List (หรือ Array)
    fruit = ['apple','orange','banana']

    # การทำซ้ำ (loop)
    for i in fruit:
        print(i)


main()
