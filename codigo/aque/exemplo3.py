import cv2

video = cv2.VideoCapture(0)
classificadorFace = cv2.CascadeClassifier('cascades\\Hand.Cascade.1.xml')
while True:
    conectado, frame= video.read()
   #print(conectado)

    frameCinza = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    FacesDectadas= classificadorFace.detectMultiScale(frameCinza)
    #, minSize=(70,70)

    for(x,y,l,a) in FacesDectadas:
        cv2.rectangle(frame, (x,y),(x +l, y +a), (0,0,255), 2)
    cv2.imshow('video',frame)
    if cv2.waitKey(1) == ord('q'):
        break

video.release()
cv2.destroyAllWindows()