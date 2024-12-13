import qrcode 
from PIL import Image
import qrcode.constants 
data=str(input("enter your qr data: "))
qr= qrcode.QRCode(version=1,
                  error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=25,border=1,)
qr.add_data(data)
qr.make(fit=True)
img=qr.make_image(fill_color="darkgreen",back_color="lightgray")
img.save("raj1.png")