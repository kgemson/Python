import cv2
import glob

images = glob.glob('sample_images/*.jpg')

for i in images:
    img = cv2.imread(i,1)
    resized_image = cv2.resize(img,(100,100))
    cv2.imshow("Resized image",resized_image)
    cv2.waitKey(500)
    cv2.destroyAllWindows()
    cv2.imwrite(i+"_resized.jpg",resized_image)