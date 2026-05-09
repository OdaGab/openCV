import cv2

# Este é um arquivo introdutório básico para processamento de imagens com OpenCV
# Vamos importar uma imagem, convertê-la para preto e branco (escala de cinza) e salvar o resultado

# 1. Importar a imagem: Usamos cv2.imread para carregar a imagem do caminho especificado
# O caminho '../imagens/Odair.png' aponta para a pasta 'imagens' no diretório pai
img = cv2.imread('../imagens/Odair.png')

# Verificar se a imagem foi carregada corretamente
if img is None:
    print("Erro: Não foi possível carregar a imagem. Verifique o caminho.")
else:
    # 2. Converter para preto e branco: cv2.cvtColor converte a imagem colorida para escala de cinza
    # COLOR_BGR2GRAY transforma de BGR (formato padrão do OpenCV) para grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 3. Salvar a imagem em preto e branco: cv2.imwrite salva a imagem no disco
    # Aqui, salvamos como 'Odair_gray.png' na mesma pasta
    cv2.imwrite('Odair_gray.png', gray)

    print("Imagem convertida e salva como 'Odair_gray.png'!")

    # Opcional: Exibir a imagem (descomente as linhas abaixo se quiser ver)
    # cv2.imshow('Imagem Original', img)
    # cv2.imshow('Imagem em Preto e Branco', gray)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()