import requests

url = 'https://notify-api.line.me/api/notify'
token = 'qocgwRkAjYvUVhTfyjzHmSvzpcL9L8PUu5v24Df6eo3'
headers = {'content-type': 'application/x-www-form-urlencoded', 'Authorization': 'Bearer '+token}
msg = {'message': "สวัสดีวันพฤหัส", 'stickerPackageId': 446, 'stickerId': 1989}
r = requests.post(url, headers=headers, data=msg)

print(r.text)
