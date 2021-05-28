from tkinter import *  # โหลดโมดูล tkinter เข้ามายังโปรแกรมทุกคลาส
from tkinter import ttk

# สร้าง Object tkinter
mainFrm = Tk()


# สร้างฟังก์ชันการคำนวณ  VAT
def calVat():
    get_amount = amount.get()
    get_vat = vat.get()
    result = float(get_amount) + (float(get_amount) * float(get_vat) / 100)

    total.delete(0, END)  # เคลียร์ช่องผลลัพธ์ให้เป็นค่าว่างก่อนทุกครั้ง
    total.insert("", str(result)) # แสดงผลลัพธ์จากค่าที่ได้

    print("%.2f" % result)

#  การกำหนด title ให้กับโปรแกรม
mainFrm.title('โปรแกรมคำนวณภาษี')

# กำหนดตัวแปรเก็บความกว้าง x สูง ของโปรแกรม
window_width = 300
window_height = 150

# กำหนดตัวแปรเก็บความกว้าง x สูงของหน้าจอคอมพิวเตอร์
screen_width = mainFrm.winfo_screenwidth()
screen_height = mainFrm.winfo_screenheight()

x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))

# กำหนดความกว้างและความสูงของหน้าต่างโปรแกรม
mainFrm.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

# สร้าง Widget
ttk.Label(mainFrm, text='ยอดเงิน (บาท): ').grid(column=0, row=0, padx=10, pady=10, sticky='e')
amount = ttk.Entry(mainFrm)
amount.grid(column=1, row=0)

ttk.Label(mainFrm, text='Vat (%): ').grid(column=0, row=1, padx=10, pady=10, sticky='e')
vat = ttk.Entry(mainFrm)
vat.grid(column=1, row=1)

btnCal = ttk.Button(mainFrm, text='คำนวณยอด', command=calVat).grid(column=1, row=2, sticky='w')

ttk.Label(mainFrm, text='ยอดรวม Vat: ').grid(column=0, row=3, padx=10, pady=10, sticky='e')
total = ttk.Entry(mainFrm)
total.grid(column=1, row=3, padx=0, pady=10, sticky='w')

# การสั่ง run แสดงหน้าต่างโปรแกรม
mainFrm.mainloop()

