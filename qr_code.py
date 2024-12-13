# import qrcode 
# data=str(input("enter qrcude_data: "))
# img= qrcode.make(data)
# img.save("raviqr.png")
import pyttsx3
engine=pyttsx3.init()
voices=engine.getProperty('voices')
for voice in voices:
    print(f"ID:{voice.id}")
    print(f"Name:b{voice.name}")