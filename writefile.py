#  ตัวอย่างการเขียนข้อมูลลงในไฟล์
import time
import csv
row = 1
while True:
    f = open('mydata.txt', 'a')
    f.write("Food\n")
    print("Food %d" % row)
    row = row + 1
    time.sleep(2)
    f.close()