# Projeto de Visão Computacional com OpenCV

Olá! Este é um projeto simples que demonstra o uso da biblioteca OpenCV em Python para processamento de imagens.

## Visão Geral

O objetivo deste projeto é carregar uma imagem, convertê-la para tons de cinza e exibi-la na tela. Este é um dos passos fundamentais em muitas tarefas de visão computacional.

## O Código

O script `opcv.py` realiza as seguintes ações:

1.  **Importa a biblioteca OpenCV:**
    ```python
    import cv2 as cv
    ```
    Aqui, importamos a biblioteca `cv2` e a apelidamos de `cv` para facilitar o uso.

2.  **Carrega a imagem:**
    ```python
    img = cv.imread('Odair.png')
    ```
    A função `cv.imread()` é usada para carregar a imagem `Odair.png` do disco.

3.  **Converte para tons de cinza:**
    ```python
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    ```
    Utilizamos `cv.cvtColor()` para converter a imagem do espaço de cores BGR (padrão do OpenCV) para tons de cinza.

4.  **Exibe a imagem:**
    ```python
    cv.imshow('imagem', gray)
    ```
    `cv.imshow()` abre uma janela com o título 'imagem' e mostra a imagem em tons de cinza.

5.  **Aguarda o usuário:**
    ```python
    cv.waitKey(0)
    ```
    A função `cv.waitKey(0)` espera indefinidamente até que qualquer tecla seja pressionada. Isso é importante para que a janela com a imagem não feche imediatamente.

6.  **Fecha as janelas:**
    ```python
    cv.destroyAllWindows()
    ```
    Após o usuário pressionar uma tecla, `cv.destroyAllWindows()` fecha todas as janelas criadas pelo OpenCV.

## Como Executar

1.  Certifique-se de ter o Python e o OpenCV instalados.
2.  Clone este repositório.
3.  Coloque uma imagem chamada `Odair.png` no mesmo diretório do script.
4.  Execute o script no seu terminal:
    ```bash
    python opcv.py
    ```

Sinta-se à vontade para experimentar com outras imagens e explorar mais funcionalidades do OpenCV!
