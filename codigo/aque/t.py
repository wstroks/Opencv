import cv2
imagem= cv2.imread('opencv-python.jpg')
imagemcinza= cv2.cvtColor(imagem,cv2.COLOR_BGR2GRAY)
cv2.imshow("Aque", imagem)
cv2.imshow("CINZA", imagemcinza)
cv2.waitKey()