import cv2
from google.colab.patches import cv2_imshow

# faça o upload de uma imagem (JPG ou PNG) e altere o nome do arquivo na linha abaixo
image = cv2.imread('pessoa.jpg')

cinza = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
invertido = 255 - cinza

blur = cv2.GaussianBlur(invertido, (21, 21), 0)
invertido_blue = 255 - blur

sketch = cv2.divide(cinza, invertido_blue, scale=256)

# salva o sketch em um arquivo chamado 'sketch.png'. Faça o download!
cv2.imwrite('sketch.png', sketch)

# mostra o sketch criado
cv2_imshow(sketch)

