import cv2

#classificador = cv2.CascadeClassifier('cascades\\haarcascade_frontalcatface.xml')
#classificador = cv2.CascadeClassifier('cascades\\relogios.xml')
classificador = cv2.CascadeClassifier('cascades\\cars.xml')

imagem = cv2.imread('outros\\carro3.jpg')
imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

detectado = classificador.detectMultiScale(imagemCinza, scaleFactor=1.01)
print(detectado)

for (x, y, l, a) in detectado:
    imagem = cv2.rectangle(imagem, (x, y), (x + l, y + a), (0, 0, 255), 2)
    if (l > 50 or a > 50):
        print("Fora do padrão")

cv2.imshow("Encontrado", imagem)
cv2.waitKey()