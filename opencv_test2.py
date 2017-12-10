import cv2
import requests

header = {
    'Cookie':'PHPSESSID=n5c04f3oahfj59g47akjmbku36; citrix_ns_id=jgMWzQJQa1eKrb5p5YEi91UGXoc0002; PHPSESSID=uedofb9g9sp9thae9is1c130d2; __utmt=1; __utma=156794426.953449383.1512136712.1512622159.1512659659.13; __utmb=156794426.20.10.1512659659; __utmc=156794426; __utmz=156794426.1512136712.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
    'Referer':'https://portal.nctu.edu.tw/portal/login.php',
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
}
with open('pic.php', 'wb') as f:
    #res = requests.get('https://portal.nctu.edu.tw/captcha/pic.php?t=1512570353936', headers = header)
    res = requests.get('https://portal.nctu.edu.tw/captcha/pitctest/pic.php?t=1512570353936', headers = header)#paint
    #res = requests.get('https://portal.nctu.edu.tw/captcha/securimage/pic.php/captcha/pic.php?t=1512570353936', headers = header)#snake
    #res = requests.get('https://portal.nctu.edu.tw/captcha/claviska-simple-php-captcha/simple-php-captcha.php?_CAPTCHA&amp;t=0.26682400+1512572804')#///
    #res = requests.get('https://portal.nctu.edu.tw/captcha/cool-php-captcha/pic.php?t=1512570353936', headers = header)#text
    f.write(res.content)
#==========================  nothing  ==============
from PIL import Image

image = Image.open('pic.php')
#print(image)
#==========================  matrix  ================
import PIL
import numpy

pil_image = PIL.Image.open('pic.php').convert('RGB')
open_cv_image = numpy.array(pil_image)
#print(open_cv_image)
#==========================  image(show_out)  ========
from matplotlib import pyplot as plt
#plt.imshow(open_cv_image)
#plt.show()
#===========================  bounding  ================
imgray = cv2.cvtColor(open_cv_image, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray, 127, 255, 0)
image, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cnts = sorted([(c, cv2.boundingRect(c)[0]) for c in contours], key = lambda x:x[1])
ary = []
for (c,_) in cnts:
    (x, y, w, h) = cv2.boundingRect(c)
    print(x, y, w, h)
    if h >= 25 and h <= 32:
        ary.append((x, y, w, h))
    # if h >= 25 and h <= 45:
    #     ary.append((x, y, w, h))

print(ary)
#=========================  split_img + save_img  =======
# plt.imshow(thresh)
# plt.show()
import random
i = random.randint(0,99)
fig = plt.figure()
for id, (x, y, w, h) in enumerate(ary):
    roi = open_cv_image[y:y+h, x:x+w]
    thresh = roi.copy()
    #a = fig.add_subplot(1, len(ary), id+1)
    plt.imshow(thresh)
    plt.savefig('{}.jpg'.format(id+1+i), dpi = 100)
    #plt.show()
#plt.show()
#======================


#=======================  end_test  =========    
print(cv2.__version__)
