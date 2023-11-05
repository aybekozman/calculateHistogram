import cv2
import numpy as np
import matplotlib.pyplot as plt

#burda klasörden görüntüyü alıyoruz
icardi = cv2.imread("icardi.jpg")

cv2.imshow("Orjinal Resim",icardi)

#görüntüyü griye çevirme
griTon = cv2.cvtColor(icardi,cv2.COLOR_BGR2GRAY)
cv2.imshow("Gri Ton",griTon)
cv2.waitKey()
#histogram hesaplama
def histogramHesaplama(resim):
    genislik , yukseklik = resim.shape
    histogram=[0]*256
    for y in range(genislik):
        for x in range(yukseklik):
            pixel_value = resim[y,x]
            histogram[pixel_value]+=1

    return histogram
histogram=histogramHesaplama(griTon)

plt.bar(range(256), histogram)
plt.title("Histogram")
plt.xlabel("Piksel Değeri")
plt.ylabel("Piksel Sayısı")
plt.show()