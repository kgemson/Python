import cv2, time

fps = 24
video = cv2.VideoCapture(0,cv2.CAP_DSHOW)

#Need to generate static image from first frame for comparison
first_frame = None

while True:
    check, frame = cv2.FORMATTER_FMT_C = video.read()   #'video.read' returns a tuple with a boolean at the start to say if capture is successful
    
    #convert video frame to grey, then blur it
    #this will be used in comparison against first frame
    grey=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    grey=cv2.GaussianBlur(grey,(21,21),0)

    if first_frame is None:
        first_frame = grey
        continue    #i.e. go back to start of loop

    #compare difference between start frame and current, and output to image
    delta_frame = cv2.absdiff(first_frame,grey)

    # comparison step outputs a data frame with values for each pixel...
    # black (value 0) means no difference, white(255) is a large difference
    # We want to convert this to a 'threshold' image where everything is black or white
    # based on a threshold value - here we are choosing 30 (<30 = black, >=30 is white (255))

    thresh_frame = (cv2.threshold(delta_frame,30,255,cv2.THRESH_BINARY))[1] #last param is conversion method
    #'threshold' returns a tuple, so need to specify [1] to get single frame

    # we want to dilate the image to make areas more distinct. The main effect of the dilation on a binary image is to
    # continuously increase the boundaries of regions of foreground pixels (for example, white pixels, typically). 
    # Thus areas of foreground pixels expand in size while holes within those regions become smaller.
    thresh_frame = cv2.dilate(thresh_frame,None,iterations=2)

    # Next, find contours (outline) of shapes and store in tuple
    # (function returns contours and hierarchy)
    conts, hierarchy = cv2.findContours(thresh_frame.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    #Loop through returned contours, disregarding anything below 5000 pixels in area
    for c in conts:
        if cv2.contourArea(c) < 5000:
            continue
        
        #get coordinates of the contour's bounding rectangle and use to draw rectangle on captured output
        (x,y,w,h)=cv2.boundingRect(c)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)

    #display all images for testing purposes
    #cv2.imshow("First frame", first_frame) #show single image
    #cv2.imshow("Current image", grey) #show single image
    #cv2.imshow("Delta", delta_frame) #show single image
    #cv2.imshow("Threshold", thresh_frame) #show single image
    cv2.imshow("Contours", frame) #show single image

    key = cv2.waitKey(int(1000/fps))

    if key==ord('q'):
        break

video.release()
cv2.destroyAllWindows()