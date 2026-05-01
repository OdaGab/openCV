import cv2 as cv # Importa a biblioteca OpenCV e a renomeia como 'cv' para facilitar o uso.
import matplotlib.pyplot as plt # Importa a biblioteca Matplotlib para exibir imagens.

# Carrega a imagem colorida 'Odair.png'. O flag cv.IMREAD_COLOR indica que a imagem deve ser lida em cores (BGR).
img_color = cv.imread('Odair.png', cv.IMREAD_COLOR)

# Verifica se a imagem foi carregada corretamente.
if img_color is None:
    print("Erro: Não foi possível carregar a imagem Odair.png")
else:
    # Converte a imagem colorida (BGR) para escala de cinza.
    img = cv.cvtColor(img_color, cv.COLOR_BGR2GRAY)

    # Imprime o tipo do objeto 'img' (que será um array NumPy).
    print("Tipo da imagem em escala de cinza:", type(img))
    # Imprime as dimensões da imagem em escala de cinza (altura, largura).
    print("Dimensões da imagem em escala de cinza:", img.shape)
    
    # Exibe a imagem em escala de cinza.
    # 'cmap='gray'' garante que a imagem seja exibida corretamente em tons de cinza.
    plt.imshow(img, cmap='gray')
    plt.title('Imagem em Escala de Cinza') # Adiciona um título ao gráfico.
    plt.show() # Mostra o gráfico da imagem em escala de cinza.

    # Converte a imagem colorida de BGR (formato do OpenCV) para RGB (formato do Matplotlib)
    img_rgb = cv.cvtColor(img_color, cv.COLOR_BGR2RGB)
    # Exibe a imagem colorida original.
    plt.imshow(img_rgb)
    plt.title('Imagem Colorida Original') # Adiciona um título ao gráfico.
    plt.show() # Mostra o gráfico da imagem colorida.
