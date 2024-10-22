# Base de Imagens
!git clone https://github.com/guimota-uerj/TestImages.git
!pwd
!ls

# Seleção da Pasta da Imagem de Teste
%cd /content/TestImages/StormTrooper/
!ls

'''Questão 1:
A imagem StormTrooper.jpg foi distorcida por uma transformação projetiva. 

**a.** Obtenha a matriz de transformação que recupera a geometria original usando a função cv2.getPerspectiveTransform(). 
**b.** Calcule a mesma matriz pelo método dos mínimos quadrados, usando operações com matrizes.
**c.** Compare e analise os resultados obtidos nos itens **a.** e **b.**.

**Atenção:** no item **b.** somente é permitido usar funções prontas que invertam, transponham e multipliquem matrizes.
**Dica:** utilize os vértices da folha de papel, que tem formato A4, como referência. '''

import cv2
import matplotlib.pyplot as plt
import numpy as np

pts1 = np.float32([[56,65],[368,52],[28,387],[389,390]]) #Pontos da Imagem Original
pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]]) #Pontos da Imagem de Destino

#Calcular a matriz de transformação
M = cv2.getPerspectiveTransform(pts1,pts2)
print('M = ', M)

# Calcular a matriz de transformação utilizando método dos mínimos quadrados
A = []
b = []
for i in range(4):
    x, y = pts1[i]
    u, v = pts2[i]
    A.append([x, y, 1, 0, 0, 0, -u*x, -u*y])
    A.append([0, 0, 0, x, y, 1, -v*x, -v*y])
    b.append(u)
    b.append(v)
A = np.array(A)
b = np.array(b)

# Solução para a matriz de transformação utilizando mínimos quadrados:
h = np.linalg.solve(A.T @ A, A.T @ b)
M_ls = np.array([[h[0], h[1], h[2]],
                  [h[3], h[4], h[5]],
                  [h[6], h[7], 1]])
print('M_ls = ', M_ls)


#Erro Médio Quadrado - MSE
mse = np.mean((M - M_ls) ** 2)
print('MSE = ', mse)


'''Questão 2:
Aplique a matriz de transformação obtida na questão 1 e corrija a prespectiva da imagem utilizando as interpolações:

**a.**  vizinho mais próximo
**b.**  bilinear
**c.**  bicúbica

**Atenção:** Explique os resultados com base na teoria apresentada nas aulas. 
**Dica:** para mostrar o efeito da intepolação, apresente um pequeno fragmento das imagens de saída lado a lado.
'''

import cv2
import matplotlib.pyplot as plt
import numpy as np

#Carregar a Imagem
img_in = cv2.imread('StormTrooper.jpg')
print(img_in.shape)

#Matriz M
M

# Aplique a transformação com diferentes interpolações
img_nearest = cv2.warpPerspective(img_in, M, (1500, 1800), flags=cv2.INTER_NEAREST)
img_bilinear = cv2.warpPerspective(img_in, M, (1500, 1800), flags=cv2.INTER_LINEAR)
img_bicubic = cv2.warpPerspective(img_in, M, (1500, 1800), flags=cv2.INTER_CUBIC)

# Exiba as imagens
plt.figure(figsize=(20, 15))
plt.subplot(131), plt.imshow(img_nearest), plt.title('Vizinho Mais Próximo')
plt.subplot(132), plt.imshow(img_bilinear), plt.title('Bilinear')
plt.subplot(133), plt.imshow(img_bicubic), plt.title('Bicúbica')
plt.show()

# Recorte um fragmento para comparação detalhada
fragmento_nearest = img_nearest[600:650, 550:600]
fragmento_bilinear = img_bilinear[600:650, 550:600]
fragmento_bicubic = img_bicubic[600:650, 550:600]

plt.figure(figsize=(20, 15))
plt.subplot(131), plt.imshow(fragmento_nearest), plt.title('Fragmento - Vizinho Mais Próximo')
plt.subplot(132), plt.imshow(fragmento_bilinear), plt.title('Fragmento - Bilinear')
plt.subplot(133), plt.imshow(fragmento_bicubic), plt.title('Fragmento - Bicúbica')
plt.show()


