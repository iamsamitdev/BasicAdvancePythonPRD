# วิธีการเขียนโปรแกรมเพื่อตรวจสอบข้อผิดพลาด
try:
    number1 = float(input('Enter number 1: '))
    number2 = float(input('Enter number 2: '))
    # หาผลการหาร
    result = number1 / number2
    print('Result is ', result)
except ValueError:
    print('คุณป้อนข้อมูลไม่ถูกรูปแบบ')
except ZeroDivisionError:
    print('ผิดพลาดไม่สามารถหาร 0 ได้')
finally:
    print('จบการทำงาน')