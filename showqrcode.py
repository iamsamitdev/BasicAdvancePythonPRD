import qrcode

# สร้าง QRCode
qr = qrcode.QRCode()
qr.add_data('https://www.google.co.th/')
qr.make()

# บันทึก qrcode เก็บลงในโปรเจ็กต์
img = qr.make_image()
img.save('qrcode_test.png')

