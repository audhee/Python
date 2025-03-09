import qrcode

data = input("Enter the data>> ")
qr = qrcode.make(data)
qr.save("QR.png",scale=5)
print("Qrcode generated and saved successfully")