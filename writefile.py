#  ตัวอย่างการเขียนข้อมูลลงในไฟล์
import time
import csv
row = 1
while True:
    with open('mydata.txt', 'a') as f:
        f.write("Food\n")
        print("Food %d" % row)
        row = row + 1
        time.sleep(2)