import pyqrcode
n = str(input("enter the text: "))
q = pyqrcode.create(n)
q.png('qr1.png', scale=10)
print("done:")
