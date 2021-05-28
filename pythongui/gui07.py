from tkinter import *
from tkinter import ttk

mainfrm = Tk()
mainfrm.title("โปรแกรมเครื่องคิดเลข")   # แสดงข้อความที่ title bar

# สร้างฟังก์ชัน calculate() กำหนดรูปแบบการคำนวณ
def calculate():
    result = 0  # ก่อนการคำนวณควรเซ็ตค่าผลลัพธ์เป็น 0 ทุกครั้ง
    entResult.delete(0, END)  # เคลียร์ช่องผลลัพธ์ให้เป็นค่าว่างก่อนทุกครั้ง

    num1 = entNum1.get()
    num2 = entNum2.get()

    # ตรวจสอบเงื่อนไขแล้วว่าค่าสตริง v ของ Radio button เป็น 1 2 3 หรือ 4 (บรรทัด 78)
    # ให้เข้าเงื่อนไข บวก ลบ คูณ หรือหาร นั้นๆ แล้วคำนวณค่าเก็บใน result พร้อมแสดงผล
    if str(v.get()) == "1":
        result = int(num1) + int(num2)
        entResult.insert("", str(result))
    elif str(v.get()) == "2":
        result = int(num1) - int(num2)
        entResult.insert("", str(result))
    elif str(v.get()) == "3":
        result = int(num1) * int(num2)
        entResult.insert("", str(result))
    elif str(v.get()) == "4":
        result = int(num1) / int(num2)
        entResult.insert("", str(result))

# สร้างฟังก์ชัน clearEntry() สำหรับลบข้อมูลแต่ละ Entry widget
def clearEntry():
    entNum1.delete(0, END)
    entNum2.delete(0, END)
    entResult.delete(0, END)

# สร้าง LabelFrame เอาไว้ใช้สำหรับจัดกลุ่ม Label และ Entry widget
lblFrm1 = ttk.LabelFrame(mainfrm, text="โปรแกรมคำนวณ", labelanchor="n")
lblFrm1.pack(padx=10, pady=10, side="left")

# สร้าง Label widget กำหนดให้แสดงข้อความ
lblNum1 = ttk.Label(lblFrm1,
                    text="ป้อนตัวเลขที่ 1 :").grid(column=0, row=0,
                                                   padx=5, sticky="e")
lblNum2 = ttk.Label(lblFrm1,
                    text="ป้อนตัวเลขที่ 2 :").grid(column=0, row=1,
                                                   padx=5, sticky="e")
lblResult = ttk.Label(lblFrm1,
                      text="ผลลัพธ์ :").grid(column=0, row=2,
                                             padx=5, sticky="e")

# สร้าง Entry widget ขึ้นมา 3 ตัว สำหรับป้อนข้อมูล
entNum1 = ttk.Entry(lblFrm1)
entNum2 = ttk.Entry(lblFrm1)
entResult = ttk.Entry(lblFrm1)

# จัดวาง Entry widget ด้วยเมธอด grid()
entNum1.grid(column=1, row=0, padx=5)
entNum2.grid(column=1, row=1, padx=5)
entResult.grid(column=1, row=2, padx=5)

# สร้างปุ่มกด Button widget เรียกใช้งานฟังก์ชัน calculate() และฟังก์ชัน clearEntry()
btnEnter = ttk.Button(lblFrm1, text="Enter",
                      command=calculate).grid(column=0, row=3,
                                              padx=5, pady=5)
btnClear = ttk.Button(lblFrm1, text="Clear",
                      command=clearEntry).grid(column=1, row=3,
                                               padx=5, )

# สร้าง LabelFrame widget สำหรับจัดกลุ่ม Radio button widget
lblFrm2 = ttk.LabelFrame(mainfrm, text="เลือกการคำนวณ", labelanchor="n")
lblFrm2.pack(padx=10, pady=10)

# สร้าง Radio button widget 4 ตัว ใช้ตรวจสอบการเลือกการ + - * /

# กำหนดค่าเริ่มต้นของ Radio button ที่ 1 (การบวก)
v = StringVar(lblFrm2, "1")

# สร้างดิกชันนารี key และ value เป็นชนิดข้อมูลสตริงเก็บค่าเครื่องหมาย
operations = {"การบวก": "1",
              "การลบ": "2",
              "การคูณ": "3",
              "การหาร": "4"
              }

# สร้าง Radio button โดยใช้การวน loop กำหนดค่าต่าง ๆ
for (text, operations) in operations.items():
    Radiobutton(lblFrm2, text=text, variable=v,
                value=operations).pack(side=TOP, ipady=4)

mainfrm.mainloop()