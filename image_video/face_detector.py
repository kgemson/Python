import cv2

#import face detector XML file
face_cascade = cv2.CascadeClassifier("Files/haarcascade_frontalface_default.xml")

#import image and convert to grey
img = cv2.imread("Files/photo.jpg",1)
grey_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#define 'faces' as rectangles where face is found (start x,y / width / height)
#note - may be more than 1
faces = face_cascade.detectMultiScale(grey_img,
scaleFactor=1.05,
minNeighbors=5)

print(faces)

#for each face found, create rectangle on original image starting at (x,y) going to bottom corner,
#with a 3-pixel green border
for x, y, w, h in faces:
    img=cv2.rectangle(img,(x,y),(x+w, y+h),(0,255,0),3)

#resize output image to half size and display
resized_image = cv2.resize(img,(int(img.shape[1]/2), int(img.shape[0]/2)))
cv2.imshow("Resized",resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()