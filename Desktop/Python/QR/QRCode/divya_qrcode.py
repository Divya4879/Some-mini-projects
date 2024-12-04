import qrcode

profile_link = 'https://x.com/Divya67274866'

qr = qrcode.QRCode(version = 2, box_size = 5, border = 5)
qr.add_data(profile_link)
qr.make()

img = qr.make_image(fill_color = 'violet', back_color = 'blue')
img.save('profile_qr.png')