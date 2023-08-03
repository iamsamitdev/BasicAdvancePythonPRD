import time

for row in range(1, 101):
    if row % 10 == 0:
        print(row)
    else:
        print("%02d" % row, end=" ")
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