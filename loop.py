import time

# While loop
row = 1
while row <= 100:
    if row % 10 == 0:
        print(row)
    else:
        print("%02d" % row, end=" ")
    row = row+1

# Infinity loop
number = 0
while True:
    if number == 0:
        print(1)
        number = 1
    else:
        print(0)
        number = 0
    time.sleep(1)