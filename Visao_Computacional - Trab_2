!git clone https://github.com/guimota-uerj/TestImages.git
!pwd
!ls

%cd /content/TestImages/PorDoSol/
!ls

'''
#**Questão 1:**
Utilizando a imagem colorida PorDoSol.tiff, implemente uma correção gama.
Utilize valores de gama acima de um e abaixo de um. Execute a correção gama nos canais R, G e B independentemente e apresente a imagem resultante.
Em seguida, analise os resultados quanto aos seus efeitos qualitativos nas partes claras e escuras da imagem.
Apresente também os gráficos das funções gama e os histogramas das imagens.
'''

import cv2
import matplotlib.pyplot as plt
import numpy as np

# Load the image
original = cv2.imread('PorDoSol.tiff')

# Define gamma values
gamma_values = [0.5, 1.0, 1.5]  # Values above and below 1

# Create a figure to display the results
plt.figure(figsize=(15, 12))

# Loop through each gamma value
for i, gamma in enumerate(gamma_values):
    # Apply gamma correction to each channel independently
    gamma_corrected_b = np.uint8(((np.float32(original[:, :, 0]) / 255) ** gamma) * 255)
    gamma_corrected_g = np.uint8(((np.float32(original[:, :, 1]) / 255) ** gamma) * 255)
    gamma_corrected_r = np.uint8(((np.float32(original[:, :, 2]) / 255) ** gamma) * 255)

    # Merge the corrected channels
    gamma_corrected = cv2.merge([gamma_corrected_b, gamma_corrected_g, gamma_corrected_r])

    # Plot the gamma-corrected image
    plt.subplot(3, 3, 3 * i + 1)
    plt.title(f'Gamma = {gamma}')
    plt.axis('off')
    plt.imshow(cv2.cvtColor(gamma_corrected, cv2.COLOR_BGR2RGB))

    # Plot the gamma function
    x = np.linspace(0, 1, 256)
    y = x ** gamma
    plt.subplot(3, 3, 3 * i + 2)
    plt.title(f'Gamma Function (γ = {gamma})')
    plt.plot(x, y)
    plt.xlabel('Input Intensity')
    plt.ylabel('Output Intensity')

    # Plot the histogram
    plt.subplot(3, 3, 3 * i + 3)
    plt.title(f'Histogram (Gamma = {gamma})')
    plt.hist(gamma_corrected.ravel(), 256, [0, 256])
    plt.xlabel('Pixel Value')
    plt.ylabel('Frequency')

# Adjust layout and display the figure
plt.tight_layout()
plt.show()

mean_original = np.mean(original)
std_original = np.std(original)

# Calcular e exibir a média e o desvio padrão do histograma da imagem com gama 0.5
gamma_corrected_05 = np.uint8(((np.float32(original) / 255) ** 0.5) * 255)
mean_05 = np.mean(gamma_corrected_05)
std_05 = np.std(gamma_corrected_05)

# Calcular e exibir a média e o desvio padrão do histograma da imagem com gama 1.5
gamma_corrected_15 = np.uint8(((np.float32(original) / 255) ** 1.5) * 255)
mean_15 = np.mean(gamma_corrected_15)
std_15 = np.std(gamma_corrected_15)

print(f"Histograma Original - Média: {mean_original:.2f}, Desvio Padrão: {std_original:.2f}")
print(f"Média do histograma com gama 0.5: {mean_05:.2f}, Desvio padrão do histograma com gama 0.5: {std_05:.2f}")
print(f"Média do histograma com gama 1.5: {mean_15:.2f}, Desvio padrão do histograma com gama 1.5: {std_15:.2f}")


'''
# **Questão 2:**
Dada a imagem colorida RecortePorDoSol.tiff, converta-a para tons de cinza. 
Peque a imagem resultante e aplique a operação de equalização de histograma. 
Explique esta operação detalhadamente e, em seguida, analise os resultados quanto aos seus efeitos qualitativos nas partes 
claras e escuras da imagem. Utilize também os gráficos dos histogramas que julgar necessário.
'''
import cv2
import matplotlib.pyplot as plt

# Carregar Imagem
Original = cv2.imread('RecortePorDoSol.tiff')

# Converter para Escala de Cinza
grayImg = cv2.cvtColor(Original, cv2.COLOR_BGR2GRAY)

# Aplicando Equalização de Histograma
EqualizedImg = cv2.equalizeHist(grayImg)

# Mostrar Imagens Original, Cinza e Equalizada
plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.title('Imagem Original')
plt.imshow(cv2.cvtColor(original, cv2.COLOR_BGR2RGB))  # Converter para RGB
plt.axis('off')

plt.subplot(1, 3, 2)
plt.title('Imagem Cinza')
plt.imshow(grayImg, cmap='gray')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.title('Image Equalizada')
plt.imshow(EqualizedImg, cmap='gray')
plt.axis('off')

plt.show()

# Plotar Histogramas
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.title('Histograma Tons Cinza')
plt.hist(grayImg.ravel(), 256, [0, 256])

plt.subplot(1, 2, 2)
plt.title('Histograma Equalizado')
plt.hist(EqualizedImg.ravel(), 256, [0, 256])

plt.show()

# Calcular Média e Desvio Padrão do Histograma Original
mean_grayscale = np.mean(grayImg)
std_grayscale = np.std(grayImg)

# Calcular Média e Desvio Padrão do Histograma Equalizado
mean_equalized = np.mean(EqualizedImg)
std_equalized = np.std(EqualizedImg)

# Print the results
print(f"Histograma Tons Cinza - Média: {mean_grayscale:.2f}, Desvio Padrão: {std_grayscale:.2f}")
print(f"Histograma Equalizedo - Média: {mean_equalized:.2f}, Desvio Padrão: {std_equalized:.2f}")




