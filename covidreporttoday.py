import requests

r = requests.get('https://covid19.th-stat.com/api/open/today')

url = 'https://notify-api.line.me/api/notify'
token = 'qocgwRkAjYvUVhTfyjzHmSvzpcL9L8PUu5v24Df6eo3'
headers = {
    'content-type': 'application/x-www-form-urlencoded',
    'Authorization': f'Bearer {token}',
}

msg1 = 'อัพเดตผู้ป่วยโควิด 19 ใหม่ในไทย ประจำวันที่ : ' + str(r.json()['UpdateDate']) + '\n'
msg2 = 'จำนวนผู้ติดเชื้อรายใหม่ : ' + str(r.json()['NewConfirmed']) + '\n'
msg3 = 'จำนวนผู้ป่วยที่รักษาหาย : ' + str(r.json()['NewRecovered']) + '\n'
msg4 = 'จำนวนผู้เสียชีวิต : ' + str(r.json()['NewDeaths']) + '\n'
msg5 = 'จำนวนผู้ติดเชื้อสะสมทั้งหมด : ' + str(r.json()['Confirmed']) + '\n'
msg6 = 'อย่าลืมสวมหน้ากาก ล้างมือ เว้นระยะห่าง ขอให้ปลอดภัยทุกคนค่ะ'

sendmsg = {'message': msg1+msg2+msg3+msg4+msg5+msg6, 'stickerPackageId': 11538, 'stickerId': 51626502}

requests.post(url, headers=headers, data=sendmsg)
