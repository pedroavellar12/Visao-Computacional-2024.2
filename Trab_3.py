# Obtenção de Imagem
!git clone https://github.com/guimota-uerj/TestImages.git
!pwd
!ls

#Entrar na pasta de teste utilizada
%cd /content/TestImages/Logos/
!ls

'''
# **Questão:**
A derivada parcial em $x$ do gradiente digital definido por Roberts é dada pela matriz 
$ G_x=\begin{vmatrix}
-1 & -2 & -1\\
0 & 0 & 0 \\
1 & 2 & 1
\end{vmatrix}$

Esta matriz pode ser fatorada em duas matrizes: $Gx_v$, com dimensões $3\times1$, e  $Gx_h$, com dimensões $1\times3$.
$  Gx = Gx_v*Gx_h = \begin{vmatrix}
-1 \\
0  \\
1 
\end{vmatrix} * \begin{vmatrix}
1 & 2 & 1 
\end{vmatrix} $

Dada a função imagem $f$, compare do ponto de vista quantitativo e qualitativo os resultados obtidos por:

(A). $f*Gx$

(B). $f*Gx_v* Gx_h$

(C). $f* Gx_h * Gx_v$

Para isso, modifique o código a seguir de forma a implementar as estratégias (B) e (C) .
Dica: Ampare-se nas propriedades de comutatividade e associatividade da convolução e no cálculo do erro quadrático para realizar sua argumentação. 
'''

# INÍCIO DO CÓDIGO

import cv2
import matplotlib.pyplot as plt
import numpy as np

#Carregar imagem original
original = cv2.imread('CCompLogo1.png',0)

#Carregar a matriz Gx e seus fatores
Gx = np.array([[-1,-2,-1], [0,0,0], [1,2,1]])
Gx_v = np.array([[-1], [0], [1]])
Gx_h = np.array([[1, 2, 1]])

#Carregar os resultados para os itens A, B e C
ItemA = cv2.filter2D(original, -1, Gx)
ItemB = cv2.filter2D(cv2.filter2D(original, -1, Gx_v), -1, Gx_h)  
ItemC = cv2.filter2D(cv2.filter2D(original, -1, Gx_h), -1, Gx_v)

plt.figure(figsize = (15,45))

plt.subplot(3,1,1)
plt.title('Item A')
plt.axis('off')
plt.imshow(ItemA, cmap = 'gray')

plt.subplot(3,1,2)
plt.title('Item B')
plt.axis('off')
plt.imshow(ItemB, cmap = 'gray')

plt.subplot(3,1,3)
plt.title('Item C')
plt.axis('off')
plt.imshow(ItemC, cmap = 'gray')

plt.show()

# Análise Qualitativa (Mean Squared Error - MSE)
mse_AB = np.mean((ItemA - ItemB)**2)
mse_AC = np.mean((ItemA - ItemC)**2)

# Mostrar Resultados Qualitativos
print(f"MSE between Item A and Item B: {mse_AB}")
print(f"MSE between Item A and Item C: {mse_AC}")
