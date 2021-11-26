import picamera
import time
import requests
import json
import datetime as dt
from PIL import Image
from time import sleep
from tkinter import *
#from PIL import image,ImageDraw,ImageFont

list1 = {1: "星期一", 2: "星期二", 3: "星期三", 4: "星期四", 5: "星期五"}
table = {'星期一': {
         'course':{'web程序设计'  " 串口通信编程" "  数字图像处理"},
         'range':{" 1-2(1,18)" "   3-5(10,15)" "    10-11(1,18)"},
         'room':{" 信809""    网络实验室" "    理405"}
    },
         '星期二': {
         'course':{"数字通信原理""  串口通信编程"},
         'range':{"6-7(1,18)""   10-11(1,18)"},
         'room':{" 理312""       理101"}
    },
         '星期三': {
         'course':{"数字图像处理"},
         'range':{ "6-7(1,18)"},
         'room':{"  文308"}
    },
         '星期四': {
         'course':{"web程序设计"},
         'range':{"1-2(1,18)"},
         'room':{"  信809"}
    },
         '星期五': {
         'course':{"数字通信原理""   数字通信原理"},
         'range':{"3-5(10,16)双""   6-7(2-16)双"},
         'room':{" 通信实验室""      信805"}
    }
}

mon = list1[1]      #星期一
course1 = table['星期一']['course']
range1 = table['星期一']['range']
room1 = table['星期一']['room']
tue = list1[2]
course2 = table['星期二']['course']
range2 = table['星期二']['range']
room2 = table['星期二']['room']
wed = list1[3]
course3 = table['星期三']['course']
range3 = table['星期三']['range']
room3 = table['星期三']['room']
tur = list1[4]
course4 = table['星期四']['course']
range4 = table['星期四']['range']
room4 = table['星期四']['room']
fri = list1[5]
course5 = table['星期五']['course']
range5 = table['星期五']['range']
room5 = table['星期五']['room']

camera = picamera.PiCamera()
camera.resolution = (640,480)
camera.framerate = 24
camera.start_preview()

#fountText = ImageFont.truetype('font/simfang.ttf',textSize,encording='utf-8')
#draw.text((left,top),text,textColor,font=fontText)
KEY = 'S218cSfnT2wPJE7Lg'           #密钥
currentWeatherAPI = 'https://api.seniverse.com/v3/weather/now.json?key=S218cSfnT2wPJE7Lg&location=chaozhou&language=zh-Hans&unit=c'
res = requests.get(currentWeatherAPI)
json_date = json.loads(res.text)
id = json_date['results'][0]['location']['id']
country = json_date['results'][0]['location']['country']
path = json_date['results'][0]['location']['path']
text = json_date['results'][0]['now']['text']
dailyAPI = 'https://api.seniverse.com/v3/weather/daily.json'

def c():
    can1 = Canvas(root, bg='black', width=800, height=900)
    can1.pack()
    can1.create_text(80, 20, text=path, font=('宋体', 10,), fill='white')
    can1.create_text(50, 40, text=text, font=('宋体', 9,), fill='white')
    can1.create_text(30, 60, text=mon, font=('宋体', 9,), fill='white')
    can1.create_text(130, 80, text=course1, font=('宋体', 9,), fill='white')
    can1.create_text(130, 100, text=range1, font=('宋体', 9,), fill='white')
    can1.create_text(125, 120, text=room1, font=('宋体', 10,), fill='white')
    can1.create_text(30, 140, text=tue, font=('宋体', 10,), fill='white')
    can1.create_text(105, 160, text=course2, font=('宋体', 10,), fill='white')
    can1.create_text(110, 180, text=range2, font=('宋体', 10,), fill='white')
    can1.create_text(90, 200, text=room2, font=('宋体', 10,), fill='white')
    can1.create_text(30, 220, text=wed, font=('宋体', 10,), fill='white')
    can1.create_text(60, 240, text=course3, font=('宋体', 10,), fill='white')
    can1.create_text(60, 260, text=range3, font=('宋体', 10,), fill='white')
    can1.create_text(60, 280, text=room3, font=('宋体', 10,), fill='white')
    can1.create_text(30, 300, text=tur, font=('宋体', 10,), fill='white')
    can1.create_text(60, 320, text=course4, font=('宋体', 10,), fill='white')
    can1.create_text(60, 340, text=range4, font=('宋体', 10,), fill='white')
    can1.create_text(60, 360, text=room4, font=('宋体', 10,), fill='white')
    can1.create_text(30, 380, text=fri, font=('宋体', 10,), fill='white')
    can1.create_text(105, 400, text=course5, font=('宋体', 10,), fill='white')
    can1.create_text(105, 420, text=range5, font=('宋体', 10,), fill='white')
    can1.create_text(95, 440, text=room5, font=('宋体', 10,), fill='white')
root = Tk()
root.title("魔镜")
root.geometry("800x900+0+0")
c()
root.mainloop()

# img = Image.open('测试.jpg')
# pad = Image.new('RGB',(
#     96,
#     48 ,
#     ))
# print((img.size[0] + 31) // 32)
# print((img.size[1] + 15) // 16)
# pad.paste(img, (0, 0))
# o = camera.add_overlay(pad.tobytes(),size=img.size)
# o.alpha = 70
# o.layer = 3
# while True:
#     sleep(1)



while 1:
    
    
    t = time.time()
    t = time.localtime(t)
    t = time.strftime('%Y-%m-%d %H:%M:%S',t)
    
    a='''                         {}
                               {}
                  {}
    '''.format(id,country,t)

    camera.annotate_text = a
  
# time.sleep(3)

#camera.capture('lmh45 cctv.jpg')
