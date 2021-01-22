import time
from PIL import ImageGrab

time.sleep(5)

for i in range(1, 11): # 2초 간격으로 이미지 10개 저장
    img = ImageGrab.grab() # 현재 스크린 이미지를 가져옴
    img.save("image{}.png".format(i)) # 파일로 저장 (image1.png ~ image10.png)
    time.sleep(2) # 2초 간격