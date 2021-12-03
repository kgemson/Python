import cv2

#import face detector XML file
face_cascade = cv2.CascadeClassifier("Files/haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier("Files/haarcascade_eye.xml")

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
for (x, y, w, h) in faces:
    img=cv2.rectangle(img,(x,y),(x+w, y+h),(0,255,0),3)
    
    #we can narrow down search area to just the face as eyes must be there
    grey_face_img = grey_img[y:y+h, x:x+w]
    eyes = eye_cascade.detectMultiScale(grey_face_img)
    for (ex,ey,ew,eh) in eyes:
        #draw red rectangle using start and end point of eyes, remembering to add in original x/y as start points
        cv2.rectangle(img,(x+ex,y+ey),(x+ex+ew,y+ey+eh),(0,0,255),2)

#resize output image to half size and display
resized_image = cv2.resize(img,(int(img.shape[1]/2), int(img.shape[0]/2)))
cv2.imshow("Resized",resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()