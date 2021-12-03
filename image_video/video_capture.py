import cv2, time

fps = 24
video = cv2.VideoCapture(0,cv2.CAP_DSHOW)

while True:
    check, frame = cv2.FORMATTER_FMT_C = video.read()   #'video.read' returns a tuple with a boolean at the start to say if capture is successful
    #time.sleep(3)
    
    grey=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow("Capturing", grey) #show single image
    
    key = cv2.waitKey(int(1000/fps))

    if key==ord('q'):
        break

video.release()
cv2.destroyAllWindows()