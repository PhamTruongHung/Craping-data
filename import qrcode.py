import qrcode
img = qrcode.make('Pham Truong Hung 123')
type(img)  # qrcode.image.pil.PilImage
img.save("1.png")
