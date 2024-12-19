# Obtenção de Imagens
!git clone https://github.com/guimota-uerj/TestImages.git
!pwd
!ls

%cd /content/TestImages/HRTEM/
!ls

'''
**Questão:**
A imagem de teste Au.tif é uma imagem de microscopia eletrônica de transmissão de alta resolução. 
Na parte escura, próximo ao centro da imagem, podem ser observados diferentes orientações cristalográficas, cada uma contribuindo com diferentes componentes no domínio da frequência. 
A partir de uma análise de Fourier e filtragem no domínio da frequência usando filtros Gaussianos, separe tais orientações cristalográficas no maior número de grupos que você for capaz.
O primeiro grupo já está segmentado aparecendo na cor azul na figura 'Enhanced'.

Explique e analise os resultados obtidos.

Note que o filtro presente no programa original é um filtro ideal
'''

import cv2
import matplotlib.pyplot as plt
import numpy as np

def ImageFilter(fft_img,mask):
    fshift = fft_img*mask
    f_ishift = np.fft.ifftshift(fshift)
    img_back = cv2.idft(f_ishift)
    img_back = cv2.magnitude(img_back[:,:,0], img_back[:,:,1])
    return fshift,img_back

# Carregar a imagem Au.tif em escala de cinza
f = cv2.imread('Au.tif', 0)

#Exibir imagem original
plt.figure(figsize = (25, 25))
plt.subplot(3, 3, 1)
plt.title('$f$')
plt.axis('off')
plt.imshow(f,cmap = 'gray')

#Aplicar o filtro 1 e exibir o resultado
dft_f = cv2.dft(np.float32(f), flags = cv2.DFT_COMPLEX_OUTPUT)
dft_f_shift = np.fft.fftshift(dft_f)
magnitude = np.sqrt(dft_f_shift[:,:,0]**2 + dft_f_shift[:,:,1]**2)

plt.subplot(3, 3, 2)
plt.title('|F|')
plt.axis('on')
plt.imshow(255*np.log(magnitude/255 + 1), cmap = 'gray')

# filter g
g1 = (np.float32(([[[ 900>=(x - 144)**2 + (y - 237)**2 for z in range(1,3)]\
                      for y in range(0,512)] for x in range(0,512)]))) +\
    (np.float32(([[[ 900>=(x - 368)**2 + (y - 275)**2 for z in range(1,3)]\
                      for y in range(0,512)] for x in range(0,512)])))
    
g2 = np.float32(([[[900 >= (x - 200)**2 + (y - 300)**2 for z in range(1, 3)]\
                    for y in range(0, 512)] for x in range(0, 512)]))

plt.subplot(3, 3, 3)
plt.title('Filter')
plt.axis('off')
plt.imshow(g[:,:,0], cmap = 'gray')

plt.subplot(3, 3, 4)
plt.title('filtered')
plt.axis('off')
plt.imshow( magnitude * g[:,:,0], cmap = 'gray')

#Aplicar filtro g
f_dft_filtered_shift_g1, img_filtered_g1 = ImageFilter(dft_f_shift, g1)

# Aplicar o g2
f_dft_filtered_shift_g2, img_filtered_g2 = ImageFilter(dft_f_shift, g2)

plt.subplot(3, 3, 5)
plt.title('filtered')
plt.axis('off')
plt.imshow(img_filtered_g1, cmap = 'gray')

plt.subplot(3, 3, 6)
plt.title('Enhanced')
plt.axis('off')

img_filtered_g1 = np.uint8(255*img_filtered_g1/np.amax(img_filtered_g1))
RGB = np.stack((f,f, img_filtered_g1), axis=2)
plt.imshow(RGB)

# Exibir a imagem filtrada com o filtro g2
plt.subplot(3, 3, 7) 
plt.title('filtered g2')
plt.axis('off')
plt.imshow(img_filtered_g2, cmap='gray')

plt.subplot(3, 3, 8)
plt.title('Enhanced g2')
plt.axis('off')

img_filtered_g2 = np.uint8(255*img_filtered_g2/np.amax(img_filtered_g2))
RGB2 = np.stack((f, img_filtered_g2, f), axis=2)
plt.imshow(RGB2)
