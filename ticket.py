def ticket(passenger_type):
    try:
        passenger_type = passenger_type.upper().strip()
        if passenger_type == "A":
            fare = 50
        elif passenger_type == "S":
            fare = 45
        elif passenger_type == "C" or passenger_type == "E":
            fare = 25
        return fare
    except UnboundLocalError:
        print('มีข้อผิดพลาด ข้อมูลที่ป้อนไม่ถูกต้อง')
        return ""


p = input("Passenger type [A]dule , [S]tudent, [C]hild, [E]lder -> ")
print(ticket(p))
