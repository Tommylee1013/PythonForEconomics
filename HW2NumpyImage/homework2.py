import numpy as np
from PIL import Image, ImageFilter
import urllib.request
import pandas as pd
import matplotlib.pyplot as plt

url = 'https://raw.githubusercontent.com/k5yi/econ2005/master/datasets/%EC%8B%9C%EC%95%84.png'
im = Image.open(urllib.request.urlopen(url))

img = np.array(im) + 40

print(img.shape)
print('pixel value range', np.min(img), np.max(img))
plt.imshow(img)

def invert_image(img) :
  a = np.arange(256*256*3).reshape((256,256,3))
  a.fill(255)
  return plt.imshow(a - img)

invert_image(img) # 3.1

def grayscale_image(img):
    weights=np.array([0.2989, 0.5870, 0.1140])
    grayImage = img.copy()

    for i in range(3):
        grayImage[:,:,i] = np.array(img[:, :, 0]) * weights[0] + np.array(img[:, :, 1]) * weights[1] + np.array(img[:, :, 2]) * weights[2]
           
    return plt.imshow(grayImage)    

grayscale_image(img) # 3.2

def boundary(img, cutoff):
  segmented_Image = img.copy()

  for i in range(3):
    segmented_Image[:,:,i] = np.array(img[:, :, 0])/3 + np.array(img[:, :, 1])/3 + np.array(img[:, :, 2])/3

  for i in range(256) :
    for j in range(256) :
      for k in range(3) :
        if segmented_Image[i][j][k] < cutoff :
          segmented_Image[i][j][k] = 0
        else :
          segmented_Image[i][j][k] = 255

  return plt.imshow(segmented_Image)  

boundary(img, cutoff=100) # 3.3

def flip(img, by = None) :
  if by == 'vertical' :
    return plt.imshow(img[::-1])
  elif by == 'horizontal' :
    return plt.imshow(img[:,::-1])
  else :
    return print("Choose one between 'vertical' or 'horizontal'.")

flip(img, by='vertical')
flip(img, by='horizontal') # 3.4

def padding(img, padding_size, pad=255):
  if type(padding_size) == int :
    a = np.zeros(padding_size*(padding_size + padding_size + 256)*3).reshape(padding_size,(padding_size + padding_size + 256),3)
    a.fill(pad)
    b = np.zeros(256*padding_size*3).reshape(256,padding_size,3)
    b.fill(pad)
    c = np.zeros(256*padding_size*3).reshape(256,padding_size,3)
    c.fill(pad)
    d = np.zeros(padding_size*(padding_size + padding_size + 256)*3).reshape(padding_size,(padding_size + padding_size + 256),3)
    d.fill(pad)
  else : 
    a = np.zeros(padding_size[0]*(padding_size[1] + padding_size[1] + 256)*3).reshape(padding_size[0],(padding_size[1] + padding_size[1] + 256),3)
    a.fill(pad)
    b = np.zeros(256*padding_size[1]*3).reshape(256,padding_size[1],3)
    b.fill(pad)
    c = np.zeros(256*padding_size[1]*3).reshape(256,padding_size[1],3)
    c.fill(pad)
    d = np.zeros(padding_size[0]*(padding_size[1] + padding_size[1] + 256)*3).reshape(padding_size[0],(padding_size[1] + padding_size[1] + 256),3)
    d.fill(pad)
  
  new = np.concatenate((a,np.concatenate((b,img,c), axis=1),d), axis=0)
  return plt.imshow(new.astype(np.uint8))

padding(img, padding_size=20, pad=255)
padding(img, padding_size=(10,20), pad=255) # 3.5



