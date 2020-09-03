import cv2
cap = cv2.VideoCapture(0)

#while cap.isOpened():
#    ret, frame = cap.read()
#    cv2.imshow('lala',frame)
#    if cv2.waitKey(1) & 0xFF == ord('q'):
#        file = 'C:/Users/nicoy/Desktop/SafeWave/SafeCam/Archivos python\imagen.jpg'
#        cv2.imwrite(file,frame)
#        break

if cap.isOpened:
    ret, frame = cap.read()
    file = 'C:/Users/nicoy/Desktop/SafeWave/SafeCam/Archivos python\imagen.jpg'
    cv2.imwrite(file,frame)
    
    
cap.release() 
cv2.destroyAllWindows()
