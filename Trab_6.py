!git clone https://github.com/guimota-uerj/TestImages.git
%cd /content/TestImages/Landsat/

'''
**Trabalho 8: Pan-Sharpening**
Implemente o esquema de fusão PAN (Pan-Sharpening) apresentado na figura a seguir. Inspire-se nos trechos de código apresentados ao longo destes exemplos para fazê-lo.
'''

import cv2
import matplotlib.pyplot as plt
#from google.colab.patches import cv2_imshow
img = cv2.imread('FusaoLandsat8.png', 1)
print(img.shape)
plt.figure(figsize = (20,15)) # figsize : (float width, float height)  in inches.
plt.title('Esquema do Enunciado do Trabalho')
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.axis('off')
#plt.show()

'''
** 1) Este código apresenta como obter as bandas 1, 2, 3 e 8 da imagem de teste diretamente do github**
'''

import cv2
import numpy as np
import matplotlib.pyplot as plt
#from google.colab.patches import cv2_imshow

# Carregar as bandas
band1 = cv2.imread('LANDSAT_7_ETMXS_20000111_217_076_L2_BAND1.tif', 0)
band2 = cv2.imread('LANDSAT_7_ETMXS_20000111_217_076_L2_BAND2.tif', 0)
band3 = cv2.imread('LANDSAT_7_ETMXS_20000111_217_076_L2_BAND3.tif', 0)
band8 = cv2.imread('LANDSAT_7_ETMPAN_20000111_217_076_L2_BAND8.tif', 0)

# 1. Redimensionar as bandas H e S (bandas 2 e 3)
height, width = band8.shape  # Dimensões da banda PAN
band1_resized = cv2.resize(band1, (width, height), interpolation=cv2.INTER_CUBIC)
band2_resized = cv2.resize(band2, (width, height), interpolation=cv2.INTER_CUBIC)
band3_resized = cv2.resize(band3, (width, height), interpolation=cv2.INTER_CUBIC)

# 2. Converter RGB (bandas 3, 2, 1) para HSV
rgb_image = np.stack((band3_resized, band2_resized, band1_resized), axis=2)  # Compor a imagem RGB
vsh_image = cv2.cvtColor(rgb_image.astype(np.uint8), cv2.COLOR_BGR2HSV)  # Converter para HSV

# 3. Substituir a banda V pela banda PAN
vsh_image[:, :, 0] = band8  # Substituir a intensidade (V - Value)

# 4. Converter de volta para RGB
fused_image = cv2.cvtColor(vsh_image, cv2.COLOR_HSV2BGR)  # Converter de volta para RGB

plt.subplot(2,1,1)
plt.title('Exemplo gray')
plt.imshow(band8, cmap = 'gray', interpolation = 'bicubic',aspect='auto')
plt.axis('off')

plt.subplot(2,1,2)
plt.imshow(cv2.cvtColor(fused_image, cv2.COLOR_BGR2RGB))
plt.title('Imagem Pan-Sharpened')
plt.axis('off')

plt.show()

'''
** 2) O código a seguir demonstra como fazer a uma operação geométrica. Modifique-o para fazer o zoom das bandas H e S**
'''

%cd /content/TestImages/StormTrooper/
import cv2
import matplotlib.pyplot as plt
import numpy as np

img_in = cv2.imread('StormTrooper.jpg')

# Converter a imagem para HSV
hsv = cv2.cvtColor(img_in, cv2.COLOR_BGR2HSV)

# Separar os canais H, S e V
h, s, v = cv2.split(hsv)

# Definir o fator de zoom
zoom = 5  # Aumentar este valor para mais zoom

# Aplicando zoom nas bandas H e S usando interpolação bicúbica
h_zoom = cv2.resize(h, None, fx=zoom, fy=zoom, interpolation=cv2.INTER_CUBIC)
s_zoom = cv2.resize(s, None, fx=zoom, fy=zoom, interpolation=cv2.INTER_CUBIC)

# Resize the v channel to match the zoomed dimensions of h and s
v_zoom = cv2.resize(v, (h_zoom.shape[1], h_zoom.shape[0]), interpolation=cv2.INTER_CUBIC)

# Combinar os canais H, S e V com zoom
hsv_zoom = cv2.merge((h_zoom, s_zoom, v_zoom))

# Converter a imagem de volta para BGR
img_zoom = cv2.cvtColor(hsv_zoom, cv2.COLOR_HSV2BGR)


print("Dimensões da imagem original:", img_in.shape)
print("Dimensões da imagem com zoom:", img_zoom.shape)

M = np.float32([[1, 0,0], [0,1,0], [0,0,1]])

img_out = cv2.warpPerspective(img_in,M,(1500,1800),flags=cv2.INTER_NEAREST)

plt.figure(figsize=(15,15))
plt.subplot (121), plt.axis('off'), plt.imshow(img_in),plt.title('Input')
plt.subplot (122), plt.axis('off'), plt.imshow(img_zoom),plt.title('Zoom')
plt.show()

'''
** 3) Fusão de imagens tons de cinza em uma imagem colorida**
Agora eu vou mostrar como fundir **imagens** tons de cinza em uma única imagem RGB
'''

%cd /content/TestImages/Landsat/
band1 = cv2.imread('LANDSAT_7_ETMXS_20000111_217_076_L2_BAND1.tif', 0)
band2 = cv2.imread('LANDSAT_7_ETMXS_20000111_217_076_L2_BAND2.tif', 0)
band3 = cv2.imread('LANDSAT_7_ETMXS_20000111_217_076_L2_BAND3.tif', 0)
plt.figure(figsize = (18,18)) # figsize : (float width, float height)  in inches.

plt.subplot(1,3,1)
plt.title('Exemplo composite 321')
plt.axis('off')
plt.imshow(cv2.cvtColor(np.stack((band1,band2, band3), axis=2), cv2.COLOR_BGR2RGB))

plt.subplot(1,3,2)
plt.title('Exemplo composite 123')
plt.axis('off')
plt.imshow(np.stack((band1,band2, band3), axis=2))

plt.subplot(1,3,3)
plt.title('Exemplo composite 321 "de uma outra forma"')
plt.axis('off')
plt.imshow(np.stack((band3,band2, band1), axis=2))

#plt.show()






