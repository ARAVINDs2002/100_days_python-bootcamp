import pyqrcode

s = "www.facebook.org"


url = pyqrcode.create(s)


url.svg("myqr.svg", scale=8)


url.png('myqr.png', scale=8)
