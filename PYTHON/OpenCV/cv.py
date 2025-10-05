import cv2 as cv

####Reading and Displaying an Image####
'''
img=cv.imread("/home/viscous/#Viscous/Wallpaper/PNG/Pokemon 4k wallpaper.jpg")#reads the image.
cv.imshow("Pikachu",img)#opens a window with the image.

cv.waitKey(0)#Waits for infinite time to press any key.
'''


####Reading and Displaying a Video####
'''
vdo=cv.VideoCapture("/home/viscous/#Viscous/Wallpaper/PinDown.io_1753704910.mp4")#reads the video.
#If you write 0 instead of the path of the video, it will open the webcam.

while True:    
    isTrue,frame=vdo.read()#reads the video frame by frame.
    
    if not isTrue:#if there is no frame, it will break the loop.
        vdo.set(cv.CAP_PROP_POS_FRAMES, 0)#sets the frame position to 0.
        continue
    
    cv.imshow("Video",frame)#opens a window with the video.
    
    
    if cv.waitKey(20) & 0xFF==ord('q'):#waits for 20 milliseconds to press any key. If 'd' is pressed, the loop will break.
        break
vdo.release()#releases the video.
cv.destroyAllWindows()#closes all the windows.
'''