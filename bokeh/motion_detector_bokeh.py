import cv2, time, pandas
from datetime import datetime

fps = 24
video = cv2.VideoCapture(0,cv2.CAP_DSHOW)
status_list = [None,None]
times = []

df=pandas.DataFrame(columns=["Start","End"])

#Need to generate static image from first frame for comparison
first_frame = None

while True:
    check, frame = cv2.FORMATTER_FMT_C = video.read()   #'video.read' returns a tuple with a boolean at the start to say if capture is successful
    
    # Set status to 'not found'
    status = 0

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
        
       # otherwise, if we have found something, set status to 1
        status = 1
        
        #get coordinates of the contour's bounding rectangle and use to draw rectangle on captured output
        (x,y,w,h)=cv2.boundingRect(c)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)
    
    # Write status (1 or 0) to list. If the status has gone from 0 to 1 (or reverse), write the timestamp
    # need to import 'datetime'
    status_list.append(status)

    # Truncate the status list as we are only interested in the last two items
    status_list = status_list[-2:]

    if status_list[-1]==1 and status_list[-2]==0:
        times.append(datetime.now())
    if status_list[-1]==0 and status_list[-2]==1:
        times.append(datetime.now())

    #display all images for testing purposes
    #cv2.imshow("First frame", first_frame) #show single image
    #cv2.imshow("Current image", grey) #show single image
    #cv2.imshow("Delta", delta_frame) #show single image
    #cv2.imshow("Threshold", thresh_frame) #show single image
    cv2.imshow("Contours", frame) #show single image

    key = cv2.waitKey(int(1000/fps))

    # add additional check to 'quit' step so that if item is found at that point, write an extra timestamp 
    if key==ord('q'):
        if status_list[-1]==1:
            times.append(datetime.now())
        break

video.release()
cv2.destroyAllWindows()

print(times)

for i in range(0,len(times),2): # for all entries in 'times', in steps of 2...
    df=df.append({"Start":times[i],"End":times[i+1]},ignore_index=True)

df.to_csv("Times.csv")